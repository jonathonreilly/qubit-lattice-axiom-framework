#!/usr/bin/env python3
"""Cycle 77: mixed-transient audit and zero-site repair of Cycle 72.

The Cycle-72 downstream table is exact after the Cycle-67 terminal, but its
bare-X_B D_y row is live earlier.  This runner scans all reachable Cycle-60
states, the exact Cycle-67 rank availability above each state, and a strong
local over-approximation of every correct downstream subset.  It reproduces
the early Z_C theft, reorders B_y before D_y without adding a site, and reruns
the same mixed scan plus the exact downstream graph.

Authority: none.  No axiom or law-selection status follows.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import numpy as np

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import cycle60_cycle67_mixed_composition_audit_cycle70_2026_07_14 as c70
import cycle67_terminal_bdh_rebind_cycle72_2026_07_14 as c72
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MIXED_CYCLE72_GUIDE_REPAIR_CYCLE77_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

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


@dataclass(frozen=True)
class Construction:
    source: dict[Coord, str]
    new_table: dict[Signature, str]
    union_table: dict[Signature, str]
    allowed: dict[Coord, str]
    stage_aliases: dict[str, tuple[Coord, ...]]


def build_repaired_construction() -> Construction:
    source = dict(c67.BASE)
    source.update(c67.ALLOWED)
    records = dict(source)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    aliases_by_stage: dict[str, tuple[Coord, ...]] = {}

    def stage(name: str, representative: Coord, output: str) -> None:
        signature = key(records, representative)
        aliases = tuple(c53.signature_classes(records).get(signature, ()))
        if not aliases:
            raise ValueError(f"empty class: {name}")
        prior = table.get(signature)
        if prior is not None and prior != output:
            raise ValueError(f"table conflict: {prior}/{output}")
        table[signature] = output
        aliases_by_stage[name] = aliases
        for site in aliases:
            if site in records:
                raise ValueError(f"occupied alias: {name} {site}")
            records[site] = output
            allowed[site] = output

    rows = (
        ("BY", (1, 1, 0), "B1"),
        ("DY", (2, 1, 0), "D1"),
        ("DZ", (2, 0, 1), "D1"),
        ("HPAIR", (3, 1, 0), "H1"),
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
    for row in rows:
        stage(*row)

    union = dict(c60.CONSTRUCTION.table)
    for component in (c67.RULES, table):
        for signature, output in component.items():
            prior = union.get(signature)
            if prior is not None and prior != output:
                raise ValueError(f"union conflict: {prior}/{output}")
            union[signature] = output
    return Construction(source, table, union, allowed, aliases_by_stage)


REPAIRED = build_repaired_construction()


@dataclass(frozen=True)
class ParentSet:
    comb: frozenset[Coord]
    phase: frozenset[Coord]
    downstream: frozenset[Coord]


@dataclass(frozen=True)
class DownModel:
    construction: Construction | c72.Construction
    sites: tuple[Coord, ...]
    index: dict[Coord, int]
    rank: dict[Coord, int]
    parents: dict[Coord, ParentSet]
    must: dict[Coord, frozenset[Coord]]


def downstream_model(
    construction: Construction | c72.Construction,
    phase_must: dict[Coord, frozenset[Coord]],
) -> DownModel:
    rank = {
        site: stage_rank
        for stage_rank, (_, aliases) in enumerate(construction.stage_aliases.items())
        for site in aliases
    }
    sites = tuple(sorted(construction.allowed, key=lambda site: (rank[site], site)))
    index = {site: bit for bit, site in enumerate(sites)}
    records = dict(construction.source)
    parents: dict[Coord, ParentSet] = {}
    must = dict(phase_must)
    raw = c70.raw_outputs(construction.new_table)

    for _, aliases in construction.stage_aliases.items():
        for target in aliases:
            signature = c53.local_signature(records, target)
            if raw.get(signature) != frozenset((construction.allowed[target],)):
                raise ValueError(f"staged row mismatch at {target}")
            positive = {
                c53.add(target, direction)
                for direction, _ in signature
            }
            comb_parents = frozenset(positive.intersection(c60.CONSTRUCTION.allowed))
            phase_parents = frozenset(positive.intersection(c67.ALLOWED))
            down_parents = frozenset(positive.intersection(construction.allowed))
            if any(rank[parent] >= rank[target] for parent in down_parents):
                raise ValueError(f"non-lower downstream parent at {target}")
            parents[target] = ParentSet(comb_parents, phase_parents, down_parents)
            closure = set(phase_parents) | set(down_parents)
            for parent in phase_parents | down_parents:
                closure.update(must[parent])
            must[target] = frozenset(closure)
        records.update({site: construction.allowed[site] for site in aliases})
    return DownModel(construction, sites, index, rank, parents, must)


@dataclass(frozen=True)
class DownAvailability:
    masks: np.ndarray
    ids: np.ndarray
    unique_masks: tuple[int, ...]


def downstream_availability(
    states: tuple[int, ...],
    phase_availability: c70.Availability,
    model: DownModel,
) -> DownAvailability:
    comb_sites = tuple(sorted(c60.CONSTRUCTION.allowed))
    comb_index = {site: bit for bit, site in enumerate(comb_sites)}
    phase_index = phase_availability.phase_index
    masks = np.empty(len(states), dtype=np.uint64)
    ids = np.empty(len(states), dtype=np.uint16)
    unique: list[int] = []
    mask_ids: dict[int, int] = {}

    metadata = []
    for site in model.sites:
        parents = model.parents[site]
        metadata.append((
            sum(1 << comb_index[parent] for parent in parents.comb),
            sum(1 << phase_index[parent] for parent in parents.phase),
            sum(1 << model.index[parent] for parent in parents.downstream),
        ))

    for state_index, comb_mask in enumerate(states):
        phase_mask = phase_availability.availability_masks[
            int(phase_availability.availability_ids[state_index])
        ]
        down_mask = 0
        for bit, (comb_required, phase_required, down_required) in enumerate(metadata):
            if (
                comb_mask & comb_required == comb_required
                and phase_mask & phase_required == phase_required
                and down_mask & down_required == down_required
            ):
                down_mask |= 1 << bit
        if down_mask not in mask_ids:
            mask_ids[down_mask] = len(unique)
            unique.append(down_mask)
        masks[state_index] = down_mask
        ids[state_index] = mask_ids[down_mask]
    return DownAvailability(masks, ids, tuple(unique))


@dataclass(frozen=True)
class ScanResult:
    interface_candidates: int
    retained_candidates: int
    contexts: int
    certified_wrong_contexts: int
    certified_wrong_classes: int
    feasible_wrong_contexts: int
    feasible_wrong_classes: tuple[tuple[Coord, str, tuple[str, ...], str | None], ...]
    certified_conflicts: int
    feasible_conflicts: int
    certified_comb_blockers: int
    feasible_comb_blockers: int
    certified_phase_blockers: int
    feasible_phase_blockers: int


def mixed_scan(
    states: tuple[int, ...],
    phase_availability: c70.Availability,
    model: DownModel,
    down_availability: DownAvailability,
) -> ScanResult:
    fixed = c60.CONSTRUCTION.base
    comb = c60.CONSTRUCTION.allowed
    phase = c67.ALLOWED
    down = model.construction.allowed
    comb_sites = tuple(sorted(comb))
    comb_index = {site: bit for bit, site in enumerate(comb_sites)}
    phase_index = phase_availability.phase_index
    down_index = model.index

    raw_tables = {
        "C60": c70.raw_outputs(c60.CONSTRUCTION.table),
        "C67": c70.raw_outputs(c67.RULES),
        "DOWN": c70.raw_outputs(model.construction.new_table),
    }
    all_raw = set().union(*(set(table) for table in raw_tables.values()))
    expected_map = dict(comb)
    expected_map.update(phase)
    expected_map.update(down)

    _, _, phase_must, _, _ = c67.causal_safety_certificate(c67.compile_conditions())
    must = dict(phase_must)
    must.update({site: model.must[site] for site in down})

    occupied = set(fixed) | set(comb) | set(phase) | set(down)
    interface = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in fixed
    }

    retained = []
    for target in interface:
        variables = tuple(
            neighbour
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in comb
            or neighbour in phase
            or neighbour in down
        )
        fixed_parts = tuple(
            (direction, fixed[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in fixed
        )
        possible = False
        for mask in range(1 << len(variables)):
            signature = tuple(sorted(
                list(fixed_parts)
                + [
                    (
                        next(direction for direction in c53.DIRECTIONS if c53.add(target, direction) == site),
                        (comb | phase | down)[site],
                    )
                    for bit, site in enumerate(variables)
                    if mask & (1 << bit)
                ]
            ))
            if signature in all_raw:
                possible = True
                break
        later_neighbours = any(site in phase or site in down for site in variables)
        phase_later_neighbours = any(site in down for site in variables)
        if possible or (target in comb and later_neighbours) or (target in phase and phase_later_neighbours):
            retained.append(target)

    contexts = certified_wrong = feasible_wrong = 0
    certified_conflicts = feasible_conflicts = 0
    certified_comb_blockers = feasible_comb_blockers = 0
    certified_phase_blockers = feasible_phase_blockers = 0
    certified_classes: set[tuple[Coord, str, tuple[str, ...], str | None]] = set()
    feasible_classes: set[tuple[Coord, str, tuple[str, ...], str | None]] = set()

    phase_ids = phase_availability.availability_ids.astype(np.uint64)
    down_ids = down_availability.ids.astype(np.uint64)
    comb_masks_array = phase_availability.comb_masks

    for target in retained:
        comb_neighbours = tuple(
            (direction, neighbour, comb[neighbour], 1 << comb_index[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in comb
        )
        phase_neighbours = tuple(
            (direction, neighbour, phase[neighbour], 1 << phase_index[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in phase
        )
        down_neighbours = tuple(
            (direction, neighbour, down[neighbour], 1 << down_index[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in down
        )
        fixed_parts = tuple(
            (direction, fixed[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in fixed
        )

        compressed_comb = np.zeros(len(states), dtype=np.uint64)
        for bit, (_, _, _, global_bit) in enumerate(comb_neighbours):
            compressed_comb |= (
                ((comb_masks_array & np.uint64(global_bit)) != 0).astype(np.uint64)
                << bit
            )
        codes = (down_ids << 22) | (phase_ids << 6) | compressed_comb
        if target in comb_index:
            target_bit = np.uint64(1 << comb_index[target])
            codes = np.where(
                (comb_masks_array & target_bit) != 0,
                np.uint64((1 << 64) - 1),
                codes,
            )

        for code in np.unique(codes):
            if code == np.uint64((1 << 64) - 1):
                continue
            comb_local = int(code & 63)
            phase_id = int((code >> 6) & ((1 << 16) - 1))
            down_id = int(code >> 22)
            phase_max = phase_availability.availability_masks[phase_id]
            down_max = down_availability.unique_masks[down_id]
            phase_local_max = sum(
                1 << bit
                for bit, (_, _, _, global_bit) in enumerate(phase_neighbours)
                if phase_max & global_bit
            )
            down_local_max = sum(
                1 << bit
                for bit, (_, _, _, global_bit) in enumerate(down_neighbours)
                if down_max & global_bit
            )

            phase_local = phase_local_max
            while True:
                down_local = down_local_max
                while True:
                    contexts += 1
                    signature_parts = list(fixed_parts)
                    present_later: set[Coord] = set()
                    absent_later: set[Coord] = set()
                    for bit, (direction, _, output, _) in enumerate(comb_neighbours):
                        if comb_local & (1 << bit):
                            signature_parts.append((direction, output))
                    for bit, (direction, site, output, _) in enumerate(phase_neighbours):
                        if phase_local & (1 << bit):
                            signature_parts.append((direction, output))
                            present_later.add(site)
                        else:
                            absent_later.add(site)
                    for bit, (direction, site, output, _) in enumerate(down_neighbours):
                        if down_local & (1 << bit):
                            signature_parts.append((direction, output))
                            present_later.add(site)
                        else:
                            absent_later.add(site)
                    if target in phase or target in down:
                        absent_later.add(target)
                    signature = tuple(sorted(signature_parts))
                    witness = next((
                        (present, ancestor)
                        for present in present_later
                        for ancestor in must[present].intersection(absent_later)
                    ), None)

                    merged = {
                        source_name: outputs
                        for source_name, table in raw_tables.items()
                        if (outputs := table.get(signature))
                    }
                    outputs_union = set().union(*merged.values()) if merged else set()
                    if len(outputs_union) > 1:
                        if witness is None:
                            feasible_conflicts += 1
                        else:
                            certified_conflicts += 1
                    expected = expected_map.get(target)
                    for source_name, outputs in merged.items():
                        if outputs == (frozenset((expected,)) if expected is not None else frozenset()):
                            continue
                        row = (target, source_name, tuple(sorted(outputs)), expected)
                        if witness is None:
                            feasible_wrong += 1
                            feasible_classes.add(row)
                        else:
                            certified_wrong += 1
                            certified_classes.add(row)

                    if target in comb and present_later:
                        stripped = tuple(
                            item for item in signature
                            if c53.add(target, item[0]) not in phase
                            and c53.add(target, item[0]) not in down
                        )
                        if stripped in raw_tables["C60"] and signature not in raw_tables["C60"]:
                            if witness is None:
                                feasible_comb_blockers += 1
                            else:
                                certified_comb_blockers += 1
                    if target in phase and any(site in down for site in present_later):
                        stripped = tuple(
                            item for item in signature
                            if c53.add(target, item[0]) not in down
                        )
                        if stripped in raw_tables["C67"] and signature not in raw_tables["C67"]:
                            if witness is None:
                                feasible_phase_blockers += 1
                            else:
                                certified_phase_blockers += 1

                    if down_local == 0:
                        break
                    down_local = (down_local - 1) & down_local_max
                if phase_local == 0:
                    break
                phase_local = (phase_local - 1) & phase_local_max

    return ScanResult(
        len(interface), len(retained), contexts,
        certified_wrong, len(certified_classes),
        feasible_wrong, tuple(sorted(feasible_classes)),
        certified_conflicts, feasible_conflicts,
        certified_comb_blockers, feasible_comb_blockers,
        certified_phase_blockers, feasible_phase_blockers,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    check("A01 note exists", NOTE.is_file())
    check("A02 proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)

    conditions = c67.compile_conditions()
    _, witnesses, phase_must, _, _ = c67.causal_safety_certificate(conditions)
    check("A03 Cycle-67 first-bad certificate remains exact", len(witnesses) == 47)
    states = c70.reachable_cycle60_states()
    check("A04 all Cycle-60 states are retained", len(states) == 242_033, f"{len(states):,}")
    phase_availability = c70.phase_availability(states)
    check("A05 exact Cycle-67 availability has 67 masks", len(phase_availability.availability_masks) == 67)

    baseline_model = downstream_model(c72.CONSTRUCTION, phase_must)
    baseline_availability = downstream_availability(states, phase_availability, baseline_model)
    baseline = mixed_scan(states, phase_availability, baseline_model, baseline_availability)
    print("BASELINE", baseline)

    by_signature = key(REPAIRED.source, (1, 1, 0))
    with_by = dict(REPAIRED.source)
    with_by[(1, 1, 0)] = "B1"
    dy_signature = key(with_by, (2, 1, 0))
    check("B01 early BY row is base-H1 pair plus Z_A singleton", set(value for _, value in by_signature) == {"H1", "Z_A"} and REPAIRED.stage_aliases["BY"] == ((1, 1, 0),))
    check("B02 repaired DY row is X_B+B1 singleton", set(value for _, value in dy_signature) == {"X_B", "B1"} and REPAIRED.stage_aliases["DY"] == ((2, 1, 0),))
    check("B03 DZ remains X_B+L10 singleton", REPAIRED.stage_aliases["DZ"] == ((2, 0, 1),))

    repaired_raw = c70.raw_outputs(REPAIRED.new_table)
    raw_domains = (
        set(c70.raw_outputs(c60.CONSTRUCTION.table)),
        set(c70.raw_outputs(c67.RULES)),
        set(repaired_raw),
    )
    check("C01 repaired table is 27 canonical / 630 raw rows", (len(REPAIRED.new_table), len(repaired_raw)) == (27, 630), str((len(REPAIRED.new_table), len(repaired_raw))))
    check("C02 repaired union is 147 canonical / 3,224 raw rows", (len(REPAIRED.union_table), len(c70.raw_outputs(REPAIRED.union_table))) == (147, 3_224), str((len(REPAIRED.union_table), len(c70.raw_outputs(REPAIRED.union_table)))))
    check("C03 all repaired raw domains are pairwise disjoint", all(raw_domains[i].isdisjoint(raw_domains[j]) for i in range(3) for j in range(i + 1, 3)))
    check("C04 repair adds no record or site", len(REPAIRED.allowed) == len(c72.CONSTRUCTION.allowed) == 31)

    graph = c63.exact_graph(REPAIRED.source, REPAIRED.union_table, REPAIRED.allowed)
    complete = (1 << len(graph.sites)) - 1
    check("D01 repaired terminal graph has 50 conditions", graph.conditions == 50, str(graph.conditions))
    check("D02 repaired terminal graph has 475 states", len(graph.states) == 475, f"{len(graph.states):,}")
    check("D03 repaired terminal graph has 1,339 edges", graph.edges == 1_339, f"{graph.edges:,}")
    check("D04 repaired terminal graph has one complete terminal", graph.terminals == (complete,))
    check("D05 repaired terminal graph has no parasite/conflict", not graph.parasites and not graph.conflicts)

    repaired_model = downstream_model(REPAIRED, phase_must)
    repaired_availability = downstream_availability(states, phase_availability, repaired_model)
    repaired = mixed_scan(states, phase_availability, repaired_model, repaired_availability)
    print("REPAIRED", repaired)

    check("E01 baseline census is 19,240 contexts / 203 apparent / one feasible", (baseline.contexts, baseline.certified_wrong_contexts, baseline.certified_wrong_classes, baseline.feasible_wrong_contexts) == (19_240, 203, 48, 1), str(baseline))
    check("E02 baseline feasible class is the Z_C theft", baseline.feasible_wrong_classes == (((3, 0, 0), "DOWN", ("D1",), "Z_C"),), str(baseline.feasible_wrong_classes))
    check("E03 repaired census preserves 19,240 / 203 / 48 and removes the feasible write", (repaired.contexts, repaired.certified_wrong_contexts, repaired.certified_wrong_classes, repaired.feasible_wrong_contexts) == (19_240, 203, 48, 0), str(repaired))
    check("E04 repaired scan has no feasible wrong class", repaired.feasible_wrong_classes == (), str(repaired.feasible_wrong_classes))
    check("E05 repaired scan has no feasible raw conflict", repaired.feasible_conflicts == 0)
    check("E06 repaired scan has no feasible comb blocker", repaired.feasible_comb_blockers == 0)
    check("E07 repaired scan has no feasible Cycle-67 blocker", repaired.feasible_phase_blockers == 0)

    print(f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
