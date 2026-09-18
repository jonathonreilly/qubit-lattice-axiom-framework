#!/usr/bin/env python3
"""J:derive:uniqueness-region-up:a2 (worker w-jonathonsmac4f50-j1ba5, claude-opus-5): exact checks for ATTEMPT.md.

The six-axis formation law in level order (blocks 08, 28): the record at x is drawn from r(s | a) = prod_j phi(s, a_j) / sum_s' prod_j
phi(s', a_j), a = (a_1, a_2, a_3) the records of the three predecessors x - e_j, independently over a level given the previous one.

Criterion (ATTEMPT.md step 6): with the cube-invariant ground metric rho(w, w') = 0, 1 (orthogonal), alpha (antipodal), 1 <= alpha <= 2,
    kappa(w, w'; u1, u2) = W_rho(r(.|w,u1,u2), r(.|w',u1,u2)) / rho(w, w')          (upper bound by an explicit transport plan),
    kbar = max over w != w' and over achievable laws lam1, lam2 in A = {r(.|a) : a in M^3} of sum lam1(u1) lam2(u2) kappa(w, w'; u1, u2),
if 3 kbar < 1 the causal coupling contracts in the per-site W_rho distance from the second level on, so the level automaton has one
invariant law and forgets its initial plane exponentially.

Exact checks (fractions throughout):
  E1  the transport plan: keep min(mu, nu), route a maximum flow of the excess orthogonally (exact augmenting paths), the rest antipodally;
      its cost TV + (alpha - 1)(TV - maxflow) is an upper bound on W_rho, and the plan is feasible (remaining excess sits on one point, its
      remaining deficit on the antipode);
  E2  block 08's worst-case criterion 3c (c the one-site total-variation sensitivity) at p = 37/10 and 19/5 (block 28's bracket), and
      the new averaged criterion 3 kbar at alpha = 5/4 on the grid p = 37/10, 38/10, ..., 51/10 (two disagreement types, by the cube
      symmetry of step 5) and at p = 51/10 over all 30 ordered pairs w != w' (no symmetry used);
  E3  the first-level constant 3 kappa_max (worst case over u1, u2) at p = 51/10, for the explicit decay bound;
  E4  the exact sensitivity matrices kappa(+x, w'; u1, u2) for w' = -x and +y at p = 51/10, and the maximizing achievable laws.
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


def main():
    q, r = 1, 2
    alpha = F(5, 4)
    configs = list(itertools.product(M, repeat=3))
    # block 08's bracket
    for p in (F(37, 10), F(19, 5)):
        c = tv_c(phi(p, q, r))
        print(f"[block 08] p = {p}: c = {float(c):.6f}, 3c = {float(3 * c):.6f} ({'< 1' if 3 * c < 1 else '>= 1'})")
    # the grid, two disagreement types (cube symmetry, ATTEMPT.md step 5)
    feas_all, grid = True, []
    for k in range(37, 52):
        p = F(k, 10)
        P = phi(p, q, r)
        laws = [cond(P, a) for a in configs]
        vals = []
        for w2 in (1, 2):
            K, ok = kappa_matrix(P, 0, w2, alpha)
            feas_all &= ok
            vals.append(bilinear_max(K, laws)[0])
        kb = max(vals)
        grid.append((p, kb))
    print("[grid] 3 kbar at alpha = 5/4 (two types): " + ", ".join(f"{float(p):.1f}: {float(3 * kb):.5f}" for p, kb in grid)
          + f"; every value < 1: {all(3 * kb < 1 for _, kb in grid)}; transport plans feasible: {feas_all}")
    # the edge p = 51/10 with all 30 ordered pairs, no symmetry used
    p = F(51, 10)
    P = phi(p, q, r)
    laws = [cond(P, a) for a in configs]
    per_pair, kmax_first = {}, F(0)
    for w, w2 in itertools.permutations(M, 2):
        K, ok = kappa_matrix(P, w, w2, alpha)
        feas_all &= ok
        per_pair[(w, w2)] = bilinear_max(K, laws)
        kmax_first = max(kmax_first, max(max(row) for row in K))
    kbar = max(v for v, _ in per_pair.values())
    types = sorted({float(v) for v, _ in per_pair.values()})
    print(f"[edge] p = 51/10, alpha = 5/4, all 30 ordered pairs: kbar = {kbar} = {float(kbar):.8f}; 3 kbar = {float(3 * kbar):.8f} < 1: "
          f"{3 * kbar < 1}; distinct pair values {len(types)} ({', '.join(f'{t:.6f}' for t in types)}): the two relation types; first-level "
          f"3 kappa_max = {float(3 * kmax_first):.6f}; plans feasible: {feas_all}")
    for w2, name in ((1, "-x"), (2, "+y")):
        K, _ = kappa_matrix(P, 0, w2, alpha)
        val, (i1, i2) = per_pair[(0, w2)]
        print(f"[matrix +x vs {name}] rows u1, columns u2 (0:+x 1:-x 2:+y 3:-y 4:+z 5:-z): "
              + "; ".join("[" + ", ".join(f"{float(x):.4f}" for x in row) + "]" for row in K)
              + f"; maximized by the laws of predecessor patterns {configs[i1]}, {configs[i2]} with value {float(val):.6f}")
    ok = all(3 * kb < 1 for _, kb in grid) and 3 * kbar < 1 and feas_all
    if ok:
        print("HIT: the six-axis formation law in level order at (p, 1, 2) has a unique invariant law and forgets its initial plane "
              "exponentially at every p in {37/10, 38/10, ..., 51/10}: with the ground metric rho = 1 (orthogonal), 5/4 (antipodal) the "
              "averaged Wasserstein sensitivity satisfies 3 kbar < 1 exactly (3 kbar = %.6f at p = 51/10), extending block 08's criterion "
              "3c < 1 (which fails at p = 19/5)" % float(3 * kbar))
        print("SUMMARY: PARTIAL - exact certificates of uniqueness and exponential memory loss for the six-axis formation law on (p,1,2) at "
              "p = 3.7 ... 5.1 by an averaged Wasserstein contraction (alpha = 5/4); the numerical edge of the criterion is near p = 5.11; the "
              "located threshold 10.5-11 is not reached")
    else:
        print("SUMMARY: ROUTE FAILS AT the exact criterion (see above)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
