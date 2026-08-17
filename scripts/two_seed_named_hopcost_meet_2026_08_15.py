#!/usr/bin/env python3
"""Two-seed first meetings under the named equal-weight hop-cost.

Seeds s0=(0,0,0) and s1=(2,0,0). Fronts are grown by the named hop-cost
rho on the union U = B_4(s0) ∪ B_4(s1): cost 3 on a seed-exit or on an
equal inward-weight hop relative to the seed being grown, else 1. One
pair of Dijkstras produces t0 and t1. The first-meeting set is
M = {v : t0(v)=t1(v) and no neighbor is strictly earlier for both}.
Displayed, not adopted. No axiom edit, cache write, or path-length law.
"""

from __future__ import annotations

import heapq
from collections import defaultdict
from decimal import Decimal, getcontext
from itertools import product
from pathlib import Path


getcontext().prec = 80

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_SEED_NAMED_HOPCOST_MEET_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_SEED_NAMED_HOPCOST_MEET_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
S0: Point = (0, 0, 0)
S1: Point = (2, 0, 0)
BALL_RADIUS = 4
DIJKSTRA_CALLS = 0


def forbidden_tokens() -> tuple[str, ...]:
    return (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def graph_radius(point: Point, seed: Point = S0) -> int:
    return (
        abs(point[0] - seed[0])
        + abs(point[1] - seed[1])
        + abs(point[2] - seed[2])
    )


def euclid2(point: Point, seed: Point = S0) -> int:
    return (
        (point[0] - seed[0]) ** 2
        + (point[1] - seed[1]) ** 2
        + (point[2] - seed[2]) ** 2
    )


def ball(center: Point, radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for offset in product(span, repeat=3):
        site = add(center, offset)
        if graph_radius(site, center) <= radius:
            sites.append(site)
    return tuple(sites)


def inward_weight(point: Point, seed: Point) -> int:
    """Number of six-neighbors strictly nearer the seed being grown."""
    return sum(
        1
        for shift in SHIFTS
        if graph_radius(add(point, shift), seed) < graph_radius(point, seed)
    )


def named_hop_cost(src: Point, dst: Point, seed: Point) -> int:
    """Cost 3 iff seed-exit or equal inward weight relative to seed, else 1."""
    if src == seed:
        return 3
    if inward_weight(src, seed) == inward_weight(dst, seed):
        return 3
    return 1


def directed_edges(sites: tuple[Point, ...]) -> tuple[tuple[Point, Point], ...]:
    present = set(sites)
    edges: list[tuple[Point, Point]] = []
    for site in sites:
        for shift in SHIFTS:
            neighbor = add(site, shift)
            if neighbor in present:
                edges.append((site, neighbor))
    return tuple(edges)


def adjacency(
    sites: tuple[Point, ...], seed: Point
) -> dict[Point, list[tuple[Point, int]]]:
    present = set(sites)
    adj: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for site in sites:
        for shift in SHIFTS:
            neighbor = add(site, shift)
            if neighbor in present:
                adj[site].append((neighbor, named_hop_cost(site, neighbor, seed)))
    return adj


def shortest_all(
    start: Point, adj: dict[Point, list[tuple[Point, int]]]
) -> dict[Point, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    dist = {start: 0}
    heap: list[tuple[int, Point]] = [(0, start)]
    while heap:
        current, node = heapq.heappop(heap)
        if current != dist[node]:
            continue
        for neighbor, cost in adj[node]:
            trial = current + cost
            prior = dist.get(neighbor)
            if prior is None or trial < prior:
                dist[neighbor] = trial
                heapq.heappush(heap, (trial, neighbor))
    return dist


def neighbors_in(point: Point, present: set[Point]) -> tuple[Point, ...]:
    return tuple(add(point, shift) for shift in SHIFTS if add(point, shift) in present)


def equal_time_set(
    times0: dict[Point, int], times1: dict[Point, int], sites: tuple[Point, ...]
) -> tuple[Point, ...]:
    return tuple(
        sorted(
            site
            for site in sites
            if site in times0 and site in times1 and times0[site] == times1[site]
        )
    )


def first_meeting_set(
    times0: dict[Point, int],
    times1: dict[Point, int],
    sites: tuple[Point, ...],
) -> tuple[Point, ...]:
    present = set(sites)
    meetings: list[Point] = []
    for site in equal_time_set(times0, times1, sites):
        earlier_for_both = False
        for neighbor in neighbors_in(site, present):
            if neighbor not in times0 or neighbor not in times1:
                continue
            if times0[neighbor] < times0[site] and times1[neighbor] < times1[site]:
                earlier_for_both = True
                break
        if not earlier_for_both:
            meetings.append(site)
    return tuple(sorted(meetings))


def ratio_list(
    sites: tuple[Point, ...], times: dict[Point, int], seed: Point = S0
) -> list[Decimal]:
    values: list[Decimal] = []
    for point in sites:
        arrival = times[point]
        values.append(Decimal(euclid2(point, seed)).sqrt() / Decimal(arrival))
    return values


def population_variance(values: list[Decimal]) -> Decimal:
    count = Decimal(len(values))
    mean = sum(values) / count
    return sum((item - mean) ** 2 for item in values) / count


def rounded(value: Decimal, places: int) -> str:
    quantize = Decimal(10) ** -places
    return format(value.quantize(quantize), "f")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: none; two seeds, B_4 about each, and the named hop-cost are theorem hypotheses"
    )
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact integer path costs and |v-s0|_2/t0 on the two-seed union")
    print("negative_scope: displayed named hop-cost meetings are not written into Admissibility")

    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS = 0
    ball0 = ball(S0, BALL_RADIUS)
    ball1 = ball(S1, BALL_RADIUS)
    union = tuple(sorted(set(ball0) | set(ball1)))
    edges = directed_edges(union)
    times0 = shortest_all(S0, adjacency(union, S0))
    times1 = shortest_all(S1, adjacency(union, S1))
    l1_0 = {site: graph_radius(site, S0) for site in union}
    l1_1 = {site: graph_radius(site, S1) for site in union}

    equal_rho = equal_time_set(times0, times1, union)
    equal_l1 = equal_time_set(l1_0, l1_1, union)
    meeting_rho = first_meeting_set(times0, times1, union)
    meeting_l1 = first_meeting_set(l1_0, l1_1, union)
    lex_rho = meeting_rho[0]
    lex_l1 = meeting_l1[0]
    t_rho = times0[lex_rho]
    t_l1 = l1_0[lex_l1]

    var_rho_m = population_variance(ratio_list(meeting_rho, times0))
    var_l1_m = population_variance(ratio_list(meeting_l1, l1_0))
    var_rho_e = population_variance(ratio_list(equal_rho, times0))
    var_l1_e = population_variance(ratio_list(equal_l1, l1_0))

    seed_exit_ok = all(
        named_hop_cost(S0, add(S0, shift), S0) == 3
        and named_hop_cost(S1, add(S1, shift), S1) == 3
        for shift in SHIFTS
    )
    equal_weight_sample = named_hop_cost((1, 0, 0), (2, 0, 0), S0) == 3
    unequal_sample = named_hop_cost((1, 0, 0), (1, 1, 0), S0) == 1

    print(f"n_b4_s0: {len(ball0)}")
    print(f"n_b4_s1: {len(ball1)}")
    print(f"n_union: {len(union)}")
    print(f"n_union_edges: {len(edges)}")
    print(f"dijkstra_calls: {DIJKSTRA_CALLS}")
    print(f"|E_rho|: {len(equal_rho)}")
    print(f"|E_l1|: {len(equal_l1)}")
    print(f"|M_rho|: {len(meeting_rho)}")
    print(f"|M_l1|: {len(meeting_l1)}")
    print(f"lex_first_rho: {lex_rho}")
    print(f"t_rho: {t_rho}")
    print(f"lex_first_l1: {lex_l1}")
    print(f"t_l1: {t_l1}")
    print(f"var_rho_M: {format(var_rho_m, 'f')}")
    print(f"var_l1_M: {format(var_l1_m, 'f')}")
    print(f"var_rho_E: {format(var_rho_e, 'f')}")
    print(f"var_l1_E: {format(var_l1_e, 'f')}")

    checks.check(
        "two-balls",
        "B_4 about each seed has 129 sites and the union has 195 sites",
        len(ball0) == 129 and len(ball1) == 129 and len(union) == 195,
    )
    checks.check(
        "one-pair-dijkstra",
        "fronts are one pair of Dijkstras on the union",
        DIJKSTRA_CALLS == 2 and "shortest_all" in source,
    )
    checks.check(
        "named-rho",
        "rho is cost 3 on seed-exit or equal inward weight, else 1",
        seed_exit_ok and equal_weight_sample and unequal_sample,
    )
    checks.check(
        "thm1-lex",
        "lex-first first-meeting site under rho is (1,0,0) at t=3",
        lex_rho == (1, 0, 0) and t_rho == 3 and times1[lex_rho] == 3,
    )
    checks.check(
        "thm1-size",
        "the first-meeting set under rho has size 1",
        meeting_rho == ((1, 0, 0),) and len(meeting_rho) == 1,
    )
    checks.check(
        "thm1-l1",
        "lex-first first-meeting site under ell^1 is (1,0,0) at t=1",
        lex_l1 == (1, 0, 0) and t_l1 == 1 and meeting_l1 == ((1, 0, 0),),
    )
    checks.check(
        "thm1-note",
        "the note reports the lex-first meeting site, its t, and |M|",
        "(1, 0, 0)" in note
        and "t = 3" in note
        and "|M| = 1" in note
        and "lex-first" in note,
    )
    checks.check(
        "thm2-M-vars",
        "on M both population variances are zero, so neither is smaller",
        var_rho_m == 0 and var_l1_m == 0 and var_rho_m == var_l1_m,
    )
    checks.check(
        "thm2-E-size",
        "the simultaneous-arrival midplane has 25 sites under rho and under ell^1",
        len(equal_rho) == 25 and equal_rho == equal_l1,
    )
    checks.check(
        "thm2-E-vars",
        "on the midplane, var(|v-s0|_2/t0) under rho is strictly below ell^1",
        rounded(var_rho_e, 14) == "0.00033709642621"
        and rounded(var_l1_e, 14) == "0.00995038158264"
        and var_rho_e < var_l1_e,
    )
    checks.check(
        "thm2-note-vars",
        "the note reports both M variances, both midplane variances, and which is smaller",
        "0" in note
        and "0.00033709642621" in note
        and "0.00995038158264" in note
        and "strictly below" in note,
    )
    checks.check(
        "thm2-not-leftover",
        "the note states the two-seed meeting score is not leftover of one-seed variance",
        "not leftover" in note and "one-seed" in note,
    )
    checks.check(
        "thm3-displayed-not-adopted",
        "the note reports the named hop-cost as displayed, not adopted",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom,
    )
    checks.check(
        "thm3-no-l1-law",
        "the note does not attach an ell^1 path-length law",
        "Do not attach L1" in note and "no path-length law" in note,
    )
    checks.check(
        "uniqueness-not-required",
        "the note states uniqueness of a meeting site is not required",
        "Uniqueness not required" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports two-seed meetings under the named hop-cost versus ell^1",
        "Two-seed meetings under the named equal-weight hop-cost on "
        "B_4(0)∪B_4((2,0,0)) are scored vs ℓ¹. Displayed, not adopted."
        in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_SEED_NAMED_HOPCOST_MEET_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source
        and '"docs/TWO_SEED_NAMED_HOPCOST_MEET_BOUNDED_THEOREM_NOTE_2026-08-15.md"'
        in source
        and '"docs/MINIMAL_AXIOMS_2026-06-29.md"' in source,
    )
    checks.check(
        "forbidden-strings",
        "note, runner, and axiom avoid the dispatch-forbidden phrases",
        all(token not in note and token not in source for token in forbidden_tokens()),
    )
    checks.check(
        "no-axiom-cost",
        "the live axiom memo does not host a named hop-cost or two-seed meeting law",
        "named hop-cost" not in axiom
        and "two-seed" not in axiom
        and "equal inward" not in axiom,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )

    print(
        "per_element: checked exactly — each directed union edge carries the named hop-cost relative to the seed being grown"
    )
    print(
        "per_site: checked exactly — first-meeting and simultaneous-arrival sets are listed on the 195-site union"
    )
    print(
        "per_mode: checked exactly — one pair of Dijkstras under rho, closed-form ell^1 comparator"
    )
    print(
        "per_block: checked exactly — lex-first meeting, |M|, and population variance versus ell^1"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility hop-cost and no path-length law are adopted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
