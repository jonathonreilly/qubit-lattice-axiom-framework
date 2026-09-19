#!/usr/bin/env python3
"""Referee check for J:derive:lightcone-formation:a3 (author w-macbookpro90c72-j05f1, grok-4.6); referee w-jonathonsmac4f50-j2e27.

Independent code. Light-cone chain: s'_x drawn with weight prod_{y in N[x]} phi(s'_x, s_y), N[x] = {x, x +- e_j} (a multiset on
L = 2, where x + e_j = x - e_j); pi(s) = prod_x Z_x(s), Z_x(s) = sum_{s'} prod_{y in N[x]} phi(s', s_y).

R1  step 1 (reversibility): pi(s) T(s -> s') = prod_x prod_{y in N[x]} phi(s'_x, s_y) is symmetric in (s, s') -- exhaustive on
    the 3-ring with the 3-stencil (6^6 pairs), and on random pairs on the NONdegenerate 3^3 torus with the 7-stencil for the six-axis
    menu at (5,1,2) and for sphere spins with phi = exp(beta s.s') (the task's menu), in log form.
R2  step 2: exact pi-weight ratios on the 2x2x2 torus at p = 3, 5, 10, 20 (one-site antipodal and orthogonal flips against a
    constant), my own closed form (the flip site, its three neighbours counted twice, the four other sites), cross-checked by a
    direct product over all eight sites.
R3  'decrease in p': the two ratios on an exact grid p = 2.01 .. 200 (fine near p = max(q, r) = 2): monotone or not, below 1 or not.
R4  scope: the task's light-cone law uses exp(beta s.S) on the sphere; its six-axis restriction has (p, q, r) = (e^beta, e^-beta, 1),
    which (p, 1, 2) is not (r > q there): the defect ratios for the exp six-axis weights at beta = 1, 2, 3 for comparison.
"""
from __future__ import annotations

import itertools
import math
import random
from fractions import Fraction as F

AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def phi6(a, b, p, q, r):
    d = dot(a, b)
    return p if d == 1 else (q if d == -1 else r)


def r1(seed=5):
    p, q, r = F(5), F(1), F(2)
    # 3-ring, 3-stencil, exhaustive
    n = 3
    nb = {x: [x, (x - 1) % n, (x + 1) % n] for x in range(n)}
    bad = 0
    for s in itertools.product(range(6), repeat=n):
        for t in itertools.product(range(6), repeat=n):
            lhs = F(1)
            rhs = F(1)
            for x in range(n):
                for y in nb[x]:
                    lhs *= phi6(AXES[t[x]], AXES[s[y]], p, q, r)
                    rhs *= phi6(AXES[s[x]], AXES[t[y]], p, q, r)
            bad += lhs != rhs
    # 3^3 torus, 7-stencil, random pairs, six-axis and sphere (log form)
    rng = random.Random(seed)
    L = 3
    sites = list(itertools.product(range(L), repeat=3))
    N7 = {x: [x] + [tuple((x[i] + (d if i == j else 0)) % L for i in range(3)) for j in range(3) for d in (1, -1)] for x in sites}
    bad6 = 0
    for _ in range(300):
        s = {x: rng.randrange(6) for x in sites}
        t = {x: rng.randrange(6) for x in sites}
        lhs = sum(math.log(phi6(AXES[t[x]], AXES[s[y]], 5, 1, 2)) for x in sites for y in N7[x])
        rhs = sum(math.log(phi6(AXES[s[x]], AXES[t[y]], 5, 1, 2)) for x in sites for y in N7[x])
        bad6 += abs(lhs - rhs) > 1e-9
    worst = 0.0
    for _ in range(300):
        def unit():
            v = [rng.gauss(0, 1) for _ in range(3)]
            nrm = math.sqrt(sum(c * c for c in v))
            return [c / nrm for c in v]
        s = {x: unit() for x in sites}
        t = {x: unit() for x in sites}
        beta = 1.7
        lhs = sum(beta * dot(t[x], s[y]) for x in sites for y in N7[x])
        rhs = sum(beta * dot(s[x], t[y]) for x in sites for y in N7[x])
        worst = max(worst, abs(lhs - rhs))
    return bad, bad6, worst


def cube_pi(conf, p, q, r):
    """direct product over the 8 sites of the 2x2x2 torus with the 7-stencil multiset."""
    sites = list(itertools.product((0, 1), repeat=3))
    tot = F(1)
    for x in sites:
        stencil = [x] + [tuple((x[i] + (1 if i == j else 0)) % 2 for i in range(3)) for j in range(3) for _ in (1, -1)]
        Z = F(0)
        for sp_ in AXES:
            w = F(1)
            for y in stencil:
                w *= phi6(sp_, conf[y], p, q, r)
            Z += w
        tot *= Z
    return tot


def ratios_closed(p, q, r):
    p, q, r = F(p), F(q), F(r)
    Zc = p ** 7 + q ** 7 + 4 * r ** 7
    # antipodal flip at x0: x0's stencil = itself (-a) once + three neighbours (+a) twice; neighbours: x0 twice, own/other 5 (+a)
    Zf_a = q * p ** 6 + p * q ** 6 + 4 * r ** 7
    Zn_a = p ** 5 * q ** 2 + q ** 5 * p ** 2 + 4 * r ** 7
    # orthogonal flip to b: x0's weights: s'=b: p r^6; s'=-b: q r^6; s'=+a: r p^6; s'=-a: r q^6; s' = +-c: r^7 each
    Zf_o = p * r ** 6 + q * r ** 6 + r * p ** 6 + r * q ** 6 + 2 * r ** 7
    # a neighbour of x0: 5 copies of +a (itself, and the two other neighbours twice) and 2 copies of b:
    # s'=+a: p^5 r^2; s'=-a: q^5 r^2; s'=b: r^5 p^2; s'=-b: r^5 q^2; s'=+-c: r^7 each
    Zn_o = p ** 5 * r ** 2 + q ** 5 * r ** 2 + r ** 5 * p ** 2 + r ** 5 * q ** 2 + 2 * r ** 7
    return (Zf_a * Zn_a ** 3) / Zc ** 4, (Zf_o * Zn_o ** 3) / Zc ** 4


def r2():
    a, b = (1, 0, 0), (0, 1, 0)
    sites = list(itertools.product((0, 1), repeat=3))
    out = {}
    for p in (3, 5, 10, 20):
        const = {x: a for x in sites}
        flip_a = dict(const)
        flip_a[(0, 0, 0)] = (-1, 0, 0)
        flip_o = dict(const)
        flip_o[(0, 0, 0)] = b
        pc = cube_pi(const, p, 1, 2)
        ra, ro = cube_pi(flip_a, p, 1, 2) / pc, cube_pi(flip_o, p, 1, 2) / pc
        ca, co = ratios_closed(p, 1, 2)
        out[p] = (ra, ro, ra == ca and ro == co)
    return out


def r3():
    fine = [F(200 + k, 100) for k in range(1, 26)]  # 2.01 .. 2.25
    grid = fine + [F(25, 10)] + [F(k) for k in (3, 4, 5, 7, 10, 15, 20, 30, 50, 100, 200)]
    vals = [(p, *ratios_closed(p, 1, 2)) for p in grid]
    mono_a = all(vals[i + 1][1] < vals[i][1] for i in range(len(vals) - 1))
    mono_o = all(vals[i + 1][2] < vals[i][2] for i in range(len(vals) - 1))
    below_one = all(v[1] < 1 and v[2] < 1 for v in vals)
    peak_o = max(vals, key=lambda v: v[2])
    tail = [v for v in vals if v[0] >= 3]
    mono_tail = all(tail[i + 1][1] < tail[i][1] and tail[i + 1][2] < tail[i][2] for i in range(len(tail) - 1))
    return vals, mono_a, mono_o, below_one, peak_o, mono_tail


def r4():
    out = []
    for beta in (1, 2, 3):
        p, q, r = math.exp(beta), math.exp(-beta), 1.0
        Zc = p ** 7 + q ** 7 + 4 * r ** 7
        Zf_a = q * p ** 6 + p * q ** 6 + 4 * r ** 7
        Zn_a = p ** 5 * q ** 2 + q ** 5 * p ** 2 + 4 * r ** 7
        Zf_o = p * r ** 6 + q * r ** 6 + r * p ** 6 + r * q ** 6 + 2 * r ** 7
        Zn_o = p ** 5 * r ** 2 + q ** 5 * r ** 2 + r ** 5 * p ** 2 + r ** 5 * q ** 2 + 2 * r ** 7
        out.append((beta, Zf_a * Zn_a ** 3 / Zc ** 4, Zf_o * Zn_o ** 3 / Zc ** 4))
    return out


def main():
    bad, bad6, worst = r1()
    print(f"R1 product identity: 3-ring exhaustive (6^6 pairs) failures {bad}; 3^3 torus 7-stencil six-axis (5,1,2), 300 random pairs, "
          f"failures {bad6}; sphere spins exp(beta s.s'), 300 random pairs, max |log difference| {worst:.2e}")
    out = r2()
    for p, (ra, ro, same) in out.items():
        print(f"R2 p={p}: antipodal flip/const = {ra} ({float(ra):.6e}), orthogonal flip/const = {ro} ({float(ro):.6e}); closed form = "
              f"direct product {same}")
    vals, mono_a, mono_o, below, peak_o, mono_tail = r3()
    shown = [v for v in vals if v[0] in (F(201, 100), F(205, 100), F(210, 100), F(215, 100), F(225, 100), F(3), F(20), F(200))]
    print("R3 ratios on (p,1,2): " + "; ".join(f"p={float(p):g}: {float(a):.4e}, {float(o):.4e}" for p, a, o in shown) +
          f"; on p = 2.01..200: antipodal decreasing {mono_a}, orthogonal decreasing {mono_o} (orthogonal ratio peaks at p = "
          f"{float(peak_o[0]):g}, value {float(peak_o[2]):.5f}), all below 1 {below}; both decreasing on p >= 3 {mono_tail}")
    for beta, ra, ro in r4():
        print(f"R4 exp six-axis weights (e^beta, e^-beta, 1), beta={beta}: antipodal {ra:.4e}, orthogonal {ro:.4e}")
    attempt = {3: (F(2167007881, 207594140625), F(28796658496, 207594140625)),
               5: (F(7077735687223, 341437969896529303), F(715012822753408, 341437969896529303))}
    match = all(out[p][0] == attempt[p][0] and out[p][1] == attempt[p][1] for p in attempt)
    all_below = all(out[p][0] < 1 and out[p][1] < 1 for p in out)
    if bad == 0 and bad6 == 0 and worst < 1e-9 and match and all_below and all(out[p][2] for p in out) and mono_tail and below:
        print("HIT: confirmed - the reversibility identity holds (exhaustive on the 3-ring, random pairs on the nondegenerate 3^3 torus for "
              "the six-axis (5,1,2) weights and for sphere spins), and the 2x2x2 flip ratios re-derive exactly (p=3: 2167007881/207594140625 "
              "and 28796658496/207594140625; p=5 as stated; p=10, 20 below 1) by a closed form checked against the direct product; both "
              "ratios stay below 1 on p = 2.01..200 and decrease on p >= 3")
        print(f"SUMMARY: confirmed - a finite exact partial: one-site flips are lighter than a constant in pi on the degenerate L=2 cube for "
              f"(p,1,2); correction: 'both ratios decrease in p' holds on the sampled p >= 3 but not on all of p > 2 (the orthogonal ratio "
              f"rises to a peak {float(peak_o[2]):.5f} at p = {float(peak_o[0]):g}); scope: (p,1,2) is not the six-axis restriction "
              f"(e^beta, e^-beta, 1) of the task's exp(beta s.S) law, a one-site cost on L=2 controls no contour sum, and the task's (a) Gibbs "
              f"identification, (b) sphere LRO and (c) kernel bounds are not addressed")
    else:
        print(f"SUMMARY: fails at step 2 - identity {bad}/{bad6}/{worst}, match {match}, below {all_below}, monotone tail {mono_tail}")


if __name__ == "__main__":
    main()
