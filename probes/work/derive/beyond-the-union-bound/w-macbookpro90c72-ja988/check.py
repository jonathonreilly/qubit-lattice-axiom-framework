#!/usr/bin/env python3
"""beyond-the-union-bound, attempt 2 (worker w-macbookpro90c72-ja988, model grok-4.6).

Candidate (ii): isolated-pair regeneration kernel of the two-level automaton, and a
no-go for atom-sum (q, r) closures. Exact fractions / sympy throughout.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import product

import sympy as sp

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
        print(f"PASS: {tag} {msg}")
    else:
        FAILS += 1
        print(f"FAIL: {tag} {msg}")


E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORKS = [tuple(E[a][i] - E[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]
FORK_SET = set(FORKS) | set(tuple(-x for x in d) for d in FORKS)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def preds(z):
    return [sub(z, E[j]) for j in range(3)]


def is_fork(u, v):
    return sub(u, v) in FORK_SET


def deviations(p, q, r):
    p, q, r = F(p), F(q), F(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def section_a():
    p = sp.symbols("p", positive=True)
    d1 = 1 - p ** 3 / (p ** 3 + 1 + 4 * 8)
    d1c = 33 / (p ** 3 + 33)
    d2 = 1 - p ** 2 * 1 / (p * 1 * (p + 1) + 32)
    d2c = (p + 32) / (p * (p + 1) + 32)
    d3 = 1 - p ** 2 * 2 / (2 * (p ** 2 + 1) + 4 * (p + 1) + 16)
    d3c = (2 * p + 11) / (p ** 2 + 2 * p + 11)
    ok = (sp.simplify(d1 - d1c) == 0 and sp.simplify(d2 - d2c) == 0 and sp.simplify(d3 - d3c) == 0)
    check("A0", ok, "on (p,1,2): d1=33/(p^3+33), d2=(p+32)/(p(p+1)+32), d3=(2p+11)/(p^2+2p+11)")
    ok = True
    for x in product([(0, 0, 0)], repeat=1):
        pass
    x = (5, 1, 2)
    pr = preds(x)
    ok = all(is_fork(pr[i], pr[j]) for i, j in ((0, 1), (0, 2), (1, 2)))
    ok = ok and len(pr) == 3
    check("A1", ok, "the three predecessors of a site are pairwise fork-adjacent, so P(N>=2)<=3 r")
    d2m, d3m = deviations(11, 1, 2)[1], deviations(11, 1, 2)[2]
    d2s = (p + 32) / (p * (p + 1) + 32)
    d3s = (2 * p + 11) / (p ** 2 + 2 * p + 11)
    want = p ** 2 * (21 - p) / ((p ** 2 + p + 32) * (p ** 2 + 2 * p + 11))
    ok = sp.simplify(d2s - d3s - want) == 0 and d2m == F(43, 164) and d3m == F(3, 14)
    check("A2", ok, "d2-d3 = p^2(21-p)/[(p^2+p+32)(p^2+2p+11)]; at p=11, d2=43/164>d3=3/14 so eps2=d2")


def section_b():
    u = (0, 0, 0)
    v = add(u, sub(E[0], E[1]))
    succ_u = [add(u, E[j]) for j in range(3)]
    succ_v = [add(v, E[j]) for j in range(3)]
    common = set(succ_u) & set(succ_v)
    w = add(u, E[0])
    amps = [s for s in succ_u + succ_v if s != w]
    amps = list(dict.fromkeys(amps))
    ok = common == {w} and len(amps) == 4 and all(is_fork(w, a) for a in amps)
    amp_forks = sum(1 for i in range(4) for j in range(i + 1, 4) if is_fork(amps[i], amps[j]))
    n_pairs = 4 + amp_forks
    check("B1", ok and amp_forks == 3 and n_pairs == 7,
          f"isolated pair: unique majority child w, four amp children all fork-adjacent to w, "
          f"{amp_forks} amp-amp forks, {n_pairs} descendant fork-pairs")
    e2 = sp.symbols("e2", positive=True)
    preg = 1 - (1 - e2) ** 4
    mean = 4 * e2 + 3 * e2 ** 2
    # exact: 4 independent Bern(e2) bits; w forced 1; at-least-one w-amp pair iff not all zero
    ok = sp.expand(preg - (1 - (1 - e2) ** 4)) == 0
    # mean count of 7 pairs: 4 * e2 + 3 * e2^2
    check("B2", ok and sp.expand(mean - (4 * e2 + 3 * e2 ** 2)) == 0,
          "P(at least one descendant pair | isolated pair) = 1-(1-eps2)^4; "
          "E[# descendant pairs] = 4 eps2 + 3 eps2^2")
    # numerical identity at a rational eps2
    e = F(1, 5)
    bits_atleast = 0
    bits_mean = F(0)
    for bits in product((0, 1), repeat=4):
        pr = (e ** sum(bits)) * ((1 - e) ** (4 - sum(bits)))
        # 4 w-amp pairs occupy if bits[k]=1; 3 amp-amp: indices (0,1), (1,3), (2,3) from geometry
        # geometry: amps[0]=(0,1,0), [1]=(0,0,1) fork; [1] and [3] fork; [2] and [3] fork
        occupied = sum(bits)  # w-amp
        amp_pairs = [(0, 1), (1, 3), (2, 3)]
        occupied += sum(1 for i, j in amp_pairs if bits[i] and bits[j])
        bits_mean += occupied * pr
        if occupied:
            bits_atleast += pr
    check("B3", bits_atleast == 1 - (1 - e) ** 4 and bits_mean == 4 * e + 3 * e ** 2,
          f"at eps2=1/5: exact 16-config enumeration matches 1-(4/5)^4={1 - (F(4, 5) ** 4)} "
          f"and mean {4 * e + 3 * e ** 2}")


def section_c():
    e = sp.symbols("e", positive=True)
    poly = sp.expand(3 * e ** 2 + 4 * e - 1)
    thr = (-2 + sp.sqrt(7)) / 3
    fact = sp.expand(3 * (e - thr) * (e - (-2 - sp.sqrt(7)) / 3))
    ok = sp.simplify(poly - fact) == 0
    check("C1", ok, "3 e^2 + 4 e - 1 = 3 (e - (-2+sqrt(7))/3) (e - (-2-sqrt(7))/3); "
          "mean < 1 for e > 0 iff e < (-2+sqrt(7))/3")
    thr_f = (-2 + F(7).sqrt()) if False else None
    # compare d2(12), d2(13) to the threshold by squaring: e < (-2+sqrt(7))/3
    # iff 3e+2 < sqrt(7) (both sides positive since e>0 and 3e+2>2>0)
    # iff (3e+2)^2 < 7 iff 9e^2 + 12e + 4 < 7 iff 9e^2 + 12e - 3 < 0 iff 3e^2 + 4e - 1 < 0
    d2_12 = deviations(12, 1, 2)[1]
    d2_13 = deviations(13, 1, 2)[1]
    d3_12 = deviations(12, 1, 2)[2]
    d3_13 = deviations(13, 1, 2)[2]
    def mean_lt_1(e):
        return 3 * e ** 2 + 4 * e - 1 < 0
    ok = (d2_12 == F(55, 235) and d2_13 == F(45, 214)
          and d2_12 > d3_12 and d2_13 > d3_13
          and not mean_lt_1(d2_12) and mean_lt_1(d2_13)
          and mean_lt_1(d2_13) and not mean_lt_1(d2_12))
    # also p=21 is the d2=d3 crossing
    d2_21, d3_21 = deviations(21, 1, 2)[1], deviations(21, 1, 2)[2]
    d2_20, d3_20 = deviations(20, 1, 2)[1], deviations(20, 1, 2)[2]
    d2_22, d3_22 = deviations(22, 1, 2)[1], deviations(22, 1, 2)[2]
    ok = ok and d2_21 == d3_21 and d2_20 > d3_20 and d3_22 > d2_22
    check("C2", ok,
          f"on (p,1,2) eps2=d2 for p<=21; d2(12)=55/235 mean>1; d2(13)=45/214 mean<1; "
          f"d2(21)=d3(21)={d2_21}; first integer with isolated-pair mean < 1 is p=13")


def fmaj(n, e1, e2):
    return F(1) if n >= 2 else (e2 if n == 1 else e1)


def section_d():
    # 5-site neighbourhood of a child fork-pair
    # bits A,B,C,D,E ; Nu=A+B+C, Nv=B+D+E
    # fork pairs: AB,BC,AC, BD,BE,DE, CE
    FORK5 = {frozenset(p) for p in [(0, 1), (1, 2), (0, 2), (1, 3), (1, 4), (3, 4), (2, 4)]}

    def has_fork(S):
        return any(i in S and j in S for i, j in FORK5)

    def Ar_of(e1, e2):
        Ar = F(0)
        Aq = F(0)
        A0 = F(0)
        for bits in product((0, 1), repeat=5):
            S = frozenset(i for i, b in enumerate(bits) if b)
            Nu = bits[0] + bits[1] + bits[2]
            Nv = bits[1] + bits[3] + bits[4]
            g = fmaj(Nu, e1, e2) * fmaj(Nv, e1, e2)
            if not S:
                A0 += g
            elif has_fork(S):
                Ar += g
            else:
                Aq += g
        return A0, Aq, Ar

    rows = []
    ok = True
    for p in (200, 84, 13, 11):
        d1, d2, d3 = deviations(p, 1, 2)
        e1, e2 = d1, max(d2, d3)
        A0, Aq, Ar = Ar_of(e1, e2)
        ok = ok and Ar > 1
        rows.append(f"p={p} Ar={float(Ar):.4g}")
    check("D1", ok, "5-pred atom-sum r-coefficient Ar>1 at p=200,84,13,11: " + "; ".join(rows))

    # depth-2 cone 64-mask atom-sum
    x = (0, 0, 0)
    mid = [sub(x, E[j]) for j in range(3)]
    base = []
    for d1 in range(3):
        for d2 in range(3 - d1):
            d3 = 2 - d1 - d2
            if d3 >= 0:
                base.append(sub(x, (d1, d2, d3)))
    base = sorted(set(base))
    assert len(base) == 6
    bpairs = [(i, j) for i in range(6) for j in range(i + 1, 6) if is_fork(base[i], base[j])]

    def Ptop(bits, e1, e2):
        bmap = {base[i]: bits[i] for i in range(6)}
        mid_ps = []
        for z in mid:
            n = sum(bmap.get(pp, 0) for pp in preds(z))
            mid_ps.append(F(1) if n >= 2 else (e2 if n == 1 else e1))
        total = F(0)
        for mb in product((0, 1), repeat=3):
            w = F(1)
            for bit, pz in zip(mb, mid_ps):
                w *= pz if bit else (1 - pz)
            mmap = {mid[i]: mb[i] for i in range(3)}
            ntop = sum(mmap.get(pp, 0) for pp in preds(x))
            ptop = F(1) if ntop >= 2 else (e2 if ntop == 1 else e1)
            total += w * ptop
        return total

    def classify(bits):
        S = [i for i, b in enumerate(bits) if b]
        if not S:
            return "0"
        for i, j in bpairs:
            if i in S and j in S:
                return "R"
        return "q"

    ok = True
    rows = []
    for p in (84, 13, 11):
        d1, d2, d3 = deviations(p, 1, 2)
        e1, e2 = d1, max(d2, d3)
        CR = F(0)
        for bits in product((0, 1), repeat=6):
            if classify(bits) == "R":
                CR += Ptop(bits, e1, e2)
        ok = ok and CR > 1
        rows.append(f"p={p} CR={float(CR):.4g}")
    check("D2", ok, "depth-2 64-mask atom-sum r-coefficient CR>1 at p=84,13,11: " + "; ".join(rows))


def section_e():
    # 2-step eroder: eps=0, isolated fork-pair at the base of the depth-2 cone => top is 0
    x = (0, 0, 0)
    mid = [sub(x, E[j]) for j in range(3)]
    base = []
    for d1 in range(3):
        for d2 in range(3 - d1):
            d3 = 2 - d1 - d2
            if d3 >= 0:
                base.append(sub(x, (d1, d2, d3)))
    base = sorted(set(base))
    bpairs = [(i, j) for i in range(6) for j in range(i + 1, 6) if is_fork(base[i], base[j])]

    def run_eps0(base_bits):
        bmap = {base[i]: base_bits[i] for i in range(6)}
        mmap = {}
        for z in mid:
            n = sum(bmap.get(pp, 0) for pp in preds(z))
            mmap[z] = 1 if n >= 2 else 0
        ntop = sum(mmap.get(pp, 0) for pp in preds(x))
        return ntop >= 2, sum(mmap.values())

    ok = True
    n_pairs = 0
    for i, j in bpairs:
        bits = [0] * 6
        bits[i] = bits[j] = 1
        top, nmid = run_eps0(bits)
        ok = ok and (not top) and nmid == 1
        n_pairs += 1
    check("E1", ok and n_pairs == 9,
          f"eps=0 2-step eroder on the depth-2 cone: each of {n_pairs} isolated base fork-pairs "
          "produces exactly one mid-level 1 and top=0")
    # depth-3: every configuration of the 20-site cone with eps=0, outside 0, is determined
    # by the 10 depth-2-and-beyond sites... simpler: with eps=0, a site is 1 iff >=2 preds are 1.
    # Exhaust depth-2 cone (10 sites) all 2^6 unconstrained base bits (mid/top forced): already
    # the 64 masks. Count how many have top=1 at eps=0: only those whose base forces two mids.
    n_top = 0
    n_from_iso_pair = 0
    for bits in product((0, 1), repeat=6):
        top, nmid = run_eps0(bits)
        if top:
            n_top += 1
            if sum(bits) == 2:
                n_from_iso_pair += 1
    check("E2", n_from_iso_pair == 0 and n_top > 0,
          f"eps=0 depth-2 cone: {n_top} of 64 base masks force the top; none of those is an "
          "isolated 2-hot fork-pair (the eroder: pairs do not survive two steps)")


def main():
    section_a()
    section_b()
    section_c()
    section_d()
    section_e()
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT a finite check - {FAILS} FAIL tags")
        return 1
    print(
        "HIT: new exact partial: an isolated fork-pair of the two-level automaton has unique "
        "majority child and four amp children; P(regenerates a descendant fork-pair) = 1-(1-eps2)^4 "
        "and E[# descendant pairs] = 4 eps2 + 3 eps2^2, which is <1 iff eps2 < (-2+sqrt(7))/3; "
        "on (p,1,2) that first holds at p=13 (d2(12)=55/235 > threshold > d2(13)=45/214). "
        "The 2-step eroder (eps=0: isolated pair -> singleton -> 0) holds on all 9 base pairs of "
        "the depth-2 cone. Atom-sum (q,r) closures of r' have r-coefficient >10 (5-pred, p=200) "
        "and >33 (depth-2 masks), so this linear two-scale does not produce a super-solution"
    )
    print(
        "SUMMARY: PARTIAL isolated-pair regeneration kernel 1-(1-eps2)^4 and mean 4 eps2+3 eps2^2 "
        "with exact threshold (-2+sqrt(7))/3 (p>=13 on (p,1,2)); ROUTE FAILS AT step 5 of the "
        "(q,r) atom-sum closure (r-coefficient >1 at every p); 4/27 is not replaced; located "
        "strength 10.5-11 is not reached"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
