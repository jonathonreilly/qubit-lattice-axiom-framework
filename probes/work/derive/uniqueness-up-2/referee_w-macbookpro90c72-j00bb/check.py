#!/usr/bin/env python3
"""Independent referee for uniqueness-up-2 a2.

Six-axis level automaton on (p, 1, 2). The two-level constant is recomputed
with upward-rounded integer arithmetic. The attempt's script is not imported.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import numpy as np

FAILS: list[str] = []
LAW_SCALE = 24
TABLE_SCALE = 34


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def scaled_ceiling(value, shift):
    return -((-(value.numerator << shift)) // value.denominator)


class Formation:
    def __init__(self, equal, antipodal):
        self.equal = F(equal)
        self.antipodal = F(antipodal)
        self.weight = [
            [self.equal if spin == axis else (F(1) if spin == axis ^ 1 else F(2)) for axis in range(6)]
            for spin in range(6)
        ]
        self._law = {}

    def law(self, *parents):
        key = tuple(sorted(parents))
        if key not in self._law:
            masses = [self.weight[spin][parents[0]] * self.weight[spin][parents[1]] * self.weight[spin][parents[2]] for spin in range(6)]
            total = sum(masses)
            self._law[key] = tuple(mass / total for mass in masses)
        return self._law[key]

    def ground(self, left, right):
        if left == right:
            return F(0)
        if left == right ^ 1:
            return self.antipodal
        return F(1)

    def distance(self, left, right):
        excess = [max(a - b, F(0)) for a, b in zip(left, right)]
        deficit = [max(b - a, F(0)) for a, b in zip(left, right)]
        variation = sum(excess)
        antipodal_mass = max([F(0)] + [excess[i] + deficit[i ^ 1] - variation for i in range(6)])
        return variation + (self.antipodal - 1) * antipodal_mass

    def plan(self, left, right):
        coupled = {}
        kept = [min(a, b) for a, b in zip(left, right)]
        for index, mass in enumerate(kept):
            if mass:
                coupled[index, index] = mass
        excess = [a - mass for a, mass in zip(left, kept)]
        deficit = [b - mass for b, mass in zip(right, kept)]
        variation = sum(excess)
        if variation == 0:
            return coupled
        score = [excess[i] + deficit[i ^ 1] - variation for i in range(6)]
        antipodal_mass = max(score)
        if antipodal_mass > 0:
            critical = score.index(antipodal_mass)
            if sum(value > 0 for value in score) != 1:
                raise RuntimeError("two critical antipodes")
            coupled[critical, critical ^ 1] = antipodal_mass
            excess[critical] -= antipodal_mass
            deficit[critical ^ 1] -= antipodal_mass
        axis_excess = [excess[0] + excess[1], excess[2] + excess[3], excess[4] + excess[5]]
        axis_deficit = [deficit[0] + deficit[1], deficit[2] + deficit[3], deficit[4] + deficit[5]]
        if sum(axis_excess) == 0:
            return coupled
        lower = max(F(0), axis_deficit[1] - axis_excess[2], axis_deficit[0] + axis_deficit[1] - axis_excess[1] - axis_excess[2])
        upper = min(axis_excess[0], axis_deficit[1], axis_deficit[0] + axis_deficit[1] - axis_excess[2])
        if lower > upper:
            raise RuntimeError("axis transport is empty")
        share = (lower + upper) / 2
        flow = {
            (0, 1): share,
            (0, 2): axis_excess[0] - share,
            (2, 1): axis_deficit[1] - share,
            (2, 0): axis_excess[2] - axis_deficit[1] + share,
            (1, 0): axis_deficit[0] - axis_excess[2] + axis_deficit[1] - share,
            (1, 2): axis_excess[1] - axis_deficit[0] + axis_excess[2] - axis_deficit[1] + share,
        }
        for source in range(6):
            for target in range(6):
                source_axis, target_axis = source // 2, target // 2
                if source_axis != target_axis and axis_excess[source_axis] and axis_deficit[target_axis] and excess[source] and deficit[target]:
                    coupled[source, target] = coupled.get((source, target), 0) + (
                        flow[source_axis, target_axis] * excess[source] / axis_excess[source_axis] * deficit[target] / axis_deficit[target_axis]
                    )
        return coupled

    def plan_is_optimal(self, left, right, coupled):
        row = [sum(mass for (source, _target), mass in coupled.items() if source == index) for index in range(6)]
        column = [sum(mass for (_source, target), mass in coupled.items() if target == index) for index in range(6)]
        cost = sum(mass * self.ground(source, target) for (source, target), mass in coupled.items())
        excess = [max(a - b, F(0)) for a, b in zip(left, right)]
        deficit = [max(b - a, F(0)) for a, b in zip(left, right)]
        variation = sum(excess)
        score = [excess[i] + deficit[i ^ 1] - variation for i in range(6)]
        if max(score) > 0:
            critical = score.index(max(score))
            witness = [F(1) if not deficit[i] else self.antipodal - 1 for i in range(6)]
            witness[critical], witness[critical ^ 1] = self.antipodal, F(0)
        else:
            witness = [F(0) if deficit[i] else F(1) for i in range(6)]
        lipschitz = all(abs(witness[i] - witness[j]) <= self.ground(i, j) for i in range(6) for j in range(6))
        dual = sum(witness[i] * (left[i] - right[i]) for i in range(6))
        return row == list(left) and column == list(right) and min(coupled.values()) >= 0 and lipschitz and dual == cost == self.distance(left, right)


def signed_permutations():
    permutations = []
    for axes in itertools.permutations(range(3)):
        for flips in itertools.product((0, 1), repeat=3):
            permutations.append([2 * axes[i // 2] + ((i % 2) ^ flips[i // 2]) for i in range(6)])
    return permutations


MULTISETS = list(itertools.combinations_with_replacement(range(6), 3))
MULTISET_INDEX = {combo: index for index, combo in enumerate(MULTISETS)}


def predecessors(site):
    return ["".join(sorted(site + direction)) for direction in "123"]


def corner_slots(index):
    others = [direction for direction in (1, 2, 3) if direction != index]
    left, right = others
    pair = lambda a, b: f"{min(a, b)}{max(a, b)}"
    return [pair(index, left), pair(index, right), f"{left}{left}", pair(left, right), f"{right}{right}"]


def edge_slots(left, right):
    missing = ({1, 2, 3} - {left, right}).pop()
    pair = lambda a, b: f"{min(a, b)}{max(a, b)}"
    return [f"{left}{left}", pair(left, missing), f"{right}{right}", pair(right, missing), f"{missing}{missing}"]


ORDER = ["11", "12", "13", "22", "23", "33"]
SLOTS = {
    "11": ("corner", corner_slots(1)),
    "22": ("corner", corner_slots(2)),
    "33": ("corner", corner_slots(3)),
    "12": ("edge", edge_slots(1, 2)),
    "13": ("edge", edge_slots(1, 3)),
    "23": ("edge", edge_slots(2, 3)),
}


def geometric_order():
    site = (4, 5, 6)
    grand = {}
    for i in (1, 2, 3):
        for j in range(i, 4):
            point = list(site)
            point[i - 1] -= 1
            point[j - 1] -= 1
            grand[f"{i}{j}"] = tuple(point)
    ordered = sorted(grand, key=lambda name: (grand[name][0], grand[name][1]))
    shared = set(predecessors("11")) & set(predecessors("12"))
    return ordered == ORDER and shared == {"112"}


check("geometry", geometric_order(), "the six grand-predecessors are ordered 11,12,13,22,23,33, and adjacent ones share a parent")

round_one = Formation(F(51, 10), F(5, 4))
laws = [round_one.law(*combo) for combo in MULTISETS]
reproduced = F(0)
for left, right in ((0, 1), (0, 2)):
    sensitivity = [
        [round_one.distance(round_one.law(left, u, v), round_one.law(right, u, v)) / round_one.ground(left, right) for v in range(6)]
        for u in range(6)
    ]
    for first in laws:
        collapsed = [sum(first[u] * sensitivity[u][v] for u in range(6)) for v in range(6)]
        for second in laws:
            reproduced = max(reproduced, sum(collapsed[v] * second[v] for v in range(6)))
sample = Formation(F(27, 5), F(27, 20))
sample_ok = True
sample_count = 0
for left_parents in itertools.product(range(6), repeat=3):
    for right_parents in itertools.product(range(6), repeat=3):
        if sum(left_parents) % 7 == 0 and sum(right_parents) % 5 == 1:
            mu, nu = sample.law(*left_parents), sample.law(*right_parents)
            sample_ok = sample_ok and sample.plan_is_optimal(mu, nu, sample.plan(mu, nu))
            sample_count += 1
check(
    "A1 plan",
    reproduced == F(52187574259076840991934694, 156963184970376094931272779) and sample_ok and sample_count == 1333,
    f"round 1's constant matches, and the plan is optimal on {sample_count} law pairs",
)

equivariant = True
equivariant_count = 0
for left, right in ((0, 1), (0, 2)):
    for environment in itertools.combinations_with_replacement(range(6), 2):
        mu, nu = sample.law(left, *environment), sample.law(right, *environment)
        base = sample.plan(mu, nu)
        for permutation in signed_permutations():
            moved_left = sample.law(permutation[left], permutation[environment[0]], permutation[environment[1]])
            moved_right = sample.law(permutation[right], permutation[environment[0]], permutation[environment[1]])
            direct = sample.plan(moved_left, moved_right)
            pushed = {(permutation[i], permutation[j]): mass for (i, j), mass in base.items()}
            equivariant = equivariant and direct == pushed
            equivariant_count += 1
check(
    "A2 symmetry",
    equivariant and len({tuple(item) for item in signed_permutations()}) == 48,
    f"the plan commutes with all 48 signed permutations on {equivariant_count} checks",
)


def realised_rows(sites):
    if not sites:
        return np.zeros((1, 0), dtype=np.int64)
    triples = [predecessors(site) for site in sites]
    names = sorted({name for triple in triples for name in triple})
    place = {name: index for index, name in enumerate(names)}
    slots = [[place[name] for name in triple] for triple in triples]
    lookup = np.empty((6, 6, 6), dtype=np.int16)
    for values in itertools.product(range(6), repeat=3):
        lookup[values] = MULTISET_INDEX[tuple(sorted(values))]
    tail_rank = len(names) - 2
    tail = np.indices((6,) * tail_rank, dtype=np.int8).reshape(tail_rank, -1).T
    found = []
    for first, second in itertools.product(range(6), repeat=2):
        head = np.repeat(np.array([[first, second]], dtype=np.int8), len(tail), axis=0)
        grid = np.concatenate([head, tail], axis=1)
        columns = np.stack([lookup[grid[:, slot[0]], grid[:, slot[1]], grid[:, slot[2]]] for slot in slots], axis=1)
        found.append(np.unique(columns, axis=0))
    return np.unique(np.concatenate(found), axis=0).astype(np.int64)


print("enumerating realisable environments", flush=True)
GROUPS = {}
for index, site in enumerate(ORDER):
    for group in (ORDER[:index], ORDER[index + 1 :]):
        key = tuple(group)
        if key not in GROUPS:
            GROUPS[key] = realised_rows(list(group))
            print(f"  group {key or '()'}: {len(GROUPS[key])} tuples", flush=True)
five_site = len(GROUPS[tuple(ORDER[1:])])
check(
    "A3 environments",
    five_site == 8536256 and five_site < 56**5,
    f"the five-site group realises {five_site} of the 56^5 law tuples",
)


def contract(table, rows, laws):
    width = rows.shape[1]
    ordered = rows[np.lexsort(rows.T[::-1])]
    current = table[None]
    parent = np.zeros(len(ordered), dtype=np.int64)
    for axis in range(width):
        prefix, inverse = np.unique(ordered[:, : axis + 1], axis=0, return_inverse=True)
        inverse = inverse.ravel()
        first = np.zeros(len(prefix), dtype=np.int64)
        first[inverse[::-1]] = np.arange(len(ordered))[::-1]
        total = np.einsum("pa,pma...->pm...", laws[prefix[:, axis]], current[parent[first]])
        current = (total + ((1 << LAW_SCALE) - 1)) >> LAW_SCALE
        parent = inverse
    return current[parent]


def position_ceiling(table, template, before, after, laws):
    earlier = GROUPS[tuple(before)]
    later = GROUPS[tuple(after)]
    ordered = np.transpose(table, [template.index(site) for site in before + after])
    early_count, late_count = len(before), len(after)
    if early_count == 0:
        return int(contract(ordered[None], later, laws).max())
    if late_count == 0:
        return int(contract(ordered[None], earlier, laws).max())
    swapped = np.ascontiguousarray(np.transpose(ordered, list(range(early_count, early_count + late_count)) + list(range(early_count))))
    partial = contract(swapped.reshape((6**late_count,) + (6,) * early_count), earlier, laws)
    best = 0
    for start in range(0, len(partial), 256):
        block = partial[start : start + 256].reshape((-1,) + (6,) * late_count)
        best = max(best, int(contract(block, later, laws).max()))
    return best


def switch_tables(model, left, right):
    corner_cost = {
        key: model.distance(model.law(key[0], key[2], key[3]), model.law(key[1], key[2], key[3]))
        for key in itertools.product(range(6), repeat=4)
    }
    corner = np.empty((6,) * 5, dtype=object)
    plans = []
    for edge_left, edge_right in itertools.product(range(6), repeat=2):
        mu, nu = model.law(left, edge_left, edge_right), model.law(right, edge_left, edge_right)
        coupled = model.plan(mu, nu)
        plans.append((mu, nu, coupled))
        averaged = [
            [sum(mass * corner_cost[a, b, second, third] for (a, b), mass in coupled.items()) for third in range(6)]
            for second in range(6)
        ]
        for far_left, middle, far_right in itertools.product(range(6), repeat=3):
            law_left, law_right = model.law(edge_left, far_left, middle), model.law(edge_right, middle, far_right)
            corner[edge_left, edge_right, far_left, middle, far_right] = sum(
                law_left[second] * law_right[third] * averaged[second][third] for second in range(6) for third in range(6)
            )
    first_child = {
        pair: model.plan(model.law(pair[0], left, pair[1]), model.law(pair[0], right, pair[1]))
        for pair in itertools.product(range(6), repeat=2)
    }
    second_child = {
        pair: model.plan(model.law(left, pair[0], pair[1]), model.law(right, pair[0], pair[1]))
        for pair in itertools.product(range(6), repeat=2)
    }
    edge = np.empty((6,) * 5, dtype=object)
    cached_cost = {}
    for near_left, far_left, near_right, middle in itertools.product(range(6), repeat=4):
        folded = [F(0)] * 6
        for (a, b), first_mass in first_child[near_left, far_left].items():
            for (c, d), second_mass in second_child[near_right, middle].items():
                for third in range(6):
                    key = (a, b, c, d, third)
                    if key not in cached_cost:
                        cached_cost[key] = model.distance(model.law(a, c, third), model.law(b, d, third))
                    folded[third] += first_mass * second_mass * cached_cost[key]
        for far_right in range(6):
            third_law = model.law(far_left, middle, far_right)
            edge[near_left, far_left, near_right, middle, far_right] = sum(folded[third] * third_law[third] for third in range(6))
    return corner, edge, plans


def certify(equal, antipodal):
    model = Formation(equal, antipodal)
    rounded_laws = np.array(
        [[scaled_ceiling(value, LAW_SCALE) for value in model.law(*combo)] for combo in MULTISETS],
        dtype=np.int64,
    )
    sensitivity = {site: F(0) for site in ORDER}
    plans_ok = True
    for left, right in ((0, 1), (0, 2)):
        corner, edge, plans = switch_tables(model, left, right)
        for mu, nu, coupled in plans:
            plans_ok = plans_ok and model.plan_is_optimal(mu, nu, coupled)
        ceiling = np.vectorize(lambda value: scaled_ceiling(value, TABLE_SCALE), otypes=[object])
        corner_int = ceiling(corner).astype(np.int64)
        edge_int = ceiling(edge).astype(np.int64)
        for site in ORDER:
            kind, template = SLOTS[site]
            index = ORDER.index(site)
            raw = position_ceiling(
                corner_int if kind == "corner" else edge_int,
                template,
                ORDER[:index],
                ORDER[index + 1 :],
                rounded_laws,
            )
            sensitivity[site] = max(sensitivity[site], F(raw, 1 << TABLE_SCALE) / model.ground(left, right))
    return sum(sensitivity.values()), sensitivity, plans_ok, model


TABLE = (
    (F(51, 10), F(27, 20), "0.845071"),
    (F(21, 4), F(27, 20), "0.894864"),
    (F(27, 5), F(27, 20), "0.944946"),
    (F(11, 2), F(27, 20), "0.978358"),
    (F(111, 20), F(27, 20), "0.995052"),
    (F(139, 25), F(34, 25), "0.998429"),
)
POSITIONS = {
    "11": "0.11087",
    "22": "0.12093",
    "33": "0.11087",
    "12": "0.22142",
    "13": "0.21292",
    "23": "0.22142",
}
table_ok = True
top_model = None
top_sensitivity = None
for equal, antipodal, printed in TABLE:
    constant, sensitivity, plans_ok, model = certify(equal, antipodal)
    shown = f"{float(constant):.6f}"
    print(f"  p = {equal} alpha = {antipodal}: K2c <= {shown}", flush=True)
    table_ok = table_ok and constant < 1 and plans_ok and shown == printed
    if equal == F(139, 25):
        top_model = model
        top_sensitivity = sensitivity
        table_ok = table_ok and all(f"{float(sensitivity[site]):.5f}" == POSITIONS[site] for site in ORDER)
check(
    "A4 contraction",
    table_ok,
    "every tabulated two-level constant is an exact upper bound below 1, and the six weights at p = 139/25 match",
)

kappa_max = max(
    top_model.distance(top_model.law(left, u, v), top_model.law(right, u, v)) / top_model.ground(left, right)
    for left, right in ((0, 1), (0, 2))
    for u in range(6)
    for v in range(6)
)
check(
    "A5 one level",
    f"{float(kappa_max):.5f}" == "0.39208" and 0 < kappa_max < 1,
    f"at p = 139/25, kappa_max = {float(kappa_max):.5f}",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. On (p, 1, 2) the two-level Wasserstein constant K2c, with group-consistent "
    "environments and upward rounding, is below 1 at p = 51/10, 21/4, 27/5, 11/2, 111/20 (alpha 27/20) and at "
    "p = 139/25 (alpha 34/25), where it is at most 0.998429. The one-level kappa_max there is 0.39208. So the "
    "level automaton has one invariant law and forgets its initial plane exponentially up to p = 139/25. "
    "The located threshold 10.5 is not reached, and the constants are pointwise.",
    flush=True,
)
print(
    "HIT: confirmed - the six-axis formation law on (p, 1, 2) is unique and loses memory exponentially for every "
    "tabulated p through 139/25, because the two-level constant K2c is an exact upper bound below 1 there",
    flush=True,
)
