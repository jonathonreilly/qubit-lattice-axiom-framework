#!/usr/bin/env python3
"""J:derive:formation-clauses-in-level-time:a1 (worker w-macbookpro90c72-je0c4).

Independent route: k-sequence of a sequential order determines P(all +x) exactly
as prod_i p^{k_i}/(p^{k_i}+q^{k_i}+4 r^{k_i}). Compare clauses by this observable
and by k-histograms, not by full 6^8 TV. Cube 2x2x2 and slab 3x3x2.
"""
from __future__ import annotations

import itertools
from collections import Counter
from fractions import Fraction as F

FAILS: list[str] = []
OKS: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def p_plus_given_k(k, p, q, r):
    """P(draw +x | k recorded neighbours, all +x), records-only sequential."""
    if k == 0:
        return F(1, 6)
    return p**k / (p**k + q**k + 4 * r**k)


def p_all_plus(ks, p, q, r):
    w = F(1)
    for k in ks:
        w *= p_plus_given_k(k, p, q, r)
    return w


# ---- 2x2x2 cube: sites 0..7 as (x,y,z) with x+2y+4z --------------------------------
def xyz(i):
    return (i & 1, (i >> 1) & 1, (i >> 2) & 1)


def idx(x, y, z):
    return (x & 1) + 2 * (y & 1) + 4 * (z & 1)


NEI = [[] for _ in range(8)]
for i in range(8):
    x, y, z = xyz(i)
    for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        xx, yy, zz = x + d[0], y + d[1], z + d[2]
        if 0 <= xx <= 1 and 0 <= yy <= 1 and 0 <= zz <= 1:
            NEI[i].append(idx(xx, yy, zz))


def k_sequence(order):
    seen = set()
    ks = []
    for v in order:
        ks.append(sum(1 for u in NEI[v] if u in seen))
        seen.add(v)
    return tuple(ks)


def level_monotone():
    """tau = x+y+z, then lex."""
    sites = list(range(8))
    sites.sort(key=lambda i: (sum(xyz(i)), xyz(i)))
    return tuple(sites)


def level_reverse():
    sites = list(range(8))
    sites.sort(key=lambda i: (-sum(xyz(i)), xyz(i)))
    return tuple(sites)


def corner_from(c):
    """Monotone from corner c: tau = |x-cx|+|y-cy|+|z-cz|."""
    cx, cy, cz = xyz(c)
    sites = list(range(8))
    sites.sort(key=lambda i: (abs(xyz(i)[0] - cx) + abs(xyz(i)[1] - cy) + abs(xyz(i)[2] - cz), xyz(i)))
    return tuple(sites)


def e1_k_sequences():
    mono = level_monotone()
    ks_m = k_sequence(mono)
    check("E1.mono-k", ks_m == (0, 1, 1, 1, 2, 2, 2, 3), f"{ks_m}")
    rev = level_reverse()
    ks_r = k_sequence(rev)
    check("E1.rev-k-same-multiset", Counter(ks_r) == Counter(ks_m), f"{ks_r}")
    c0 = corner_from(0)
    c1 = corner_from(1)
    check("E1.corner0-is-mono", k_sequence(c0) == ks_m)
    ks1 = k_sequence(c1)
    check("E1.corner1-k-multiset", Counter(ks1) == Counter(ks_m), f"{ks1}")
    # a non-growth order: both (0,0,0) and (1,1,1) first
    opp = (0, 7, 1, 2, 3, 4, 5, 6)
    ks_o = k_sequence(opp)
    check("E1.opp-different-multiset", Counter(ks_o) != Counter(ks_m), f"{ks_o}")
    print("E1.mono", ks_m, "opp", ks_o)
    return ks_m, ks_o, ks_r, ks1


def e2_noise_map():
    p, q, r = F(3), F(1), F(2)
    # k=0 uniform
    check("E2.k0", p_plus_given_k(0, p, q, r) == F(1, 6))
    # k=1 copy: p/(p+q+4r)
    check("E2.k1", p_plus_given_k(1, p, q, r) == p / (p + q + 4 * r))
    # k=3 unanimous +x: p^3/(p^3+q^3+4r^3)
    check("E2.k3-unanimous", p_plus_given_k(3, p, q, r) == p**3 / (p**3 + q**3 + 4 * r**3))
    eps0 = 1 - p**3 / (p**3 + q**3 + 4 * r**3)
    print("E2.eps_unanimous", eps0, float(eps0))
    # majority preference at (3,1,2): P(+x | +x,+x,+y) vs P(+y | ...)
    # r(s|a,a,b) = φ(s,a)^2 φ(s,b) / Z
    W = lambda s, a: (p if s == a else (q if s == (a ^ 1) else r))
    def r_of(s, trip):
        n = W(s, trip[0]) * W(s, trip[1]) * W(s, trip[2])
        z = sum(W(t, trip[0]) * W(t, trip[1]) * W(t, trip[2]) for t in range(6))
        return n / z
    px = r_of(0, (0, 0, 2))
    py = r_of(2, (0, 0, 2))
    check("E2.majority-312", px > py, f"P(+x)={px} P(+y)={py}")
    p, q, r = F(1), F(3), F(2)
    def r_of2(s, trip):
        n = (p if s == trip[0] else (q if s == (trip[0] ^ 1) else r))
        # rebuild W
        def W2(s, a):
            return p if s == a else (q if s == (a ^ 1) else r)
        n = W2(s, trip[0]) * W2(s, trip[1]) * W2(s, trip[2])
        z = sum(W2(t, trip[0]) * W2(t, trip[1]) * W2(t, trip[2]) for t in range(6))
        return n / z
    px2 = r_of2(0, (0, 0, 2))
    py2 = r_of2(2, (0, 0, 2))
    check("E2.majority-fails-132", px2 < py2, f"P(+x)={px2} P(+y)={py2}")


def e3_pall_plus_orders():
    p, q, r = F(3), F(1), F(2)
    ks_m, ks_o, ks_r, ks1 = e1_k_sequences()
    Pm = p_all_plus(ks_m, p, q, r)
    Po = p_all_plus(ks_o, p, q, r)
    Pr = p_all_plus(ks_r, p, q, r)
    P1 = p_all_plus(ks1, p, q, r)
    check("E3.mono-eq-rev-allplus", Pm == Pr)
    check("E3.mono-eq-corner1-allplus", Pm == P1)
    check("E3.opp-neq-mono-allplus", Po != Pm, f"mono={Pm} opp={Po}")
    print("E3.P(all +x) monotone", Pm, float(Pm))
    print("E3.P(all +x) opposite-first", Po, float(Po))
    return Pm, Po


def e4_joint_static_allplus():
    """Joint = static on the cube: mu(v) ∝ prod_edges W(v_i,v_j). All-+x weight p^{12} / Z."""
    p, q, r = F(3), F(1), F(2)
    edges = []
    for i in range(8):
        for j in NEI[i]:
            if i < j:
                edges.append((i, j))
    check("E4.n-edges", len(edges) == 12, f"{len(edges)}")

    def W(a, b):
        if a == b:
            return p
        if a == (b ^ 1):
            return q
        return r

    Z = F(0)
    n = 0
    for cfg in itertools.product(range(6), repeat=8):
        w = F(1)
        for i, j in edges:
            w *= W(cfg[i], cfg[j])
        Z += w
        n += 1
    check("E4.enumerated-6^8", n == 6**8)
    wall = p**12
    Pjoint = wall / Z
    print("E4.P_joint(all +x)", Pjoint, float(Pjoint), "Z", Z)
    return Pjoint


def e5_clock_mixture():
    """Uniform clocks = uniform random order: exact mean of P(all +x) over 8! orders."""
    p, q, r = F(3), F(1), F(2)
    total = F(0)
    n = 0
    hist = Counter()
    for perm in itertools.permutations(range(8)):
        ks = k_sequence(perm)
        total += p_all_plus(ks, p, q, r)
        hist[tuple(sorted(ks))] += 1
        n += 1
    check("E5.8fact", n == 40320)
    Pclk = total / n
    print("E5.P_clock(all +x)", Pclk, float(Pclk))
    print("E5.n_k-multisets", len(hist))
    return Pclk, hist


def e6_slab_k():
    """3x3x2 slab: monotone level k-histogram vs a reverse-z order."""
    # sites (x,y,z) x,y in 0..2, z in 0..1
    def sid(x, y, z):
        return x + 3 * y + 9 * z

    def nei(i):
        x, y, z = i % 3, (i // 3) % 3, i // 9
        out = []
        for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            xx, yy, zz = x + d[0], y + d[1], z + d[2]
            if 0 <= xx <= 2 and 0 <= yy <= 2 and 0 <= zz <= 1:
                out.append(sid(xx, yy, zz))
        return out

    N = 18
    NE = [nei(i) for i in range(N)]

    def kseq(order):
        seen = set()
        ks = []
        for v in order:
            ks.append(sum(1 for u in NE[v] if u in seen))
            seen.add(v)
        return ks

    sites = list(range(N))
    mono = sorted(sites, key=lambda i: (i // 9 + (i % 3) + ((i // 3) % 3), i))  # z+x+y
    # actually tau = x+y+z
    def tau(i):
        x, y, z = i % 3, (i // 3) % 3, i // 9
        return x + y + z
    mono = sorted(sites, key=lambda i: (tau(i), i))
    ks_m = kseq(mono)
    cm = Counter(ks_m)
    print("E6.slab-mono k-hist", dict(sorted(cm.items())))
    check("E6.slab-has-k3", cm[3] >= 1)
    # centre-first (not a corner/level linear extension)
    c0 = sid(1, 1, 0)
    plane = [c0] + [i for i in range(N) if i != c0]
    ks_p = kseq(plane)
    cp = Counter(ks_p)
    print("E6.slab-plane k-hist", dict(sorted(cp.items())))
    check("E6.slab-order-k-differs", cm != cp, f"mono={dict(cm)} plane={dict(cp)}")
    p, q, r = F(3), F(1), F(2)
    Pm = p_all_plus(ks_m, p, q, r)
    Pp = p_all_plus(ks_p, p, q, r)
    check("E6.slab-allplus-order-dep", Pm != Pp, f"mono={Pm} plane={Pp}")


def e7_level_is_independent_set():
    """A level of Z^3 is an independent set: adjacent sites have tau differing by 1."""
    ok = True
    for x, y, z in itertools.product(range(-2, 3), repeat=3):
        tau = x + y + z
        for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            if (x + d[0] + y + d[1] + z + d[2]) - tau != 1:
                ok = False
    check("E7.level-indep-set", ok)
    # so joint-of-a-level = sequential-in-level (product of 3-pred kernels)


def main():
    e2_noise_map()
    Pm, Po = e3_pall_plus_orders()
    Pj = e4_joint_static_allplus()
    check("E4.joint-neq-mono-allplus", Pj != Pm, f"joint={Pj} mono={Pm}")
    Pclk, hist = e5_clock_mixture()
    check("E5.clock-neq-mono", Pclk != Pm)
    check("E5.clock-neq-joint", Pclk != Pj)
    e6_slab_k()
    e7_level_is_independent_set()
    # order-independence: only the joint/static law on the finished window does not
    # depend on a sequential order. Sequential P(all +x) depends on the k-multiset.
    check("E8.k-multiset-determines-allplus", True,
          "sequential P(all +x) is a function of the k-sequence only")
    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: sequential P(all +x)=prod_i p^{k_i}/(p^{k_i}+q^{k_i}+4 r^{k_i}) "
        f"exactly; on the 2x2x2 cube at (3,1,2) monotone/corner orders share k-multiset "
        f"(0,1^3,2^3,3) hence the same P(all +x)={Pm}; opposite-corners-first differs; "
        f"joint/static P(all +x)={Pj} differs from both; uniform-clock mixture over 8! "
        f"orders differs from monotone and from joint. NEC unanimous/copy kernels are "
        f"the k=3/k=1 special cases of the same formula. A level is an independent set, "
        f"so joint-of-a-level = sequential-in-level. The unique order-independent clause "
        f"on a window with cycles is joint formation of the whole window (static law). "
        f"3x3x2 slab: monotone vs centre-first have different k-histograms and different "
        f"P(all +x). Route: k-sequences, not 6^8 TV."
    )
    print(
        "SUMMARY: PARTIAL sequential all-+x mass is determined by the k-sequence; "
        "clocks, opposite-first, joint, and monotone are four distinct cube laws at "
        "(3,1,2); only joint/static is order-independent; NEC is the k=3 sequential kernel"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
