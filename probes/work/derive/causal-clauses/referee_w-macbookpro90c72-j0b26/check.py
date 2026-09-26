#!/usr/bin/env python3
"""Independent referee for causal-clauses a2.

Formation sequences and total-variation distances are recomputed in exact
arithmetic. The attempt's script is not imported. The seeded random policies
were not repeated.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
PARENT_STEPS = STEPS[0::2]
DIRECTION = {step: index for index, step in enumerate(STEPS)}


def shift(site, step):
    return tuple(site[axis] + step[axis] for axis in range(3))


def relation(left, right):
    if left == right:
        return 0
    return 1 if left // 2 == right // 2 else 2


class Rule:
    def __init__(self, same, opposite, orthogonal):
        self.weights = (same, opposite, orthogonal)
        self.one = same + opposite + 4 * orthogonal
        self.phi = [[self.weights[relation(left, right)] for right in range(6)] for left in range(6)]
        self.kernel = [[F(self.phi[left][right], self.one) for right in range(6)] for left in range(6)]

    def normalizer(self, recorded):
        total = F(0)
        for value in range(6):
            weight = F(1)
            for parent in recorded:
                weight *= self.kernel[parent][value]
            total += weight
        return total

    def conditional(self, recorded, value):
        if not recorded:
            return F(1, 6)
        weight = F(1)
        for parent in recorded:
            weight *= self.kernel[parent][value]
        return weight / self.normalizer(recorded)


class Window:
    def __init__(self, name, sites):
        self.name = name
        self.sites = list(sites)
        self.index = {site: position for position, site in enumerate(self.sites)}
        self.parents = []
        self.neighbours = []
        for site in self.sites:
            self.parents.append([self.index[shift(site, tuple(-step[axis] for axis in range(3)))] for step in PARENT_STEPS if shift(site, tuple(-step[axis] for axis in range(3))) in self.index])
            self.neighbours.append([self.index[shift(site, step)] for step in STEPS if shift(site, step) in self.index])
        self.edges = sorted({tuple(sorted((left, right))) for left in range(len(self.sites)) for right in self.neighbours[left]})

    def configurations(self):
        return itertools.product(range(6), repeat=len(self.sites))


def product(values):
    total = F(1)
    for value in values:
        total *= value
    return total


def causal(window, rule):
    law = {}
    for values in window.configurations():
        law[values] = product(rule.conditional(tuple(sorted(values[parent] for parent in window.parents[site])), values[site]) for site in range(len(window.sites)))
    return law


def linear_extensions(window):
    extensions = []
    for order in itertools.permutations(range(len(window.sites))):
        position = {site: index for index, site in enumerate(order)}
        if all(position[parent] < position[site] for site in range(len(window.sites)) for parent in window.parents[site]):
            extensions.append(order)
    return extensions


def sequential(window, rule, order, values):
    done = set()
    probability = F(1)
    for site in order:
        recorded = tuple(sorted(values[neighbour] for neighbour in window.neighbours[site] if neighbour in done))
        probability *= rule.conditional(recorded, values[site])
        done.add(site)
    return probability


def clock(window, rule, rate):
    law = {}
    for values in window.configurations():
        total = F(0)
        for order in itertools.permutations(range(len(window.sites))):
            done = set()
            probability = F(1)
            for site in order:
                weights = {other: rate(other, frozenset(done), values) for other in range(len(window.sites)) if other not in done}
                scale = sum(weights.values())
                if scale == 0 or weights[site] == 0:
                    probability = F(0)
                    break
                probability *= F(weights[site], scale)
                recorded = tuple(sorted(values[neighbour] for neighbour in window.neighbours[site] if neighbour in done))
                probability *= rule.conditional(recorded, values[site])
                done.add(site)
            total += probability
        law[values] = total
    return law


def static(window, rule):
    weights = {}
    for values in window.configurations():
        weights[values] = product(rule.phi[values[left]][values[right]] for left, right in window.edges)
    partition = sum(weights.values())
    return {values: F(weight, partition) for values, weight in weights.items()}


def distance(left, right):
    return sum((abs(left[values] - right[values]) for values in left), F(0)) / 2


def joint(window, rule, unit, done, values):
    members = list(unit)

    def weight(choice):
        total = 1
        for position, site in enumerate(members):
            for neighbour in window.neighbours[site]:
                if neighbour in done:
                    total *= rule.phi[choice[position]][values[neighbour]]
                elif neighbour in members and members.index(neighbour) > position:
                    total *= rule.phi[choice[position]][choice[members.index(neighbour)]]
        return total

    partition = sum(weight(choice) for choice in itertools.product(range(6), repeat=len(members)))
    return F(weight([values[site] for site in members]), partition)


WINDOWS = (
    Window("bent chain", ((0, 0, 0), (1, 0, 0), (1, 1, 0))),
    Window("straight chain", ((0, 0, 0), (1, 0, 0), (2, 0, 0))),
    Window("V", ((0, 1, 0), (1, 0, 0), (1, 1, 0))),
    Window("lambda", ((1, 0, 0), (0, 0, 0), (0, 1, 0))),
    Window("plaquette", ((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0))),
    Window("claw", ((0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1))),
)
RULES = (Rule(3, 1, 2), Rule(5, 1, 2))

extensions_ok = True
for window in WINDOWS:
    for rule in RULES:
        target = causal(window, rule)
        for order in linear_extensions(window):
            for values in window.configurations():
                if sequential(window, rule, order, values) != target[values]:
                    extensions_ok = False
check("linear extensions", extensions_ok, "every parent-first order of the six windows equals the causal product, at (3,1,2) and (5,1,2)")


def formable_rate(window, site, done):
    if site in done or any(parent not in done for parent in window.parents[site]):
        return 0
    return 1 + site


causal_clock_ok = True
for window in WINDOWS[:4]:
    target = causal(window, RULES[0])
    produced = clock(window, RULES[0], lambda site, done, values: formable_rate(window, site, done))
    causal_clock_ok = causal_clock_ok and all(produced[values] == target[values] for values in target) and sum(target.values()) == 1
check("causal clocks", causal_clock_ok, "rates supported only on formable sites reproduce the causal product")

pair_mass = {}
for left in range(6):
    for right in range(6):
        pair_mass[(left, right)] = RULES[0].normalizer((left, right))
factors = sorted({int(144 * pair_mass[(left, right)]) for left in range(6) for right in range(6)})
static_pair = {}
for left in range(6):
    for right in range(6):
        static_pair[(left, right)] = pair_mass[(left, right)] / 6
free_pair = {key: F(1, 36) for key in static_pair}
pair_gap = distance(static_pair, free_pair)
check(
    "pair gap",
    factors == [22, 24, 26] and pair_gap == F(1, 72),
    "144 K_2 is 22, 24 or 26, and the two-parent marginal differs from 1/36 by total variation 1/72",
)


def uniform(site, done, values):
    return 0 if site in done else 1


def seeded(window):
    def rate(site, done, values):
        if site in done:
            return 0
        if not done or any(neighbour in done for neighbour in window.neighbours[site]):
            return 1
        return 0
    return rate


def attracting(window):
    def rate(site, done, values):
        if site in done:
            return 0
        return 1 + sum(1 for neighbour in window.neighbours[site] if neighbour in done)
    return rate


def parallel(window):
    def rate(site, done, values):
        if site in done:
            return 0
        aligned = 0
        for neighbour in window.neighbours[site]:
            if neighbour in done:
                step = tuple(window.sites[site][axis] - window.sites[neighbour][axis] for axis in range(3))
                if values[neighbour] == DIRECTION[step]:
                    aligned = 1
        return 1 + aligned
    return rate


three = {window.name: window for window in WINDOWS[:4]}
rule = RULES[0]
distances = {}
for name in ("bent chain", "V", "lambda"):
    window = three[name]
    target = causal(window, rule)
    distances[(name, "uniform")] = distance(clock(window, rule, uniform), target)
    distances[(name, "seeded")] = distance(clock(window, rule, seeded(window)), target)
    distances[(name, "attracting")] = distance(clock(window, rule, attracting(window)), target)
    distances[(name, "parallel")] = distance(clock(window, rule, parallel(window)), target)
    distances[(name, "static")] = distance(static(window, rule), target)

expected = {
    ("V", "static"): F(1, 72),
    ("V", "uniform"): F(1, 108),
    ("V", "seeded"): F(1, 72),
    ("V", "attracting"): F(7, 648),
    ("V", "parallel"): F(37, 3888),
    ("bent chain", "static"): F(0),
    ("bent chain", "uniform"): F(1, 216),
    ("bent chain", "seeded"): F(0),
    ("bent chain", "attracting"): F(1, 324),
    ("bent chain", "parallel"): F(17, 3888),
    ("lambda", "static"): F(0),
    ("lambda", "seeded"): F(0),
    ("lambda", "uniform"): F(1, 216),
    ("lambda", "attracting"): F(1, 324),
    ("lambda", "parallel"): F(17, 3888),
}
check(
    "three-site distances",
    all(distances[key] == value for key, value in expected.items()),
    "at (3,1,2) the V, bent chain and lambda match the stated total variations, including parallel growth",
)

vee = three["V"]
target = causal(vee, rule)
domino = {}
for values in vee.configurations():
    domino[values] = rule.conditional((), values[1]) * joint(vee, rule, (0, 2), {1}, values)
check(
    "domino",
    distance(domino, target) == F(1, 72) and distance(domino, static(vee, rule)) == 0,
    "forming the parent-child domino after the other parent is the static law and differs by 1/72",
)

bond = Window("bond", ((0, 0, 0), (1, 0, 0)))
bond_target = causal(bond, rule)
bond_ok = distance(static(bond, rule), bond_target) == 0 and all(
    distance(clock(bond, rule, rate), bond_target) == 0 for rate in (uniform, seeded(bond), attracting(bond), parallel(bond))
)
check("two sites", bond_ok, "every candidate on a single bond reproduces the causal law")

marginal_ok = True
for window in WINDOWS:
    target = causal(window, rule)
    for size in range(1, len(window.sites)):
        for chosen in itertools.combinations(range(len(window.sites)), size):
            if not all(parent in chosen for site in chosen for parent in window.parents[site]):
                continue
            marginal = {}
            for values in window.configurations():
                key = tuple(values[site] for site in chosen)
                marginal[key] = marginal.get(key, F(0)) + target[values]
            sub = Window("sub", [window.sites[site] for site in chosen])
            restricted = causal(sub, rule)
            if any(marginal[key] != restricted[key] for key in marginal):
                marginal_ok = False
check("marginals", marginal_ok, "on every down-closed subset the causal marginal is the subset's own causal law")

plaquette = WINDOWS[4]
plaquette_target = causal(plaquette, rule)
plaquette_distances = {
    "static": distance(static(plaquette, rule), plaquette_target),
    "uniform": distance(clock(plaquette, rule, uniform), plaquette_target),
    "seeded": distance(clock(plaquette, rule, seeded(plaquette)), plaquette_target),
    "attracting": distance(clock(plaquette, rule, attracting(plaquette)), plaquette_target),
    "parallel": distance(clock(plaquette, rule, parallel(plaquette)), plaquette_target),
}
check(
    "plaquette",
    plaquette_distances == {
        "static": F(455, 31176),
        "uniform": F(53347, 4416984),
        "seeded": F(691, 61776),
        "attracting": F(129427, 11042460),
        "parallel": F(12853, 1070784),
    },
    "on the four-site diamond the five noncausal laws have the stated total variations",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. Every parent-first order equals the product of one-site kernels. Rates supported only on "
    "formable sites do too. At (3,1,2) the V differs from that product by 1/72 for the static law, 1/108 for uniform clocks, "
    "1/72 for the seeded clock, 7/648 for the attracting clock and 37/3888 for parallel growth. The bent chain and lambda give "
    "1/216, 0, 1/324 and 17/3888 for those four clocks, and the static law agrees. A two-site window does not separate them. "
    "Down-closed marginals reproduce the subset law. The random policy sample was not repeated.",
    flush=True,
)
print(
    "HIT: confirmed - on a causal window every parent-first clock finishes in the product of kernels given the parents, "
    "and the recorded noncausal candidates first differ from it on a three-site window by the stated total variations",
    flush=True,
)
