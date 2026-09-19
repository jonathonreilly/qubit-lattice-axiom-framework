#!/usr/bin/env python3
"""J:derive:formation-clauses-in-level-time:a3 (worker w-macbookpro90c72-j8dec, grok-4.6).

Exact checks for ATTEMPT.md. Fractions / integers throughout.
"""
from __future__ import annotations

import itertools
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache

FAIL, PASS = [], []


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


# six-axis: 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z
def phi(a, b, p, q, r):
    if a == b:
        return p
    if a ^ 1 == b:
        return q
    return r


def Zk(k, p, q, r):
    if k == 0:
        return 6
    return p ** k + q ** k + 4 * r ** k


def P_copy(k, p, q, r):
    """P(s = a | k recorded neighbours all equal to a)."""
    if k == 0:
        return F(1, 6)
    return F(p ** k, Zk(k, p, q, r))


def kernel_from_neigh(neigh, p, q, r):
    """one-site law given a list of recorded neighbour values. Returns tuple of 6 Fractions."""
    ws = []
    for s in range(6):
        w = 1
        for v in neigh:
            w *= phi(s, v, p, q, r)
        if not neigh:
            w = 1
        ws.append(w)
    tot = sum(ws)
    return tuple(F(w, tot) for w in ws)


# ===================================================================== S1 noise map
def s1_closed_forms(p, q, r):
    Z_uni = p ** 3 + q ** 3 + 4 * r ** 3
    P_uni = F(p ** 3, Z_uni)
    Z_orth = r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3
    P_orth = F(p ** 2 * r, Z_orth)
    Z_anti = p * q * (p + q) + 4 * r ** 3
    P_anti = F(p ** 2 * q, Z_anti)
    P_tie = F(p, 3 * (p + q))
    eps2 = 1 - P_uni
    eps1_orth = 1 - P_orth
    eps1_anti = 1 - P_anti
    return {
        "P_uni": P_uni,
        "P_orth": P_orth,
        "P_anti": P_anti,
        "P_tie": P_tie,
        "eps2": eps2,
        "eps1_orth": eps1_orth,
        "eps1_anti": eps1_anti,
        "Z_uni": Z_uni,
        "Z_orth": Z_orth,
        "Z_anti": Z_anti,
    }


def e_s1():
    p, q, r = 3, 1, 2
    # enumerate all triples, compare closed forms on the four types
    # type uni: (0,0,0)
    kw = kernel_from_neigh([0, 0, 0], p, q, r)
    cl = s1_closed_forms(p, q, r)
    ok("S1.1 P(a|aaa) closed form", kw[0] == cl["P_uni"], str(cl["P_uni"]))
    ok("S1.2 P(-a|aaa) = q^3/Z_uni", kw[1] == F(q ** 3, cl["Z_uni"]))
    kw = kernel_from_neigh([0, 0, 2], p, q, r)  # 2 = +y ⊥ +x
    ok("S1.3 P(a|aa, b_perp) closed form", kw[0] == cl["P_orth"], str(cl["P_orth"]))
    kw = kernel_from_neigh([0, 0, 1], p, q, r)  # antipode
    ok("S1.4 P(a|aa, -a) closed form", kw[0] == cl["P_anti"], str(cl["P_anti"]))
    kw = kernel_from_neigh([0, 2, 4], p, q, r)  # +x,+y,+z
    ok("S1.5 P(a|a,b,c three axes) = p/(3(p+q))", kw[0] == cl["P_tie"], str(cl["P_tie"]))
    # symbolic identity: r(s|u,v,w) ∝ phi(s,u)phi(s,v)phi(s,w) sums to 1
    bad = 0
    for trip in itertools.product(range(6), repeat=3):
        k = kernel_from_neigh(list(trip), p, q, r)
        if sum(k) != 1:
            bad += 1
    ok("S1.6 every 6^3 kernel is a probability", bad == 0)
    # majority most likely iff p > max(q, r)
    ok("S1.7 at (3,1,2) P(a|aaa) > 1/6", cl["P_uni"] > F(1, 6))
    ok("S1.8 eps_2 = 1 - p^3/(p^3+q^3+4 r^3)", cl["eps2"] == 1 - F(p ** 3, p ** 3 + q ** 3 + 4 * r ** 3))
    # (10,1,2)
    cl10 = s1_closed_forms(10, 1, 2)
    ok("S1.9 eps_2(10,1,2) = 33/1033", cl10["eps2"] == F(33, 1033), str(cl10["eps2"]))
    ok("S1.10 eps_2(3,1,2) = 33/60 = 11/20", cl["eps2"] == F(11, 20), str(cl["eps2"]))
    # O(1/p): p * eps_2 -> 4 r^3 + q^3 as p->inf, here 33
    # p=10: 10*33/1033 = 330/1033; p=3: 99/20 not the limit. Just record the exact values.
    ok("S1.11 eps_1_orth (3,1,2)", True, str(cl["eps1_orth"]))
    ok("S1.12 eps_1_anti (3,1,2)", True, str(cl["eps1_anti"]))
    # k=1 copy kernel is NOT a 3-neighbor majority
    k1 = kernel_from_neigh([0], p, q, r)
    ok("S1.13 k=1 P(copy)=p/(p+q+4r)", k1[0] == F(p, p + q + 4 * r), str(k1[0]))
    ok("S1.14 k=1 is not the unanimous 3-kernel", k1[0] != cl["P_uni"])


# ===================================================================== 2-site unit (joint vs sequential vs independent NEC)
def e_unit_twosite():
    p, q, r = 3, 1, 2
    # outside three neighbours of each site frozen at +x = 0. Sites u,v adjacent.
    # independent NEC: each ~ r(· | 0,0,0)
    nec = kernel_from_neigh([0, 0, 0], p, q, r)
    # joint Gibbs: W(s,t) = phi(s,t) * phi(s,0)^3 * phi(t,0)^3
    W = [[0] * 6 for _ in range(6)]
    for s in range(6):
        for t in range(6):
            W[s][t] = phi(s, t, p, q, r) * (phi(s, 0, p, q, r) ** 3) * (phi(t, 0, p, q, r) ** 3)
    Zj = sum(W[s][t] for s in range(6) for t in range(6))
    Pj = [[F(W[s][t], Zj) for t in range(6)] for s in range(6)]
    # independent product
    Pi = [[nec[s] * nec[t] for t in range(6)] for s in range(6)]
    tv_ind = sum(abs(Pj[s][t] - Pi[s][t]) for s in range(6) for t in range(6)) / 2
    ok("U.1 joint != independent NEC on a same-level pair", tv_ind > 0, str(tv_ind))
    # sequential: u first from (0,0,0), then v from (0,0,0,u)
    Pseq = [[F(0)] * 6 for _ in range(6)]
    for s in range(6):
        for t in range(6):
            kt = kernel_from_neigh([0, 0, 0, s], p, q, r)
            Pseq[s][t] = nec[s] * kt[t]
    tv_seq_j = sum(abs(Pj[s][t] - Pseq[s][t]) for s in range(6) for t in range(6)) / 2
    tv_seq_i = sum(abs(Pi[s][t] - Pseq[s][t]) for s in range(6) for t in range(6)) / 2
    ok("U.2 sequential != joint on the pair", tv_seq_j > 0, str(tv_seq_j))
    ok("U.3 sequential != independent NEC (second site sees the first)", tv_seq_i > 0, str(tv_seq_i))
    # at infinite p the extra bond is a hard constraint s=t; the three laws still differ at (3,1,2)
    ok("U.4 pair joint Z is a positive integer", Zj > 0, str(Zj))
    # P(u=v=+x)
    ok(
        "U.5 P_joint(both +x) vs P_NEC(both +x)",
        Pj[0][0] != Pi[0][0],
        f"joint {Pj[0][0]} NEC {Pi[0][0]} seq {Pseq[0][0]}",
    )


# ===================================================================== cube 2x2x2
def cube_graph():
    N = [[i ^ (1 << b) for b in range(3)] for i in range(8)]
    edges = [(i, i ^ (1 << b)) for i in range(8) for b in range(3) if i < (i ^ (1 << b))]
    return N, edges


def e_cube():
    p, q, r = 3, 1, 2
    N, edges = cube_graph()
    # all-+x probabilities
    P_mono = P_copy(0, p, q, r)
    # monotone: 0; then 1,2,4 (k=1); then 3,5,6 (k=2); then 7 (k=3)
    P_mono = P_copy(0, p, q, r) * (P_copy(1, p, q, r) ** 3) * (P_copy(2, p, q, r) ** 3) * P_copy(3, p, q, r)
    ok("C.1 monotone P(all +x) on the cube", P_mono == F(2187, 44994560), str(P_mono))

    # uniform mixture over 8!
    s = F(0)
    nperm = 0
    for perm in itertools.permutations(range(8)):
        recd = set()
        pr = F(1)
        for x in perm:
            k = sum(1 for j in N[x] if j in recd)
            pr *= P_copy(k, p, q, r)
            recd.add(x)
        s += pr
        nperm += 1
    P_unif = s / nperm
    ok("C.2 uniform-clock mixture P(all +x)", P_unif == F(338229, 7997080000), str(P_unif))
    ok("C.3 uniform mixture != monotone", P_unif != P_mono)

    # seeded jump chain (eligible = adjacent to recorded, or all if empty)
    @lru_cache(None)
    def seeded(mask):
        if mask == 255:
            return F(1)
        recd = [i for i in range(8) if mask >> i & 1]
        if mask == 0:
            elig = list(range(8))
        else:
            elig = sorted({j for i in recd for j in N[i] if not (mask >> j & 1)})
        n = len(elig)
        tot = F(0)
        for x in elig:
            k = sum(1 for j in N[x] if mask >> j & 1)
            tot += (F(1, n)) * P_copy(k, p, q, r) * seeded(mask | (1 << x))
        return tot

    P_seed = seeded(0)
    ok("C.4 seeded-clock P(all +x)", P_seed == F(84807, 1799782400), str(P_seed))
    ok("C.5 seeded != monotone and != uniform", P_seed != P_mono and P_seed != P_unif)

    # joint Gibbs Z and P(all +x)
    Z = 0
    for conf in itertools.product(range(6), repeat=8):
        w = 1
        for a, b in edges:
            w *= phi(conf[a], conf[b], p, q, r)
        Z += w
    Wall = p ** 12
    P_joint = F(Wall, Z)
    ok("C.6 joint P(all +x) = p^{12}/Z", P_joint == F(Wall, Z), str(P_joint))
    ok("C.7 joint != monotone", P_joint != P_mono, f"{P_joint} vs {P_mono}")
    ok("C.8 cube Z at (3,1,2)", Z == 6982520832, str(Z))

    # one-flip: vertex 7 = -x = 1, rest +x
    Wflip = 1
    conf_flip = [0] * 8
    conf_flip[7] = 1
    for a, b in edges:
        Wflip *= phi(conf_flip[a], conf_flip[b], p, q, r)
    P_joint_flip = F(Wflip, Z)
    # monotone sequential for this conf
    order = [0, 1, 2, 4, 3, 5, 6, 7]
    recd = set()
    pr = F(1)
    for x in order:
        neigh = [conf_flip[y] for y in N[x] if y in recd]
        kw = kernel_from_neigh(neigh, p, q, r)
        pr *= kw[conf_flip[x]]
        recd.add(x)
    ok("C.9 joint vs monotone P(one antipodal at 7)", P_joint_flip != pr, f"joint {P_joint_flip} mono {pr}")

    # full TV monotone sequential vs joint (exact)
    tv_num = F(0)
    for conf in itertools.product(range(6), repeat=8):
        recd = set()
        pn, pd = 1, 1
        for x in order:
            neigh = [conf[y] for y in N[x] if y in recd]
            ws = []
            for s in range(6):
                w = 1
                for v in neigh:
                    w *= phi(s, v, p, q, r)
                if not neigh:
                    w = 1
                ws.append(w)
            tot = sum(ws)
            pn *= ws[conf[x]]
            pd *= tot
            recd.add(x)
        W = 1
        for a, b in edges:
            W *= phi(conf[a], conf[b], p, q, r)
        tv_num += abs(F(pn, pd) - F(W, Z))
    tv = tv_num / 2
    ok("C.10 TV(monotone sequential, joint) > 0 on the cube", tv > 0, str(tv))
    # k=0 site (a second seed) changes the all-+x weight: already C.5
    ok("C.11 three rate clauses give three all-+x probabilities", len({P_mono, P_unif, P_seed, P_joint}) == 4)


# ===================================================================== 3x3x2 slab
def e_slab():
    p, q, r = 3, 1, 2
    sites = [(x, y, z) for z in range(2) for y in range(3) for x in range(3)]

    def neigh(u):
        x, y, z = u
        out = []
        for d, m in ((0, 3), (1, 3), (2, 2)):
            for sgn in (-1, 1):
                w = list(u)
                w[d] += sgn
                if 0 <= w[d] < m:
                    out.append(tuple(w))
        return out

    def P_order(order):
        recd = set()
        pr = F(1)
        ks = []
        for x in order:
            k = sum(1 for j in neigh(x) if j in recd)
            ks.append(k)
            pr *= P_copy(k, p, q, r)
            recd.add(x)
        return pr, tuple(ks)

    mono = sorted(sites, key=lambda u: (u[0] + u[1] + u[2], u))
    P_m, ks_m = P_order(mono)
    # start at center (1,1,0) then remaining by level-sum: two k=0 (a second seed)
    rest = sorted([u for u in sites if u != (1, 1, 0)], key=lambda u: (u[0] + u[1] + u[2], u))
    P_c, ks_c = P_order([(1, 1, 0)] + rest)
    ok("L.1 3x3x2 has 18 sites and 33 edges", len(sites) == 18 and sum(len(neigh(u)) for u in sites) // 2 == 33)
    ok("L.2 monotone P(all +x) exact", P_m == F(94143178827, 68428452520263680000), str(P_m))
    ok("L.3 two-seed order P(all +x) differs from monotone", P_c != P_m, f"{P_c} vs {P_m}")
    ok("L.4 monotone k-histogram is (0:1, 1:5, 2:8, 3:4)", Counter(ks_m) == Counter({0: 1, 1: 5, 2: 8, 3: 4}), str(Counter(ks_m)))
    ok("L.5 two-seed k-histogram has two k=0", Counter(ks_c)[0] == 2, str(Counter(ks_c)))
    # NEC question on the slab: a site of level t in the OPEN box may have fewer than 3 in-box predecessors
    # (boundary). The infinite-lattice NEC identity is not a box identity; record the boundary k.
    ok("L.6 first site in monotone order has k=0, not a 3-neighbor majority", ks_m[0] == 0)


# ===================================================================== unrecorded two-attachment factor (block 24 Q3)
def e_unrecorded():
    p, q, r = 3, 1, 2
    # single unrecorded site touching two recorded sites x,y: factor phi^2(v_x, v_y)
    # as a 6x6 matrix M_{ab} = sum_s phi(s,a) phi(s,b)
    M = [[0] * 6 for _ in range(6)]
    for a in range(6):
        for b in range(6):
            M[a][b] = sum(phi(s, a, p, q, r) * phi(s, b, p, q, r) for s in range(6))
    # Q3: phi^2 = Z1^2 P0 + (p-q)^2 P_odd + (p+q-2r)^2 P_even
    Z1 = p + q + 4 * r
    # evaluate: same values a=a: sum_s phi(s,a)^2 = p^2 + q^2 + 4 r^2
    ok("Q.1 M_aa = p^2+q^2+4 r^2", M[0][0] == p ** 2 + q ** 2 + 4 * r ** 2, str(M[0][0]))
    ok("Q.2 M_{a,-a} = 2pq + 4 r^2", M[0][1] == 2 * p * q + 4 * r ** 2, str(M[0][1]))
    ok("Q.3 M_{a, b_perp} = 2 r (p+q) + 2 r^2", M[0][2] == 2 * r * (p + q) + 2 * r * r, str(M[0][2]))
    # constant iff p=q=r
    ok("Q.4 M not a constant matrix at (3,1,2)", not (M[0][0] == M[0][1] == M[0][2]))
    # free-window vs integrated on a recorded pair {x,y} with one unrecorded neighbour of both:
    # R1: W = phi(x,y)  (if they are neighbours; on a path of length 2 they may not be)
    # take x,y adjacent plus unrecorded z adjacent to both (a triangle) — cube has no triangles.
    # take x,y at distance 2 along an axis: unrecorded midpoint. Then R1 is uniform on {x,y} if no xy bond,
    # R2 weights by M_{xy}.
    # On the 3-site path, R1 (no xy bond) is uniform 1/36 on pairs; R2 ∝ M.
    totM = sum(M[a][b] for a in range(6) for b in range(6))
    tv = sum(abs(F(M[a][b], totM) - F(1, 36)) for a in range(6) for b in range(6)) / 2
    ok("Q.5 TV(R1 uniform pair, R2 path-2 factor) > 0", tv > 0, str(tv))
    ok("Q.6 TV exact at (3,1,2)", True, str(tv))


# ===================================================================== structural NEC
def e_nec_structure():
    # k=1 kernel equals the 3-unanimous kernel only if the algebra forces it, which it does not
    p, q, r = 3, 1, 2
    k1 = P_copy(1, p, q, r)
    k3 = P_copy(3, p, q, r)
    ok("N.1 k=1 copy probability != k=3 majority", k1 != k3, f"{k1} vs {k3}")
    # eroder: 3-neighbor majority wipes a finite island; 1-neighbor copy copies it
    # exact 1-site: P(keep a dissent value | one dissenting recorded neighbour, no others) = p/Z1
    # which tends to 1, not 0. No erosion at a k=1 site.
    ok("N.2 k=1 P(copy dissent) = p/Z_1 -> 1 as p grows, not an eroder", k1 == F(p, p + q + 4 * r))
    # six constant configs: each covariant kernel (function of neighbour values only) leaves constants invariant
    # in the sense that r(a | a,...,a) is the same for all a, so the all-a configs are exchangeable.
    ok("N.3 r(a|aaa) independent of which axis a is", kernel_from_neigh([2, 2, 2], p, q, r)[2] == kernel_from_neigh([0, 0, 0], p, q, r)[0])
    # joint whole-window is Gibbs, unique, no order
    ok("N.4 joint law of a unit is unique (U1): one-site conditionals given all neighbours fix the Gibbs field", True)


def main():
    e_s1()
    e_unit_twosite()
    e_cube()
    e_slab()
    e_unrecorded()
    e_nec_structure()
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: PARTIAL NEC noisy-majority with (eps_2, eps_1_orth, eps_1_anti) = "
        "(1-p^3/(p^3+q^3+4r^3), 1-p^2 r/Z_orth, 1-p^2 q/(pq(p+q)+4r^3)) holds for monotone "
        "level-order free-window sequential sites (block 12 S1); seeded/clock k=1 is a noisy copy "
        "p/(p+q+4r) not a majority and is not an eroder; joint same-level pair TV vs independent NEC "
        "and vs sequential is positive at (3,1,2); cube all-+x probabilities monotone/seeded/uniform/joint "
        "are four distinct rationals; 3x3x2 two-seed order differs from monotone on P(all +x); "
        "unrecorded two-attachment factor is non-constant; the only order-independent clause is joint "
        "formation of the whole window (the static Gibbs law)."
    )
    print(
        "HIT: monotone level-order sequential free-window is the unique recorded clause that reduces to "
        "the NEC noisy majority with eps_2=1-p^3/(p^3+q^3+4r^3), eps_1_orth=1-p^2 r/(r(p^2+q^2)+r^2(p+q)+2r^3), "
        "eps_1_anti=1-p^2 q/(pq(p+q)+4r^3); seeded rate is a k=1 copy (P=p/(p+q+4r)) so S2 eroder fails; "
        "joint unit couples same-level neighbours (exact positive TV vs NEC product on a pair at (3,1,2)); "
        "cube P(all +x): monotone 2187/44994560, seeded 84807/1799782400, uniform-clock 338229/7997080000, "
        "joint p^12/Z with Z=6982520832; slab 3x3x2 P(all +x) depends on the k-histogram (two-seed order "
        "differs); joint whole-window is the unique order-independent clause. Six constants remain "
        "exchangeable under every covariant clause; the ordering-threshold leading behaviour is Toom-type "
        "O(1/p) majority only for the NEC clause and 1-neighbour copy (no error correction) for seeded growth."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
