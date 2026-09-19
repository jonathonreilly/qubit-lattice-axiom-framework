#!/usr/bin/env python3
"""uniqueness-up-2, attempt a3 (w-jonathonsmac4f50-j96fc): exact certificates for the shared-predecessor averaged Wasserstein recursion.

Objects (blocks 08, 28; round-1 attempt uniqueness-region-up a2): six-axis menu M = {+-e1, +-e2, +-e3}, phi = p (equal), q = 1 (antipodal),
r = 2 (orthogonal); r(s | a1, a2, a3) = prod_j phi(s, a_j)/Z; ground metric rho = 1 (orthogonal), alpha (antipodal), 1 <= alpha <= 2;
kappa(w, w'; u1, u2) = W_rho(r(.|w,u1,u2), r(.|w',u1,u2))/rho(w, w'); A = the 56 achievable one-site laws.
  kappa_max = max kappa;  k1 = max over lambda1, lambda2 in A of E kappa (round 1's averaged constant);
  ks = max over z, {b1, b2}, {c1, c2} in M of E kappa with lambda1 = r(.|z,b1,b2), lambda2 = r(.|z,c1,c2) (sibling sites share a predecessor).
Criterion (ATTEMPT.md S4): C = 3 ks + min(alpha, 3 kappa_max)(k1 - ks) < 1 gives D_{t+1} <= 3 ks D_t + min(alpha, 3 kappa_max)(k1 - ks) D_{t-1},
hence one invariant law and exponential forgetting.
 W1  the closed form W_rho(mu, nu) = TV + (alpha - 1) max_i (e_i + d_{-i} - TV)^+ against an exact brute-force LP (vertex enumeration of the
     transport polytope is replaced by exact min-cost flow on small integer-mass instances)
 W2  round-1 cross-check: at p = 51/10, alpha = 5/4 the recomputed k1 equals round 1's exact 52187574259076840991934694/156963184970376094931272779
 C1  exact certificates C < 1 at alpha = 27/20 for p = 511/100, 513/100, ..., 525/100, 526/100; C > 1 at p = 527/100 and 53/10 (the edge)
 C2  the symmetry reduction to the two ordered-pair types (+x, -x), (+x, +y): all 30 ordered pairs at p = 526/100 give exactly two values of
     the shared constant
"""
import itertools
import sys
import time
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
NEG = [1, 0, 3, 2, 5, 4]


def phi(i, j, w):
    d = sum(a * b for a, b in zip(AX[i], AX[j]))
    return w[0] if d == 1 else (w[1] if d == -1 else w[2])


def laws(w):
    L = {}
    for t in cwr(range(6), 3):
        ws = [phi(s, t[0], w) * phi(s, t[1], w) * phi(s, t[2], w) for s in range(6)]
        Z = sum(ws)
        L[t] = tuple(F(x) / Z for x in ws)
    return L


def W(mu, nu, alpha):
    e = [max(F(0), a - b) for a, b in zip(mu, nu)]
    d = [max(F(0), b - a) for a, b in zip(mu, nu)]
    TV = sum(e)
    M = max(max(F(0), e[i] + d[NEG[i]] - TV) for i in range(6))
    return TV + (alpha - 1) * M


def rho(i, j, alpha):
    return 0 if i == j else (alpha if j == NEG[i] else 1)


def constants(w, alpha, pairs=((0, 1), (0, 2))):
    L = laws(w)

    def lw(*a):
        return L[tuple(sorted(a))]
    kap = {}
    for (a, b) in pairs:
        for u1 in range(6):
            for u2 in range(6):
                kap[(a, b, u1, u2)] = W(lw(a, u1, u2), lw(b, u1, u2), alpha) / rho(a, b, alpha)
    kmax = max(kap.values())
    envs = list(L.values())

    def avg(a, b, l1, l2):
        return sum(l1[u1] * l2[u2] * kap[(a, b, u1, u2)] for u1 in range(6) for u2 in range(6))
    k1 = max(avg(a, b, l1, l2) for (a, b) in pairs for l1 in envs for l2 in envs)
    ks = F(0)
    ks_by_pair = {}
    for (a, b) in pairs:
        best = F(0)
        for z in range(6):
            Ez = [lw(z, b1, b2) for (b1, b2) in cwr(range(6), 2)]
            for l1 in Ez:
                for l2 in Ez:
                    v = avg(a, b, l1, l2)
                    if v > best:
                        best = v
        ks_by_pair[(a, b)] = best
        ks = max(ks, best)
    return kmax, k1, ks, ks_by_pair


def mincost_bruteforce(mu, nu, alpha, scale):
    """exact min-cost transport between integer mass vectors (mu*scale, nu*scale) by successive shortest paths on the 6x6 bipartite graph"""
    import heapq
    src = [int(x * scale) for x in mu]
    dst = [int(x * scale) for x in nu]
    cost = 0
    supply = src[:]
    demand = dst[:]
    # greedy is not optimal in general; use LP via exhaustive search on flows for tiny masses (total mass <= 6)
    best = None
    cells = [(i, j) for i in range(6) for j in range(6)]

    def rec(k, sup, dem, acc):
        nonlocal best
        if best is not None and acc >= best:
            return
        if k == len(cells):
            if all(s == 0 for s in sup) and all(d == 0 for d in dem):
                best = acc
            return
        i, j = cells[k]
        m = min(sup[i], dem[j])
        for x in range(m, -1, -1):
            sup[i] -= x
            dem[j] -= x
            rec(k + 1, sup, dem, acc + x * rho(i, j, alpha))
            sup[i] += x
            dem[j] += x
    rec(0, supply, demand, 0)
    return F(best, scale)


def main():
    # W1: closed form against exhaustive exact transport on small integer masses
    import random
    rng = random.Random(8146)
    ok = True
    n = 0
    for _ in range(60):
        tot = 5
        a = [0] * 6
        b = [0] * 6
        for _ in range(tot):
            a[rng.randrange(6)] += 1
            b[rng.randrange(6)] += 1
        mu = [F(x, tot) for x in a]
        nu = [F(x, tot) for x in b]
        for alpha in (F(1), F(27, 20), F(2)):
            ok &= W(mu, nu, alpha) == mincost_bruteforce(mu, nu, alpha, tot)
            n += 1
    check("W1", ok, f"W_rho(mu, nu) = TV + (alpha - 1) max_i (e_i + d_(-i) - TV)^+ equals the exhaustive exact minimum transport cost on {n} random "
          f"integer-mass instances (alpha = 1, 27/20, 2); the formula is proved in ATTEMPT.md S1 (plan + 1-Lipschitz dual)")
    # W2: cross-check with round 1
    kmax, k1, ks, _ = constants((F(51, 10), 1, 2), F(5, 4))
    ok2 = k1 == F(52187574259076840991934694, 156963184970376094931272779)
    check("W2", ok2, f"at p = 51/10, alpha = 5/4: k1 = {k1} (round 1's exact value), 3 k1 = {float(3 * k1):.8f}; shared constant 3 ks = {float(3 * ks):.8f}")
    # C1: certificates
    alpha = F(27, 20)
    rows = []
    ok3 = True
    grid = [F(511, 100)] + [F(x, 100) for x in range(513, 527, 2)] + [F(526, 100)]
    certs = {}
    for p in grid:
        kmax, k1, ks, _ = constants((p, 1, 2), alpha)
        C = 3 * ks + min(alpha, 3 * kmax) * (k1 - ks)
        certs[p] = C
        ok3 &= C < 1 and 3 * k1 >= 1
        rows.append(f"p = {float(p):.2f}: 3k1 = {float(3 * k1):.5f}, C = {float(C):.6f}")
    fails = []
    for p in (F(527, 100), F(53, 10)):
        kmax, k1, ks, _ = constants((p, 1, 2), alpha)
        C = 3 * ks + min(alpha, 3 * kmax) * (k1 - ks)
        fails.append(f"p = {float(p):.2f}: C = {float(C):.6f}")
        ok3 &= C > 1
    Cedge = certs[F(526, 100)]
    check("C1", ok3, f"alpha = 27/20, exact: " + "; ".join(rows) + f" (all C < 1, while round 1's 3k1 >= 1 at every one of these points at this alpha); edge: " + "; ".join(fails)
          + f"; at p = 526/100, C = {Cedge.numerator}/{Cedge.denominator}"[:4000])
    # C2: symmetry
    allpairs = [(a, b) for a in range(6) for b in range(6) if a != b]
    _, _, _, byp = constants((F(526, 100), 1, 2), alpha, pairs=allpairs)
    vals = set(byp.values())
    anti = {byp[(a, b)] for (a, b) in allpairs if b == NEG[a]}
    orth = {byp[(a, b)] for (a, b) in allpairs if b != NEG[a]}
    ok4 = len(vals) == 2 and len(anti) == 1 and len(orth) == 1
    check("C2", ok4, f"at p = 526/100 the shared constant over all 30 ordered pairs takes exactly two values (antipodal {float(next(iter(anti))):.6f}, "
          f"orthogonal {float(next(iter(orth))):.6f}): the reduction to the types (+x, -x), (+x, +y) holds")
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("certificates above 5.11: with the ground metric (1, 27/20) and the sibling-shared-predecessor restriction of the environment "
            "laws, D_{t+1} <= 3 ks D_t + min(alpha, 3 kappa_max)(k1 - ks) D_{t-1} and the exact constant C = 3 ks + min(alpha, 3 kappa_max)(k1 - ks) "
            "is below 1 at p = 5.11, 5.13, ..., 5.25, 5.26 on (p, 1, 2) (C(5.26) = %.6f) and above 1 at 5.27: one invariant law and exponential "
            "forgetting of every initial plane for the six-axis formation law at those p; largest certified p = 263/50 = 5.26 (round 1: 5.11); "
            "the criterion saturates near 5.3: the maximizing environment is a w | w' wall, one sibling with predecessors (w, w, w), the other "
            "with (w, w', w'), sharing the w-valued predecessor" % float(Cedge))
    print("SUMMARY: PARTIAL " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
