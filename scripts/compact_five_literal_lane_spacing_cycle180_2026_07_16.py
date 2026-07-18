#!/usr/bin/env python3
"""Cycle 180: compact-spacing boundary for the Cycle-178 literal bundle.

The probe keeps the Cycle-178 law, rail orientation, source template, output
template, and five ordered H0/H1 lanes fixed.  It sweeps the common transverse
lane spacing, identifies the first spacing with disjoint source ownership, and
then reruns all 32 words at that spacing.

The result is deliberately construction-bounded.  It is a compactability
certificate for five unchanged translated rails, not a universal lower bound
on encodings and not a generated binding theorem.

This runner has no authority.  It edits no foundation, axiom, primitive,
registry, policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import recurrent_carrier_matter_kinematics_cycle172_2026_07_16 as c172
import recurrent_five_literal_lane_worldline_cycle178_2026_07_16 as c178


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPACT_FIVE_LITERAL_LANE_SPACING_CYCLE180_NOTE_2026-07-16.md"
)

Coord = tuple[int, int, int]
RoleMap = dict[Coord, str]
ExitMap = dict[Coord, frozenset[str]]

WORDS = c178.WORDS
BIT_ROLES = c178.BIT_ROLES
REFERENCE_SPACING = c178.LANE_SPACING
SEARCH_SPACINGS = tuple(range(1, REFERENCE_SPACING + 1))

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def offsets(spacing: int) -> tuple[Coord, ...]:
    return tuple((0, spacing * lane, 0) for lane in range(5))


def translate(records, offset: Coord):
    return {
        c172.shift(site, offset): value
        for site, value in records.items()
    }


def source_parts(
    word: tuple[int, ...],
    spacing: int,
) -> tuple[RoleMap, ...]:
    return tuple(
        translate(c172.source(c178.bit_role(bit)), offset)
        for bit, offset in zip(word, offsets(spacing), strict=True)
    )


def output_parts(
    word: tuple[int, ...],
    spacing: int,
) -> tuple[RoleMap, ...]:
    return tuple(
        translate(c172.outputs(c178.bit_role(bit)), offset)
        for bit, offset in zip(word, offsets(spacing), strict=True)
    )


def exit_parts(spacing: int) -> tuple[ExitMap, ...]:
    return tuple(
        translate(c172.EXITS, offset)
        for offset in offsets(spacing)
    )


def ownership_collisions(parts) -> tuple[tuple[Coord, tuple], ...]:
    owners = defaultdict(list)
    for lane, records in enumerate(parts):
        for site, role in records.items():
            owners[site].append((lane, role))
    return tuple(
        (site, tuple(entries))
        for site, entries in sorted(owners.items())
        if len(entries) > 1
    )


def merge_disjoint(parts):
    collisions = ownership_collisions(parts)
    if collisions:
        raise ValueError(("ownership-collisions", collisions[:4]))
    merged = {}
    for records in parts:
        merged.update(records)
    return merged


def record_owners(
    source_lanes: tuple[RoleMap, ...],
    output_lanes: tuple[RoleMap, ...],
) -> tuple[dict[Coord, int], tuple]:
    owners = {}
    conflicts = []
    for lane, records in enumerate(source_lanes):
        for site in records:
            previous = owners.setdefault(site, lane)
            if previous != lane:
                conflicts.append((site, previous, lane, "source"))
    for lane, records in enumerate(output_lanes):
        for site in records:
            previous = owners.setdefault(site, lane)
            if previous != lane:
                conflicts.append((site, previous, lane, "output"))
    return owners, tuple(conflicts)


def source_collision_profile(spacing: int):
    # Payload value changes only the seed role, not source geometry.  H0 is
    # therefore sufficient for the exact ownership-spacing census.
    return ownership_collisions(source_parts((0, 0, 0, 0, 0), spacing))


SOURCE_COLLISIONS = {
    spacing: source_collision_profile(spacing)
    for spacing in SEARCH_SPACINGS
}
MINIMUM_DISJOINT_SPACING = next(
    spacing
    for spacing in SEARCH_SPACINGS
    if not SOURCE_COLLISIONS[spacing]
)
FIRST_FAILED_SPACING = MINIMUM_DISJOINT_SPACING - 1
FIRST_FAILURES = SOURCE_COLLISIONS[FIRST_FAILED_SPACING]


def minimum_interlane_l1(parts) -> int:
    return min(
        abs(left[0] - right[0])
        + abs(left[1] - right[1])
        + abs(left[2] - right[2])
        for lane, left_records in enumerate(parts)
        for right_records in parts[lane + 1 :]
        for left in left_records
        for right in right_records
    )


def compact_bundle(word: tuple[int, ...], spacing: int):
    sources = source_parts(word, spacing)
    outputs = output_parts(word, spacing)
    exits = exit_parts(spacing)
    initial = merge_disjoint(sources)
    expected = merge_disjoint(outputs)
    terminal = merge_disjoint(exits)
    owners, owner_conflicts = record_owners(sources, outputs)
    if owner_conflicts:
        raise ValueError(("record-owner-conflicts", owner_conflicts[:4]))
    return sources, outputs, initial, expected, terminal, owners


def dependency_scope(certificate, owners):
    cross_lane = []
    missing = []
    multi_lane_targets = []
    for target, parents in certificate["dependencies"].items():
        target_owner = owners.get(target)
        if target_owner is None:
            missing.append(("target", target))
            continue
        parent_lanes = set()
        for parent in parents:
            parent_owner = owners.get(parent)
            if parent_owner is None:
                missing.append(("parent", parent))
                continue
            parent_lanes.add(parent_owner)
            if parent_owner != target_owner:
                cross_lane.append((parent, target, parent_owner, target_owner))
        if len(parent_lanes) > 1:
            multi_lane_targets.append((target, tuple(sorted(parent_lanes))))
    return tuple(cross_lane), tuple(missing), tuple(multi_lane_targets)


def payload_sites(lane: int, spacing: int) -> tuple[Coord, ...]:
    offset = offsets(spacing)[lane]
    return tuple(
        c172.shift(c172.payload_site(x), offset)
        for x in range(c172.SEED_X, c172.COPY_X[-1] + 1)
    )


def lineage_certificate(
    certificate,
    initial: RoleMap,
    expected: RoleMap,
    spacing: int,
):
    direct = c172.direct_parents(
        initial,
        expected,
        certificate["dependencies"],
    )
    failures = []
    endpoints = []
    for lane in range(5):
        payloads = payload_sites(lane, spacing)
        payload_set = set(payloads)
        children = {site: [] for site in payloads}
        for index, target in enumerate(payloads[1:], 1):
            parents = tuple(sorted(direct[target] & payload_set))
            if parents != (payloads[index - 1],):
                failures.append(("parents", lane, target, parents))
            for parent in parents:
                children[parent].append(target)
        lane_endpoints = tuple(
            site
            for site, descendants in children.items()
            if not descendants
        )
        if lane_endpoints != (payloads[-1],):
            failures.append(("endpoints", lane, lane_endpoints))
        endpoints.extend(lane_endpoints)
    return tuple(failures), tuple(endpoints)


def y_width(records) -> int:
    ys = tuple(site[1] for site in records)
    return max(ys) - min(ys) + 1


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    old_full_raw = c178.c171.FULL_RAW
    c178.c171.FULL_RAW = c178.FULL_RAW
    try:
        print("AUTHORITY AND FIXED CONSTRUCTION")
        check("Cycle-180 review note exists", NOTE.is_file())
        check(
            "the probe keeps the Cycle-178 law and literal alphabet fixed",
            BIT_ROLES == (c178.H0, c178.H1)
            and len(c178.BIT_CARRIER_TABLE) == 12
            and len(c178.BIT_CARRIER_RAW) == 288
            and len(c178.FULL_RAW) == 101_996
            and not c178.RAW_CONFLICTS,
            (
                BIT_ROLES,
                len(c178.BIT_CARRIER_TABLE),
                len(c178.BIT_CARRIER_RAW),
                len(c178.FULL_RAW),
            ),
        )

        print("\nEXACT SPACING SWEEP")
        check(
            "spacing 12 is the first disjoint five-source translation",
            MINIMUM_DISJOINT_SPACING == 12
            and all(SOURCE_COLLISIONS[spacing] for spacing in range(1, 12))
            and all(
                not SOURCE_COLLISIONS[spacing]
                for spacing in range(12, REFERENCE_SPACING + 1)
            ),
            (
                MINIMUM_DISJOINT_SPACING,
                {
                    spacing: len(SOURCE_COLLISIONS[spacing])
                    for spacing in range(8, 13)
                },
            ),
        )
        first_failure_roles = Counter(
            tuple(role for _lane, role in entries)
            for _site, entries in FIRST_FAILURES
        )
        check(
            "spacing 11 fails by eight hard adjacent source-role collisions",
            FIRST_FAILED_SPACING == 11
            and len(FIRST_FAILURES) == 8
            and first_failure_roles == {("R_B32", "L6"): 8}
            and {
                tuple(lane for lane, _role in entries)
                for _site, entries in FIRST_FAILURES
            } == {(0, 1), (1, 2), (2, 3), (3, 4)},
            (FIRST_FAILED_SPACING, first_failure_roles, FIRST_FAILURES),
        )
        compact_sources = source_parts((0, 0, 0, 0, 0), 12)
        check(
            "the compact sources are disjoint but nearest-neighbor adjacent",
            not ownership_collisions(compact_sources)
            and minimum_interlane_l1(compact_sources) == 1,
            minimum_interlane_l1(compact_sources),
        )

        print("\nALL-32 COMPACT CAUSAL CERTIFICATES")
        shapes = Counter()
        failures = {}
        cross_lane_edges = []
        missing_owners = []
        multi_lane_targets = []
        lineage_failures = []
        endpoint_sets = set()
        for word in WORDS:
            (
                _source_lanes,
                _output_lanes,
                initial,
                expected,
                terminal,
                owners,
            ) = compact_bundle(word, MINIMUM_DISJOINT_SPACING)
            certificate = c178.c171.causal_certificate(
                initial,
                expected,
                terminal,
            )
            if not certificate["ok"]:
                failures[word] = certificate
                continue
            shapes[(
                certificate["minimum"]["states"],
                certificate["edge_checks"]["edges"],
                certificate["minimum"]["max_frontier"],
                certificate["maximum"]["max_frontier"],
                len(certificate["unordered"]),
                len(certificate["minimum"]["terminal"]),
            )] += 1
            cross, missing, multi = dependency_scope(certificate, owners)
            cross_lane_edges.extend((word, edge) for edge in cross)
            missing_owners.extend((word, item) for item in missing)
            multi_lane_targets.extend((word, item) for item in multi)
            lineage_bad, endpoints = lineage_certificate(
                certificate,
                initial,
                expected,
                MINIMUM_DISJOINT_SPACING,
            )
            lineage_failures.extend((word, item) for item in lineage_bad)
            endpoint_sets.add(endpoints)
        check(
            "all 32 words retain the exact Cycle-178 causal shape at spacing 12",
            not failures
            and shapes == {(1_521, 3_455, 18, 16, 0, 10): 32},
            (shapes, tuple(failures)[:2]),
        )
        check(
            "all five compact payload lineages remain exact and disjoint",
            not lineage_failures
            and endpoint_sets
            == {
                tuple(
                    c172.shift(
                        c172.payload_site(c172.COPY_X[-1]),
                        offset,
                    )
                    for offset in offsets(MINIMUM_DISJOINT_SPACING)
                )
            },
            (tuple(lineage_failures)[:3], endpoint_sets),
        )
        check(
            "the compact causal graph has zero cross-lane ancestry",
            not cross_lane_edges
            and not missing_owners
            and not multi_lane_targets,
            (
                tuple(cross_lane_edges)[:3],
                tuple(missing_owners)[:3],
                tuple(multi_lane_targets)[:3],
            ),
        )
        check(
            "the five-lane graph factorizes exactly into five single-lane graphs",
            next(iter(shapes), None)
            == (
                5 * (305 - 1) + 1,
                5 * 691,
                18,
                16,
                0,
                5 * 2,
            ),
            next(iter(shapes), None),
        )

        print("\nCOMPACTION AND BINDING STATUS")
        compact_initial = merge_disjoint(
            source_parts((1, 0, 1, 0, 1), MINIMUM_DISJOINT_SPACING)
        )
        reference_initial = merge_disjoint(
            source_parts((1, 0, 1, 0, 1), REFERENCE_SPACING)
        )
        check(
            "transverse source width falls from 813 to 61 sites",
            y_width(reference_initial) == 813
            and y_width(compact_initial) == 61
            and 4 * MINIMUM_DISJOINT_SPACING == 48
            and 4 * REFERENCE_SPACING == 800,
            (
                y_width(reference_initial),
                y_width(compact_initial),
                4 * REFERENCE_SPACING,
                4 * MINIMUM_DISJOINT_SPACING,
            ),
        )
        check(
            "compaction generates no common binding or membership target",
            not cross_lane_edges and not multi_lane_targets,
            (
                len(cross_lane_edges),
                len(multi_lane_targets),
            ),
        )

        print("\nSCOPE AND NO-GO DISCIPLINE")
        note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
        normalized_note = " ".join(note.split())
        check(
            "the note freezes the construction-bounded scope and N1-N8 gate",
            "f8af74c263" in normalized_note
            and "2a8ecad9e8f5" in normalized_note
            and "c36131ceddf4" in normalized_note
            and "construction-bounded minimum" in normalized_note
            and "not a universal lower bound" in normalized_note
            and "runner-supplied bundle membership" in normalized_note
            and "generated join tree" in normalized_note
            and all(f"N{index}" in normalized_note for index in range(1, 9))
            and "No axiom addition follows" in normalized_note,
        )

        print("\nACCOUNTING")
        print("REFERENCE_SPACING", REFERENCE_SPACING)
        print("MINIMUM_DISJOINT_SPACING", MINIMUM_DISJOINT_SPACING)
        print("FIRST_FAILED_SPACING", FIRST_FAILED_SPACING)
        print("FIRST_FAILURES", FIRST_FAILURES)
        print("COMPACT_OFFSETS", offsets(MINIMUM_DISJOINT_SPACING))
        print("BUNDLE_SHAPES", shapes)
        print("CROSS_LANE_EDGES", len(cross_lane_edges))
        print("MULTI_LANE_TARGETS", len(multi_lane_targets))
        print("PASS", PASS, "FAIL", FAIL)
        print(
            "RESULT",
            "CONSTRUCTION_BOUNDED_COMPACT_FIVE_LITERAL_BUNDLE"
            if FAIL == 0
            else "CYCLE180_OPEN",
        )
        return int(FAIL != 0)
    finally:
        c178.c171.FULL_RAW = old_full_raw


if __name__ == "__main__":
    raise SystemExit(main())
