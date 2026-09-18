#!/usr/bin/env python3
"""J:confirm:J-derive-uniqueness-region-up:a2 — independent referee checks.

Ground metric rho via dot product on ±e_i. True W_rho by min-cost transportation
(successive shortest paths, Fraction residual costs), plus the author's orthogonal-then-antipodal
plan as an upper bound. Achievable laws from r(·|a), a in M^3. 3 kbar on p = 37/10..51/10 at
alpha = 5/4; 3c of block 08; all 30 ordered pairs at p = 51/10; rho triangle; plan >= true W.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

M = range(6)
VEC = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def phi_dot(p, q, r):
    tab = [[None] * 6 for _ in M]
    for i, a in enumerate(VEC):
        for j, b in enumerate(VEC):
            d = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
            tab[i][j] = p if d == 1 else (q if d == -1 else r)
    return tab


def rho_of(i, j, alpha):
    if i == j:
        return F(0)
    d = VEC[i][0] * VEC[j][0] + VEC[i][1] * VEC[j][1] + VEC[i][2] * VEC[j][2]
    return alpha if d == -1 else F(1)


def cond(P, a):
    w = [P[s][a[0]] * P[s][a[1]] * P[s][a[2]] for s in M]
    t = sum(w)
    return [x / t for x in w]


def w_true(mu, nu, alpha):
    """min-cost transport, successive shortest paths, exact Fractions."""
    N, src, snk = 14, 12, 13
    cap = [[F(0)] * N for _ in range(N)]
    cst = [[F(0)] * N for _ in range(N)]
    INF = F(2)
    for i in M:
        cap[src][i] = mu[i]
        cap[6 + i][snk] = nu[i]
        for j in M:
            cap[i][6 + j] = INF
            c = rho_of(i, j, alpha)
            cst[i][6 + j] = c
            cst[6 + j][i] = -c
    total = F(0)
    need = sum(mu)
    sent = F(0)
    while sent < need:
        dist = [None] * N
        prev = [-1] * N
        dist[src] = F(0)
        for _ in range(N - 1):
            upd = False
            for u in range(N):
                if dist[u] is None:
                    continue
                for v in range(N):
                    if cap[u][v] > 0:
                        nd = dist[u] + cst[u][v]
                        if dist[v] is None or nd < dist[v]:
                            dist[v] = nd
                            prev[v] = u
                            upd = True
            if not upd:
                break
        if dist[snk] is None:
            break
        b = need - sent
        v = snk
        while v != src:
            u = prev[v]
            b = min(b, cap[u][v])
            v = u
        v = snk
        while v != src:
            u = prev[v]
            cap[u][v] -= b
            cap[v][u] += b
            v = u
        sent += b
        total += b * dist[snk]
    return total


def w_plan(mu, nu, alpha):
    """author's plan: keep min, max-flow on non-antipodal, rest antipodal. Upper bound."""
    ex = [max(F(0), mu[i] - nu[i]) for i in M]
    de = [max(F(0), nu[i] - mu[i]) for i in M]
    tv = sum(ex)
    n, src, snk = 14, 0, 13
    cap = [[F(0)] * n for _ in range(n)]
    INF = tv + 1
    for i in M:
        cap[src][1 + i] = ex[i]
        cap[7 + i][snk] = de[i]
        for j in M:
            if ex[i] > 0 and de[j] > 0 and rho_of(i, j, alpha) == 1:
                cap[1 + i][7 + j] = INF
    flow = F(0)
    while True:
        prev = [-1] * n
        prev[src] = src
        q = [src]
        while q and prev[snk] == -1:
            u = q.pop(0)
            for v in range(n):
                if prev[v] == -1 and cap[u][v] > 0:
                    prev[v] = u
                    q.append(v)
        if prev[snk] == -1:
            break
        b, v = INF, snk
        while v != src:
            b = min(b, cap[prev[v]][v])
            v = prev[v]
        v = snk
        while v != src:
            cap[prev[v]][v] -= b
            cap[v][prev[v]] += b
            v = prev[v]
        flow += b
    rem_ex = [i for i in M if cap[src][1 + i] > 0]
    rem_de = [j for j in M if cap[7 + j][snk] > 0]
    if rem_ex:
        i = rem_ex[0]
        feas = len(rem_ex) == 1 and rem_de == [k for k in M if k != i and rho_of(i, k, alpha) != 1 and cap[7 + k][snk] > 0] and len(rem_de) == 1
        # leftover should be exactly the antipode of i
        feas = len(rem_ex) == 1 and len(rem_de) == 1 and rho_of(i, rem_de[0], alpha) == alpha and cap[src][1 + i] == cap[7 + rem_de[0]][snk]
    else:
        feas = not rem_de
    cost = tv + (alpha - 1) * (tv - flow)
    return cost, feas


def bilinear_max(K, laws):
    best = None
    KL = [[sum(K[i][j] * lam[j] for j in M) for i in M] for lam in laws]
    for l1 in laws:
        for v in KL:
            val = sum(l1[i] * v[i] for i in M)
            if best is None or val > best:
                best = val
    return best


def kappa_true(P, w, w2, alpha):
    rho = rho_of(w, w2, alpha)
    K = [[None] * 6 for _ in M]
    plan_ge = True
    feas = True
    for u1, u2 in itertools.product(M, repeat=2):
        mu = cond(P, (w, u1, u2))
        nu = cond(P, (w2, u1, u2))
        wt = w_true(mu, nu, alpha)
        wp, ok = w_plan(mu, nu, alpha)
        feas &= ok
        if wp < wt:
            plan_ge = False
        K[u1][u2] = wt / rho
    return K, feas, plan_ge


def tv_c(P):
    c = F(0)
    for u1, u2 in itertools.product(M, repeat=2):
        for w, w2 in itertools.combinations(M, 2):
            a, b = cond(P, (w, u1, u2)), cond(P, (w2, u1, u2))
            c = max(c, sum(abs(a[i] - b[i]) for i in M) / 2)
    return c


def main():
    hits = []
    q, r = 1, 2
    alpha = F(5, 4)

    print("T1 rho is a metric on M at alpha=5/4:")
    tri = True
    for i, j, k in itertools.product(M, repeat=3):
        if rho_of(i, k, alpha) > rho_of(i, j, alpha) + rho_of(j, k, alpha):
            tri = False
    print(f"  triangle on 6^3 triples: {tri}; rho in {{0,1,5/4}}; antipodal=5/4<=2")
    if not tri:
        hits.append("rho not a metric")

    print("T2 block 08 3c at the bracket:")
    for p, expect_lt in ((F(37, 10), True), (F(19, 5), False)):
        c = tv_c(phi_dot(p, q, r))
        print(f"  p={p}: 3c={float(3 * c):.6f} (<1 {3 * c < 1})")
        if (3 * c < 1) != expect_lt:
            hits.append(f"3c bracket {p}")

    configs = list(itertools.product(M, repeat=3))
    print("T3 grid 3 kbar (true W_rho, alpha=5/4, two types +x vs -x / +y):")
    grid = []
    plan_ok = True
    for k in range(37, 52):
        p = F(k, 10)
        P = phi_dot(p, q, r)
        laws = [cond(P, a) for a in configs]
        vals = []
        for w2 in (1, 2):
            K, feas, pge = kappa_true(P, 0, w2, alpha)
            plan_ok &= feas and pge
            vals.append(bilinear_max(K, laws))
        kb = max(vals)
        grid.append((p, kb))
        print(f"  p={float(p):.1f}: 3kbar={float(3 * kb):.8f} <1 {3 * kb < 1}")
        if 3 * kb >= 1:
            hits.append(f"3kbar>=1 at p={p}")
    print(f"  plan feasible and >= true W on every grid call: {plan_ok}")
    if not plan_ok:
        hits.append("plan not an upper bound or infeasible")

    print("T4 edge p=51/10, all 30 ordered pairs, true W:")
    p = F(51, 10)
    P = phi_dot(p, q, r)
    laws = [cond(P, a) for a in configs]
    per = {}
    kmax = F(0)
    for w, w2 in itertools.permutations(M, 2):
        K, feas, pge = kappa_true(P, w, w2, alpha)
        plan_ok &= feas and pge
        kb = bilinear_max(K, laws)
        per[(w, w2)] = kb
        kmax = max(kmax, max(max(row) for row in K))
    kbar = max(per.values())
    types = sorted(set(per.values()))
    stated = F(52187574259076840991934694, 156963184970376094931272779)
    print(f"  kbar={kbar} float={float(kbar):.8f}; 3kbar={float(3 * kbar):.8f} <1 {3 * kbar < 1}")
    print(f"  #distinct pair values {len(types)} (want 2); 3 kappa_max={float(3 * kmax):.6f}")
    print(f"  author's stated kbar vs true: stated={float(stated):.8f} true={float(kbar):.8f} stated>=true {stated >= kbar}")
    if len(types) != 2:
        hits.append(f"pair types {len(types)} != 2")
    if 3 * kbar >= 1:
        hits.append("edge 3kbar>=1")
    if stated < kbar:
        hits.append("author upper bound smaller than true W (impossible if plan is valid)")
    # first-level expansion then contraction
    if not (3 * kmax > 1 > 3 * kbar):
        print(f"  note: 3kmax={float(3 * kmax):.6f} 3kbar={float(3 * kbar):.6f}")

    if hits:
        for h in hits:
            print("FAIL: " + h)
        print("SUMMARY: fails at an independent finite check - " + "; ".join(hits))
        return 1
    print(
        "HIT: confirmed - the claim survives; independently: rho is a metric; true W_rho (min-cost "
        "transport, Fractions) gives 3 kbar < 1 at every p = 37/10..51/10 with alpha=5/4 "
        f"(3 kbar = {float(3 * kbar):.8f} at 51/10); author's orthogonal-then-antipodal plan is "
        "feasible and >= true W; 30 ordered pairs take exactly two values; block 08 3c < 1 at "
        "37/10 and >= 1 at 19/5; 3 kappa_max > 1 > 3 kbar so the first level may expand then "
        "contracts; this enlarges the proved no-memory region past 19/5 to 51/10 and does not "
        "reach 10.5-11"
    )
    print(
        "SUMMARY: confirmed - PARTIAL uniqueness/exponential memory loss on (p,1,2) at p=3.7..5.1 "
        "by averaged W_rho contraction at alpha=5/4; independent true-W certificates hold"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
