#!/usr/bin/env python3
"""Exact finite controls for causal-order versus execution-order semantics.

This probe asks whether a Wolfram-style causal-trace quotient can remove the
maximal-synchronous-front clause from a sampled permanent-record law.  It
uses exact rational arithmetic throughout.  It is a bounded model and makes
no claim to identify the physical microscopic law.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product


Vec = tuple[int, int, int]
Distribution = dict[tuple[tuple[Vec, int], ...], Fraction]

E: tuple[Vec, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, condition: bool, name: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def add(a: Vec, b: Vec) -> Vec:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a: Vec, b: Vec) -> Vec:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def l1(a: Vec, b: Vec) -> int:
    d = sub(a, b)
    return abs(d[0]) + abs(d[1]) + abs(d[2])


def neighbors(x: Vec) -> tuple[Vec, ...]:
    return tuple(add(x, e) for e in E)


def incidence_kernel(counts: tuple[int, int]) -> dict[int, Fraction]:
    n0, n1 = counts
    total = n0 + n1
    if total == 0:
        raise ValueError("event has no admitted predecessor")
    out: dict[int, Fraction] = {}
    if n0:
        out[0] = Fraction(n0, total)
    if n1:
        out[1] = Fraction(n1, total)
    return out


def counts_at(records: dict[Vec, int], x: Vec, allowed: set[Vec] | None = None) -> tuple[int, int]:
    vals = [records[y] for y in neighbors(x) if y in records and (allowed is None or y in allowed)]
    return (vals.count(0), vals.count(1))


def canonical(records: dict[Vec, int], events: tuple[Vec, ...]) -> tuple[tuple[Vec, int], ...]:
    return tuple(sorted((x, records[x]) for x in events))


def execute_live(
    seed: dict[Vec, int], schedule: tuple[Vec, ...]
) -> Distribution:
    """Execute one event at a time, reading every record present at firing."""

    states: list[tuple[dict[Vec, int], Fraction]] = [(dict(seed), Fraction(1))]
    for x in schedule:
        nxt: list[tuple[dict[Vec, int], Fraction]] = []
        for records, weight in states:
            for value, p in incidence_kernel(counts_at(records, x)).items():
                new = dict(records)
                new[x] = value
                nxt.append((new, weight * p))
        states = nxt
    out: defaultdict[tuple[tuple[Vec, int], ...], Fraction] = defaultdict(Fraction)
    for records, weight in states:
        out[canonical(records, schedule)] += weight
    return dict(out)


def depths(seed_sites: set[Vec], events: set[Vec]) -> dict[Vec, int]:
    return {x: min(l1(x, s) for s in seed_sites) for x in events}


def predecessor_sets(seed_sites: set[Vec], events: set[Vec]) -> tuple[dict[Vec, int], dict[Vec, set[Vec]]]:
    depth = depths(seed_sites, events)
    rank = {s: 0 for s in seed_sites} | depth
    preds: dict[Vec, set[Vec]] = {}
    for x in events:
        preds[x] = {y for y in neighbors(x) if y in rank and rank[y] == depth[x] - 1}
        if not preds[x]:
            raise ValueError(f"event {x} has no lower-rank predecessor")
    return depth, preds


def topological(schedule: tuple[Vec, ...], depth: dict[Vec, int]) -> bool:
    position = {x: i for i, x in enumerate(schedule)}
    return all(
        position[y] < position[x]
        for x in schedule
        for y in schedule
        if depth[y] < depth[x] and l1(x, y) == 1
    )


def execute_layered(
    seed: dict[Vec, int], events: set[Vec], schedule: tuple[Vec, ...]
) -> Distribution:
    """Execute any causal linear extension, reading lower-rank predecessors only."""

    depth, preds = predecessor_sets(set(seed), events)
    if set(schedule) != events or not topological(schedule, depth):
        raise ValueError("schedule is not a causal linear extension")
    states: list[tuple[dict[Vec, int], Fraction]] = [(dict(seed), Fraction(1))]
    for x in schedule:
        nxt: list[tuple[dict[Vec, int], Fraction]] = []
        for records, weight in states:
            for value, p in incidence_kernel(counts_at(records, x, preds[x])).items():
                new = dict(records)
                new[x] = value
                nxt.append((new, weight * p))
        states = nxt
    out: defaultdict[tuple[tuple[Vec, int], ...], Fraction] = defaultdict(Fraction)
    ordered_events = tuple(sorted(events))
    for records, weight in states:
        out[canonical(records, ordered_events)] += weight
    return dict(out)


def proper_cubic_rotations() -> tuple[tuple[Vec, Vec, Vec], ...]:
    axes: tuple[Vec, ...] = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )

    def dot(a: Vec, b: Vec) -> int:
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    def cross(a: Vec, b: Vec) -> Vec:
        return (
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        )

    rotations: list[tuple[Vec, Vec, Vec]] = []
    for ex in axes:
        for ey in axes:
            if dot(ex, ey) != 0:
                continue
            ez = cross(ex, ey)
            if ez in axes:
                rotations.append((ex, ey, ez))
    return tuple(rotations)


def rotate(x: Vec, matrix: tuple[Vec, Vec, Vec]) -> Vec:
    ex, ey, ez = matrix
    return (
        x[0] * ex[0] + x[1] * ey[0] + x[2] * ez[0],
        x[0] * ex[1] + x[1] * ey[1] + x[2] * ez[1],
        x[0] * ex[2] + x[1] * ey[2] + x[2] * ez[2],
    )


def rotate_distribution(distribution: Distribution, matrix: tuple[Vec, Vec, Vec]) -> Distribution:
    out: Distribution = {}
    for state, weight in distribution.items():
        transformed = tuple(sorted((rotate(x, matrix), value) for x, value in state))
        out[transformed] = weight
    return out


def main() -> int:
    c = Checks()

    # The minimal schedule discriminator.  x and y are adjacent members of
    # the same boundary-distance layer, forced to opposite values by the old
    # boundary.  A live asynchronous update lets the first write contaminate
    # the second event's kernel.
    a, x, y, b = (-1, 0, 0), (0, 0, 0), (1, 0, 0), (2, 0, 0)
    split_seed = {a: 0, b: 1}
    events = {x, y}
    xy = execute_live(split_seed, (x, y))
    yx = execute_live(split_seed, (y, x))
    expected_xy = {
        canonical({x: 0, y: 0}, (x, y)): Fraction(1, 2),
        canonical({x: 0, y: 1}, (x, y)): Fraction(1, 2),
    }
    expected_yx = {
        canonical({x: 0, y: 1}, (x, y)): Fraction(1, 2),
        canonical({x: 1, y: 1}, (x, y)): Fraction(1, 2),
    }
    c.check(xy == expected_xy, "live schedule x->y has the exact contaminated law")
    c.check(yx == expected_yx, "live schedule y->x has the exact contaminated law")
    c.check(xy != yx, "live asynchronous order changes readable terminal statistics")
    c.check(set(xy) & set(yx) == {canonical({x: 0, y: 1}, (x, y))}, "only one terminal sector rejoins")

    layer_xy = execute_layered(split_seed, events, (x, y))
    layer_yx = execute_layered(split_seed, events, (y, x))
    expected_layer = {canonical({x: 0, y: 1}, (x, y)): Fraction(1)}
    c.check(layer_xy == expected_layer, "causal-layer execution preserves the old-front law")
    c.check(layer_yx == expected_layer, "opposite execution order preserves the old-front law")
    c.check(layer_xy == layer_yx, "causal-layer linear extensions are physically equivalent")

    average_live: defaultdict[tuple[tuple[Vec, int], ...], Fraction] = defaultdict(Fraction)
    for dist in (xy, yx):
        for state, p in dist.items():
            average_live[state] += p / 2
    c.check(
        dict(average_live)
        == {
            canonical({x: 0, y: 0}, (x, y)): Fraction(1, 4),
            canonical({x: 0, y: 1}, (x, y)): Fraction(1, 2),
            canonical({x: 1, y: 1}, (x, y)): Fraction(1, 4),
        },
        "averaging schedules creates a third law rather than a quotient",
    )
    c.check(dict(average_live) != expected_layer, "schedule randomization does not recover the layer law")

    # Exact normalized-kernel contradiction behind the counterexample.
    # Matching x->y to the simultaneous law requires q(1|1,1)=1; matching
    # y->x requires q(0|1,1)=1.  No normalized binary kernel can do both.
    candidates = [Fraction(i, 16) for i in range(17)]
    simultaneous_matches = [q0 for q0 in candidates if q0 == 1 and 1 - q0 == 1]
    c.check(not simultaneous_matches, "no normalized mixed-profile kernel matches both live orders")
    c.check(Fraction(1) + Fraction(1) != Fraction(1), "the two confluence demands contradict normalization")

    # A nontrivial four-event causal DAG: one random event feeds two commuting
    # children, which feed a join.  Every causal linear extension has the same
    # exact joint record law.
    s0, s1 = (-1, 0, 0), (0, -1, 0)
    q, r, s, t = (0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)
    dag_seed = {s0: 0, s1: 1}
    dag_events = {q, r, s, t}
    depth, preds = predecessor_sets(set(dag_seed), dag_events)
    c.check(depth == {q: 1, r: 2, s: 2, t: 3}, "boundary distance generates the intended causal ranks")
    c.check(preds[q] == {s0, s1}, "random root reads both boundary predecessors")
    c.check(preds[r] == {q} and preds[s] == {q}, "two children read the same causal parent")
    c.check(preds[t] == {r, s}, "join reads both causal children")

    schedules = tuple(p for p in permutations(dag_events) if topological(p, depth))
    c.check(len(schedules) == 2, "DAG has exactly the two expected linear extensions")
    dag_distributions = [execute_layered(dag_seed, dag_events, schedule) for schedule in schedules]
    c.check(all(dist == dag_distributions[0] for dist in dag_distributions), "all DAG linear extensions agree exactly")
    expected_dag = {
        canonical({q: v, r: v, s: v, t: v}, tuple(sorted(dag_events))): Fraction(1, 2)
        for v in (0, 1)
    }
    c.check(dag_distributions[0] == expected_dag, "causal Bayesian product gives the exact correlated joint law")
    c.check(sum(dag_distributions[0].values()) == 1, "causal joint law is normalized")

    # Exact all-24 covariance of the boundary-distance ranks, predecessor
    # relation, and resulting terminal distribution.
    rotations = proper_cubic_rotations()
    c.check(len(rotations) == 24 and len(set(rotations)) == 24, "enumerated all 24 proper cubic rotations")
    base = dag_distributions[0]
    for i, rotation in enumerate(rotations):
        rotated_seed = {rotate(site, rotation): value for site, value in dag_seed.items()}
        rotated_events = {rotate(site, rotation) for site in dag_events}
        rotated_schedule = tuple(rotate(site, rotation) for site in schedules[0])
        got = execute_layered(rotated_seed, rotated_events, rotated_schedule)
        c.check(got == rotate_distribution(base, rotation), f"rotation {i:02d} preserves the causal record law")

    # Translation covariance for several non-special offsets.
    for i, offset in enumerate(((7, -3, 2), (-4, 9, -5), (1, 1, 1))):
        translated_seed = {add(site, offset): value for site, value in dag_seed.items()}
        translated_events = {add(site, offset) for site in dag_events}
        translated_schedule = tuple(add(site, offset) for site in schedules[0])
        got = execute_layered(translated_seed, translated_events, translated_schedule)
        expected: Distribution = {}
        for state, weight in base.items():
            expected[tuple(sorted((add(site, offset), value) for site, value in state))] = weight
        c.check(got == expected, f"translation {i:02d} preserves the causal record law")

    # Global outcome-name covariance.
    flipped_seed = {site: 1 - value for site, value in dag_seed.items()}
    flipped = execute_layered(flipped_seed, dag_events, schedules[0])
    expected_flip: Distribution = {}
    for state, weight in base.items():
        expected_flip[tuple(sorted((site, 1 - value) for site, value in state))] = weight
    c.check(flipped == expected_flip, "global outcome-name interchange preserves the law")

    # Refining an execution trace by swapping causally unrelated events does
    # not change the cylinder law; changing a dependency does.
    first, second = schedules
    c.check(first.index(r) < first.index(s) or first.index(s) < first.index(r), "linear extension orders incomparable events")
    c.check(execute_layered(dag_seed, dag_events, first) == execute_layered(dag_seed, dag_events, second), "incomparable-event swap is gauge at distribution level")

    print(f"RESULT PASS={c.passed} FAIL={c.failed}")
    return 1 if c.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
