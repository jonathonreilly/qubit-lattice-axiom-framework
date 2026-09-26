#!/usr/bin/env python3
"""Independent referee for local-clock-for-inertia-with-weights a2.

Six-axis inertial streaming on the 3-torus at (p, q, r) = (3, 1, 2).
The attempt's script is not imported. A float linear program only proposes
a vector; every balance and the Farkas inequality are checked in Fractions.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import numpy as np
from scipy.optimize import linprog

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


SIDE = 3
SITES = [(i, j, k) for i in range(SIDE) for j in range(SIDE) for k in range(SIDE)]
AXIS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
AXIS_INDEX = {step: i for i, step in enumerate(AXIS)}
SAME, OPPOSITE, ORTHOGONAL = 3, 1, 2


def shift(site, step):
    return tuple((site[i] + step[i]) % SIDE for i in range(3))


def weight(left, right):
    if left == right:
        return SAME
    if AXIS[left] == tuple(-AXIS[right][i] for i in range(3)):
        return OPPOSITE
    return ORTHOGONAL


ROTATIONS = [
    (perm, signs)
    for perm in itertools.permutations(range(3))
    for signs in itertools.product((1, -1), repeat=3)
]


def rotate(spec, vector):
    perm, signs = spec
    return tuple(signs[i] * vector[perm[i]] for i in range(3))


STABILISER = [spec for spec in ROTATIONS if rotate(spec, (1, 0, 0)) == (1, 0, 0)]


def pair_weight(occupied, scale):
    total = F(1)
    seen = set()
    for site, content in occupied.items():
        for step in AXIS:
            other = shift(site, step)
            if other in occupied and (other, site) not in seen:
                seen.add((site, other))
                total *= scale * weight(content, occupied[other])
    return total


def site_weight(occupied, site, scale):
    total = F(1)
    content = occupied[site]
    for step in AXIS:
        other = shift(site, step)
        if other in occupied:
            total *= scale * weight(content, occupied[other])
    return total


def predecessor(occupied, site):
    content = occupied[site]
    origin = shift(site, tuple(-AXIS[content][i] for i in range(3)))
    previous = dict(occupied)
    if origin in occupied:
        previous[site], previous[origin] = occupied[origin], occupied[site]
    else:
        del previous[site]
        previous[origin] = content
    return previous, origin


def pattern(occupied, site):
    content = occupied[site]
    step = AXIS[content]
    target = shift(site, step)
    frame = next(spec for spec in ROTATIONS if rotate(spec, step) == (1, 0, 0))
    neighbourhood = set()
    for endpoint in (site, target):
        for step_out in AXIS:
            neighbourhood.add(shift(endpoint, step_out))
    neighbourhood.discard(site)
    neighbourhood.discard(target)
    others = []
    for place in neighbourhood:
        if place in occupied:
            relative = tuple((place[i] - site[i] + 1) % SIDE - 1 for i in range(3))
            others.append((relative, occupied[place]))
    best = None
    for spec in STABILISER:
        def turn(vector, spec=spec):
            return rotate(spec, rotate(frame, vector))

        def turn_content(index, spec=spec):
            return AXIS_INDEX[turn(AXIS[index], spec)]

        target_state = ("occupied", turn_content(occupied[target])) if target in occupied else ("empty",)
        companions = tuple(sorted((turn(relative), turn_content(index)) for relative, index in others))
        candidate = (turn_content(content), target_state, companions)
        if best is None or candidate < best:
            best = candidate
    return best


def balance(occupied, scale):
    coefficient = {}
    here = pair_weight(occupied, scale)
    for site in occupied:
        key = pattern(occupied, site)
        coefficient[key] = coefficient.get(key, F(0)) + here
    for site in occupied:
        previous, origin = predecessor(occupied, site)
        key = pattern(previous, origin)
        coefficient[key] = coefficient.get(key, F(0)) - pair_weight(previous, scale)
    return tuple(sorted((key, value) for key, value in coefficient.items() if value != 0))


def three_records():
    origin = (0, 0, 0)
    others = [site for site in SITES if site != origin]
    configs = []
    for rest in itertools.combinations(others, 2):
        places = (origin,) + rest
        for contents in itertools.product(range(6), repeat=3):
            configs.append({places[i]: contents[i] for i in range(3)})
    return configs


def stream(occupied, site):
    content = occupied[site]
    target = shift(site, AXIS[content])
    moved = dict(occupied)
    if target in occupied:
        moved[site], moved[target] = occupied[target], occupied[site]
    else:
        del moved[site]
        moved[target] = content
    return moved


CONFIGS = three_records()
counting_ok = len(CONFIGS) == 70200 == len(list(itertools.combinations(range(26), 2))) * 6**3

scale_one = F(1)
defects = 0
largest = (F(0), None)
for occupied in CONFIGS:
    leaving = sum((pair_weight(occupied, scale_one) / site_weight(occupied, site, scale_one) for site in occupied), F(0))
    entering = F(0)
    for site in occupied:
        previous, origin = predecessor(occupied, site)
        entering += pair_weight(previous, scale_one) / site_weight(previous, origin, scale_one)
    if leaving != entering:
        defects += 1
        gap = leaving - entering
        if abs(gap) > abs(largest[0]):
            largest = (gap, occupied)
witness = {((0, 0, 0), 2), ((0, 0, 1), 4), ((0, 1, 0), 2)}
check(
    "V1 local clock",
    counting_ok and defects == 3168 and largest[0] == 3 and set(largest[1].items()) == witness,
    "70200 three-record states, 3168 local-clock failures, largest defect 3 at the stated witness",
)

number_kept = True
contents_kept = True
for occupied in CONFIGS:
    for site in occupied:
        moved = stream(occupied, site)
        number_kept = number_kept and len(moved) == len(occupied)
        contents_kept = contents_kept and sorted(moved.values()) == sorted(occupied.values())
obstruction = {(1, 0, 1): 1, (1, 0, 2): 4, (1, 1, 2): 1, (1, 2, 1): 1}
for site in obstruction:
    moved = stream(obstruction, site)
    number_kept = number_kept and len(moved) == len(obstruction)
    contents_kept = contents_kept and sorted(moved.values()) == sorted(obstruction.values())
check(
    "V2 conservation",
    number_kept and contents_kept,
    "every three-record event and the four-record witness keep the record count and the content multiset",
)


def rows_for(scale, extra=()):
    distinct = {balance(occupied, scale) for occupied in CONFIGS}
    distinct.discard(())
    equations = list(distinct)
    for occupied in extra:
        equations.append(balance(occupied, scale))
    columns = sorted({key for equation in equations for key, _value in equation})
    index = {key: i for i, key in enumerate(columns)}
    return equations, columns, index


def exact_rates(equations, columns, index):
    matrix = np.zeros((len(equations), len(columns)))
    for row, equation in enumerate(equations):
        for key, value in equation:
            matrix[row, index[key]] = float(value)
    proposed = linprog(
        np.zeros(len(columns)),
        A_eq=matrix,
        b_eq=-matrix @ np.ones(len(columns)),
        bounds=[(0, None)] * len(columns),
        method="highs",
    )
    if proposed.status != 0:
        return None
    rates = [F(value).limit_denominator(10**9) + 1 for value in proposed.x]
    if any(rate <= 0 for rate in rates):
        return None
    if any(sum(value * rates[index[key]] for key, value in equation) != 0 for equation in equations):
        return None
    return rates


feasible = True
for scale, label, equations_expected, patterns_expected in (
    (F(1), "c = 1", 332, 274),
    (F(1, 2), "c = 1/2", 334, None),
):
    equations, columns, index = rows_for(scale)
    rates = exact_rates(equations, columns, index)
    count_ok = len(equations) == equations_expected and (patterns_expected is None or len(columns) == patterns_expected)
    feasible = feasible and count_ok and rates is not None
    span = "" if rates is None else f" rates in [{min(rates)}, {max(rates)}]"
    check(
        "V3 " + label,
        count_ok and rates is not None,
        f"{len(equations)} equations, {len(columns)} patterns, exact positive solution{span}",
    )

equations, columns, index = rows_for(F(1), extra=(obstruction,))
matrix = np.zeros((len(equations), len(columns)))
for row, equation in enumerate(equations):
    for key, value in equation:
        matrix[row, index[key]] = float(value)
blocked = linprog(
    np.zeros(len(columns)),
    A_eq=matrix,
    b_eq=-matrix @ np.ones(len(columns)),
    bounds=[(0, None)] * len(columns),
    method="highs",
)
certificate = linprog(
    c=matrix @ np.ones(len(columns)),
    A_ub=matrix.T,
    b_ub=np.zeros(len(columns)),
    bounds=[(-1, 1)] * len(equations),
    method="highs",
)
dual = [F(value).limit_denominator(10**9) for value in certificate.x] if certificate.success else None
products = [F(0)] * len(columns)
if dual is not None:
    for row, equation in enumerate(equations):
        if dual[row] == 0:
            continue
        for key, value in equation:
            products[index[key]] += dual[row] * value
farkas_ok = (
    len(columns) == 275
    and blocked.status != 0
    and dual is not None
    and all(value <= 0 for value in products)
    and sum(products) == F(-36, 5)
)
check(
    "V4 four records",
    farkas_ok,
    f"{len(equations)} equations, {len(columns)} patterns, sum of the certificate "
    + (str(sum(products)) if dual is not None else "missing"),
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial on the 3-torus at (3,1,2). Distance-one rates make pi stationary "
    "on the whole three-record sector, at c = 1 (332 equations, 274 patterns) and at c = 1/2 "
    "(334 equations), with a strictly positive solution checked in exact arithmetic. Adjoining "
    "(1,0,1):-x, (1,0,2):+z, (1,1,2):-x, (1,2,1):-x makes that class infeasible: a rational "
    "Farkas vector is nonpositive on all 275 patterns and sums to -36/5. The local clock 1/pi_x "
    "fails on 3168 of the 70200 three-record states, with largest defect 3. Record number and the "
    "content multiset are kept by every checked event. A larger window and a wider locality class "
    "were not examined.",
    flush=True,
)
print(
    "HIT: confirmed - three-record stationarity is feasible with strictly positive distance-one "
    "rates at c = 1 and at c = 1/2, and one four-record configuration makes the same class "
    "infeasible by an exact certificate summing to -36/5",
    flush=True,
)
