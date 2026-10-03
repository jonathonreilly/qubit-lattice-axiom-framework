"""Check 3: feasibility of the minimal MH rule for random range-1 two-component walks.

Random inhomogeneous walks on a ring of N=8 sites with d=2 components per site are built
as L3 L2 L1 on the 2N 'half-sites' (h = 2x+s):  L1, L3 act inside each site (pairs (2x,2x+1)),
L2 acts across sites (pairs (2x+1, 2x+2 mod 2N)).  Every such U is strictly range 1 on sites.

Per tick we test
  (a) existence of SOME nearest-neighbour equivariant coupling (LP)  -- Theorem A says always;
  (b) sign of pi_MH (is the MH split itself a coupling?);
  (c) outflow bound of the minimal MH rule  sum_y J_MH^+(x->y) <= P_t(x);
  (d) if (c) fails: repaired rule with circulation clipped into the feasible interval.
"""
import numpy as np
from common import (haar_unitary, rand_state, site_probs, mh_split, rule_from_flow,
                    lp_coupling, lp_circulation_range, ring_allowed)

N, d = 8, 2
rng = np.random.default_rng(11)
allowed = ring_allowed(N)


def random_walk():
    n = N * d
    def lay(pairs):
        U = np.eye(n, dtype=complex)
        for (a, b) in pairs:
            U[np.ix_([a, b], [a, b])] = haar_unitary(2, rng)
        return U
    inside = [(2 * x, 2 * x + 1) for x in range(N)]
    across = [(2 * x + 1, (2 * x + 2) % n) for x in range(N)]
    return lay(inside) @ lay(across) @ lay(inside)


def check_range1(U):
    Ub = U.reshape(N, d, N, d)
    worst = 0.0
    for x in range(N):
        for y in range(N):
            if not allowed[y, x]:
                worst = max(worst, float(np.abs(Ub[y, :, x, :]).max()))
    return worst


def repaired_rule(P, Pn, J):
    """Keep J_MH's shape; move its ring circulation to the nearest feasible value."""
    F0 = np.zeros(N)
    acc = 0.0
    for x in range(N):
        acc += P[x] - Pn[x]
        F0[x] = acc                       # net flow across bond (x, x+1) with zero circulation offset
    F0 = F0 - F0[N - 1]                   # F0[N-1] = 0 (total conserved)
    c_mh = J[N - 1, 0] - F0[N - 1]
    c_lo, c_hi = lp_circulation_range(P, Pn, allowed, N - 1, 0)
    c = min(max(c_mh, c_lo), c_hi)
    Jr = np.zeros((N, N))
    for x in range(N):
        f = F0[x] + c
        Jr[x, (x + 1) % N] = f
        Jr[(x + 1) % N, x] = -f
    T, ex = rule_from_flow(Jr, P)
    return T, ex, c_mh, c_lo, c_hi


trials, ticks = 400, 6
n_neg, n_inf, n_lp_fail, worst_neg, worst_ex, worst_range = 0, 0, 0, 0.0, -1.0, 0.0
rep_worst_eq, rep_worst_ex, total = 0.0, -1.0, 0
examples = []
for tr in range(trials):
    U = random_walk()
    worst_range = max(worst_range, check_range1(U))
    psi = rand_state(N * d, rng) if tr % 2 == 0 else np.eye(N * d)[rng.integers(N * d)].astype(complex)
    for t in range(ticks):
        total += 1
        P = site_probs(psi, N, d)
        piMH, K, psin = mh_split(U, psi, N, d)
        Pn = site_probs(psin, N, d)
        ok, _, _ = lp_coupling(P, Pn, allowed, 'zero')
        n_lp_fail += (not ok)
        if piMH.min() < -1e-12:
            n_neg += 1
            worst_neg = min(worst_neg, float(piMH.min()))
        J = piMH - piMH.T
        T, ex = rule_from_flow(J, P)
        worst_ex = max(worst_ex, ex)
        if ex > 1e-12:
            n_inf += 1
            Tr, exr, c_mh, c_lo, c_hi = repaired_rule(P, Pn, J)
            rep_worst_ex = max(rep_worst_ex, exr)
            rep_worst_eq = max(rep_worst_eq, float(np.abs(P @ Tr - Pn).max()))
            if len(examples) < 3:
                examples.append((tr, t, ex, c_mh, c_lo, c_hi))
        psi = psin

print(f"random range-1 d=2 walks: {trials} walks x {ticks} ticks = {total} ticks; "
      f"max matrix element beyond range 1 = {worst_range:.1e}")
print(f"  (a) ticks with NO nearest-neighbour coupling (LP)      : {n_lp_fail}")
print(f"  (b) ticks with some pi_MH < 0                          : {n_neg}  (most negative {worst_neg:.3f})")
print(f"  (c) ticks where minimal MH rule breaks the outflow bound: {n_inf}  (largest excess {worst_ex:.3e})")
print(f"  (d) repaired rule on those ticks: max outflow excess = {rep_worst_ex:.2e}, "
      f"max|P_t T - P_t+1| = {rep_worst_eq:.2e}")
for e in examples:
    print(f"      example walk {e[0]} tick {e[1]}: excess {e[2]:.3e}; c_MH = {e[3]:+.4f}, "
          f"feasible c in [{e[4]:+.4f}, {e[5]:+.4f}]")
