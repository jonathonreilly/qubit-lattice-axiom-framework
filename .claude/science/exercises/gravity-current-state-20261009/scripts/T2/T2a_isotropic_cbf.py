#!/usr/bin/env python3
"""T2a: family A = complete-Bernstein function of the metric-coupled nn Laplacian (R2 Route 3 'ratl', generalized).

  S_G(q) = 2(1-cos q0) + sum_ij (g^-1)_ij V_ij(k)      (R2 C1 nn_form, time axis identical to space at G=1)
  D_G(q) = m^2 + F(S_G),  F(S) = beta S + sum_k a_k S/(1 + r_k S),  a_k, r_k, beta >= 0,  beta + sum a_k = 1.
RP: S_G is affine in z0 = cos q0 with slope -2, and F is a CBF, so -D is Nevanlinna in z0 with poles at t > 1
for every spatial momentum and every g (EXACT; see T2e for the Hankel checks). Hypercubic at g = 1.
Width (Lemma N): sigma_N^2 = -4 c4/c2 along an axis = 1/3 + 4 sum a_k r_k (beta = 0).
Prediction (asymptotic, m = 0): kappa ~ -(T/2) W'',  T = (sum a/r^2)/(sum a/r),  W = <1/S_G> (4D Watson integral).
Log-convexity of the moments of {a_k} gives T * sum a r >= 1, equality iff one pole:  min |kappa| ~ 2|W''|/(sigma_N^2 - 1/3).
"""
import numpy as np
from t2_core import CHANNELS, V_matrix, contract, spatial_mesh, kappa_from_slices, fit_power

rng = np.random.default_rng(20261009)


def make_gen(L, X, a, r, beta=0.0, m2=0.0, want_watson=False):
    k1, k2, k3 = spatial_mesh(L)
    V = V_matrix(k1, k2, k3)
    Ssp = V[0][0] + V[1][1] + V[2][2]
    S1 = -contract(X, V)
    S2 = contract(X @ X, V)
    a = np.asarray(a, float); r = np.asarray(r, float)

    def gen(q0):
        S = 2 - 2 * np.cos(q0) + Ssp
        if want_watson:  # D := S, but we want <-S''/S^2 + 2 S'^2/S^3> = d^2 <1/S>; return in kappa form
            return S, S1, S2
        F = beta * S; F1 = beta + 0 * S; F2 = 0 * S
        for ak, rk in zip(a, r):
            den = 1 + rk * S
            F = F + ak * S / den
            F1 = F1 + ak / den ** 2
            F2 = F2 - 2 * ak * rk / den ** 3
        D = m2 + F
        return D, F1 * S1, F2 * S1 ** 2 + F1 * S2
    return gen


def watson_dd(L, X):
    k1, k2, k3 = spatial_mesh(L)
    V = V_matrix(k1, k2, k3)
    Ssp = V[0][0] + V[1][1] + V[2][2]
    S1 = -contract(X, V); S2 = contract(X @ X, V)
    acc = 0.0
    from t2_core import midgrid
    for q0 in midgrid(L):
        S = 2 - 2 * np.cos(q0) + Ssp
        acc += np.sum(-S2 / S ** 2 + 2 * S1 ** 2 / S ** 3)
    return acc / L ** 4


def kappa(L, X, a, r, beta=0.0, m2=0.0):
    return kappa_from_slices(make_gen(L, X, a, r, beta, m2), L)


if __name__ == "__main__":
    print("== T2a: F(S_G), F complete Bernstein; m = 0 unless stated ==")
    # Watson-integral curvature (the predicted coefficient), with grid convergence
    Wpp = {}
    for L in (32, 48, 64):
        Wpp[L] = {ch: watson_dd(L, X) for ch, X in CHANNELS.items()}
        print(f"L={L}: W''_E = {Wpp[L]['E_g']:+.6f}   W''_T = {Wpp[L]['T_2g']:+.6f}   (W = <1/S_G>, 4D nn Watson)")
    W = Wpp[64]

    print("\n-- single pole F = S/(1 + r S): kappa vs sigma_N (grid L = 32/48/64) --")
    print(" sigma_N    r       L   kappa_E        kappa_T        pred_E=-W''_E/(2r)  pred_T")
    rows = []
    for sN in (1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0):
        r = (sN ** 2 - 1 / 3) / 4
        for L in (32, 48, 64):
            kE = kappa(L, CHANNELS["E_g"], [1.0], [r])
            kT = kappa(L, CHANNELS["T_2g"], [1.0], [r])
            print(f" {sN:5.1f}  {r:8.4f}  {L:3d}  {kE:+.4e}  {kT:+.4e}   {-W['E_g']/(2*r):+.4e}  {-W['T_2g']/(2*r):+.4e}")
        rows.append((sN, r, kE, kT))
    sN = np.array([x[0] for x in rows]); kE = np.array([x[2] for x in rows]); kT = np.array([x[3] for x in rows])
    sel = sN >= 3
    for name, kk in (("E_g", kE), ("T_2g", kT)):
        p, c = fit_power(sN[sel], kk[sel])
        print(f" fit sigma_N>=3, {name}: |kappa| ~ {c:.4f} * sigma_N^-{p:.3f}")

    print("\n-- massive check m = 0.2 (single pole), L = 64 --")
    for sN in (2.0, 4.0, 8.0):
        r = (sN ** 2 - 1 / 3) / 4
        kE = kappa(64, CHANNELS["E_g"], [1.0], [r], m2=0.04)
        kT = kappa(64, CHANNELS["T_2g"], [1.0], [r], m2=0.04)
        print(f" sigma_N={sN:4.1f}: kappa_E={kE:+.4e} kappa_T={kT:+.4e}")

    print("\n-- multi-pole search at fixed sigma_N (2-4 poles, random a_k, r_k spread over 4 decades), L = 48 --")
    print(" sigma_N  n_samples  single-pole max|k|   best multi max(|kE|,|kT|)   ratio   min|kE| alone   min|kT| alone")
    for sN in (2.0, 4.0, 8.0):
        mu1 = (sN ** 2 - 1 / 3) / 4
        k1E = kappa(48, CHANNELS["E_g"], [1.0], [mu1]); k1T = kappa(48, CHANNELS["T_2g"], [1.0], [mu1])
        best = np.inf; bestE = np.inf; bestT = np.inf
        n = 60
        for _ in range(n):
            K = rng.integers(2, 5)
            a = rng.dirichlet(np.ones(K))
            r = 10 ** rng.uniform(-2, 2, size=K)
            r = r * mu1 / (a * r).sum()
            kE = kappa(48, CHANNELS["E_g"], a, r); kT = kappa(48, CHANNELS["T_2g"], a, r)
            best = min(best, max(abs(kE), abs(kT))); bestE = min(bestE, abs(kE)); bestT = min(bestT, abs(kT))
        one = max(abs(k1E), abs(k1T))
        print(f" {sN:5.1f}   {n:5d}      {one:.4e}            {best:.4e}            {best/one:6.3f}   {bestE:.3e}      {bestT:.3e}")

    print("\n-- adding the linear (b) term beta at sigma_N = 4 (pole part keeps sum a r fixed), L = 48 --")
    mu1 = (16 - 1 / 3) / 4
    for beta in (0.0, 1e-3, 1e-2, 1e-1):
        kE = kappa(48, CHANNELS["E_g"], [1 - beta], [mu1 / (1 - beta)], beta=beta)
        kT = kappa(48, CHANNELS["T_2g"], [1 - beta], [mu1 / (1 - beta)], beta=beta)
        print(f" beta={beta:6.0e}: kappa_E={kE:+.4e} kappa_T={kT:+.4e}")
