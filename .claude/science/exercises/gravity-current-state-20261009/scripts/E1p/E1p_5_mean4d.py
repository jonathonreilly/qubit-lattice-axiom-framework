"""E1' (a): exact finite-density mean of the 4D Johnston path sum, rho = 1.
Johnston arXiv:0806.3083 eq.(3.15) (exact: consecutive link intervals are disjoint, so path probabilities factorize):
    Kbar(tau) = a P1(tau) + a b rho (P1 * Kbar)(tau),   P1(tau) = exp(-pi tau^4/24),  b = -m^2.
Invariant convolution in 4D (rest frame of x - y, w = (t, r)):
    (F*G)(tau) = int d^4w F(tau_xw) G(tau_wy) = int int dsigma1 dsigma2 (pi r/tau) F(sqrt s2) G(sqrt s1),
    t = (tau^2 + s1 - s2)/(2 tau), r = sqrt(t^2 - s1);  region sqrt s1 + sqrt s2 <= tau.
Solved by marching in tau (Volterra). Outputs Kbar vs continuum Gm = -(m/(4 pi tau)) J1(m tau) (timelike part).
Also: exact E L^2(tau) = (P1*P1)(tau) -> 3 pi.
"""
import numpy as np
from scipy.special import j1
import sys

A = 1.0 / (2 * np.pi * np.sqrt(6))
xg, wg = np.polynomial.legendre.leggauss(80)
S2 = 5.0 * (xg + 1); WS2 = 5.0 * wg           # sigma2 in [0,10]
P1s2 = np.exp(-np.pi * S2**2 / 24)
xa, wa = np.polynomial.legendre.leggauss(48)
xb, wb = np.polynomial.legendre.leggauss(160)


def conv_nodes(tau):
    """nodes (tau1 values, weights incl. jacobian pi r/tau * 2 tau1 * w_s2 * P1(s2)) for (P1 * G)(tau)."""
    T1 = []; W = []
    for s2, ws, p in zip(S2, WS2, P1s2):
        top = tau - np.sqrt(s2)
        if top <= 0:
            continue
        # split [0, min(6,top)] and [min(6,top), top]; second piece with v-substitution tau1 = top - (top-c) v^2
        c = min(6.0, top)
        t1a = 0.5 * c * (xa + 1); wa_ = 0.5 * c * wa
        pieces = [(t1a, wa_)]
        if top > c:
            v = 0.5 * (xb + 1); wv = 0.5 * wb
            t1b = top - (top - c) * v**2
            wb_ = 2 * (top - c) * v * wv
            pieces.append((t1b, wb_))
        for t1, w1 in pieces:
            tt = (tau**2 + t1**2 - s2) / (2 * tau)
            r = np.sqrt(np.maximum(tt * tt - t1 * t1, 0))
            T1.append(t1); W.append(w1 * (np.pi * r / tau) * 2 * t1 * ws * p)
    if not T1:
        return np.zeros(0), np.zeros(0)
    return np.concatenate(T1), np.concatenate(W)


def solve_mean(m, taumax, h_fine=0.02, h=0.05):
    taus = np.unique(np.concatenate([np.arange(0, 8, h_fine), np.arange(8, taumax + h, h)]))
    K = np.zeros_like(taus)
    b = -m * m
    for i, tau in enumerate(taus):
        if tau == 0:
            K[i] = A
            continue
        t1, w = conv_nodes(tau)
        Kint = np.interp(t1, taus[:i], K[:i]) if i > 0 else 0 * t1
        K[i] = A * np.exp(-np.pi * tau**4 / 24) + A * b * np.sum(w * Kint)
    return taus, K


if __name__ == "__main__":
    # E L^2 check
    for tau in [4, 8, 12, 17, 23, 40]:
        t1, w = conv_nodes(tau)
        print(f"E L^2(tau={tau}) = {np.sum(w*np.exp(-np.pi*t1**4/24)):.4f}   (3 pi = {3*np.pi:.4f})")
    res = {}
    for ml, mtmax in [(0.05, 20), (0.1, 20), (0.2, 16), (0.4, 14), (0.7, 14)]:
        taus, K = solve_mean(ml, mtmax / ml, h=0.05 if ml >= 0.1 else 0.1)
        np.savez(f"../out/mean4d_ml{ml}.npz", taus=taus, K=K, m=ml)
        g = -(ml / (4 * np.pi * np.maximum(taus, 1e-9))) * j1(ml * taus)
        env = (ml / (4 * np.pi * np.maximum(taus, 1e-9))) * np.sqrt(2 / (np.pi * np.maximum(ml * taus, 1e-9)))
        print(f"\nm*ell = {ml}:  m tau | Kbar | continuum Gm | (Kbar - Gm)/envelope")
        for mt in [0.5, 1, 2, 3, 5, 7, 10, 13, 16, 20]:
            if mt > mtmax: continue
            i = np.argmin(np.abs(ml * taus - mt))
            e = env[i] if mt >= 2 else abs(g[i])
            print(f"   {ml*taus[i]:6.2f}  {K[i]: .4e}  {g[i]: .4e}   {(K[i]-g[i])/e: .4f}")
        # max deviation beyond m tau = 2
        sel = ml * taus > 2
        print(f"   max |Kbar - Gm|/envelope for m tau in [2, {mtmax}]: {np.max(np.abs(K[sel]-g[sel])/env[sel]):.4f}")
