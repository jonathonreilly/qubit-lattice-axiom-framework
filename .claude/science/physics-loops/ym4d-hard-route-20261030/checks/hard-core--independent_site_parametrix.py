#!/usr/bin/env python3
"""Three checks for the repairs of `gates/independent-3s-codex-98dd68c8f.md` in Text 4.5k, 4.7. Algebra and logic only, on a chain.

Part A, gate D3: the parametrix in the site algebra, Step 5 of Lemma 4.5k. S[s] = S_0 + sum_i s_i Delta_i + D[s], s_i in {0, 1}, D[s] of degree >= 2 in s.
G[s] := G_0 + sum_i s_i (G_i - G_0), G_i := (S_0 + Delta_i)^(-1). The claim is the identity
    S[s] G[s] = 1 + sum_{i != j} s_i s_j Delta_i (G_j - G_0) + D[s] G[s],
and that the mixed coefficients of S[s]^(-1) over ALL subsets Xi of sites sum, with the weight exp(sigma tau(l, l'; Xi)), to at most twice the same norm of G[s].
Part B, gate D4: the sum over a mixed row, (ROW-SUM). With P R = 1 on X, x = xi + s_tot on K_2, s_tot = 2^(1/2) R (b* / g + G xi').
Part C, gate D4: supports on a chain. Old link -> label -> link -> W. The radius R_P + rho_P / L + 1 of (R2) covers the chain, and R_P alone does not.

PRE-STATED CRITERIA, written before the first run.
PASS-IDENT: the identity of Part A holds to 1e-10 at all s in {0,1}^n, for random dense S_0, Delta_i, D, n = 6.
PASS-NORM: on a chain of N sites with 5 sites of the family at spacing Ls, exponentially local S_0 (rate about 1), Delta_i local to site i at the same rate, a term D at |Xi| = 2 of
  size e^(-Ls / 2): the weighted norm of the exact S[s]^(-1), read from its Mobius coefficients over all 2^5 subsets, is at most 2 |||G[s]|||, for Ls = 12 and 24, sigma = 0.25.
FAIL-EXPECTED: the control, the same norm at sigma = 1.5, above the rate, exceeds 2 |||G[s]||| at Ls = 12. If it does not, the test cannot see the weight, and PASS-NORM is VOID.
PASS-ROWSUM: (ROW-SUM) holds to 1e-10 at random complex data, for a row holding labels of both kinds, with P_l frozen.
FAIL-ROWSUM-CONTROL: with P_l not frozen on the row, the same formula has residual above 1e-3: the freezing is what it reads.
PASS-SUPPORT: for all old links and all labels and links of Part C, the W read lies in the (R2) neighbourhood at radius R_P + rho + 1.
FAIL-SUPPORT-CONTROL: at radius R_P some W read lies outside: this is the gate's composition of three supports. These two are a count of supports, not of coefficients.

RESULT OF THE FIRST RUN: PASS-IDENT (3.6e-15), PASS-ROWSUM (1.3e-15), FAIL-ROWSUM-CONTROL as expected (0.10), PASS-SUPPORT and FAIL-SUPPORT-CONTROL as expected (furthest W at 14 = R_P + rho + 1, with R_P = 10).
PASS-NORM was VOID, as registered, since FAIL-EXPECTED did not fail, by two errors of mine: the chain was periodic while tau is an interval, so l, l' close across the wrap got a weight exp(sigma N); and the empty coefficient
G_0 dominates both norms, so they cannot separate at any sigma.
CRITERIA OF THE SECOND RUN, written after that and before the second run. Open chain. M2 := the weighted norm restricted to |Xi| >= 2, which is what the separation has to pay; M_G := the norm of G[s] at the same sigma.
PASS-NORM2: at sigma = 0.25 (rate about 1), M2(Ls = 24) <= M2(Ls = 12) / 10 and M2(Ls = 12) <= M_G(Ls = 12) / 2.
FAIL-EXPECTED2: at sigma = 1.5, above the rate, M2(24) >= M2(12): no decay in the separation. If it does decay, PASS-NORM2 is VOID.

RESULT OF THE SECOND RUN: PASS-NORM2 FAILED as registered, M2(12) = 1.1e-6, M2(24) = 3.39, with M_G = 1.04; FAIL-EXPECTED2 as expected. The size suggests roundoff and not the claim: at Ls = 24, N = 168, a Mobius coefficient has noise of about 1e-16 and the
weight is up to exp(0.25 * 168) = 1.7e18. That is a guess until tested, so:
CRITERIA OF THE THIRD RUN, written after that and before the third run. The same criteria, PASS-NORM2 and FAIL-EXPECTED2, with arithmetic at 100 decimal digits (mpmath), 4 sites, Ls = 8 and Ls = 16, so that noise times weight is below 1e-60. If PASS-NORM2 still fails, the
claim that the separation pays for |Xi| >= 2 is false on this chain, and Step 5 has to change.
RESULT OF THE THIRD RUN: PASS-NORM2 (M2 = 6.2e-5 at Ls = 8, 2.0e-8 at Ls = 16, with M_G = 1.04), FAIL-EXPECTED2 as expected (at sigma = 1.5, 5.0e5 and 5.9e11). So the second run was roundoff. It tests the algebra of the parametrix and the sum over sets of sites, on a chain.
"""
import itertools
import os
import resource
import sys

os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import mpmath as mp
import numpy as np

mp.mp.dps = 100

rng = np.random.default_rng(20261101)
results = {}


def check_rss():
    """The script checks its own RSS against 2 GB (macOS has no usable RLIMIT_AS)."""
    rss_gb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3
    if rss_gb > 2.0:
        sys.exit(f"ABORT: RSS {rss_gb:.2f} GB above 2 GB")


def part_a_identity(n_mat=30, n_sites=6):
    S0 = np.eye(n_mat) * 3 + rng.normal(size=(n_mat, n_mat)) * 0.1
    Delta = [rng.normal(size=(n_mat, n_mat)) * 0.1 for _ in range(n_sites)]
    D = {}
    for i, j in itertools.combinations(range(n_sites), 2):
        D[(i, j)] = rng.normal(size=(n_mat, n_mat)) * 0.01
    G0 = np.linalg.inv(S0)
    Gi = [np.linalg.inv(S0 + Delta[i]) for i in range(n_sites)]
    worst = 0.0
    for s in itertools.product((0, 1), repeat=n_sites):
        S = S0 + sum(s[i] * Delta[i] for i in range(n_sites)) + sum(s[i] * s[j] * D[(i, j)] for (i, j) in D)
        Dsum = sum(s[i] * s[j] * D[(i, j)] for (i, j) in D)
        G = G0 + sum(s[i] * (Gi[i] - G0) for i in range(n_sites))
        rhs = np.eye(n_mat) + Dsum @ G
        for i in range(n_sites):
            for j in range(n_sites):
                if i != j:
                    rhs = rhs + s[i] * s[j] * Delta[i] @ (Gi[j] - G0)
        worst = max(worst, np.abs(S @ G - rhs).max())
    results["ident_residual"] = worst
    results["PASS-IDENT"] = worst < 1e-10


def chain_setup(N, sites, Ls, rate=1.0):
    d = np.abs(np.arange(N)[:, None] - np.arange(N)[None, :])
    S0 = np.eye(N) * 1.5 + 0.3 * np.exp(-rate * d) * (d > 0)
    Delta = []
    for x0 in sites:
        dx = np.abs(np.arange(N) - x0)
        env = np.exp(-rate * dx)
        Delta.append(0.4 * np.outer(env, env) * np.exp(-rate * d))
    D = {}
    for i, j in itertools.combinations(range(len(sites)), 2):
        di = np.abs(np.arange(N) - sites[i])
        dj = np.abs(np.arange(N) - sites[j])
        D[(i, j)] = 0.2 * np.exp(-Ls / 2) * np.outer(np.exp(-rate * di), np.exp(-rate * dj)) * np.exp(-rate * d)
    return d, S0, Delta, D


def tau(l, lp, xi, sites, N):
    """Length of the least interval of the open chain holding l, l' and the sites of xi."""
    pts = [l, lp] + [sites[i] for i in xi]
    return max(pts) - min(pts)


def weighted_norm(coef, sites, N, sigma):
    """sup_l sum_{l', Xi} |coef[Xi](l, l')| exp(sigma tau(l, l'; Xi)), both rows and columns."""
    best = mp.mpf(0)
    for use_cols in (False, True):
        for l in range(N):
            tot = mp.mpf(0)
            for xi, K in coef.items():
                row = K[:, l] if use_cols else K[l, :]
                for lp in range(N):
                    tot += abs(row[lp]) * mp.exp(sigma * tau(l, lp, xi, sites, N))
            best = max(best, tot)
    return best


def mobius(fn, n_sites):
    """Coefficients of a function on {0,1}^n in the monomials s^Xi."""
    vals = {}
    for xi_size in range(n_sites + 1):
        for xi in itertools.combinations(range(n_sites), xi_size):
            s = [1 if i in xi else 0 for i in range(n_sites)]
            vals[xi] = fn(s)
    coef = {}
    for xi in vals:
        total = 0.0
        for k in range(len(xi) + 1):
            for sub in itertools.combinations(xi, k):
                total = total + (-1) ** (len(xi) - k) * vals[sub]
        coef[xi] = total
    return coef


def mp_inverse(A):
    return np.array(mp.inverse(mp.matrix(A.tolist())).tolist(), dtype=object)


def part_a_norm(Ls, sigma, n_sites=4):
    N = Ls * n_sites + 2 * Ls
    sites = [Ls + i * Ls for i in range(n_sites)]
    d, S0, Delta, D = chain_setup(N, sites, Ls)
    to_mp = np.vectorize(mp.mpf, otypes=[object])
    S0, Delta, D = to_mp(S0), [to_mp(x) for x in Delta], {k: to_mp(v) for k, v in D.items()}
    G0 = mp_inverse(S0)
    Gi = [mp_inverse(S0 + Delta[i]) for i in range(n_sites)]

    def Sinv(s):
        S = S0.copy()
        for i in range(n_sites):
            if s[i]:
                S = S + Delta[i]
        for (i, j) in D:
            if s[i] and s[j]:
                S = S + D[(i, j)]
        return mp_inverse(S)

    coef_exact = mobius(Sinv, n_sites)
    coef_G = {(): G0}
    for i in range(n_sites):
        coef_G[(i,)] = Gi[i] - G0
    high = {xi: K for xi, K in coef_exact.items() if len(xi) >= 2}
    return weighted_norm(high, sites, N, sigma), weighted_norm(coef_G, sites, N, sigma)


def part_b_rowsum():
    """(ROW-SUM). X = the range of P, R a right inverse; all data complex, all of it arbitrary except that P R = 1 on X and b*, B' are in X."""
    n_x, n_lab = 12, 18
    P = rng.normal(size=(n_x, n_lab))
    R = np.linalg.pinv(P)
    assert np.abs(P @ R - np.eye(n_x)).max() < 1e-12
    g = 0.01
    K1 = [0, 1, 2]
    K2 = list(range(3, n_lab))
    def data():
        b = rng.normal(size=n_x) + 1j * rng.normal(size=n_x)
        Bp = g * (rng.normal(size=n_x) + 1j * rng.normal(size=n_x))
        return b, Bp, 2 ** 0.5 * R @ (b / g + Bp / g)
    b0, Bp0, s0 = data()
    b0, Bp0 = b0.real, Bp0.real
    s0 = 2 ** 0.5 * R @ (b0 / g + Bp0 / g)
    bw, Bpw, sw = data()
    xi = rng.normal(size=n_lab)
    h = np.zeros(n_lab, dtype=complex)
    h[K1] = 1e-2 * (rng.normal(size=3) + 1j * rng.normal(size=3))
    # K_1 labels hold real x_i (plus a height h_i); K_2 labels hold xi_j + s_tot,j(w).
    x_real = np.zeros(n_lab, dtype=complex)
    x_real[K1] = rng.normal(size=3)
    def b_of(s_tot, Pl, Pl_row=None):
        x = np.zeros(n_lab, dtype=complex)
        x[K1] = x_real[K1]
        x[K2] = xi[K2] + s_tot[K2]
        return x
    l = 4
    Pl = P[l, :]
    x_w = b_of(sw, Pl)
    x_w[K1] += h[K1]
    x_0 = b_of(s0, Pl)
    Delta_b_direct = (g / 2 ** 0.5) * Pl @ (x_w - x_0)
    Delta_s = sw - s0
    Delta_b_formula = (bw[l] - b0[l]) + (Bpw[l] - Bp0[l]) + (g / 2 ** 0.5) * sum(Pl[i] * (h[i] - Delta_s[i]) for i in K1)
    res = abs(Delta_b_direct - Delta_b_formula)
    results["rowsum_residual"] = res
    results["PASS-ROWSUM"] = res < 1e-10
    # Control: the row at w is not the row at 0. The direct move then has an extra term from P_l(w) - P_l(0) on the K_1 labels, of size g |x_i| |Delta P|.
    Pl_w = Pl + 0.05 * rng.normal(size=n_lab)
    Delta_b_unfrozen = (g / 2 ** 0.5) * (Pl_w @ x_w - Pl @ x_0)
    res_c = abs(Delta_b_unfrozen - Delta_b_formula)
    results["rowsum_control_residual"] = res_c
    results["FAIL-ROWSUM-CONTROL"] = res_c > 1e-3


def part_c_support(L=9, rho_over_L=3, R_loc=4, n_len=120):
    """All positions in coarse units on a line. A level-k link is read through its coarse cell. Range of P: rho = rho_over_L coarse links; P_l reads W within R_loc + rho of l."""
    Rho = rho_over_L
    R_P = R_loc + 2 * Rho
    # Old near set: N_1(Z) = the coarse interval [50, 50] (one cell). The rough set is that image with a neighbourhood of radius r.
    z = 50
    worst_new = True
    worst_old = True
    furthest = 0
    for label in range(z - Rho - 1, z + Rho + 2):  # NV(Z): the labels the links of N_1(Z) read, with the fibre flow of one cell.
        for link in range(label - Rho, label + Rho + 1):  # every link whose row holds that label.
            for w in range(link - R_loc - Rho, link + R_loc + Rho + 1):  # what P_l, V^#_l read at fixed x.
                dist = abs(w - z)
                furthest = max(furthest, dist)
                if dist > R_P + Rho + 1:
                    worst_new = False
                if dist > R_P:
                    worst_old = False
    results["support_furthest"] = furthest
    results["R_P"] = R_P
    results["R_P_plus"] = R_P + Rho + 1
    results["PASS-SUPPORT"] = worst_new
    results["FAIL-SUPPORT-CONTROL"] = not worst_old


part_a_identity()
check_rss()
m2_12, mg_12 = part_a_norm(8, 0.25)
m2_24, mg_24 = part_a_norm(16, 0.25)
results["M2_Ls8"], results["M_G_Ls8"], results["M2_Ls16"], results["M_G_Ls16"] = float(m2_12), float(mg_12), float(m2_24), float(mg_24)
results["PASS-NORM2"] = bool((m2_24 <= m2_12 / 10) and (m2_12 <= mg_12 / 2))
check_rss()
m2c_12, _ = part_a_norm(8, 1.5)
m2c_24, _ = part_a_norm(16, 1.5)
results["M2_control_Ls8"], results["M2_control_Ls16"] = float(m2c_12), float(m2c_24)
results["FAIL-EXPECTED2"] = bool(m2c_24 >= m2c_12)
part_b_rowsum()
part_c_support()
for k, v in results.items():
    print(k, v)
print("rss_MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024)
sys.exit(0)
