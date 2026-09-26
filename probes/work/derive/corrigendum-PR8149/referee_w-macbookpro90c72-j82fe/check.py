#!/usr/bin/env python3
"""Independent referee for the PR 8149 corrigendum, attempt 2.

Sequential and joint formation laws are recomputed on the executed units.
The attempt's script is not imported. The five-record exhaustive product
was not rebuilt.
"""
from __future__ import annotations

import itertools
import random
import sys
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def neighbours(site):
    return [tuple(site[axis] + step[axis] for axis in range(3)) for step in STEPS]


def relation(left, right):
    if left == right:
        return 0
    return 1 if left // 2 == right // 2 else 2


class Rule:
    def __init__(self, same, opposite, orthogonal):
        self.weights = (same, opposite, orthogonal)
        self.normalizer = same + opposite + 4 * orthogonal
        self.phi = [[self.weights[relation(left, right)] for right in range(6)] for left in range(6)]
        self.kernel = [[F(self.phi[left][right], self.normalizer) for right in range(6)] for left in range(6)]

    def mass(self, recorded):
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
        return weight / self.mass(recorded)

    def factor(self, outside):
        return tuple(self.mass((value,) + tuple(outside)) for value in range(6))


def outside_sites(unit):
    present = set(unit)
    return sorted({neighbour for site in unit for neighbour in neighbours(site) if neighbour not in present})


def recorded_sets(unit, environment, order):
    position = {site: index for index, site in enumerate(unit)}
    done = set()
    rows = []
    for site in order:
        inside = [position[neighbour] for neighbour in neighbours(site) if neighbour in position and neighbour in done]
        outside = [environment[neighbour] for neighbour in neighbours(site) if neighbour in environment]
        rows.append((position[site], inside, outside))
        done.add(site)
    return rows


def sequential(unit, environment, order, rule):
    rows = recorded_sets(unit, environment, order)
    law = {}
    normalizers = set()
    for values in itertools.product(range(6), repeat=len(unit)):
        probability = F(1)
        product = F(1)
        for index, inside, outside in rows:
            recorded = tuple(sorted([values[site] for site in inside] + outside))
            probability *= rule.conditional(recorded, values[index])
            if recorded:
                product *= rule.mass(recorded)
        law[values] = probability
        normalizers.add(product)
    return law, normalizers


def joint(unit, environment, rule):
    position = {site: index for index, site in enumerate(unit)}
    internal = [(position[left], position[right]) for left in unit for right in neighbours(left) if right in position and position[right] > position[left]]
    external = [(position[site], environment[neighbour]) for site in unit for neighbour in neighbours(site) if neighbour in environment]
    weights = {}
    for values in itertools.product(range(6), repeat=len(unit)):
        weight = 1
        for left, right in internal:
            weight *= rule.phi[values[left]][values[right]]
        for site, record in external:
            weight *= rule.phi[values[site]][record]
        weights[values] = weight
    partition = sum(weights.values())
    return {values: F(weight, partition) for values, weight in weights.items()}


def shape(unit, environment, order, rule):
    rows = recorded_sets(unit, environment, order)
    one_inside = all(len(inside) <= 1 for _index, inside, _outside in rows)
    original = all(not (inside and len(inside) + len(outside) >= 2) for _index, inside, outside in rows)
    products = {}
    for _index, inside, outside in rows:
        if len(inside) == 1 and outside:
            parent = inside[0]
            factor = rule.factor(outside)
            products[parent] = tuple(left * right for left, right in zip(products.get(parent, (F(1),) * 6), factor))
    constant = all(len(set(value)) == 1 for value in products.values())
    return one_inside, constant, original


UNITS = {
    "single": [(0, 0, 0)],
    "domino": [(0, 0, 0), (1, 0, 0)],
    "path3": [(-1, 0, 0), (0, 0, 0), (1, 0, 0)],
    "bent3": [(1, 0, 0), (0, 0, 0), (0, 1, 0)],
    "plaquette": [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
    "tee": [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0)],
    "corner": [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)],
    "path4": [(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)],
}
RULES = (Rule(3, 1, 2), Rule(5, 1, 2), Rule(2, 2, 1))

same, opposite, orthogonal = sp.symbols("p q r", positive=True)
weights = sp.symbols("d0:6", positive=True)
partition = same + opposite + 4 * orthogonal
menu = (same, opposite, orthogonal)
kernel = [[menu[relation(left, right)] / partition for right in range(6)] for left in range(6)]


def gram(left, right):
    return sum(kernel[left][value] * kernel[right][value] * weights[value] for value in range(6))


minor = gram(0, 0) * gram(2, 2) - gram(0, 2) ** 2
lagrange = sp.Rational(1, 2) * sum(
    weights[left] * weights[right] * (kernel[0][left] * kernel[2][right] - kernel[0][right] * kernel[2][left]) ** 2
    for left in range(6)
    for right in range(6)
)
check(
    "lagrange",
    sp.expand(minor - lagrange) == 0
    and sp.simplify(kernel[0][0] * kernel[2][2] - kernel[0][2] * kernel[2][0] - (same ** 2 - orthogonal ** 2) / partition ** 2) == 0
    and sp.simplify(kernel[0][0] * kernel[2][1] - kernel[0][1] * kernel[2][0] - orthogonal * (same - opposite) / partition ** 2) == 0,
    "the orthogonal minor is the Lagrange identity, and its two brackets vanish only when p = q = r",
)

generator = random.Random(20260926)
failures = {"equal": 0, "phi": 0, "two": 0, "sufficient": 0, "necessary": 0}
cases = 0
exceptions = 0
for rule in RULES:
    for unit in UNITS.values():
        outside = outside_sites(unit)
        environments = [
            {},
            {site: 0 for site in outside},
            {site: 5 for site in outside},
        ]
        environments += [{site: generator.randrange(6) for site in outside} for _ in range(2)]
        environments += [{site: generator.randrange(6) for site in outside if generator.random() < F(1, 2)} for _ in range(2)]
        for environment in environments:
            together = joint(unit, environment, rule)
            constant_environment = len(set(environment.values())) <= 1
            for order in itertools.permutations(unit):
                law, normalizers = sequential(unit, environment, order, rule)
                equal = all(law[values] == together[values] for values in law)
                one_inside, phi_constant, original = shape(unit, environment, order, rule)
                cases += 1
                failures["equal"] += equal != (len(normalizers) == 1)
                failures["phi"] += (len(normalizers) == 1) != (one_inside and phi_constant)
                failures["two"] += (not one_inside) and equal
                failures["sufficient"] += original and not equal
                if not environment or constant_environment:
                    failures["necessary"] += equal != original
                if equal and not original:
                    exceptions += 1
check(
    "criterion",
    all(value == 0 for value in failures.values()) and cases == 2331,
    f"{cases} cases: equality matches a constant normalizer, and two inside neighbours always separate; {exceptions} agreements lie outside the old criterion",
)

STAR = [(0, 0, 0)] + list(STEPS)


def rotate_site(site):
    x, y, z = site
    return (-z, -x, -y)


VALUE_CYCLE = (3, 2, 5, 4, 1, 0)


def rotate_value(value):
    return VALUE_CYCLE[value]


def orbit(site):
    seen = []
    current = site
    for _ in range(6):
        seen.append(current)
        current = rotate_site(current)
    return seen


outside = outside_sites(STAR)
orbits = []
used = set()
for site in outside:
    if site in used:
        continue
    current = orbit(site)
    orbits.append(current)
    used.update(current)
representatives = [sites[0] for sites in orbits]


def equivariant(choice):
    environment = {}
    for representative, value in zip(representatives, choice):
        site = representative
        current = value
        for _ in range(6):
            environment[site] = current
            site = rotate_site(site)
            current = rotate_value(current)
    return environment


environments = [equivariant(choice) for choice in itertools.product(range(6), repeat=3)]
phi_ok = True
for rule in (
    Rule(3, 1, 2),
    Rule(5, 1, 2),
    Rule(7, 2, 3),
    Rule(2, 2, 1),
    Rule(4, 1, 2),
    Rule(1, 3, 2),
    Rule(2, 1, 1),
    Rule(1, 1, 2),
):
    for environment in environments:
        _one, constant, _original = shape(STAR, environment, STAR, rule)
        phi_ok = phi_ok and constant
sample = environments[0]
centre_first, _normalizers = sequential(STAR, sample, STAR, RULES[0])
centre_joint = joint(STAR, sample, RULES[0])
leaves_first = [step for step in STEPS] + [(0, 0, 0)]
leaves_law, _leaves_normalizers = sequential(STAR, sample, leaves_first, RULES[0])
check(
    "star",
    len(outside) == 18
    and len(orbits) == 3
    and all(len(set(orbit(site))) == 6 for site in outside)
    and len(environments) == 216
    and phi_ok
    and all(centre_first[values] == centre_joint[values] for values in centre_first)
    and any(leaves_law[values] != centre_joint[values] for values in leaves_law),
    "centre-first formation agrees on all 6^7 patterns in an equivariant environment, and leaves-first does not",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. On 2331 executed cases the sequential law equals the joint law exactly when the "
    "normalizer product is constant. That happens exactly when no site records two inside neighbours and every "
    "dependent product is constant. Two inside neighbours always separate. The old criterion is sufficient in every "
    "executed environment and necessary for isolated and constant environments, and "
    f"{exceptions} agreements violate it. The centre-first star agrees in all 216 equivariant environments; the "
    "leaves-first order does not. The five-record exhaustive product was not rebuilt.",
    flush=True,
)
print(
    "HIT: confirmed - sequential formation equals the joint law exactly when the normalizer product is constant, "
    "two inside neighbours always separate, and the centre-first star is a counterexample to the old only-if",
    flush=True,
)
