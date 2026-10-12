"""Asymptotic growth rate of the 4D overlap-free variance renewal with the shared-link kernel:
   W = S + b^2 rho a^2 (P1 * W),  S = a^2 P1 + Kbar_{>=2}^2  (Kbar = exact finite-density mean, eq. 3.15).
Prediction (ARGUED): Var ~ exp(gamma tau), gamma = 0.2552 m^2 ell (from P1 -> sqrt6 delta(tau^2), light-cone measure).
Composite quadrature in tau1: [0,6] (48 GL), [6,60] (64 GL), [60,top] (n ~ 4 m top, sqrt-endpoint)."""
import numpy as np
A = 1.0 / (2 * np.pi * np.sqrt(6))
xg, wg = np.polynomial.legendre.leggauss(80); S2 = 5.0 * (xg + 1); WS2 = 5.0 * wg; P1s2 = np.exp(-np.pi * S2**2 / 24)
def gl(n):
    x, w = np.polynomial.legendre.leggauss(n); return 0.5 * (x + 1), 0.5 * w
def nodes(tau, m):
    T1 = []; W = []
    for s2, ws, p in zip(S2, WS2, P1s2):
        top = tau - np.sqrt(s2)
        if top <= 0: continue
        segs = []
        a = 0.0
        for c, n in [(6.0, 48), (60.0, 64)]:
            if top > a:
                bnd = min(c, top); v, wv = gl(n); segs.append((a + (bnd - a) * v, (bnd - a) * wv)); a = bnd
        if top > a:
            n = max(160, int(4 * m * (top - a)))
            v, wv = gl(n); segs.append((top - (top - a) * v**2, 2 * (top - a) * v * wv))
        for t1, w1 in segs:
            tt = (tau**2 + t1**2 - s2) / (2 * tau); r = np.sqrt(np.maximum(tt * tt - t1 * t1, 0))
            T1.append(t1); W.append(w1 * (np.pi * r / tau) * 2 * t1 * ws * p)
    if not T1: return np.zeros(0), np.zeros(0)
    return np.concatenate(T1), np.concatenate(W)
def run(m, taumax, h):
    taus = np.unique(np.concatenate([np.arange(0, 8, 0.02), np.arange(8, taumax + h, h)]))
    K = np.zeros_like(taus); Wv = np.zeros_like(taus); b = -m * m
    for i, tau in enumerate(taus):
        P1 = np.exp(-np.pi * tau**4 / 24)
        if i == 0: K[i] = A; Wv[i] = A * A; continue
        t1, w = nodes(tau, m)
        K[i] = A * P1 + A * b * np.sum(w * np.interp(t1, taus[:i], K[:i]))
        K2 = K[i] - A * P1
        Wv[i] = A * A * P1 + K2 * K2 + b * b * A * A * np.sum(w * np.interp(t1, taus[:i], Wv[:i]))
    return taus, K, Wv
for m, tmax, h in [(0.15, 1400.0, 0.5), (0.2, 800.0, 0.5)]:
    taus, K, W = run(m, tmax, h)
    V = W - K**2
    g = 0.2552 * m * m
    x = g * taus
    sel = taus > 0.6 * tmax
    p = np.polyfit(taus[sel], np.log(V[sel] * x[sel]**1.5), 1)
    print(f"m*ell={m}: fitted d ln(Var x^1.5)/d tau = {p[0]:.5f}; predicted 0.2552 m^2 ell = {g:.5f}; ratio {p[0]/g:.3f}; "
          f"gamma*tau_max = {g*tmax:.1f}; Var(tau_max)/Var(20) = {V[-1]/V[np.argmin(abs(taus-20))]:.3e}", flush=True)
    np.savez(f"../out/renewal_rate_m{m}.npz", taus=taus, K=K, W=W)
