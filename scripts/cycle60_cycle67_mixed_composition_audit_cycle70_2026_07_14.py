#!/usr/bin/env python3
"""Cycle 70: exact mixed Cycle-60 / Cycle-67 composition audit.

Cycle 67 proves completed-comb causal safety with a must-ancestor certificate.
This runner independently checks that certificate, then scans the union of the
Cycle-60 and Cycle-67 proper-cubic tables through every one of the 242,033
reachable asynchronous Cycle-60 states.  A rank-DAG evaluation collapses
those states to the physically available Cycle-67 phase records; NumPy is
used only to project exact integer masks efficiently.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import product
from pathlib import Path

import numpy as np

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "CYCLE60_CYCLE67_MIXED_COMPOSITION_AUDIT_CYCLE70_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

# This is the count form of Cycle 67's named-parent predicate.  The runner
# exhaustively checks it against the authoritative function below before using
# it for the 242,033-state availability collapse.
REQUIRED_COUNTS: dict[str, dict[str, int]] = {
    "F": {"R2": 1, "S8": 1},
    "FP": {"F": 2},
    "I1": {"FP": 1, "R2": 2},
    "I2": {"I1": 1, "R1": 2},
    "DONE": {"I2": 3},
    "L1": {"DONE": 1},
    "L2": {"I2": 1, "L1": 1},
    "L3": {"L2": 2, "R1": 1},
    "L4": {"L3": 1, "R2": 1},
    "L5": {"F": 1, "L4": 1},
    "L6": {"L5": 1},
    "L7": {"F": 1, "L6": 1},
    "L8": {"L7": 2},
    "L9": {"L8": 1},
    "L10": {"L9": 1},
    "L11": {"L10": 2},
    "L12": {"H1": 1, "L11": 1},
    "C_Q": {"W6": 1, "Z0": 1, "L12": 1},
    "P0": {"C_Q": 1, "OPEN_B": 1},
    "P1": {"P0": 1, "E": 1, "L8": 1, "L10": 1},
    "P2": {"C_Q": 1, "P1": 1, "J6": 1, "L11": 1},
    "P3": {"P2": 1, "E": 1, "L8": 1, "L10": 1},
    "X_B": {"P3": 1, "OPEN_B": 1},
    "Z_A": {"X_B": 1, "P2": 1, "W6": 1, "Z0": 1},
    "Z_C": {"X_B": 1, "OPEN_C": 1},
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


def count_predicate(role: str, values: list[str | None]) -> bool:
    counts = Counter(value for value in values if value is not None)
    return all(counts[content] >= needed for content, needed in REQUIRED_COUNTS[role].items())


def predicate_equivalence_tests() -> tuple[int, int]:
    """Compare count form and authoritative predicate on every local subset."""

    tests = failures = 0
    fixed = c60.CONSTRUCTION.base
    comb = c60.CONSTRUCTION.allowed
    phase = c67.ALLOWED
    for target, role in phase.items():
        mandatory = [
            fixed[neighbour]
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in fixed
        ]
        optional = [
            (comb | phase)[neighbour]
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in comb or neighbour in phase
        ]
        for mask in range(1 << len(optional)):
            values = mandatory + [
                value for index, value in enumerate(optional) if mask & (1 << index)
            ]
            tests += 1
            if count_predicate(role, values) != c67.causal_parents_hold(role, values):
                failures += 1
    return tests, failures


def raw_outputs(table: dict[Signature, str]) -> dict[Signature, frozenset[str]]:
    rows: dict[Signature, set[str]] = defaultdict(set)
    for signature, output in table.items():
        for rotation in c53.ROTATIONS:
            rows[c53.rotate_signature(signature, rotation)].add(output)
    return {signature: frozenset(outputs) for signature, outputs in rows.items()}


def reachable_cycle60_states() -> tuple[int, ...]:
    prior = c59.CONSTRUCTION
    c59.CONSTRUCTION = c60.CONSTRUCTION
    try:
        conditions = c59.compile_conditions()
    finally:
        c59.CONSTRUCTION = prior

    queue = deque((0,))
    seen = {0}
    allowed = c60.CONSTRUCTION.allowed
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
    return tuple(seen)


@dataclass(frozen=True)
class Availability:
    comb_masks: np.ndarray
    availability_ids: np.ndarray
    availability_masks: tuple[int, ...]
    phase_sites: tuple[Coord, ...]
    phase_index: dict[Coord, int]


def phase_availability(states: tuple[int, ...]) -> Availability:
    """Evaluate the strict Cycle-67 parent DAG in every Cycle-60 state."""

    fixed = c60.CONSTRUCTION.base
    comb = c60.CONSTRUCTION.allowed
    comb_sites = tuple(sorted(comb))
    comb_index = {site: index for index, site in enumerate(comb_sites)}
    phase = c67.ALLOWED
    phase_sites = tuple(sorted(phase, key=lambda site: (c67.RANK[phase[site]], site)))
    phase_index = {site: index for index, site in enumerate(phase_sites)}

    metadata: list[tuple[tuple[int, tuple[int, ...], tuple[int, ...]], ...]] = []
    for site in phase_sites:
        requirements = []
        for content, needed in REQUIRED_COUNTS[phase[site]].items():
            fixed_count = sum(
                fixed.get(c53.add(site, direction)) == content
                for direction in c53.DIRECTIONS
            )
            comb_bits = tuple(
                1 << comb_index[c53.add(site, direction)]
                for direction in c53.DIRECTIONS
                if comb.get(c53.add(site, direction)) == content
            )
            phase_bits = tuple(
                1 << phase_index[c53.add(site, direction)]
                for direction in c53.DIRECTIONS
                if phase.get(c53.add(site, direction)) == content
                and c67.RANK[content] < c67.RANK[phase[site]]
            )
            requirements.append((needed - fixed_count, comb_bits, phase_bits))
        metadata.append(tuple(requirements))

    comb_masks = np.empty(len(states), dtype=np.uint64)
    availability_ids = np.empty(len(states), dtype=np.uint8)
    mask_ids: dict[int, int] = {}
    availability_masks: list[int] = []
    for state_index, comb_mask in enumerate(states):
        phase_mask = 0
        for phase_bit, requirements in enumerate(metadata):
            if all(
                needed <= 0
                or sum(bool(comb_mask & bit) for bit in comb_bits)
                + sum(bool(phase_mask & bit) for bit in phase_bits)
                >= needed
                for needed, comb_bits, phase_bits in requirements
            ):
                phase_mask |= 1 << phase_bit
        if phase_mask not in mask_ids:
            mask_ids[phase_mask] = len(availability_masks)
            availability_masks.append(phase_mask)
        comb_masks[state_index] = comb_mask
        availability_ids[state_index] = mask_ids[phase_mask]

    return Availability(
        comb_masks,
        availability_ids,
        tuple(availability_masks),
        phase_sites,
        phase_index,
    )


@dataclass(frozen=True)
class MixedResult:
    interface_candidates: int
    retained_candidates: int
    mixed_contexts: int
    certified_wrong: int
    certified_wrong_classes: int
    new_wrong: int
    union_conflicts: int
    comb_blockers: int


def mixed_union_scan(availability: Availability) -> MixedResult:
    fixed = c60.CONSTRUCTION.base
    comb = c60.CONSTRUCTION.allowed
    comb_sites = tuple(sorted(comb))
    comb_index = {site: index for index, site in enumerate(comb_sites)}
    phase = c67.ALLOWED
    phase_index = availability.phase_index
    comb_raw = raw_outputs(c60.CONSTRUCTION.table)
    phase_raw = raw_outputs(c67.RULES)
    all_raw = set(comb_raw) | set(phase_raw)

    conditions = c67.compile_conditions()
    _, _, must, _, _ = c67.causal_safety_certificate(conditions)

    occupied = set(fixed) | set(comb) | set(phase)
    interface = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in fixed
    }

    retained: list[
        tuple[
            Coord,
            tuple[tuple[Coord, str, int], ...],
            tuple[tuple[Coord, str, int], ...],
            tuple[tuple[Coord, str], ...],
        ]
    ] = []
    for target in interface:
        comb_neighbours = tuple(
            (neighbour, comb[neighbour], 1 << comb_index[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in comb
        )
        phase_neighbours = tuple(
            (neighbour, phase[neighbour], 1 << phase_index[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in phase
        )
        # Directions are restored here so each exact signature remains
        # presentation-sensitive before proper-rotation table lookup.
        fixed_neighbours = tuple(
            (direction, fixed[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in fixed
        )

        possible_match = False
        for comb_mask in range(1 << len(comb_neighbours)):
            for phase_mask in range(1 << len(phase_neighbours)):
                signature = tuple(sorted(
                    list(fixed_neighbours)
                    + [
                        (
                            next(direction for direction in c53.DIRECTIONS if c53.add(target, direction) == site),
                            output,
                        )
                        for index, (site, output, _) in enumerate(comb_neighbours)
                        if comb_mask & (1 << index)
                    ]
                    + [
                        (
                            next(direction for direction in c53.DIRECTIONS if c53.add(target, direction) == site),
                            output,
                        )
                        for index, (site, output, _) in enumerate(phase_neighbours)
                        if phase_mask & (1 << index)
                    ]
                ))
                if signature in all_raw:
                    possible_match = True
                    break
            if possible_match:
                break
        if possible_match or (target in comb and phase_neighbours):
            retained.append((target, comb_neighbours, phase_neighbours, fixed_neighbours))

    full_phase_mask = (1 << len(availability.phase_sites)) - 1
    mixed_contexts = certified_wrong = new_wrong = conflicts = blockers = 0
    certified_classes: set[tuple[Coord, str, tuple[str, ...], str | None]] = set()
    for target, comb_neighbours, phase_neighbours, fixed_neighbours in retained:
        if comb_neighbours:
            compressed = np.zeros(len(availability.comb_masks), dtype=np.uint8)
            for index, (_, _, bit) in enumerate(comb_neighbours):
                compressed |= (
                    ((availability.comb_masks & np.uint64(bit)) != 0).astype(np.uint8)
                    << index
                )
            codes = (
                availability.availability_ids.astype(np.uint16) << 6
            ) | compressed.astype(np.uint16)
            if target in comb_index:
                target_bit = np.uint64(1 << comb_index[target])
                codes = np.where(
                    (availability.comb_masks & target_bit) != 0,
                    np.uint16(65_535),
                    codes,
                )
            patterns = tuple(
                (int(code & 63), availability.availability_masks[int(code >> 6)])
                for code in np.unique(codes)
                if code != 65_535
            )
        else:
            # No variable comb neighbour means partial Cycle 60 cannot alter
            # this local signature; the completed, fully available phase is
            # the one relevant context.
            patterns = ((0, full_phase_mask),)

        for comb_mask, available_phase in patterns:
            available_local = sum(
                1 << index
                for index, (_, _, bit) in enumerate(phase_neighbours)
                if available_phase & bit
            )
            phase_mask = available_local
            while True:
                mixed_contexts += 1
                signature_parts = list(fixed_neighbours)
                present_phase: set[Coord] = set()
                absent_phase: set[Coord] = set()
                for index, (site, output, _) in enumerate(comb_neighbours):
                    if comb_mask & (1 << index):
                        direction = next(
                            direction for direction in c53.DIRECTIONS
                            if c53.add(target, direction) == site
                        )
                        signature_parts.append((direction, output))
                for index, (site, output, _) in enumerate(phase_neighbours):
                    if phase_mask & (1 << index):
                        direction = next(
                            direction for direction in c53.DIRECTIONS
                            if c53.add(target, direction) == site
                        )
                        signature_parts.append((direction, output))
                        present_phase.add(site)
                    else:
                        absent_phase.add(site)
                if target in phase:
                    absent_phase.add(target)
                signature = tuple(sorted(signature_parts))

                witness = next((
                    (present, ancestor)
                    for present in present_phase
                    for ancestor in must[present].intersection(absent_phase)
                ), None)
                merged = {
                    source: outputs
                    for source, table in (("C60", comb_raw), ("C67", phase_raw))
                    if (outputs := table.get(signature))
                }
                all_outputs = set().union(*merged.values()) if merged else set()
                if len(all_outputs) > 1 and witness is None:
                    conflicts += 1
                for source, outputs in merged.items():
                    expected = (comb if source == "C60" else phase).get(target)
                    if outputs == (
                        frozenset((expected,)) if expected is not None else frozenset()
                    ):
                        continue
                    if witness is not None:
                        certified_wrong += 1
                        certified_classes.add((target, source, tuple(sorted(outputs)), expected))
                    else:
                        new_wrong += 1
                if (
                    target in comb
                    and present_phase
                    and signature not in comb_raw
                ):
                    blockers += 1

                if phase_mask == 0:
                    break
                phase_mask = (phase_mask - 1) & available_local

    return MixedResult(
        len(interface),
        len(retained),
        mixed_contexts,
        certified_wrong,
        len(certified_classes),
        new_wrong,
        conflicts,
        blockers,
    )


def steiner_edge_minimum() -> int:
    """Exact rectilinear tree cost joining F6 to the DONE coordinate."""

    f_sites = tuple(sorted(c67.ROLE_SITES["F"]))
    done = next(iter(c67.ROLE_SITES["DONE"]))
    terminals = f_sites + (done,)
    lower = tuple(min(site[axis] for site in terminals) for axis in range(3))
    upper = tuple(max(site[axis] for site in terminals) for axis in range(3))
    vertices = tuple(product(
        range(lower[0], upper[0] + 1),
        range(lower[1], upper[1] + 1),
        range(lower[2], upper[2] + 1),
    ))
    index = {site: bit for bit, site in enumerate(vertices)}
    adjacency = tuple(
        tuple(
            index[neighbour]
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(site, direction)) in index
        )
        for site in vertices
    )

    infinity = 10**9
    subset_count = 1 << len(f_sites)
    distance = [[infinity] * len(vertices) for _ in range(subset_count)]
    for terminal_index, site in enumerate(f_sites):
        distance[1 << terminal_index][index[site]] = 0
    for subset in range(1, subset_count):
        part = (subset - 1) & subset
        while part:
            other = subset ^ part
            if part < other:
                for vertex in range(len(vertices)):
                    distance[subset][vertex] = min(
                        distance[subset][vertex],
                        distance[part][vertex] + distance[other][vertex],
                    )
            part = (part - 1) & subset
        queue = [
            (cost, vertex)
            for vertex, cost in enumerate(distance[subset])
            if cost < infinity
        ]
        # heapify without importing another name.
        from heapq import heapify
        heapify(queue)
        while queue:
            cost, vertex = heappop(queue)
            if cost != distance[subset][vertex]:
                continue
            for neighbour in adjacency[vertex]:
                if cost + 1 < distance[subset][neighbour]:
                    distance[subset][neighbour] = cost + 1
                    heappush(queue, (cost + 1, neighbour))
    return distance[-1][index[done]]


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    tests, predicate_failures = predicate_equivalence_tests()
    check("A03 count predicate exactly matches Cycle 67", predicate_failures == 0, f"{tests} local subsets")
    phase_roles = set(c67.ALLOWED.values())
    check("A04 every Cycle-67 role has an explicit parent predicate", phase_roles == set(REQUIRED_COUNTS))
    check(
        "A05 all dynamic parents are strictly lower rank",
        all(
            content not in phase_roles or c67.RANK[content] < c67.RANK[role]
            for role, requirements in REQUIRED_COUNTS.items()
            for content in requirements
        ),
    )

    conditions = c67.compile_conditions()
    bad, witnesses, must, iterations, good = c67.causal_safety_certificate(conditions)
    check("B01 completed-comb certificate independently finds 47 apparent bad rows", len(bad) == 47)
    check("B02 all 47 rows have must-ancestor witnesses", len(witnesses) == 47)
    check("B03 no must-ancestor witness is the same site twice", all(present != ancestor for present, ancestor in witnesses.values()))
    check("B04 fixed point and correct-condition counts are exact", (iterations, good) == (17, 308), f"{iterations}/{good}")
    prefix_tests, prefix_failures = c67.rank_prefix_closure()
    check("B05 all within-rank prefixes retain progress", (prefix_tests, prefix_failures) == (30_240, 0), str((prefix_tests, prefix_failures)))

    minimum_edges = steiner_edge_minimum()
    completion_records = sum(len(c67.ROLE_SITES[role]) for role in ("FP", "I1", "I2", "DONE"))
    check("C01 exact F6-to-DONE Steiner minimum is 15 edges", minimum_edges == 15, str(minimum_edges))
    check("C02 completion barrier meets the ten-new-record lower bound", completion_records == minimum_edges - 5 == 10, str(completion_records))
    expected_pair_sites = {(0, -3, -4), (3, -3, -1), (3, 0, -4)}
    check("C03 Cycle-67 FP is exactly the Cycle-68 J3 interface", set(c67.ROLE_SITES["FP"]) == expected_pair_sites)

    states = reachable_cycle60_states()
    check("D01 all 242,033 Cycle-60 states are retained", len(states) == 242_033, f"{len(states):,}")
    availability = phase_availability(states)
    check("D02 reachable comb states collapse to 67 phase-availability masks", len(availability.availability_masks) == 67, str(len(availability.availability_masks)))
    check("D03 the full 91-record phase is available at the comb terminal", (1 << len(availability.phase_sites)) - 1 in availability.availability_masks)

    result = mixed_union_scan(availability)
    check("E01 full local interface has 387 candidates", result.interface_candidates == 387, str(result.interface_candidates))
    check("E02 exact prefilter retains 171 candidates", result.retained_candidates == 171, str(result.retained_candidates))
    check("E03 mixed union scan exhausts 8,373 contexts", result.mixed_contexts == 8_373, str(result.mixed_contexts))
    check("E04 only the same 47 certified apparent wrong rows remain", (result.certified_wrong, result.certified_wrong_classes) == (47, 34), str((result.certified_wrong, result.certified_wrong_classes)))
    check("E05 partial Cycle 60 creates no new wrong/off-footprint write", result.new_wrong == 0)
    check("E06 Cycle-60/Cycle-67 union has no output conflict", result.union_conflicts == 0)
    check("E07 no feasible Cycle-67 record can block an open comb target", result.comb_blockers == 0)

    print(f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
