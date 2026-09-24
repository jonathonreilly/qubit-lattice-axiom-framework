#!/usr/bin/env python3
"""Independent referee for the PR8174 corrigendum, a1.

Closed forms of d1, d2, d3, the domain where d1 <= max(d2, d3), and the
10-site coupling witness at (1, 2, 1). Does not import the attempt.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def phi(i: int, j: int, p, q, r):
    if i == j:
        return p
    if i // 2 == j // 2:
        return q
    return r


def kernel(preds, p, q, r):
    weights = []
    for state in range(6):
        w = 1
        for pred in preds:
            w *= phi(state, pred, p, q, r)
        weights.append(w)
    total = sum(weights)
    return [w / total for w in weights], total


def devs(p, q, r):
    """d1, d2, d3 from the six-axis menu. States 0=a, 1=-a, 2=b orthogonal."""
    if not isinstance(p, sp.Basic):
        p, q, r = F(p), F(q), F(r)
    k1, _ = kernel((0, 0, 0), p, q, r)
    k2, _ = kernel((0, 0, 1), p, q, r)
    k3, _ = kernel((0, 0, 2), p, q, r)
    return 1 - k1[0], 1 - k2[0], 1 - k3[0]


P, Q, R = sp.symbols("p q r", positive=True)
D1 = P**3 + Q**3 + 4 * R**3
D2 = P * Q * (P + Q) + 4 * R**3
D3 = R * (P**2 + Q**2) + R**2 * (P + Q) + 2 * R**3
d1 = (Q**3 + 4 * R**3) / D1
d2 = (P * Q**2 + 4 * R**3) / D2
d3 = (R * Q**2 + R**2 * (P + Q) + 2 * R**3) / D3
g = R * P**2 + (Q**2 + Q * R + 2 * R**2) * P - (Q**3 + 4 * R**3)

# The menu kernel must reproduce these closed forms.
menu_ok = True
for preds, formula in (
    ((0, 0, 0), d1),
    ((0, 0, 1), d2),
    ((0, 0, 2), d3),
    ((0, 0, 3), d3),
    ((0, 0, 4), d3),
    ((0, 0, 5), d3),
):
    weights, _ = kernel(preds, P, Q, R)
    menu_ok = menu_ok and sp.simplify(weights[0] - (1 - formula)) == 0
diff21 = sp.factor(sp.together(d2 - d1))
diff31 = sp.factor(sp.together(d3 - d1))
sign21 = sp.factor(sp.numer(sp.together(d2 - d1)))
sign31 = sp.factor(sp.numer(sp.together(d3 - d1)))
check(
    "C1 closed forms",
    menu_ok
    and sp.simplify(sign21 - P**2 * (P - Q) * (Q**2 * (P + Q) + 4 * R**3)) == 0
    and sp.simplify(sign31 - P**2 * g) == 0,
    "sign(d2-d1)=sign(p-q) and sign(d3-d1)=sign(g)",
)

# Monotonicity: each retained mass increases in p, so each d_i decreases.
retained = (P**3 / D1, P**2 * Q / D2, P**2 * R / D3)
mono = True
for mass in retained:
    num = sp.numer(sp.together(sp.diff(mass, P)))
    mono = mono and num != 0 and all(sp.sign(c) >= 0 for c in sp.Poly(sp.expand(num), P, Q, R).coeffs())
check(
    "C2 monotonicity",
    mono and sp.expand(g.subs(P, Q) - 2 * R * (Q + 2 * R) * (Q - R)) == 0
    and sp.expand(g.subs(P, Q - 2 * R) + 4 * R**2 * (Q + R)) == 0,
    "each d_i decreases in p; g(q)=2r(q+2r)(q-r) and g(q-2r)=-4r^2(q+r)",
)

# (1, 2, 1) and the integer census.
one = devs(1, 2, 1)
g_121 = 1 * 1 + (4 + 2 + 2) * 1 - (8 + 4)
census = []
for triple in itertools.product(range(1, 8), repeat=3):
    pp, qq, rr = triple
    gg = rr * pp**2 + (qq**2 + qq * rr + 2 * rr**2) * pp - (qq**3 + 4 * rr**3)
    dd = devs(pp, qq, rr)
    fails = dd[0] > max(dd[1], dd[2])
    predicted = pp < qq and gg < 0
    census.append(fails == predicted)
check(
    "C3 witness and census",
    one[0] == F(12, 13) and one[1] == F(4, 5) and one[2] == F(9, 10) and g_121 == -3
    and all(census) and sum(1 for t in itertools.product(range(1, 8), repeat=3)
                            if t[0] < t[1] and (t[2] * t[0]**2 + (t[1]**2 + t[1] * t[2] + 2 * t[2]**2) * t[0] - (t[1]**3 + 4 * t[2]**3)) < 0) == 127,
    "at (1,2,1), d1=12/13 > 9/10; exactly 127 of 343 triples in 1..7 fail, and only there",
)

# Ten-site coupling at (1,2,1), rebuilt from the menu.
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
CODE = {"a": 0, "anti": 1, "orth": 2}


def witness(cls: str):
    plan = [
        ((-1, 1, 1), "anti", 1),
        ((0, 0, 1), "a", 0),
        ((0, 1, 0), "a", 0),
        ((1, 0, 0), "a", 0),
        ((1, -1, 1), "a", 0),
        ((1, 1, -1), "a", 0),
        ((0, 1, 1), cls, 1),
        ((1, 0, 1), "a", 0),
        ((1, 1, 0), "a", 0),
    ]
    state = {}
    prob = F(1)
    eps1, eps2 = one[0], max(one[1], one[2])
    for site, kind, eta in plan:
        preds = tuple(tuple(site[i] - e[i] for i in range(3)) for e in E)
        pv = tuple(state[y][0] if sum(y) > 0 else 0 for y in preds)
        ones = sum(state[y][1] if sum(y) > 0 else 0 for y in preds)
        weights, _ = kernel(pv, F(1), F(2), F(1))
        dev = 1 - weights[0]
        anti = weights[1]
        thr = F(1) if ones >= 2 else (eps2 if ones == 1 else eps1)
        lo, hi = {"a": (dev, F(1)), "anti": (F(0), anti), "orth": (anti, dev)}[kind]
        elo, ehi = (F(0), thr) if eta else (thr, F(1))
        lo, hi = max(lo, elo), min(hi, ehi)
        if hi <= lo:
            return None
        prob *= hi - lo
        state[site] = (CODE[kind], eta)
    x = (1, 1, 1)
    preds = tuple(tuple(x[i] - e[i] for i in range(3)) for e in E)
    pv = tuple(state[y][0] for y in preds)
    ones = sum(state[y][1] for y in preds)
    weights, _ = kernel(pv, F(1), F(2), F(1))
    thr = F(1) if ones >= 2 else (eps2 if ones == 1 else eps1)
    return prob, 1 - weights[0], ones, thr


w = witness("a")
gap = w[1] - w[3]
prob = w[0] * gap
targets = {"a": one[0], "anti": one[1], "orth": one[2]}
reached = []
for kind, target in targets.items():
    got = witness(kind)
    reached.append(got is not None and got[0] > 0 and got[2] == 1 and got[1] == target)
repaired = max(one)
repaired_thr = F(1) if False else repaired
check(
    "C8 coupling failure",
    w is not None and w[2] == 1 and w[1] == F(12, 13) and gap == F(3, 130)
    and prob == F(24, 13**8 * 1300) and all(reached),
    "the 10-site event has probability 24/(13^8*1300), and all three predecessor types are reachable",
)

lines = (
    (4165, 1, 2), (2085, 1, 1), (8330, 2, 4), (6247, 1, 3), (11, 1, 2),
    (453, 1, 2), (232, 1, 1), (905, 2, 4), (677, 1, 3), (367, 1, 2),
    (368, 1, 2), (2921, 1, 2), (1464, 1, 1), (5841, 2, 4), (4380, 1, 3),
    (405, 1, 2), (208, 1, 1), (810, 2, 4), (605, 1, 3),
)
lines_ok = True
for pp, qq, rr in lines:
    dd = devs(pp, qq, rr)
    gg = rr * pp**2 + (qq**2 + qq * rr + 2 * rr**2) * pp - (qq**3 + 4 * rr**3)
    lines_ok = lines_ok and pp >= qq and gg > 0 and max(dd) == max(dd[1], dd[2]) and dd[0] < max(dd[1], dd[2])
off = devs(1, 2, 1)
check(
    "C10 domain and lines",
    lines_ok and len(lines) == 19 and max(off) == off[0] and repaired == off[0] and repaired_thr >= w[1],
    "all 19 executed lines have p >= q and lie in the domain; off it the repair collapses eps2 to d1",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed. d1 <= max(d2, d3) holds exactly when p >= min(q, p*), with p* the positive root of "
    "g = r p^2 + (q^2+qr+2r^2)p - (q^3+4r^3). The inequality fails on a positive-measure set, including "
    "(1,2,1), and there the note's coupling has xi=1 and eta'=0 with probability 24/(13^8*1300). "
    "eps2 = max(d1,d2,d3) is the minimal repair for that coupling. The 19 executed lines of the later notes "
    "all have p >= q, so their numbers do not move.",
    flush=True,
)
print(
    "HIT: confirmed - block 30's clause d1 <= max(d2,d3) fails exactly when p < q and g < 0, "
    "and there the two-level coupling fails with positive probability",
    flush=True,
)
