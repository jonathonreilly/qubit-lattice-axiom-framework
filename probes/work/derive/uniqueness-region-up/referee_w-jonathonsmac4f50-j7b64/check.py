#!/usr/bin/env python3
"""Referee of J:derive:uniqueness-region-up:a1 (author w-macbookpro90c72-jcc2b, grok-4.6); referee w-jonathonsmac4f50-j7b64
(claude-opus-5). Provenance: the criterion is that of attempt a2 (worker w-jonathonsmac4f50-j1ba5, this referee's model
family, refereed as a partial); a1 re-implements it and adds the grid point p = 511/100. The functions below are copied from
a2's check.py (this referee's family's code, not the author's), so this is a recomputation, not an independent method.

U1  a2's value at p = 51/10 (alpha = 5/4, all 30 ordered pairs) against a1's fraction
U2  p = 511/100, alpha = 5/4, all 30 ordered pairs, no symmetry used: 3 kbar < 1 exactly, and the transport plans feasible
U3  p = 512/100 and 52/10 at alpha = 5/4 (the two disagreement types, cube symmetry): 3 kbar > 1
U4  alpha = 4/3 and 3/2 at p = 51/10 and 511/100 (two types): the author's values
"""
import itertools
import sys
from fractions import Fraction as F

M = range(6)                                     # 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z ; antipode of a is a ^ 1


def phi(p, q, r):
    return [[p if a == b else (q if a == b ^ 1 else r) for b in M] for a in M]


def cond(P, a):
    w = [P[s][a[0]] * P[s][a[1]] * P[s][a[2]] for s in M]
    t = sum(w)
    return [x / t for x in w]


def maxflow(ex, de):
    """exact max flow from excess points to deficit points through non-antipodal arcs i -> j (j != i ^ 1)"""
    n = 14                                        # 0 source, 1..6 excess, 7..12 deficit, 13 sink
    cap = [[F(0)] * n for _ in range(n)]
    INF = sum(ex) + 1
    for i in M:
        cap[0][1 + i] = ex[i]
        cap[7 + i][13] = de[i]
        for j in M:
            if ex[i] > 0 and de[j] > 0 and j != (i ^ 1):
                cap[1 + i][7 + j] = INF
    flow = F(0)
    while True:
        prev = [-1] * n
        prev[0] = 0
        queue = [0]
        while queue and prev[13] == -1:
            u = queue.pop(0)
            for v in range(n):
                if prev[v] == -1 and cap[u][v] > 0:
                    prev[v] = u
                    queue.append(v)
        if prev[13] == -1:
            return flow, cap
        b, v = INF, 13
        while v != 0:
            b = min(b, cap[prev[v]][v])
            v = prev[v]
        v = 13
        while v != 0:
            cap[prev[v]][v] -= b
            cap[v][prev[v]] += b
            v = prev[v]
        flow += b


def w_rho(mu, nu, alpha):
    ex = [max(F(0), mu[i] - nu[i]) for i in M]
    de = [max(F(0), nu[i] - mu[i]) for i in M]
    tv = sum(ex)
    fl, cap = maxflow(ex, de)
    rem_ex = [cap[0][1 + i] for i in M]           # residual source capacity = excess not routed
    rem_de = [cap[7 + j][13] for j in M]
    pts = [i for i in M if rem_ex[i] > 0]
    if pts:
        feasible = len(pts) == 1 and rem_de[pts[0] ^ 1] == rem_ex[pts[0]] and sum(rem_de) == rem_ex[pts[0]]
    else:
        feasible = sum(rem_de) == 0
    return tv + (alpha - 1) * (tv - fl), tv, feasible


def kappa_matrix(P, w, w2, alpha):
    rho = alpha if w2 == (w ^ 1) else F(1)
    K, ok = [[None] * 6 for _ in M], True
    for u1, u2 in itertools.product(M, repeat=2):
        cost, _, feas = w_rho(cond(P, (w, u1, u2)), cond(P, (w2, u1, u2)), alpha)
        ok &= feas
        K[u1][u2] = cost / rho
    return K, ok


def bilinear_max(K, laws):
    best, arg = None, None
    KL = [[sum(K[i][j] * lam[j] for j in M) for i in M] for lam in laws]      # K lam2
    for i1, l1 in enumerate(laws):
        for i2, v in enumerate(KL):
            val = sum(l1[i] * v[i] for i in M)
            if best is None or val > best:
                best, arg = val, (i1, i2)
    return best, arg


def tv_c(P):
    c = F(0)
    for u1, u2 in itertools.product(M, repeat=2):
        for w, w2 in itertools.combinations(M, 2):
            a, b = cond(P, (w, u1, u2)), cond(P, (w2, u1, u2))
            c = max(c, sum(abs(a[i] - b[i]) for i in M) / 2)
    return c




def three_kbar(p, alpha, all_pairs):
    P = phi(p, 1, 2)
    laws = [cond(P, a) for a in itertools.product(M, repeat=3)]
    pairs = list(itertools.permutations(M, 2)) if all_pairs else [(0, 1), (0, 2)]
    feas = True
    kb = F(0)
    for w, w2 in pairs:
        K, ok = kappa_matrix(P, w, w2, alpha)
        feas &= ok
        kb = max(kb, bilinear_max(K, laws)[0])
    return 3 * kb, feas


def main():
    fails = 0
    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)
    v51, f51 = three_kbar(F(51, 10), F(5, 4), True)
    want = F(52187574259076840991934694, 52321061656792031643757593)
    check("U1", v51 == want and f51, f"p = 51/10, alpha = 5/4, all 30 pairs: 3 kbar = {v51} = {float(v51):.8f}, the author's fraction; plans feasible")
    v511, f511 = three_kbar(F(511, 100), F(5, 4), True)
    check("U2", v511 < 1 and f511 and abs(float(v511) - 0.99981627) < 5e-9,
          f"p = 511/100, alpha = 5/4, all 30 ordered pairs: 3 kbar = {v511} = {float(v511):.8f} < 1 (the author's 0.99981627); plans feasible")
    rows = []
    ok = True
    for p in (F(512, 100), F(52, 10)):
        v, fe = three_kbar(p, F(5, 4), False)
        ok = ok and v > 1 and fe
        rows.append(f"p = {p}: {float(v):.8f}")
    check("U3", ok, "alpha = 5/4, two disagreement types: " + "; ".join(rows) + " (> 1)")
    rows = []
    ok = True
    want4 = {(F(4, 3), F(51, 10)): 0.99827159, (F(4, 3), F(511, 100)): 1.00064630, (F(3, 2), F(51, 10)): 0.99991740, (F(3, 2), F(511, 100)): 1.00230637}
    for (al, p), w in want4.items():
        v, fe = three_kbar(p, al, False)
        ok = ok and abs(float(v) - w) < 5e-8 and fe
        rows.append(f"alpha = {al}, p = {p}: {float(v):.8f}")
    check("U4", ok, "other alpha (two types): " + "; ".join(rows) + " (the author's values)")
    if fails:
        print("SUMMARY: fails at a recomputed value (see FAIL lines)")
        return 1
    print("HIT: confirmed - a1's new grid point survives: at p = 511/100 and alpha = 5/4 the averaged Wasserstein criterion gives "
          "3 kbar = %.8f < 1 exactly over all 30 ordered disagreement pairs (feasible plans), so a2's uniqueness argument applies at p = 5.11; "
          "3 kbar > 1 at 512/100 and 52/10; the author's alpha variants reproduced. Recomputed with a2's code (this referee family's), not an "
          "independent method" % float(v511))
    print("SUMMARY: confirmed - no failing step for steps 1-3 and 5; step 4 (same-copy joints) is labelled as not used and was not re-checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
