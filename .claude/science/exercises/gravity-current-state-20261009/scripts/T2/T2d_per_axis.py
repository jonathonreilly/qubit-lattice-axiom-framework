#!/usr/bin/env python3
"""T2d: family D = per-axis sums  D = m^2 + sum_mu h(s_mu),  h complete Bernstein (h(2-2z) in Lemma N's class).

Coupling to g, treated identically on every axis ("frame coupling"):
  s_0 = 2 - 2 cos q0;   s_a = (g^{-1/2} V g^{-1/2})_aa, a = 1..3,  V = R2's nn carrier matrix (V_ii = 2-2cos k_i,
  V_ij = sin k_i sin k_j), g^{1/2} the symmetric root (hypercubic-equivariant).  i.e. h of the squared proper lattice
  gradient along each orthonormal-frame axis.
  At g = 1: sum_mu h(2 - 2cos q_mu) (pure per-axis).  IR: sum_a h'(0) (g^{-1/2} k)_a^2 = k^T g^-1 k (covariant).
  RP: s_0 does not involve g, so D is h(s_0) + const at fixed spatial k: Lemma N class for every g (EXACT).
The literal alternative "each axis hop weighted by its own proper length n*sqrt(g_mumu)" has dD/deps = 0 identically
  for X_T (g_11, g_22 move only at O(eps^2)): the field cannot see g_12 at first order -> not a metric coupling (EXACT);
  it is excluded rather than scanned.
"""
import numpy as np
from t2_core import CHANNELS, V_matrix, spatial_mesh, kappa_from_slices, fit_power


def make_gen(L, X, a, r, m2=0.0):
    k1, k2, k3 = spatial_mesh(L)
    V = np.array(V_matrix(k1, k2, k3), dtype=object)
    Vm = np.empty((3, 3) + k1.shape)
    for i in range(3):
        for j in range(3):
            Vm[i, j] = V[i][j]
    XV = np.einsum("ij,jk...->ik...", X, Vm)
    XVX = np.einsum("ik...,kl->il...", XV, X)
    X2V = np.einsum("ij,jk...->ik...", X @ X, Vm)
    s = [Vm[i, i] for i in range(3)]
    s1 = [-XV[i, i] for i in range(3)]
    s2 = [0.5 * (X2V[i, i] + XVX[i, i]) for i in range(3)]

    def h(x):
        H = 0 * x; H1 = 0 * x; H2 = 0 * x
        for ak, rk in zip(a, r):
            den = 1 + rk * x
            H = H + ak * x / den; H1 = H1 + ak / den ** 2; H2 = H2 - 2 * ak * rk / den ** 3
        return H, H1, H2

    hs = [h(si) for si in s]
    Dsp = sum(x[0] for x in hs)
    D1 = sum(hs[i][1] * s1[i] for i in range(3))
    D2 = sum(hs[i][2] * s1[i] ** 2 + hs[i][1] * s2[i] for i in range(3))

    def gen(q0):
        H0, _, _ = h(np.array(2 - 2 * np.cos(q0)))
        return m2 + H0 + Dsp, D1, D2
    return gen


if __name__ == "__main__":
    print("== T2d: per-axis single pole h(s) = s/(1 + r s), frame coupling; m = 0 ==")
    print(" sigma_N    r       L    kappa_E        kappa_T")
    rows = []
    for sN in (1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0):
        r = (sN ** 2 - 1 / 3) / 4
        for L in (32, 48, 64):
            kE = kappa_from_slices(make_gen(L, CHANNELS["E_g"], [1.0], [r]), L)
            kT = kappa_from_slices(make_gen(L, CHANNELS["T_2g"], [1.0], [r]), L)
            print(f" {sN:5.1f}  {r:8.4f}  {L:3d}  {kE:+.4e}  {kT:+.4e}")
        rows.append((sN, kE, kT))
    rows = np.array(rows); sel = rows[:, 0] >= 3
    for j, name in ((1, "E_g"), (2, "T_2g")):
        p, c = fit_power(rows[sel, 0], rows[sel, j])
        print(f" fit sigma_N >= 3, {name}: |kappa| ~ {c:.4f} sigma_N^{-p:+.3f}  (negative exponent = growth)")
    print("\n-- two-pole per-axis at sigma_N = 4, L = 48 (random) --")
    rng = np.random.default_rng(3)
    mu1 = (16 - 1 / 3) / 4
    best = np.inf
    for _ in range(20):
        a = rng.dirichlet(np.ones(2)); rr = 10 ** rng.uniform(-2, 2, 2); rr = rr * mu1 / (a * rr).sum()
        kE = kappa_from_slices(make_gen(48, CHANNELS["E_g"], a, rr), 48)
        kT = kappa_from_slices(make_gen(48, CHANNELS["T_2g"], a, rr), 48)
        best = min(best, max(abs(kE), abs(kT)))
    print(f" best two-pole max(|kE|,|kT|) = {best:.4e}  vs single pole {max(abs(rows[4,1]),abs(rows[4,2])):.4e}")
