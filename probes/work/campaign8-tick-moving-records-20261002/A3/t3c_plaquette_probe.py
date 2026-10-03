"""Check 3c: a single plaquette (4-site cycle) -- the smallest loop of Z^2/Z^3.

Strictly range-1 ticks on a 4-cycle (no move across the diagonal) are sampled by
alternating projections: zero the opposite-corner blocks, then take the nearest unitary
(polar factor).  On the 4-cycle the 1D bond-identity argument (needs N >= 5) does not apply.
We probe: (a) is the lambda flow Im K - Im K^T non-zero?  (b) can the minimal MH rule break
the outflow bound?  (c) a nearest-neighbour coupling always exists (Theorem A).
"""
import numpy as np
from common import haar_unitary, rand_state, mh_split, rule_from_flow, lp_coupling

rng = np.random.default_rng(3)
N = 4
allowed = np.ones((N, N), bool)
allowed[0, 2] = allowed[2, 0] = allowed[1, 3] = allowed[3, 1] = False


def banded_unitary(d, iters=4000):
    n = N * d
    U = haar_unitary(n, rng)
    mask = np.zeros((n, n), bool)
    for x in range(N):
        for y in range(N):
            if not allowed[y, x]:
                mask[y*d:(y+1)*d, x*d:(x+1)*d] = True
    for _ in range(iters):
        V = U.copy(); V[mask] = 0
        W, s, Vh = np.linalg.svd(V)
        U = W @ Vh
        if np.abs(U[mask]).max() < 1e-13:
            break
    return U, float(np.abs(U[mask]).max())


for d in (1, 2):
    worst_band, n_im, worst_im, n_viol, worst_ex, n_lp, tot = 0.0, 0, 0.0, 0, -1.0, 0, 0
    examples = []
    for rep in range(60):
        U, band = banded_unitary(d)
        if band > 1e-10:
            continue
        worst_band = max(worst_band, band)
        for k in range(10):
            psi = rand_state(N * d, rng) if k % 2 == 0 else np.eye(N * d)[rng.integers(N * d)].astype(complex)
            P = (np.abs(psi.reshape(N, d)) ** 2).sum(1)
            piMH, K, psin = mh_split(U, psi, N, d)
            Pn = (np.abs(psin.reshape(N, d)) ** 2).sum(1)
            tot += 1
            Dim = K.imag - K.imag.T
            if np.abs(Dim).max() > 1e-10:
                n_im += 1
            worst_im = max(worst_im, float(np.abs(Dim).max()))
            T, ex = rule_from_flow(piMH - piMH.T, P)
            worst_ex = max(worst_ex, ex)
            if ex > 1e-12:
                n_viol += 1
                if len(examples) < 2:
                    examples.append((ex, np.round(P, 4), np.round(Pn, 4)))
            ok, _, _ = lp_coupling(P, Pn, allowed, 'zero')
            n_lp += (not ok)
    print(f"4-cycle, d={d}: ticks={tot}, max forbidden element = {worst_band:.1e}")
    print(f"   ticks with non-zero lambda flow (Im K - Im K^T) : {n_im}  (max {worst_im:.3e})")
    print(f"   ticks where minimal MH rule breaks outflow bound: {n_viol}  (largest excess {worst_ex:.3e})")
    print(f"   ticks with no nearest-neighbour coupling (LP)   : {n_lp}")
    for e in examples:
        print(f"      example: excess {e[0]:.3e}, P_t = {e[1]}, P_t+1 = {e[2]}")

# ---- repair on the plaquette: keep the MH flow's shape, clip its loop circulation ----
from common import lp_circulation_range


def repaired(P, Pn, J):
    F0 = np.cumsum(P - Pn)            # flow across bond (x, x+1) with zero offset on bond (3,0)
    F0 = F0 - F0[N - 1]
    c_mh = J[N - 1, 0] - F0[N - 1]
    lo, hi = lp_circulation_range(P, Pn, allowed, N - 1, 0)
    c = min(max(c_mh, lo), hi)
    Jr = np.zeros((N, N))
    for x in range(N):
        Jr[x, (x + 1) % N] = F0[x] + c
        Jr[(x + 1) % N, x] = -(F0[x] + c)
    T, ex = rule_from_flow(Jr, P)
    return T, ex, c_mh, lo, hi


rng = np.random.default_rng(3)
cnt, worst_ex_r, worst_eq_r, dist = 0, -1.0, 0.0, []
for rep in range(60):
    U, band = banded_unitary(1)
    if band > 1e-10:
        continue
    for k in range(10):
        psi = rand_state(N, rng) if k % 2 == 0 else np.eye(N)[rng.integers(N)].astype(complex)
        P = np.abs(psi) ** 2
        piMH, K, psin = mh_split(U, psi, N, 1)
        Pn = np.abs(psin) ** 2
        J = piMH - piMH.T
        T, ex = rule_from_flow(J, P)
        if ex > 1e-12:
            Tr, exr, c_mh, lo, hi = repaired(P, Pn, J)
            cnt += 1
            worst_ex_r = max(worst_ex_r, exr)
            worst_eq_r = max(worst_eq_r, float(np.abs(P @ Tr - Pn).max()))
            dist.append(min(abs(c_mh - lo), abs(c_mh - hi)))
print(f"plaquette repair (d=1): {cnt} infeasible ticks repaired; max outflow excess after repair = "
      f"{worst_ex_r:.2e}; max|P_t T - P_t+1| = {worst_eq_r:.2e}; "
      f"MH circulation outside feasible interval by up to {max(dist):.3e}")
