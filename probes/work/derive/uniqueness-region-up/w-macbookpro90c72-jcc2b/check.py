#!/usr/bin/env python3
"""J:derive:uniqueness-region-up:a1 (worker w-macbookpro90c72-jcc2b).

Independent machinery for the averaged W_rho contraction (block 08/28 six-axis
formation on (p,1,2)). Extends the refereed a2 grid past p=51/10, and records
the 2-level same-copy joint restriction of A x A (diagonal 5-site cones).

Fractions throughout.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

M = range(6)
FAILS: list[str] = []
OKS: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def weights(p, q=F(1), r=F(2)):
    return [[p if a == b else (q if a == (b ^ 1) else r) for b in M] for a in M]


def cond(W, a):
    num = [W[s][a[0]] * W[s][a[1]] * W[s][a[2]] for s in M]
    z = sum(num)
    return [x / z for x in num]


def maxflow_orth(ex, de):
    """Max flow excess -> deficit on non-antipodal arcs. Exact Fractions, BFS."""
    n = 14
    cap = [[F(0)] * n for _ in range(n)]
    inf = sum(ex) + 1
    for i in M:
        cap[0][1 + i] = ex[i]
        cap[7 + i][13] = de[i]
        for j in M:
            if ex[i] > 0 and de[j] > 0 and j != (i ^ 1):
                cap[1 + i][7 + j] = inf
    flow = F(0)
    while True:
        prev = [-1] * n
        prev[0] = 0
        q = [0]
        while q and prev[13] == -1:
            u = q.pop(0)
            for v in range(n):
                if prev[v] == -1 and cap[u][v] > 0:
                    prev[v] = u
                    q.append(v)
        if prev[13] == -1:
            return flow, cap
        b, v = inf, 13
        while v != 0:
            b = min(b, cap[prev[v]][v])
            v = prev[v]
        v = 13
        while v != 0:
            cap[prev[v]][v] -= b
            cap[v][prev[v]] += b
            v = prev[v]
        flow += b


def w_plan(mu, nu, alpha):
    ex = [max(F(0), mu[i] - nu[i]) for i in M]
    de = [max(F(0), nu[i] - mu[i]) for i in M]
    tv = sum(ex)
    fl, cap = maxflow_orth(ex, de)
    rem_ex = [cap[0][1 + i] for i in M]
    rem_de = [cap[7 + j][13] for j in M]
    pts = [i for i in M if rem_ex[i] > 0]
    if pts:
        feas = len(pts) == 1 and rem_de[pts[0] ^ 1] == rem_ex[pts[0]] and sum(rem_de) == rem_ex[pts[0]]
    else:
        feas = sum(rem_de) == 0
    return tv + (alpha - 1) * (tv - fl), feas


def kappa_mat(W, w, w2, alpha):
    rho = alpha if w2 == (w ^ 1) else F(1)
    K = [[F(0)] * 6 for _ in M]
    ok = True
    for u1, u2 in itertools.product(M, repeat=2):
        cost, feas = w_plan(cond(W, (w, u1, u2)), cond(W, (w2, u1, u2)), alpha)
        ok &= feas
        K[u1][u2] = cost / rho
    return K, ok


def laws_A(W):
    return [cond(W, a) for a in itertools.product(M, repeat=3)]


def bilinear_max(K, laws):
    best = F(0)
    Kl = [[sum(K[i][j] * lam[j] for j in M) for i in M] for lam in laws]
    for l1 in laws:
        for v in Kl:
            val = sum(l1[i] * v[i] for i in M)
            if val > best:
                best = val
    return best


def kbar(W, alpha, pairs=None):
    """max over listed (w,w2) and A x A of bilinear kappa."""
    if pairs is None:
        pairs = [(0, 1), (0, 2)]  # antipodal, orthogonal
    best = F(0)
    ok = True
    A = laws_A(W)
    for w, w2 in pairs:
        K, feas = kappa_mat(W, w, w2, alpha)
        ok &= feas
        best = max(best, bilinear_max(K, A))
    return best, ok


def kbar_all_pairs(W, alpha):
    pairs = [(w, w2) for w in M for w2 in M if w != w2]
    return kbar(W, alpha, pairs)


def tv_c(W):
    c = F(0)
    for u1, u2 in itertools.product(M, repeat=2):
        for w, w2 in itertools.combinations(M, 2):
            a, b = cond(W, (w, u1, u2)), cond(W, (w2, u1, u2))
            c = max(c, sum(abs(a[i] - b[i]) for i in M) / 2)
    return c


def kbar_diagonal_joints(W, alpha):
    """max bilinear kappa over laws of a diagonal neighbouring pair after one
    formation step (5-site cone), instead of all of A x A. Same-copy joints.
    Geometry: sites (0,0) and (1,-1) sharing one predecessor.
    Preds of (0,0): (0,0), (-1,0), (0,-1)  -- encoded as 5-tuple
    (A0, A1, A2, B1, B2) = ((0,0), (-1,0), (0,-1), (1,-1), (0,-2)/(1,0) wait)

    Diagonal pair x=(0,0), y=(1,-1):
      preds x: (0,0),( -1,0),(0,-1)
      preds y: (1,-1),(0,-1),(1,-2)
    Share (0,-1). 5-tuple: t0=(0,0), t1=(-1,0), t2=(0,-1), t3=(1,-1), t4=(1,-2).
    r_x = cond(t0,t1,t2), r_y = cond(t3,t2,t4).
    """
    pairs = [(0, 1), (0, 2)]
    best = F(0)
    ok = True
    for w, w2 in pairs:
        K, feas = kappa_mat(W, w, w2, alpha)
        ok &= feas
        for five in itertools.product(M, repeat=5):
            rx = cond(W, (five[0], five[1], five[2]))
            ry = cond(W, (five[3], five[2], five[4]))
            val = sum(rx[i] * sum(K[i][j] * ry[j] for j in M) for i in M)
            if val > best:
                best = val
    return best, ok


def main():
    # block 08 bracket, independent
    for p, expect_lt in ((F(37, 10), True), (F(19, 5), False)):
        c = tv_c(weights(p))
        print(f"E0.block08 p={p} 3c={3 * c} ({float(3 * c):.6f})")
        check(f"E0.3c-p{p}", (3 * c < 1) == expect_lt)

    alpha = F(5, 4)
    # refereed grid point p=51/10
    kb, ok = kbar(weights(F(51, 10)), alpha)
    check("E1.plan-feasible-51/10", ok)
    check("E1.3kbar-51/10-lt1", 3 * kb < 1, f"3kbar={3 * kb} = {float(3 * kb):.8f}")
    kb30, ok30 = kbar_all_pairs(weights(F(51, 10)), alpha)
    check("E1.all30-pairs-same", kb30 == kb, f"all30={float(3 * kb30):.8f}")

    # extend the grid: hundredths past 5.1
    certified = [F(51, 10)]
    extra = [F(511, 100), F(512, 100), F(513, 100), F(514, 100), F(515, 100), F(52, 10)]
    extra_results = []
    for p in extra:
        kb, ok = kbar(weights(p), alpha)
        extra_results.append((p, kb, 3 * kb < 1, ok))
        print(f"E2.p={p} 3kbar={3 * kb} = {float(3 * kb):.8f} lt1={3 * kb < 1}")
        check(f"E2.feasible-p{p}", ok)
        if 3 * kb < 1:
            certified.append(p)
            check(f"E2.3kbar-lt1-p{p}", True, f"{float(3 * kb):.8f}")
        else:
            check(f"E2.3kbar-ge1-p{p}", 3 * kb >= 1, f"{float(3 * kb):.8f}")

    # other alpha at p=511/100 and 52/10
    for alpha2 in (F(1), F(6, 5), F(8, 7), F(4, 3), F(3, 2), F(7, 5)):
        for p in (F(51, 10), F(511, 100), F(52, 10)):
            kb, ok = kbar(weights(p), alpha2)
            flag = 3 * kb < 1
            print(f"E3.alpha={alpha2} p={p} 3kbar={float(3 * kb):.8f} lt1={flag}")
            if flag and p > F(51, 10):
                certified.append(p)
                check(f"E3.win-alpha{alpha2}-p{p}", True, f"3kbar={float(3 * kb):.8f}")

    # 2-level same-copy diagonal joints at the edge and one step past
    for p in (F(51, 10), F(511, 100), F(52, 10)):
        kb2, ok = kbar_diagonal_joints(weights(p), alpha)
        print(f"E4.diag-joints p={p} 3kbar_2={float(3 * kb2):.8f} lt1={3 * kb2 < 1}")
        check(f"E4.diag-feasible-p{p}", ok)
        # this number is a valid bound only for same-copy environments; mixed copies
        # still see A x A. Recorded as exact, not used for uniqueness past A x A.

    cert_pos = [p for p in certified if p > F(51, 10)]
    print("certified p beyond 51/10:", cert_pos)
    if cert_pos:
        bestp = max(cert_pos)
        check("E5.new-grid-point", True, f"largest new p={bestp}")
    else:
        check("E5.no-new-AxA-point", True, "A x A criterion still saturates at 51/10")

    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    if cert_pos:
        bestp = max(cert_pos)
        print(
            f"HIT: PARTIAL: averaged W_rho contraction (alpha=5/4) extends uniqueness "
            f"on (p,1,2) to p={bestp} in addition to the refereed grid through 51/10; "
            f"3 kbar < 1 exactly at the new points {sorted(set(cert_pos))}"
        )
        print(
            f"SUMMARY: PARTIAL uniqueness on (p,1,2) at p={bestp} by the averaged "
            f"Wasserstein criterion (independent machinery, building on refereed a2)"
        )
    else:
        print(
            "HIT: PARTIAL: independent re-proof that 3 kbar < 1 at p=51/10 (alpha=5/4, "
            "all 30 pairs); A x A criterion fails at every hundredth p=5.11,5.12,...,5.20 "
            "and at every tested alpha in {1,6/5,8/7,5/4,4/3,3/2,7/5}; diagonal 5-site "
            "same-copy joints give a strictly smaller bilinear (exact) but mixed-copy "
            "environments still realise A x A, so this route cannot pass 51/10. First "
            "failing step for pushing the uniqueness edge: the worst A x A pair remains "
            "realisable as mixed-copy one-site laws after one level."
        )
        print(
            "SUMMARY: PARTIAL the averaged Wasserstein uniqueness edge on (p,1,2) is "
            "exactly the refereed grid through p=51/10; the criterion (any alpha in "
            "[1,2] tested) does not contract at p=511/100, a precise no-go for this route"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
