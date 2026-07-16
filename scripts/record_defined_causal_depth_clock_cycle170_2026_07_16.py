#!/usr/bin/env python3
"""Cycle 170: record-defined causal depth for the Cycle-166 apparatus.

The clock used here is the longest-path depth of the actual declared
dependency DAG. Initial records are layer zero. Every dynamic record has depth
one plus the maximum depth of its dynamic parents, with roots at depth one.

This is a finite operational commit-depth certificate for one candidate law.
It is not a continuous rate, metric time, or a new axiom.
"""

from __future__ import annotations

import hashlib
from collections import Counter, defaultdict, deque
from pathlib import Path

import physical_joint_stabilizer_update_geometry_probe_2026_07_16 as p


Coord = tuple[int, int, int]
Case = tuple[int, int]

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md"
)
PARALLEL_SHIFT: Coord = (2000, 0, 0)
SERIAL_SHIFT: Coord = (4000, 0, 0)
ROTATION_SHIFT: Coord = (1201, -1213, 1217)

EXPECTED = {
    (0, 0): {
        "nodes": 30_633,
        "edges": 30_636,
        "roots": 15,
        "sinks": 5,
        "output_depths": (4_036, 3_970),
        "depth": 4_036,
        "output_ancestors": 22_317,
        "profile_hash": (
            "d13aeee419088ef5c052c6fd5aacd241574a48ae2209c84a074e323c2e4e0627"
        ),
    },
    (0, 1): {
        "nodes": 30_637,
        "edges": 30_640,
        "roots": 15,
        "sinks": 5,
        "output_depths": (4_036, 3_974),
        "depth": 4_036,
        "output_ancestors": 22_807,
        "profile_hash": (
            "2172b45e39b58351779b89f118df3842caf0109c41adb25d9e9c53add66e331f"
        ),
    },
    (1, 0): {
        "nodes": 30_703,
        "edges": 30_706,
        "roots": 15,
        "sinks": 5,
        "output_depths": (4_106, 3_970),
        "depth": 4_106,
        "output_ancestors": 23_021,
        "profile_hash": (
            "741637eb0dd40958c5b9892572c7b6402664ace49c86c99aca20138980420bd2"
        ),
    },
    (1, 1): {
        "nodes": 30_831,
        "edges": 30_834,
        "roots": 15,
        "sinks": 5,
        "output_depths": (4_106, 4_098),
        "depth": 4_106,
        "output_ancestors": 25_958,
        "profile_hash": (
            "ec6fcee756ac9fb9f222dc90e95efdab6fa989004e8b4e47a70efc6b08ae6d53"
        ),
    },
}

COMMON_PROFILE = (
    (1, 1, 15),
    (2, 11, 19),
    (12, 411, 22),
    (412, 427, 20),
    (428, 435, 18),
    (436, 491, 16),
    (492, 1149, 14),
    (1150, 1227, 13),
    (1228, 1269, 12),
    (1270, 1331, 11),
    (1332, 1399, 10),
    (1400, 1424, 9),
    (1425, 1498, 8),
    (1499, 1545, 7),
    (1546, 1669, 6),
    (1670, 1984, 5),
    (1985, 2058, 4),
    (2059, 2305, 3),
    (2306, 2630, 2),
    (2631, 2908, 3),
)
EXPECTED_PROFILES = {
    (0, 0): COMMON_PROFILE + ((2909, 3970, 2), (3971, 4036, 1)),
    (0, 1): COMMON_PROFILE + ((2909, 3974, 2), (3975, 4036, 1)),
    (1, 0): COMMON_PROFILE + ((2909, 3970, 2), (3971, 4106, 1)),
    (1, 1): COMMON_PROFILE + ((2909, 4098, 2), (4099, 4106, 1)),
}

EXPECTED_BASE_WORK = {
    (0, 0): (269_149, 263_639),
    (0, 1): (268_513, 263_651),
    (1, 0): (269_499, 263_303),
    (1, 1): (269_435, 263_687),
}
EXPECTED_ROTATION_WORK = {
    (0, 0): (252_122, 399_165, 252_122, 398_786, 24, 24),
    (0, 1): (251_170, 399_169, 251_170, 398_790, 24, 24),
    (1, 0): (250_974, 399_305, 250_974, 398_926, 24, 24),
    (1, 1): (250_718, 399_433, 250_718, 399_054, 24, 24),
}

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


def moved(site: Coord, shift: Coord) -> Coord:
    return p.add(site, shift)


def outputs() -> tuple[Coord, Coord]:
    return tuple(
        p.MUX[label]["common"] for label in ("lane1", "lane2")
    )  # type: ignore[return-value]


def compress_profile(profile: Counter[int]) -> tuple[tuple[int, int, int], ...]:
    maximum = max(profile)
    runs = []
    start = 1
    prior = profile[1]
    for depth in range(2, maximum + 1):
        value = profile[depth]
        if value != prior:
            runs.append((start, depth - 1, prior))
            start = depth
            prior = value
    runs.append((start, maximum, prior))
    return tuple(runs)


def profile_hash(profile: Counter[int]) -> str:
    values = ",".join(
        str(profile[depth]) for depth in range(1, max(profile) + 1)
    )
    return hashlib.sha256(values.encode("utf-8")).hexdigest()


def dag_certificate(
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    output_sites: tuple[Coord, ...],
) -> dict[str, object]:
    if set(expected) != set(dependencies):
        raise AssertionError(("domain-mismatch", len(expected), len(dependencies)))
    missing = {
        parent
        for parents in dependencies.values()
        for parent in parents
        if parent not in expected
    }
    if missing:
        raise AssertionError(("missing-dynamic-parent", tuple(sorted(missing))[:3]))

    children: dict[Coord, list[Coord]] = defaultdict(list)
    indegree = {
        site: len(parents) for site, parents in dependencies.items()
    }
    edge_count = 0
    for site, parents in dependencies.items():
        edge_count += len(parents)
        for parent in parents:
            children[parent].append(site)

    ready = deque(sorted(site for site, count in indegree.items() if count == 0))
    depth: dict[Coord, int] = {}
    longest_parent: dict[Coord, Coord | None] = {}
    profile: Counter[int] = Counter()
    while ready:
        site = ready.popleft()
        parents = dependencies[site]
        if parents:
            parent = max(parents, key=lambda value: (depth[value], value))
            value = depth[parent] + 1
            longest_parent[site] = parent
        else:
            value = 1
            longest_parent[site] = None
        depth[site] = value
        profile[value] += 1
        for child in children[site]:
            indegree[child] -= 1
            if indegree[child] == 0:
                ready.append(child)

    if len(depth) != len(expected):
        raise AssertionError(("dependency-cycle", len(depth), len(expected)))

    roots = frozenset(site for site, parents in dependencies.items() if not parents)
    parent_sites = {
        parent for parents in dependencies.values() for parent in parents
    }
    sinks = frozenset(set(expected) - parent_sites)
    output_depths = tuple(depth[site] for site in output_sites)
    latest_output = (
        max(output_sites, key=lambda site: (depth[site], site))
        if output_sites
        else None
    )
    chain = []
    site: Coord | None = latest_output
    while site is not None:
        chain.append(site)
        site = longest_parent[site]
    chain.reverse()

    ancestors = set()
    pending = list(output_sites)
    while pending:
        site = pending.pop()
        if site in ancestors:
            continue
        ancestors.add(site)
        pending.extend(dependencies[site])

    return {
        "nodes": len(expected),
        "edges": edge_count,
        "roots": roots,
        "sinks": sinks,
        "depth": max(depth.values()),
        "depth_by_site": depth,
        "profile": profile,
        "compressed_profile": compress_profile(profile),
        "profile_hash": profile_hash(profile),
        "output_depths": output_depths,
        "latest_output": latest_output,
        "critical_chain": tuple(chain),
        "output_ancestors": frozenset(ancestors),
    }


def linear_schedule(
    dependencies: dict[Coord, frozenset[Coord]],
    order: str,
) -> tuple[tuple[Coord, ...], int, int]:
    children: dict[Coord, list[Coord]] = defaultdict(list)
    pending = {
        site: len(parents) for site, parents in dependencies.items()
    }
    for site, parents in dependencies.items():
        for parent in parents:
            children[parent].append(site)
    frontier = {site for site, count in pending.items() if count == 0}
    schedule = []
    frontier_work = 0
    maximum_frontier = 0
    while frontier:
        frontier_work += len(frontier)
        maximum_frontier = max(maximum_frontier, len(frontier))
        if order == "min":
            site = min(frontier)
        elif order == "max":
            site = max(frontier)
        else:
            raise ValueError(("unknown-order", order))
        frontier.remove(site)
        schedule.append(site)
        for child in children[site]:
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
    return tuple(schedule), frontier_work, maximum_frontier


def all_edge_availability_audit(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    certificate: dict[str, object],
) -> tuple[int, tuple[object, ...]]:
    depths = certificate["depth_by_site"]
    failures = []
    edge_count = 0
    for child, parents in dependencies.items():
        earlier_neighbors = {
            neighbor
            for direction in p.c53.DIRECTIONS
            if (
                (neighbor := p.add(child, direction)) in expected
                and depths[neighbor] < depths[child]
            )
        }
        if earlier_neighbors != set(parents):
            failures.append(
                (
                    "earlier-neighbor-mismatch",
                    child,
                    tuple(sorted(earlier_neighbors - set(parents)))[:2],
                    tuple(sorted(set(parents) - earlier_neighbors))[:2],
                )
            )

        records = {
            neighbor: initial[neighbor]
            for direction in p.c53.DIRECTIONS
            if (neighbor := p.add(child, direction)) in initial
        }
        records.update({parent: expected[parent] for parent in parents})
        complete_signature = p.c53.local_signature(records, child)
        complete_outputs = p.MERGED_RAW.get(
            complete_signature,
            frozenset(),
        )
        if complete_outputs != frozenset((expected[child],)):
            failures.append(
                (
                    "complete-signature",
                    child,
                    expected[child],
                    complete_outputs,
                )
            )

        for parent in parents:
            edge_count += 1
            role = records.pop(parent)
            cut_signature = p.c53.local_signature(records, child)
            cut_outputs = p.MERGED_RAW.get(cut_signature, frozenset())
            records[parent] = role
            if expected[child] in cut_outputs:
                failures.append(
                    (
                        "decorative-edge",
                        child,
                        parent,
                        expected[child],
                        cut_outputs,
                    )
                )
    return edge_count, tuple(failures)


def replay_depth(
    schedule: tuple[Coord, ...],
    dependencies: dict[Coord, frozenset[Coord]],
) -> tuple[dict[Coord, int], Counter[int]]:
    depths: dict[Coord, int] = {}
    profile: Counter[int] = Counter()
    for site in schedule:
        if not dependencies[site] <= depths.keys():
            raise AssertionError(("invalid-linear-extension", site))
        value = 1 + max(
            (depths[parent] for parent in dependencies[site]),
            default=0,
        )
        depths[site] = value
        profile[value] += 1
    return depths, profile


def rotate_graph(
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    output_sites: tuple[Coord, ...],
    rotation,
) -> tuple[
    dict[Coord, str],
    dict[Coord, frozenset[Coord]],
    tuple[Coord, ...],
]:
    def transform(site: Coord) -> Coord:
        return p.add(p.c53.matvec(rotation, site), ROTATION_SHIFT)

    return (
        {transform(site): role for site, role in expected.items()},
        {
            transform(site): frozenset(transform(parent) for parent in parents)
            for site, parents in dependencies.items()
        },
        tuple(transform(site) for site in output_sites),
    )


def translate_prepared(prepared, shift: Coord):
    (
        initial,
        expected,
        dependencies,
        results,
        case,
        lane_outputs,
        selected,
        product_role,
        ports,
    ) = prepared
    return (
        {moved(site, shift): role for site, role in initial.items()},
        {moved(site, shift): role for site, role in expected.items()},
        {
            moved(site, shift): frozenset(
                moved(parent, shift) for parent in parents
            )
            for site, parents in dependencies.items()
        },
        results,
        case,
        lane_outputs,
        selected,
        product_role,
        frozenset(moved(site, shift) for site in ports),
    )


def cross_contacts(first: set[Coord], second: set[Coord]) -> int:
    directions = ((0, 0, 0), *p.c53.DIRECTIONS)
    return sum(
        p.add(site, direction) in second
        for site in first
        for direction in directions
    )


def combined_graph(prepared_items):
    initial = {}
    expected = {}
    dependencies = {}
    for prepared in prepared_items:
        item_initial, item_expected, item_dependencies, *_rest = prepared
        if set(initial) & set(item_initial):
            raise AssertionError("initial-overlap")
        if set(expected) & set(item_expected):
            raise AssertionError("dynamic-overlap")
        initial.update(item_initial)
        expected.update(item_expected)
        dependencies.update(item_dependencies)
    return initial, expected, dependencies


def synchronous_physical_run(prepared_items) -> tuple[bool, object]:
    initial, expected, dependencies = combined_graph(prepared_items)
    certificate = dag_certificate(expected, dependencies, ())
    depths = certificate["depth_by_site"]
    layers: dict[int, list[Coord]] = defaultdict(list)
    for site, depth in depths.items():
        layers[depth].append(site)

    records = dict(initial)
    actual = p.enabled(records)
    for depth in range(1, certificate["depth"] + 1):
        wanted = {
            site: frozenset((expected[site],))
            for site in layers[depth]
        }
        if actual != wanted:
            return False, (
                "frontier",
                depth,
                len(actual),
                len(wanted),
                tuple(sorted(set(actual) ^ set(wanted)))[:3],
            )
        for target in sorted(layers[depth]):
            records[target] = expected[target]
            actual.pop(target, None)
            for direction in p.c53.DIRECTIONS:
                candidate = p.add(target, direction)
                if candidate in records:
                    actual.pop(candidate, None)
                    continue
                signature = p.c53.local_signature(records, candidate)
                if signature in p.MERGED_RAW:
                    actual[candidate] = p.MERGED_RAW[signature]
                else:
                    actual.pop(candidate, None)
    return not actual, (
        len(expected),
        certificate["depth"],
        max(certificate["profile"].values()),
        len(actual),
    )


def serial_graph(
    first_expected: dict[Coord, str],
    first_dependencies: dict[Coord, frozenset[Coord]],
    first_certificate: dict[str, object],
    second_expected: dict[Coord, str],
    second_dependencies: dict[Coord, frozenset[Coord]],
) -> tuple[dict[Coord, str], dict[Coord, frozenset[Coord]], int]:
    shifted_expected = {
        moved(site, SERIAL_SHIFT): role
        for site, role in second_expected.items()
    }
    shifted_dependencies = {
        moved(site, SERIAL_SHIFT): frozenset(
            moved(parent, SERIAL_SHIFT) for parent in parents
        )
        for site, parents in second_dependencies.items()
    }
    completion = first_certificate["latest_output"]
    linked = 0
    for site, parents in tuple(shifted_dependencies.items()):
        if parents:
            continue
        shifted_dependencies[site] = frozenset((completion,))
        linked += 1
    expected = dict(first_expected)
    dependencies = dict(first_dependencies)
    expected.update(shifted_expected)
    dependencies.update(shifted_dependencies)
    return expected, dependencies, linked


def shifted_profile(
    first: Counter[int],
    second: Counter[int],
    offset: int,
) -> Counter[int]:
    result = Counter(first)
    result.update({depth + offset: count for depth, count in second.items()})
    return result


def squared_norm(vector: Coord) -> int:
    return sum(component * component for component in vector)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    prepared_by_case = {
        case: p.apparatus(*rows)
        for case, rows in p.CASE_REPRESENTATIVES.items()
    }
    output_sites = outputs()
    certificates = {}

    print("ACTUAL DEPENDENCY DAG")
    for case, prepared in prepared_by_case.items():
        initial, expected, dependencies, *_rest = prepared
        certificate = dag_certificate(expected, dependencies, output_sites)
        certificates[case] = certificate
        observed = {
            "nodes": certificate["nodes"],
            "edges": certificate["edges"],
            "roots": len(certificate["roots"]),
            "sinks": len(certificate["sinks"]),
            "output_depths": certificate["output_depths"],
            "depth": certificate["depth"],
            "output_ancestors": len(certificate["output_ancestors"]),
            "profile_hash": certificate["profile_hash"],
        }
        local_failures = [
            (site, parent)
            for site, parents in dependencies.items()
            for parent in parents
            if p.sub(site, parent) not in p.c53.DIRECTIONS
        ]
        chain = certificate["critical_chain"]
        chain_failures = [
            (prior, site)
            for prior, site in zip(chain, chain[1:])
            if prior not in dependencies[site]
            or p.sub(site, prior) not in p.c53.DIRECTIONS
        ]
        check(
            f"case {case} has the exact local causal-depth certificate",
            observed == EXPECTED[case]
            and certificate["compressed_profile"] == EXPECTED_PROFILES[case]
            and certificate["depth"] == max(certificate["output_depths"])
            and len(initial) == 379_288
            and not local_failures
            and not chain_failures
            and len(chain) == certificate["depth"],
            {
                "observed": observed,
                "profile": certificate["compressed_profile"],
                "chain_failures": chain_failures[:1],
            },
        )

    print("\nALL-EDGE AVAILABILITY AUDIT")
    all_edge_count = 0
    all_edge_failures = []
    for case, prepared in prepared_by_case.items():
        initial, expected, dependencies, *_rest = prepared
        edge_count, edge_failures = all_edge_availability_audit(
            initial,
            expected,
            dependencies,
            certificates[case],
        )
        all_edge_count += edge_count
        all_edge_failures.extend((case, failure) for failure in edge_failures)
        check(
            f"all {edge_count:,} declared dynamic edges in case {case} "
            "are load-bearing",
            edge_count == EXPECTED[case]["edges"] and not edge_failures,
            edge_failures[:2],
        )
    check(
        "all 122,816 declared dynamic edges are exact local necessities",
        all_edge_count == 122_816 and not all_edge_failures,
        {
            "edges": all_edge_count,
            "failures": all_edge_failures[:2],
        },
    )

    print("\nPROPER-CUBIC AND LINEAR-SCHEDULE INVARIANCE")
    rotation_failures = []
    rotation_work = {}
    for case, prepared in prepared_by_case.items():
        _initial, expected, dependencies, *_rest = prepared
        base = certificates[case]
        work = {"min": [], "max": []}
        for rotation_index, rotation in enumerate(p.c53.ROTATIONS):
            rotated_expected, rotated_dependencies, rotated_outputs = (
                rotate_graph(
                    expected,
                    dependencies,
                    output_sites,
                    rotation,
                )
            )
            rotated = dag_certificate(
                rotated_expected,
                rotated_dependencies,
                rotated_outputs,
            )
            if (
                rotated["compressed_profile"]
                != base["compressed_profile"]
                or rotated["profile_hash"] != base["profile_hash"]
                or rotated["output_depths"] != base["output_depths"]
                or rotated["depth"] != base["depth"]
            ):
                rotation_failures.append((case, rotation_index, "profile"))
            for order in ("min", "max"):
                schedule, frontier_work, maximum_frontier = linear_schedule(
                    rotated_dependencies,
                    order,
                )
                replayed_depths, replayed_profile = replay_depth(
                    schedule,
                    rotated_dependencies,
                )
                work[order].append((frontier_work, maximum_frontier))
                if (
                    replayed_profile != rotated["profile"]
                    or max(replayed_depths.values()) != rotated["depth"]
                ):
                    rotation_failures.append(
                        (case, rotation_index, order)
                    )
        base_min = linear_schedule(dependencies, "min")
        base_max = linear_schedule(dependencies, "max")
        work_summary = (
            min(value for value, _width in work["min"]),
            max(value for value, _width in work["min"]),
            min(value for value, _width in work["max"]),
            max(value for value, _width in work["max"]),
            len({value for value, _width in work["min"]}),
            len({value for value, _width in work["max"]}),
        )
        rotation_work[case] = work_summary
        check(
            f"case {case} has invariant depth/profile in all 24 rotations "
            "and both linear schedules",
            not any(item[0] == case for item in rotation_failures)
            and work_summary == EXPECTED_ROTATION_WORK[case]
            and (base_min[1], base_max[1]) == EXPECTED_BASE_WORK[case]
            and base_min[0] != base_max[0]
            and {
                width
                for order in ("min", "max")
                for _value, width in work[order]
            }
            == set(range(15, 21)),
            {
                "work": work_summary,
                "base_work": (base_min[1], base_max[1]),
                "failures": [
                    value for value in rotation_failures if value[0] == case
                ][:2],
            },
        )
    check(
        "all 96 case-rotation DAGs and 192 min/max replays pass",
        not rotation_failures,
        rotation_failures[:3],
    )

    print("\nRECORD-VISIBLE BRANCH REFINEMENTS")
    path_lengths = {
        label: tuple(len(path) for path in p.MUX[label]["paths"])
        for label in ("lane1", "lane2")
    }
    c00 = certificates[(0, 0)]
    c01 = certificates[(0, 1)]
    c10 = certificates[(1, 0)]
    c11 = certificates[(1, 1)]
    check(
        "the selected physical paths expose the exact 4/70/128 refinements",
        path_lengths == {
            "lane1": (404, 474),
            "lane2": (318, 322, 446),
        }
        and c01["nodes"] - c00["nodes"] == 4
        and c01["output_depths"][1] - c00["output_depths"][1] == 4
        and c01["depth"] == c00["depth"]
        and c10["nodes"] - c00["nodes"] == 70
        and c10["output_depths"][0] - c00["output_depths"][0] == 70
        and c10["depth"] - c00["depth"] == 70
        and c11["nodes"] - c10["nodes"] == 128
        and c11["output_depths"][1] - c10["output_depths"][1] == 128
        and c11["depth"] == c10["depth"],
        {
            "paths": path_lengths,
            "depths": {
                case: certificates[case]["output_depths"]
                for case in certificates
            },
        },
    )

    print("\nPARENT-DELETION CONTROLS")
    deletion_failures = []
    deletion_count = 0
    for case, rows in p.CASE_REPRESENTATIVES.items():
        initial, expected, dependencies, *_rest = prepared_by_case[case]
        controls = p.deletion_control_pairs(*rows)
        results, error = p.parent_deletion_checks(*rows)
        deletion_count += len(results)
        for label, target, parent in controls:
            if (
                p.sub(target, parent) not in p.c53.DIRECTIONS
                or target not in expected
                or (
                    parent not in initial
                    and parent not in dependencies[target]
                )
            ):
                deletion_failures.append(
                    (case, label, "not-local-dependency")
                )
        if error is not None or len(results) != 20 or not all(results.values()):
            deletion_failures.append((case, error, results))
    check(
        "all 80 strategic local-parent deletions suppress their child commit",
        deletion_count == 80 and not deletion_failures,
        deletion_failures[:2],
    )

    print("\nPHYSICAL PARALLEL COMPOSITION")
    parallel_failures = []
    for first_case, first_prepared in prepared_by_case.items():
        first_initial, first_expected, first_dependencies, *_rest = (
            first_prepared
        )
        for second_case, second_prepared in prepared_by_case.items():
            shifted = translate_prepared(second_prepared, PARALLEL_SHIFT)
            second_initial, second_expected, second_dependencies, *_rest = (
                shifted
            )
            first_support = set(first_initial) | set(first_expected)
            second_support = set(second_initial) | set(second_expected)
            contacts = cross_contacts(first_support, second_support)
            _initial, expected, dependencies = combined_graph(
                (first_prepared, shifted)
            )
            combined = dag_certificate(expected, dependencies, ())
            wanted_profile = (
                certificates[first_case]["profile"]
                + certificates[second_case]["profile"]
            )
            if (
                contacts
                or combined["depth"]
                != max(
                    certificates[first_case]["depth"],
                    certificates[second_case]["depth"],
                )
                or combined["profile"] != wanted_profile
                or combined["nodes"]
                != (
                    certificates[first_case]["nodes"]
                    + certificates[second_case]["nodes"]
                )
            ):
                parallel_failures.append(
                    (first_case, second_case, contacts)
                )
    check(
        "all 16 separated DAG unions have summed profiles and max depth",
        not parallel_failures,
        parallel_failures[:2],
    )

    mixed_shifted = translate_prepared(
        prepared_by_case[(1, 1)],
        PARALLEL_SHIFT,
    )
    mixed_ok, mixed_detail = synchronous_physical_run(
        (prepared_by_case[(0, 0)], mixed_shifted)
    )
    doubled_shifted = translate_prepared(
        prepared_by_case[(1, 1)],
        PARALLEL_SHIFT,
    )
    doubled_ok, doubled_detail = synchronous_physical_run(
        (prepared_by_case[(1, 1)], doubled_shifted)
    )
    check(
        "the physical 00||11 union closes in 4,106 layers",
        mixed_ok and mixed_detail == (61_464, 4_106, 44, 0),
        mixed_detail,
    )
    check(
        "the physical 11||11 union doubles records but not depth",
        doubled_ok and doubled_detail == (61_662, 4_106, 44, 0),
        doubled_detail,
    )

    print("\nABSTRACT SERIAL COMPOSITION AND EXACT PHYSICAL SEAM")
    serial_failures = []
    serial_depths = {}
    for first_case, first_prepared in prepared_by_case.items():
        _fi, first_expected, first_dependencies, *_rest = first_prepared
        for second_case, second_prepared in prepared_by_case.items():
            _si, second_expected, second_dependencies, *_rest = (
                second_prepared
            )
            expected, dependencies, linked = serial_graph(
                first_expected,
                first_dependencies,
                certificates[first_case],
                second_expected,
                second_dependencies,
            )
            serial = dag_certificate(expected, dependencies, ())
            wanted_depth = (
                certificates[first_case]["depth"]
                + certificates[second_case]["depth"]
            )
            wanted_profile = shifted_profile(
                certificates[first_case]["profile"],
                certificates[second_case]["profile"],
                certificates[first_case]["depth"],
            )
            serial_depths[(first_case, second_case)] = serial["depth"]
            if (
                linked != 15
                or serial["depth"] != wanted_depth
                or serial["profile"] != wanted_profile
                or serial["nodes"]
                != (
                    certificates[first_case]["nodes"]
                    + certificates[second_case]["nodes"]
                )
            ):
                serial_failures.append(
                    (first_case, second_case, linked, serial["depth"])
                )
    source_delta = p.sub(p.SOURCE_CENTERS[1], p.SOURCE_CENTERS[0])
    output_delta = p.sub(output_sites[1], output_sites[0])
    rigid_matches = tuple(
        rotation
        for rotation in p.c53.ROTATIONS
        if p.c53.matvec(rotation, source_delta) in {
            output_delta,
            tuple(-value for value in output_delta),
        }
    )
    check(
        "all 16 abstract serial DAGs have additive depth",
        not serial_failures
        and set(serial_depths.values()) == {8_072, 8_142, 8_212},
        {"failures": serial_failures[:2], "depths": serial_depths},
    )
    check(
        "zero-cost rigid serial gluing fails for this exact source/output seam",
        source_delta == (480, 0, 0)
        and output_delta == (320, -70, 80)
        and squared_norm(source_delta) == 230_400
        and squared_norm(output_delta) == 113_700
        and not rigid_matches,
        {
            "source_delta": source_delta,
            "output_delta": output_delta,
            "norms": (
                squared_norm(source_delta),
                squared_norm(output_delta),
            ),
            "matches": len(rigid_matches),
        },
    )

    print("\nSCOPE AND NO-GO DISCIPLINE")
    note = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    required_phrases = (
        "operational commit depth",
        "dimensionless relative duration",
        "not a continuous rate",
        "not metric time",
        "not a lorentz or lapse result",
        "no axiom conclusion follows",
        "abstract dependency composition",
        "zero-cost serial gluing",
        "122,816 declared dynamic edges",
        "status: **pass for the exact seam exclusion; fail for a general serial no-go.**",
        "### n1 — alternative routes",
        "### n2 — wall independence",
        "### n3 — hidden-condition scan",
        "### n4 — residual matching",
        "### n5 — rhetoric audit",
        "### n6 — partial closure and axiom classification",
        "### n7 — strongest hostile steelman",
        "### n8 — cross-cycle echo",
    )
    missing_phrases = tuple(
        phrase for phrase in required_phrases if phrase not in note
    )
    check(
        "the Cycle-170 note states every required scope boundary",
        not missing_phrases,
        missing_phrases,
    )

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170"
        if FAIL == 0
        else "OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
