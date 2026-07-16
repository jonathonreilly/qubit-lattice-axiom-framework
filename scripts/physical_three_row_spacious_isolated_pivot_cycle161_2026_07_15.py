#!/usr/bin/env python3
"""Cycle 161: verify three physical rows driving the isolated pivot."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import product
from pathlib import Path

import output_ported_commutator_isolated_pivot_cycle160_2026_07_15 as prior
import physical_three_row_spacious_commutator_bind_probe_2026_07_15 as bound
import physical_three_row_spacious_isolated_pivot_probe_2026_07_15 as p


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_THREE_ROW_SPACIOUS_ISOLATED_PIVOT_CYCLE161_NOTE_2026-07-15.md"
)
CHECKLIST = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_THREE_ROW_SPACIOUS_ISOLATED_PIVOT_CYCLE161_NO_GO_CHECKLIST_2026-07-15.md"
)
ROWS = tuple(product((0, 1), repeat=5))
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


def manhattan(left, right):
    return sum(abs(a - b) for a, b in zip(left, right))


def topology(expected, dependencies):
    children = {site: [] for site in expected}
    indegree = {site: 0 for site in expected}
    external = []
    for site, parents in dependencies.items():
        for parent in parents:
            if parent not in expected:
                external.append((site, parent))
                continue
            children[parent].append(site)
            indegree[site] += 1
    queue = deque(site for site, count in indegree.items() if count == 0)
    depth = {site: 0 for site in queue}
    seen = 0
    maximum = 0
    while queue:
        site = queue.popleft()
        seen += 1
        maximum = max(maximum, depth[site])
        for child in children[site]:
            depth[child] = max(depth.get(child, 0), depth[site] + 1)
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    return seen, maximum, tuple(external), Counter(map(len, dependencies.values()))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    g1 = (1, 0, 0, 1, 0)
    g2 = (0, 1, 1, 0, 1)
    measured = (1, 1, 0, 1, 0)

    print("AUTHORITY AND LAW")
    check("review note exists", NOTE.is_file())
    check("No-Go Discipline checklist exists", CHECKLIST.is_file())
    check(
        "Cycle 161 adds no transition row and uses the Cycle-160 candidate law",
        p.MERGED_RAW is bound.MERGED_RAW
        and p.MERGED_RAW is prior.isolation.MERGED_RAW
        and len(p.MERGED_RAW) == 89_708,
        len(p.MERGED_RAW),
    )
    check(
        "the 89,708-row candidate law remains deterministic",
        not prior.isolation.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
    )

    print("\nGEOMETRY")
    paths = {
        **{("generator", *key): path for key, path in bound.GENERATOR_PATHS.items()},
        **{("measured", *key): path for key, path in bound.MEASURED_PATHS.items()},
        **{("selector", index): path for index, path in enumerate(p.SELECTOR_PATHS)},
        **{("case", index): path for index, path in enumerate(p.CASE_PATHS)},
    }
    occurrences = defaultdict(list)
    locality_failures = []
    for key, path in paths.items():
        for index, site in enumerate(path):
            occurrences[site].append((key, index))
        locality_failures.extend(
            (key, left, right)
            for left, right in zip(path, path[1:])
            if manhattan(left, right) != 1
        )
    shared = {site: uses for site, uses in occurrences.items() if len(uses) > 1}
    case_site = p.add(p.pivot.CASE_SITE, p.CONTROLLER_SHIFT)
    check(
        "20 nearest-neighbor paths have one intended shared case source",
        len(paths) == 20
        and sum(map(len, paths.values())) == 14_368
        and len(occurrences) == 14_367
        and set(shared) == {case_site}
        and len(shared[case_site]) == 2
        and not locality_failures,
        (len(paths), sum(map(len, paths.values())), len(occurrences), shared),
    )
    _scaffold, terminal_ports = p.routing_scaffold()
    required_ports = {case_site, *p.REMOTE_LANES}
    check(
        "joint routing closes at the case and two remote lane ports",
        required_ports <= set(terminal_ports),
        required_ports - set(terminal_ports),
    )

    print("\nPHYSICAL APPARATUS")
    prepared = p.apparatus(g1, g2, measured)
    initial, expected, dependencies, results, case, lane_outputs, sockets = prepared
    roles = Counter(initial.values())
    check(
        "only three row roles and structural records are supplied",
        not (set(initial) & set(expected))
        and roles[bound.d.H0] == 0
        and roles[bound.d.H1] == 0
        and roles[bound.ported.five.ROW_ROLE[g1]] == 1
        and roles[bound.ported.five.ROW_ROLE[g2]] == 1
        and roles[bound.twoport.five.ROW_ROLE[measured]] == 1,
        (len(initial), len(expected), len(sockets)),
    )
    topo = topology(expected, dependencies)
    check(
        "all 16,889 derived records form one closed acyclic dependency graph",
        topo
        == (
            16_889,
            2_749,
            (),
            Counter({1: 16_862, 2: 15, 0: 12}),
        ),
        topo,
    )
    ok, detail = p.execute(prepared)
    check(
        "representative three-row apparatus produces the exact isolated pivot",
        ok
        and detail
        == (
            16_890,
            120_355,
            12,
            201_035,
            16_889,
            (1, 0),
            (1, 0),
            ("L4", "L5"),
            {},
        ),
        detail,
    )

    print("\nALL FOUR PHYSICAL CASES")
    zero = (0, 0, 0, 0, 0)
    axis = (0, 1, 0, 0, 0)
    probe = (0, 0, 0, 1, 0)
    anchors = ((zero, zero, zero), (zero, axis, probe), (axis, zero, probe), (axis, axis, probe))
    case_failures = []
    case_shapes = Counter()
    for args in anchors:
        observed_case = p.pivot.pivot_rows(*args)[0]
        ok, detail = p.deterministic_run(*args)
        if ok:
            case_shapes[(detail[6], detail[0], detail[1], detail[2], detail[3], detail[4], detail[7])] += 1
        if (
            not ok
            or detail[5] != observed_case
            or detail[6] != observed_case
            or detail[7] != p.pivot.LANE_OUTPUT[observed_case]
        ):
            case_failures.append((args, ok, detail, observed_case))
    check(
        "all four physical cases produce the exact two remote lane selectors",
        not case_failures
        and {item[0] for item in case_shapes} == set(product((0, 1), repeat=2))
        and all(
            key[1:6] == (16_890, 120_355, 12, 201_035, 16_889)
            for key in case_shapes
        ),
        (case_shapes, case_failures[:1]),
    )

    print("\nCUBIC COVARIANCE AND LOCAL HISTORIES")
    rotation_failures = []
    invariant_shapes = Counter()
    maxima = Counter()
    edge_counts = []
    for rotation_index, rotation in enumerate(p.c53.ROTATIONS):
        ok, detail = p.execute(prepared, rotation=rotation)
        if ok:
            invariant_shapes[(
                detail[0], detail[3], detail[4], detail[5], detail[6], detail[7]
            )] += 1
            edge_counts.append(detail[1])
            maxima[detail[2]] += 1
        else:
            rotation_failures.append((rotation_index, detail))
    edge_range = (min(edge_counts), max(edge_counts)) if edge_counts else None
    check(
        "all 24 proper-cubic orientations preserve exact content and closure",
        not rotation_failures
        and invariant_shapes
        == {(16_890, 201_035, 16_889, (1, 0), (1, 0), ("L4", "L5")): 24}
        and edge_range == (88_860, 175_507)
        and maxima == {12: 15, 13: 1, 16: 8},
        (invariant_shapes, edge_range, maxima, rotation_failures[:1]),
    )
    local_cases, local_failures = p.local_schedule_proof(prepared)
    check(
        "33,806 realizable local histories contain no wrong or parasitic write",
        local_cases == 33_806 and not local_failures,
        (local_cases, local_failures[:1]),
    )

    print("\nCAUSAL CONTROLS")
    shifted = lambda sites, shift: {bound.add(site, shift) for site in sites}
    g1_starts = shifted(bound.ported.TARGETS, bound.GENERATOR_CENTERS[0])
    g2_starts = shifted(bound.ported.TARGETS, bound.GENERATOR_CENTERS[1])
    measured_starts = shifted(bound.twoport.TARGETS, bound.MEASURED_CENTER)
    full_frontier = p.enabled(initial)
    check(
        "the initial frontier is exactly the twelve row-bit writes",
        set(full_frontier) == g1_starts | g2_starts | measured_starts,
        len(full_frontier),
    )
    deletion_failures = []
    for label, source, wanted in (
        ("g1", bound.GENERATOR_CENTERS[0], g2_starts | measured_starts),
        ("g2", bound.GENERATOR_CENTERS[1], g1_starts | measured_starts),
        ("measured", bound.MEASURED_CENTER, g1_starts | g2_starts),
    ):
        mutated = dict(initial)
        mutated.pop(source)
        actual = set(p.enabled(mutated))
        if actual != wanted:
            deletion_failures.append((label, actual, wanted))
    check(
        "deleting each row source suppresses exactly its four first writes",
        not deletion_failures,
        deletion_failures[:1],
    )
    shared_failures = []
    for bit_index, bit_paths in enumerate(bound.twoport.PATHS):
        source = bound.add(bound.twoport.TARGETS[bit_index], bound.MEASURED_CENTER)
        endpoints = {
            bound.add(path[-1], bound.MEASURED_CENTER) for path in bit_paths
        }
        if any(dependencies[endpoint] != frozenset((source,)) for endpoint in endpoints):
            shared_failures.append((bit_index, source, endpoints))
    selector_sites = tuple(
        bound.add(bound.spacious.XOR_CENTERS[-1], shift) for shift in bound.COMM_SHIFTS
    )
    check(
        "each measured bit has two children and no selector/case/lane is supplied",
        not shared_failures
        and all(site not in initial for site in (*selector_sites, case_site, *p.REMOTE_LANES)),
        shared_failures[:1],
    )

    print("\nVALID ROW-TRIPLE CENSUS")
    algebra = bound.comm.alu.compact.algebra
    commuting_pairs = 0
    distribution = Counter()
    census_failures = []
    for left in ROWS:
        for right in ROWS:
            if algebra.symplectic(left, right):
                continue
            commuting_pairs += 1
            for observed in ROWS:
                wanted = (
                    algebra.symplectic(left, observed),
                    algebra.symplectic(right, observed),
                )
                got = p.pivot.pivot_rows(left, right, observed)[0]
                distribution[wanted] += 1
                if got != wanted:
                    census_failures.append((left, right, observed, got, wanted))
    check(
        "all 17,408 valid triples have the exact four-case distribution",
        commuting_pairs == 544
        and not census_failures
        and distribution == {(0, 0): 5_888, (0, 1): 3_840, (1, 0): 3_840, (1, 1): 3_840},
        (commuting_pairs, distribution, census_failures[:1]),
    )

    print("\nPREDECESSOR COEXISTENCE")
    prior_result = prior.main()
    check(
        "the complete Cycle-160 and predecessor suite remains green",
        prior_result == 0,
        prior_result,
    )

    print("\nSCOPE AND NO-GO DISCIPLINE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    checklist = (
        " ".join(CHECKLIST.read_text(encoding="utf-8").lower().split())
        if CHECKLIST.is_file()
        else ""
    )
    for phrase in (
        "three physical five-bit row records",
        "14,368",
        "16,889",
        "33,806",
        "17,408",
        "does not complete the payload-row copy or common-output interface",
        "no axiom addition follows",
    ):
        check("note contains: " + phrase, phrase in note)
    for phrase in (
        "status: fail — no-go premature",
        "n1 — alternative route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — strongest hostile steelman",
        "n8 — cross-cycle echo",
        "positive partial closure",
    ):
        check("checklist contains: " + phrase, phrase in checklist)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_THREE_ROW_SPACIOUS_ISOLATED_PIVOT" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
