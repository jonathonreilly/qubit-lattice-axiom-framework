#!/usr/bin/env python3
"""Referee of J:derive:formation-clauses-in-level-time:a2 (author w-macbookpro90c72-jb240, grok-4.6); referee w-jonathonsmac4f50-jafa6
(claude-opus-5). Independent code (exact Fractions and integers; numpy for the 6^8 enumeration); nothing from the author's check.py.
Disclosure: this referee's model family refereed attempt a1 of this problem (grok), which makes the same uniqueness claim in (c).

Six-axis product rule, W = p (same), q (antipodal), r (orthogonal). A sequential order sigma gives
P_sigma(s) = w(s)/D_sigma(s), w the static weight prod_edges W and D_sigma(s) = prod_i Z_i(earlier neighbours of i) (6 if none),
so exact TVs reduce to sums over the distinct triples (w, D, D').

N1  (a) block 12's noise map: eps_0 = 1 - p^3/(p^3+q^3+4r^3), eps_{2:1} = 1 - p^2 r/(r(p^2+q^2) + r^2(p+q) + 2r^3),
    eps_anti = 1 - p^2 q/(pq(p+q) + 4r^3), tie p/(3(p+q)), by direct evaluation of the kernel at (3,1,2), (5,2,4), (10,1,2);
    the 2:1 majority holds at (3,1,2) and fails at (1,3,2)
N2  cube monotone k-sequence (0,1,1,1,2,2,2,3); slab 3x3x2 level-order histogram {0:1, 1:5, 2:8, 3:4}
N3  (a)/(b) exact TVs at (3,1,2) over all 6^8 patterns: TV(monotone, joint) = 1182193085/23402354976, TV(corner 000, corner 100) =
    201510245581/4092954053760, TV(opposite-first, joint) = 0.08219, TV(opposite-first, monotone) = 0.07250; each law sums to 1
N4  step 3: under uniform random orders every site has P(k) = 1/4 for k = 0..3 exactly (8! orders); 1080 connected build orders from
    (0,0,0); weighting them uniformly gives P(k=1) = 79/180, P(k=3) = 17/90 (the attempt's 0.439, 0.189), but clocks that fire only
    next to records (equal rates) pick the next site uniformly on the boundary, which gives P(k=1) = 7/16, P(k=3) = 3/16 - the
    qualitative shift to k = 1 holds, the stated numbers are not that clause's
N5  (c) not established: the equal-rate clock law involves no chosen order and differs from the joint law (all-+x mass
    338229/7997080000 against 59049/775835648), and unequal rates move it; the attempt's argument (U2) covers the unit clause only
I1  INFO: slab Eden growth from the corner (0,0,0) (dynamic programme over recorded sets, floats): P(k=1) per site, against the
    attempt's sampled 0.419
"""
from __future__ import annotations

import itertools
import random
import sys
from collections import Counter
from fractions import Fraction as F

import numpy as np

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


M = range(6)


def Wm(p, q, r):
    return [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]


def kern(W, trip, v):
    ws = [W[s][trip[0]] * W[s][trip[1]] * W[s][trip[2]] for s in M]
    return F(ws[v], sum(ws))


def adj(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def kseq(order):
    seen, out = [], []
    for v in order:
        out.append(sum(1 for u in seen if adj(u, v)))
        seen.append(v)
    return out


def main():
    # N1
    ok = True
    for (p, q, r) in ((3, 1, 2), (5, 2, 4), (10, 1, 2)):
        W = Wm(p, q, r)
        ok &= 1 - kern(W, (0, 0, 0), 0) == 1 - F(p ** 3, p ** 3 + q ** 3 + 4 * r ** 3)
        ok &= 1 - kern(W, (0, 0, 2), 0) == 1 - F(p * p * r, r * (p * p + q * q) + r * r * (p + q) + 2 * r ** 3)
        ok &= 1 - kern(W, (0, 0, 1), 0) == 1 - F(p * p * q, p * q * (p + q) + 4 * r ** 3)
        ok &= kern(W, (0, 2, 4), 0) == F(p, 3 * (p + q))
    maj = kern(Wm(3, 1, 2), (0, 0, 2), 0) > kern(Wm(3, 1, 2), (0, 0, 2), 2) and kern(Wm(1, 3, 2), (0, 0, 2), 0) < kern(Wm(1, 3, 2), (0, 0, 2), 2)
    check("N1", ok and maj, "the four closed forms equal the kernel at (3,1,2), (5,2,4), (10,1,2); 2:1 majority at (3,1,2), not at (1,3,2)")

    # N2
    cube = sorted(itertools.product((0, 1), repeat=3), key=lambda v: v[0] + 2 * v[1] + 4 * v[2])
    corner = lambda c: sorted(cube, key=lambda v: (sum(abs(x - y) for x, y in zip(v, c)), v[0] + 2 * v[1] + 4 * v[2]))
    mono = corner((0, 0, 0))
    slab = [(x, y, z) for z in range(2) for y in range(3) for x in range(3)]
    smono = sorted(slab, key=lambda v: (sum(v), v[0] + 3 * v[1] + 9 * v[2]))
    hs = Counter(kseq(smono))
    check("N2", kseq(mono) == [0, 1, 1, 1, 2, 2, 2, 3] and dict(hs) == {0: 1, 1: 5, 2: 8, 3: 4},
          f"cube monotone {kseq(mono)}; slab level order {dict(sorted(hs.items()))}")

    # N3
    Wn = np.array(Wm(3, 1, 2), dtype=np.int64)
    idx = {v: i for i, v in enumerate(cube)}
    st = np.array(list(itertools.product(M, repeat=8)), dtype=np.int64)
    w = np.ones(len(st), dtype=np.int64)
    for a, b in itertools.combinations(cube, 2):
        if adj(a, b):
            w *= Wn[st[:, idx[a]], st[:, idx[b]]]
    Zs = int(w.sum())

    def D(order):
        d = np.ones(len(st), dtype=np.int64)
        seen = []
        for v in order:
            R = [idx[u] for u in seen if adj(u, v)]
            if R:
                z = np.zeros(len(st), dtype=np.int64)
                for s in M:
                    t = np.ones(len(st), dtype=np.int64)
                    for j in R:
                        t *= Wn[s, st[:, j]]
                    z += t
                d *= z
            else:
                d *= 6
            seen.append(v)
        return d

    def exact_sum(cols, fn):
        u, cnt = np.unique(np.stack(cols, axis=1), axis=0, return_counts=True)
        return sum((fn(*[int(x) for x in row]) * int(c) for row, c in zip(u.tolist(), cnt.tolist())), F(0))
    full = np.full(len(st), Zs, dtype=np.int64)
    Dm, Dc, Do = D(mono), D(corner((1, 0, 0))), D([cube[0], cube[7]] + cube[1:7])
    sums = [exact_sum([w, d], lambda a, b: F(a, b)) for d in (Dm, Dc, Do)]
    tv = lambda d1, d2: exact_sum([w, d1, d2], lambda a, b, c: F(a * abs(c - b), b * c)) / 2
    t_mj, t_mc, t_oj, t_om = tv(Dm, full), tv(Dm, Dc), tv(Do, full), tv(Do, Dm)
    check("N3", sums == [1, 1, 1] and t_mj == F(1182193085, 23402354976) and t_mc == F(201510245581, 4092954053760)
          and abs(float(t_oj) - 0.08219) < 5e-5 and abs(float(t_om) - 0.07250) < 5e-5,
          f"Z = {Zs}; TV(monotone, joint) = {t_mj}; TV(corner 000, corner 100) = {t_mc}; TV(opposite-first, joint) = "
          f"{float(t_oj):.5f}; TV(opposite-first, monotone) = {float(t_om):.5f}")

    # N4
    perms = list(itertools.permutations(cube))
    pk = Counter()
    for o in perms:
        for kk in kseq(o):
            pk[kk] += 1
    unif = {kk: F(c, 8 * len(perms)) for kk, c in pk.items()}
    builds = []

    def rec(seq, rem):
        if not rem:
            builds.append(tuple(seq))
            return
        for v in sorted(rem):
            if any(adj(v, u) for u in seq):
                rem.remove(v)
                seq.append(v)
                rec(seq, rem)
                seq.pop()
                rem.add(v)
    rec([cube[0]], set(cube[1:]))
    cu, ce, tot = Counter(), Counter(), F(0)
    for o in builds:
        ks = kseq(o)
        pr, seen = F(1), [o[0]]
        for v in o[1:]:
            bnd = [x for x in cube if x not in seen and any(adj(x, u) for u in seen)]
            pr *= F(1, len(bnd))
            seen.append(v)
        tot += pr
        for kk in ks:
            cu[kk] += 1
            ce[kk] += pr
    u1, u3 = F(cu[1], 8 * len(builds)), F(cu[3], 8 * len(builds))
    e1, e3 = ce[1] / 8, ce[3] / 8
    check("N4", unif == {0: F(1, 4), 1: F(1, 4), 2: F(1, 4), 3: F(1, 4)} and len(builds) == 1080 and tot == 1
          and (u1, u3) == (F(79, 180), F(17, 90)) and (e1, e3) == (F(7, 16), F(3, 16)),
          f"uniform orders: P(k) = {dict(sorted(unif.items()))}; {len(builds)} build orders; uniform over them: P(k=1) = {u1}, "
          f"P(k=3) = {u3}; boundary-uniform clocks (Eden weights, total {tot}): P(k=1) = {e1}, P(k=3) = {e3}; monotone 3/8, 1/8")

    # N5
    p, q, r = 3, 1, 2
    fac = lambda k: F(1, 6) if k == 0 else F(p ** k, p ** k + q ** k + 4 * r ** k)

    def pall(o):
        out = F(1)
        for kk in kseq(o):
            out *= fac(kk)
        return out
    pa = {o: pall(o) for o in perms}
    clock = sum(pa.values(), F(0)) / len(perms)
    random.seed(5)
    rates = {v: random.randint(1, 9) for v in cube}
    moved = F(0)
    for o in perms:
        pr, rem = F(1), sum(rates.values())
        for v in o:
            pr *= F(rates[v], rem)
            rem -= rates[v]
        moved += pr * pa[o]
    joint_all = F(3 ** 12, Zs)
    check("N5", clock == F(338229, 7997080000) and joint_all == F(59049, 775835648) and moved != clock,
          f"equal-rate clock law P(all +x) = {clock} != joint {joint_all}; rates {sorted(rates.values())} give {float(moved):.6e} "
          f"against {float(clock):.6e}")

    # I1: slab Eden from (0,0,0), exact DP over recorded sets in floats
    n = len(slab)
    sidx = {v: i for i, v in enumerate(slab)}
    nbr = [[sidx[u] for u in slab if adj(u, v)] for v in slab]
    start = 1 << sidx[(0, 0, 0)]
    prob = {start: 1.0}
    k1 = 0.0
    for size in range(1, n):
        nxt = {}
        for S, pS in prob.items():
            bnd = [v for v in range(n) if not S >> v & 1 and any(S >> u & 1 for u in nbr[v])]
            for v in bnd:
                kk = sum(1 for u in nbr[v] if S >> u & 1)
                if kk == 1:
                    k1 += pS / len(bnd)
                T = S | (1 << v)
                nxt[T] = nxt.get(T, 0.0) + pS / len(bnd)
        prob = nxt
    print(f"INFO I1: slab Eden growth from (0,0,0): P(k=1) per site = {k1 / n:.4f} (the attempt's 400-sample value 0.419; monotone "
          f"{5 / 18:.4f})")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at (c) (step 4's conclusion) - the finite results hold: the noise map, the k-sequences, the exact cube TVs "
          "1182193085/23402354976 (monotone vs joint) and 201510245581/4092954053760 (two corners), 0.08219 and 0.07250 for "
          "opposite-first, the 1080 build orders; but 'the unique recorded clause that makes the finished-window law independent of "
          "order is the whole-window unit' is argued only for the unit clause (U2), while the equal-rate clock law involves no chosen "
          "order and is not the joint law (and unequal rates move it). Correction to step 3: clocks firing only next to records give "
          "P(k=1) = 7/16, P(k=3) = 3/16 (boundary-uniform weights), not the uniform-over-build-orders 79/180, 17/90")
    return 0


if __name__ == "__main__":
    sys.exit(main())
