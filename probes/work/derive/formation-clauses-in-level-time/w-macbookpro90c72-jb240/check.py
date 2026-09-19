#!/usr/bin/env python3
"""J:derive:formation-clauses-in-level-time:a2 — exact finite checks on the cube and 3x3x2 slab.

Clauses: (rate) uniform clocks vs seeded growth vs monotone sequential;
(unit) sequential vs joint; (unrecorded) not needed for the induced Z^3 formation
process on a fully-recorded window. Noise map S1; neighborhood type k=|A_x|.
"""
from __future__ import annotations

import itertools
import math
import sys
from collections import defaultdict
from fractions import Fraction as Fr

M = range(6)


def phi_tab(p, q, r):
    return [[p if a == b else (q if a == (b ^ 1) else r) for b in M] for a in M]


def r_cond(P, neigh):
    """r(s | recorded neighbor values). Empty: uniform 1/6."""
    if not neigh:
        return [Fr(1, 6)] * 6
    w = []
    for s in M:
        pr = 1
        for a in neigh:
            pr *= P[s][a]
        w.append(pr)
    t = sum(w)
    return [Fr(x, t) if not isinstance(x, Fr) else x / t for x in w]


def r_cond_int(P, neigh):
    if not neigh:
        return [Fr(1, 6)] * 6
    w = [1] * 6
    for s in M:
        pr = 1
        for a in neigh:
            pr *= P[s][a]
        w[s] = pr
    t = sum(w)
    return [Fr(w[s], t) for s in M]


def noise_map(p, q, r):
    P = phi_tab(p, q, r)
    a, b, c = 0, 2, 4  # +x, +y, +z pairwise orthogonal

    def pa(neigh):
        rc = r_cond_int(P, neigh)
        return rc[0]

    out = {
        "aaa": pa([a, a, a]),
        "aab": pa([a, a, b]),
        "aa-a": pa([a, a, a ^ 1]),
        "abc_a": pa([a, b, c]),
        "abc_b": r_cond_int(P, [a, b, c])[b],
        "abc_-a": r_cond_int(P, [a, b, c])[a ^ 1],
    }
    stated = {
        "aaa": Fr(p ** 3, p ** 3 + q ** 3 + 4 * r ** 3),
        "aab": Fr(p * p * r, r * (p * p + q * q) + r * r * (p + q) + 2 * r ** 3),
        "aa-a": Fr(p * p * q, p * q * (p + q) + 4 * r ** 3),
        "abc_a": Fr(p, 3 * (p + q)),
        "abc_b": Fr(p, 3 * (p + q)),
        "abc_-a": Fr(q, 3 * (p + q)),
    }
    return out, stated


# ---- cube graph ----
def cube_graph():
    sites = list(itertools.product((0, 1), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    nb = [[] for _ in sites]
    for s in sites:
        i = idx[s]
        for d in range(3):
            t = list(s)
            t[d] = 1 - t[d]
            nb[i].append(idx[tuple(t)])
    return sites, nb


def monotone_order(sites):
    return sorted(range(len(sites)), key=lambda i: (sum(sites[i]), sites[i]))


def k_sequence(order, nb):
    seen = set()
    ks = []
    kinds = []  # tuple of recorded neighbor coords relative
    for x in order:
        A = [y for y in nb[x] if y in seen]
        ks.append(len(A))
        seen.add(x)
    return ks


def sequential_law(nb, order, P):
    n = len(nb)
    law = {}
    for v in itertools.product(M, repeat=n):
        seen = set()
        pr = Fr(1)
        for x in order:
            Avals = [v[y] for y in nb[x] if y in seen]
            rc = r_cond_int(P, Avals)
            pr *= rc[v[x]]
            seen.add(x)
        law[v] = pr
    return law


def joint_law(nb, P):
    n = len(nb)
    edges = []
    seen_e = set()
    for i, nbrs in enumerate(nb):
        for j in nbrs:
            e = (i, j) if i < j else (j, i)
            if e not in seen_e:
                seen_e.add(e)
                edges.append(e)
    Z = 0
    wts = {}
    for v in itertools.product(M, repeat=n):
        w = 1
        for a, b in edges:
            w *= P[v[a]][v[b]]
        wts[v] = w
        Z += w
    return {v: Fr(w, Z) for v, w in wts.items()}, Z, len(edges)


def tv(p, q):
    return sum(abs(p[v] - q[v]) for v in p) / 2


def growth_orders(nb, start=0):
    n = len(nb)
    out = []

    def rec(formed, frontier, order):
        if len(order) == n:
            out.append(list(order))
            return
        for x in list(frontier):
            order.append(x)
            formed.add(x)
            frontier.remove(x)
            added = []
            for y in nb[x]:
                if y not in formed and y not in frontier:
                    frontier.add(y)
                    added.append(y)
            rec(formed, frontier, order)
            for y in added:
                frontier.remove(y)
            frontier.add(x)
            formed.remove(x)
            order.pop()

    rec(set(), {start}, [])
    return out


def k_hist_for_orders(nb, orders):
    hist = defaultdict(int)
    n = 0
    for od in orders:
        for k in k_sequence(od, nb):
            hist[k] += 1
            n += 1
    return {k: Fr(hist[k], n) for k in sorted(hist)}, hist, n


def slab_graph():
    sites = list(itertools.product(range(3), range(3), range(2)))
    idx = {s: i for i, s in enumerate(sites)}
    nb = [[] for _ in sites]
    for s in sites:
        i = idx[s]
        for d in range(3):
            for e in (-1, 1):
                t = list(s)
                t[d] += e
                tt = tuple(t)
                if tt in idx:
                    nb[i].append(idx[tt])
    return sites, nb


def majority_pref(p, q, r):
    """2:1 triple (a,a,b) prefers a iff p > max(q,r)."""
    P = phi_tab(p, q, r)
    rc = r_cond_int(P, [0, 0, 2])
    return rc[0], rc[2], rc[0] > max(rc[1], rc[2], rc[3], rc[4], rc[5])


def main():
    hits = []
    pqr_list = [(3, 1, 2), (5, 2, 4), (10, 1, 2)]

    print("S1 noise map vs closed forms:")
    s1_ok = True
    for pqr in pqr_list:
        got, st = noise_map(*pqr)
        ok = all(got[k] == st[k] for k in st)
        s1_ok &= ok
        eps0 = 1 - got["aaa"]
        eps21 = 1 - got["aab"]
        eps_anti = 1 - got["aa-a"]
        print(
            f"  {pqr}: match {ok}; 1-P(aaa)={float(eps0):.6f}={eps0}; "
            f"1-P(aab)={float(eps21):.6f}; 1-P(aa-a)={float(eps_anti):.6f}; "
            f"P(abc a)={got['abc_a']} P(-a)={got['abc_-a']}"
        )
    if not s1_ok:
        hits.append("S1")
    pa, pb, pref = majority_pref(3, 1, 2)
    pa2, _, pref2 = majority_pref(1, 3, 2)
    print(f"  majority preference p>max(q,r): (3,1,2) P(a)={pa} P(b)={pb} pref={pref}; (1,3,2) pref={pref2}")
    if not (pref and not pref2):
        hits.append("majority preference")

    sites, nb = cube_graph()
    print(f"Cube: {len(sites)} sites, degrees {[len(nb[i]) for i in range(8)]}")
    mon = monotone_order(sites)
    ks_mon = k_sequence(mon, nb)
    print(f"  monotone (level then lex) k-seq {ks_mon}  (#k=3: {ks_mon.count(3)})")
    # opposite-corner order: 000, 111, then rest by level
    opp = [0]  # (0,0,0)
    idx_111 = sites.index((1, 1, 1))
    opp.append(idx_111)
    rest = [i for i in range(8) if i not in opp]
    rest.sort(key=lambda i: (sum(sites[i]), sites[i]))
    opp += rest
    ks_opp = k_sequence(opp, nb)
    print(f"  opposite-corners-first k-seq {ks_opp}  (#k=3: {ks_opp.count(3)})")

    grows = growth_orders(nb, 0)
    print(f"  growth orders from origin: {len(grows)}")
    kh_g, _, _ = k_hist_for_orders(nb, grows)
    print(f"  growth P(k) " + ", ".join(f"k={k}:{float(v):.3f}" for k, v in kh_g.items()))
    kh_m, _, _ = k_hist_for_orders(nb, [mon])
    print(f"  monotone P(k) " + ", ".join(f"k={k}:{float(v):.3f}" for k, v in kh_m.items()))

    # all 8! is 40320; sample uniform permutations for P(k)
    import random
    rng = random.Random(8148)
    unif = [rng.sample(range(8), 8) for _ in range(2000)]
    kh_u, _, _ = k_hist_for_orders(nb, unif)
    print(f"  uniform-order sample P(k) " + ", ".join(f"k={k}:{float(v):.3f}" for k, v in kh_u.items()))

    P = phi_tab(3, 1, 2)
    print("Cube laws at (3,1,2):")
    joint, Z, nE = joint_law(nb, P)
    print(f"  joint Z={Z} |E|={nE}")
    seq_m = sequential_law(nb, mon, P)
    tvm = tv(seq_m, joint)
    print(f"  TV(monotone sequential, joint)={tvm} = {float(tvm):.6f}")
    seq_o = sequential_law(nb, opp, P)
    tvo = tv(seq_o, joint)
    tvo_m = tv(seq_o, seq_m)
    print(f"  TV(opposite-first, joint)={float(tvo):.6f}; TV(opposite, monotone)={float(tvo_m):.6f}")
    # two corner monotone orders
    mon2 = sorted(range(8), key=lambda i: (sum((1 - c) if d == 0 else c for d, c in enumerate(sites[i])), sites[i]))
    # actually other corner: start from (1,0,0): level = (1-x)+y+z
    def corner_order(origin):
        ox, oy, oz = origin
        return sorted(range(8), key=lambda i: (abs(sites[i][0] - ox) + abs(sites[i][1] - oy) + abs(sites[i][2] - oz), sites[i]))

    o000, o100 = corner_order((0, 0, 0)), corner_order((1, 0, 0))
    s000, s100 = sequential_law(nb, o000, P), sequential_law(nb, o100, P)
    tv_corners = tv(s000, s100)
    print(f"  TV(corner 000 vs 100 sequential)={tv_corners} = {float(tv_corners):.6f} (eight corner laws differ)")
    if tv_corners == 0:
        hits.append("corner laws coincide")
    if tvm == 0:
        hits.append("monotone=joint on cube (cycle)")

    # mixture of all growth orders from origin: too many laws to average fully if many orders
    # compare one BFS growth order to monotone
    bfs = grows[0]
    seq_g = sequential_law(nb, bfs, P)
    print(f"  TV(one growth order, monotone)={float(tv(seq_g, seq_m)):.6f}; vs joint {float(tv(seq_g, joint)):.6f}")
    print(f"  that growth k-seq {k_sequence(bfs, nb)}")

    # slab
    ss, snb = slab_graph()
    print(f"Slab 3x3x2: {len(ss)} sites")
    sl_mon = sorted(range(len(ss)), key=lambda i: (sum(ss[i]), ss[i]))
    ks_sl = k_sequence(sl_mon, snb)
    from collections import Counter
    print(f"  monotone k histogram {dict(Counter(ks_sl))}; #k=3 {ks_sl.count(3)}")
    sl_grows_n = 0
    # count growth orders is huge; sample k along BFS-like and random growth
    def random_growth(nb, start, rng, nrep=500):
        hist = defaultdict(int)
        n = len(nb)
        for _ in range(nrep):
            formed, frontier, order = set(), {start}, []
            while len(order) < n:
                x = rng.choice(tuple(frontier))
                order.append(x)
                formed.add(x)
                frontier.remove(x)
                for y in nb[x]:
                    if y not in formed:
                        frontier.add(y)
            for k in k_sequence(order, nb):
                hist[k] += 1
        tot = sum(hist.values())
        return {k: Fr(hist[k], tot) for k in sorted(hist)}

    kh_sg = random_growth(snb, 0, random.Random(8158), 400)
    print("  slab growth-sample P(k) " + ", ".join(f"k={k}:{float(v):.3f}" for k, v in kh_sg.items()))
    kh_sm, _, _ = k_hist_for_orders(snb, [sl_mon])
    print("  slab monotone P(k) " + ", ".join(f"k={k}:{float(v):.3f}" for k, v in kh_sm.items()))

    # NEC reduction: a site has the S1 kernel iff its recorded neighbors are exactly three pairwise-orthogonal directions
    # (the three coordinate predecessors). Count how often that happens on cube monotone vs growth.
    def nec_count(order, sites, nb):
        n_nec = 0
        seen = set()
        for x in order:
            A = [y for y in nb[x] if y in seen]
            if len(A) == 3:
                diffs = []
                sx = sites[x]
                for y in A:
                    d = tuple(sites[y][j] - sx[j] for j in range(3))
                    diffs.append(d)
                axes = [i for i, t in enumerate(zip(*[(abs(u[0]), abs(u[1]), abs(u[2])) for u in diffs])) if any(t)]
                # three neighbors along three different axes, all "past"
                axset = set()
                for d in diffs:
                    for j in range(3):
                        if d[j] != 0:
                            axset.add(j)
                if len(axset) == 3:
                    n_nec += 1
            seen.add(x)
        return n_nec

    print(f"  cube monotone #NEC-triple sites {nec_count(mon, sites, nb)}/8")
    print(f"  cube growth[0] #NEC-triple sites {nec_count(bfs, sites, nb)}/8")
    n_nec_g = sum(nec_count(od, sites, nb) for od in grows)
    print(f"  cube growth mean #NEC-triple {n_nec_g}/{len(grows)}/8 = {n_nec_g / (len(grows) * 8):.4f}")
    print(f"  slab monotone #NEC-triple {nec_count(sl_mon, ss, snb)}/{len(ss)}")

    # order-independence: joint is unique; sequential depends on order (TV>0 above)
    # seeded growth (rate = 1[adjacent]) never has k=0 after the seed; uniform clocks do
    if ks_opp[1] != 0:
        hits.append("opposite second site should have k=0")

    if hits:
        print("SUMMARY: ROUTE FAILS AT " + "; ".join(hits))
        return 1
    print(
        "HIT: S1 noise map exact (eps_unanimous=1-p^3/(p^3+q^3+4r^3), eps_2:1=1-P(a|aab)); "
        f"on the 2x2x2 cube at (3,1,2) TV(monotone sequential, joint)={float(tvm):.5f}, "
        f"TV(two corner orders)={float(tv_corners):.5f}, TV(opposite-first, joint)={float(tvo):.5f}; "
        f"1080 seeded-growth orders have P(k=1)={float(kh_g.get(1,0)):.3f} vs monotone 0.375 "
        f"and mean NEC-triples {n_nec_g / (len(grows) * 8):.3f}/site vs 0.125; slab monotone "
        f"k-hist 4/18 sites with k=3, growth-sample P(k=1)={float(kh_sg.get(1,0)):.3f}; "
        "the NEC product kernel is the monotone-class law; the whole-window unit is the "
        "order-independent clause"
    )
    print(
        "SUMMARY: PARTIAL - exact S1; cube sequential monotone ≠ joint ≠ other corners; "
        "seeded rate shifts to k=1 (not majority); slab monotone has 4 of 18 sites at k=3; "
        "order-independence selects the joint-window unit clause"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
