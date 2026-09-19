#!/usr/bin/env python3
"""J:attack-g:PR8142 — brute-force V1–V5, E2, 16 numerators, X2 collapse.

X1/X2 finite identities from the three-body locus note:
  Z3 depends only on the triple pattern: V1..V5 as written;
  E2 = V1 V4² − V2 V3² = −(p−q)² G;
  on p=q=t, W2³−W1 W3² = 8(t−1)³(t³−3t²−6t−1) and E1 equals that (r=1);
  on p=r=1, Z3 takes exactly the three polynomials q³+5, q²+q+4, 3q+3;
  over 6^6 CR argument tuples there are exactly 16 distinct nonzero
  numerators of CR_c/CR_c' (r=1).

HIT if a pattern value, factorization, collapse, or the 16-count fails.
Exact sympy / integer. Isolating intervals for t*/ρ/σ are not this unit
(already an executed-numbers script).
"""
from __future__ import annotations

from itertools import product

import sympy as sp


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
p, q, r, t = sp.symbols("p q r t", positive=True)


def phi_sym(s, a):
    if s == a:
        return p
    if s == (-a[0], -a[1], -a[2]):
        return q
    return r


def Z3(a, b, c):
    return sp.expand(sum(phi_sym(s, a) * phi_sym(s, b) * phi_sym(s, c) for s in AXES))


def pattern(trip):
    a, b, c = trip
    def rel(u, v):
        if u == v:
            return "eq"
        if u == (-v[0], -v[1], -v[2]):
            return "anti"
        return "orth"
    rels = (rel(a, b), rel(a, c), rel(b, c))
    n_eq = rels.count("eq")
    n_anti = rels.count("anti")
    n_orth = rels.count("orth")
    # classify
    if a == b == c:
        return 1
    if n_eq == 1 and n_anti == 2:
        # two equal, one opposite: e.g. a=a, third -a. Then rels: eq, anti, anti
        return 2
    if n_eq == 1 and n_orth == 2:
        return 3
    if n_anti == 1 and n_orth == 2:
        return 4
    if n_orth == 3:
        return 5
    # two equal and the third opposite is n_eq=1 n_anti=2; two equal one orth n_eq=1 n_orth=2
    # all three equal n_eq=3
    # three pairwise anti is impossible (anti is involution of order 2, not a triangle)
    return 0


def main():
    hits = []
    V1 = p ** 3 + q ** 3 + 4 * r ** 3
    V2 = p * q * (p + q) + 4 * r ** 3
    V3 = r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3
    V4 = 2 * p * q * r + r ** 2 * (p + q) + 2 * r ** 3
    V5 = 3 * r ** 2 * (p + q)
    Vs = {1: V1, 2: V2, 3: V3, 4: V4, 5: V5}

    counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for trip in product(AXES, repeat=3):
        k = pattern(trip)
        counts[k] += 1
        z = Z3(*trip)
        if k == 0:
            hits.append(f"HIT: unclassified triple {trip}")
            print(hits[-1])
            continue
        if sp.expand(z - Vs[k]) != 0:
            hits.append(f"HIT: Z3 != V{k} at {trip}: {sp.expand(z - Vs[k])}")
            print(hits[-1])
            break
    print("pattern counts over 216:", counts)
    if counts[0]:
        hits.append("HIT: some triples unclassified")

    E1 = sp.expand(V1 * V5 ** 2 - V3 ** 3)
    E2 = sp.expand(V1 * V4 ** 2 - V2 * V3 ** 2)
    # E2 = -(p-q)^2 G
    Gpoly, rem = sp.div(sp.Poly(E2, p, q, r), sp.Poly(-(p - q) ** 2, p, q, r), domain="QQ")
    if rem != 0:
        hits.append(f"HIT: E2 is not divisible by -(p-q)^2; rem={rem}")
        print(hits[-1])
    else:
        print(f"E2 = -(p-q)^2 G with deg G={Gpoly.total_degree()} (want 5 in p,q at r=1)")
        G_r1 = sp.Poly(Gpoly.as_expr().subs(r, 1), p, q)
        if G_r1.total_degree() != 5:
            hits.append(f"HIT: G at r=1 has degree {G_r1.total_degree()} != 5")
            print(hits[-1])
        if sp.expand(Gpoly.as_expr().subs({p: q}) ) == "skip":
            pass
        if sp.expand(E2.subs(p, q)) != 0:
            hits.append("HIT: E2 does not vanish on p=q")
            print(hits[-1])

    # X2a collapse
    W1 = 2 * t ** 3 + 4
    W2 = 2 * (t ** 2 + t + 1)
    W3 = 6 * t
    collapse = sp.expand(W2 ** 3 - W1 * W3 ** 2)
    want = 8 * (t - 1) ** 3 * (t ** 3 - 3 * t ** 2 - 6 * t - 1)
    if sp.expand(collapse - want) != 0:
        hits.append(f"HIT: W2^3-W1 W3^2 = {collapse} != {want}")
        print(hits[-1])
    else:
        print("X2a: W2^3-W1 W3^2 = 8(t-1)^3 (t^3-3t^2-6t-1)")

    E1_line = sp.expand(E1.subs({p: t, q: t, r: 1}))
    # note: E1 restricted to the line equals -8(t-1)^3(...)
    if sp.expand(E1_line + 8 * (t - 1) ** 3 * (t ** 3 - 3 * t ** 2 - 6 * t - 1)) != 0:
        hits.append(f"HIT: E1 on p=q=t,r=1 is {E1_line}, not -8(t-1)^3 cubic")
        print(hits[-1])
    else:
        print("X2a: E1(t,t,1) = -8(t-1)^3 (t^3-3t^2-6t-1)")

    # X2b: p=r=1, Z3 takes three values
    vals = set()
    for trip in product(AXES, repeat=3):
        z = sp.expand(Z3(*trip).subs({p: 1, r: 1}))
        vals.add(z)
    claimed = {q ** 3 + 5, q ** 2 + q + 4, 3 * q + 3}
    claimed_e = {sp.expand(x) for x in claimed}
    if vals != claimed_e:
        hits.append(f"HIT: p=r=1 Z3 values {vals} != {claimed_e}")
        print(hits[-1])
    else:
        print("X2b: p=r=1, Z3 takes exactly q^3+5, q^2+q+4, 3q+3")

    # X1 ratios as polynomials
    def K2(a, b):
        return sp.expand(sum(phi_sym(s, a) * phi_sym(s, b) for s in AXES))

    x, y = AXES[0], AXES[2]
    mx = AXES[1]
    ratio_anti = sp.together(
        (K2(mx, mx) * K2(x, x)) / (K2(mx, x) * K2(x, mx))
    )
    # claimed [(p^2+q^2+4r^2)/(2(pq+2r^2))]^2
    claimed_anti = ((p ** 2 + q ** 2 + 4 * r ** 2) / (2 * (p * q + 2 * r ** 2))) ** 2
    if sp.simplify(ratio_anti - claimed_anti) != 0:
        hits.append(f"HIT: X1 antipodal K2 ratio {ratio_anti} != claimed")
        print(hits[-1])
    else:
        print("X1: antipodal K2 ratio matches")
    num_m_den = sp.expand((p ** 2 + q ** 2 + 4 * r ** 2) - 2 * (p * q + 2 * r ** 2))
    # = (p-q)^2, so ratio=1 iff p=q
    if sp.expand(num_m_den - (p - q) ** 2) != 0:
        hits.append(f"HIT: X1 antipodal 1-iff is not (p-q)^2: {num_m_den}")
        print(hits[-1])
    ratio_orth = sp.together((K2(y, y) * K2(x, x)) / (K2(y, x) * K2(x, y)))
    claimed_orth = ((p ** 2 + q ** 2 + 4 * r ** 2) / (2 * r * (p + q + r))) ** 2
    if sp.simplify(ratio_orth - claimed_orth) != 0:
        hits.append("HIT: X1 orthogonal K2 ratio mismatch")
        print(hits[-1])
    else:
        print("X1: orthogonal K2 ratio matches")
    gap = sp.expand((p ** 2 + q ** 2 + 4 * r ** 2) - 2 * r * (p + q + r))
    if sp.expand(gap - ((p - r) ** 2 + (q - r) ** 2)) != 0:
        hits.append(f"HIT: X1 ortho 1-iff is not (p-r)^2+(q-r)^2: {gap}")
        print(hits[-1])

    # 16 distinct nonzero numerators of CR_c/CR_c' at r=1
    # N = Z(a,b,c)Z(a',b',c)Z(a,b',c')Z(a',b,c') - Z(a,b',c)Z(a',b,c)Z(a,b,c')Z(a',b',c')
    cache = {}
    def z1(a, b, c):
        key = (a, b, c)
        if key not in cache:
            cache[key] = sp.Poly(Z3(a, b, c).subs(r, 1), p, q, domain="QQ")
        return cache[key]

    distinct = {}
    n_zero = 0
    n_checked = 0
    for a, ap, b, bp, c, cp in product(AXES, repeat=6):
        n_checked += 1
        left = z1(a, b, c) * z1(ap, bp, c) * z1(a, bp, cp) * z1(ap, b, cp)
        right = z1(a, bp, c) * z1(ap, b, c) * z1(a, b, cp) * z1(ap, bp, cp)
        N = left - right
        if N.is_zero:
            n_zero += 1
            continue
        key = tuple(N.as_expr().as_poly(p, q).as_expr().expand().as_ordered_terms()) if False else N
        # hash by coefficient tuple
        coeff_key = tuple(N.coeffs())
        distinct[coeff_key] = distinct.get(coeff_key, 0) + 1
    print(f"CR tuples {n_checked}: zero numerators {n_zero}, distinct nonzero {len(distinct)}")
    if len(distinct) != 16:
        hits.append(f"HIT: distinct nonzero CR numerators {len(distinct)} != 16")
        print(hits[-1])

    # X5 sample: (3,1,2) and (5,2,4) — at least E1,E2 nonzero
    for pv, qv, rv in ((3, 1, 2), (5, 2, 4)):
        e1 = int(E1.subs({p: pv, q: qv, r: rv}))
        e2 = int(E2.subs({p: pv, q: qv, r: rv}))
        print(f"X5 ({pv},{qv},{rv}): E1={e1} E2={e2}")
        if e1 == 0 or e2 == 0:
            hits.append(f"HIT: declared triple ({pv},{qv},{rv}) on the locus E1={e1} E2={e2}")
            print(hits[-1])

    if hits:
        print("SUMMARY: V-pattern / E2 / collapse / 16-numerator identities fail")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — all 216 triples match V1..V5, "
        "E2=-(p-q)^2 G (deg 5 at r=1), X1 K2 ratios factor as stated, X2a "
        "W2^3-W1 W3^2=8(t-1)^3 cubic and E1 on the diagonal, X2b three Z3 values "
        f"on p=r=1, exactly 16 distinct nonzero CR numerators over 6^6 tuples "
        f"({n_zero} identically zero), and (3,1,2),(5,2,4) have E1 E2 nonzero"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
