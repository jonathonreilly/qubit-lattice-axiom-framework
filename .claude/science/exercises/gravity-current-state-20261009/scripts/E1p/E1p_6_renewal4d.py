"""E1' (c): 4D variance of the point-to-point Johnston path sum from the pair-of-paths (Mecke) expansion.

Pair-of-paths expansion (Mecke formula; EXACT up to one omission):
  E[K(x,y)^2] = sum_k (b^2 rho)^k int prod_i S(w_{i+1}, w_i),
  S(w',w) = a^2 P1(w',w) + Kbar_{>=2}(w',w)^2   [shared link counted once since L^2 = L; direct-vs-indirect impossible]
  Omitted: overlaps between intervals of distinct links of the two replicas (link-link correlations) -> ARGUED O(1) factors.
  => renewal  W = S + b^2 rho (S * W)   (overlap-free).
First-order pieces at (x,y):  two-link floor a^4 b^2 Var(L^2)  +  x-end and y-end seeds 2 a^2 b^2 (P1 * Kbar_{>=2}^2)(tau).
Kbar is the exact finite-density mean (Johnston eq. 3.15).
"""
import numpy as np, glob, sys
from scipy.special import j1

A = 1.0 / (2 * np.pi * np.sqrt(6))
gA = np.polynomial.legendre.leggauss(40)
gB = np.polynomial.legendre.leggauss(90)


def seg_nodes(lo, hi, g, endpoint_sqrt=False):
    x, w = g
    if hi <= lo:
        return np.zeros(0), np.zeros(0)
    if not endpoint_sqrt:
        return lo + 0.5 * (hi - lo) * (x + 1), 0.5 * (hi - lo) * w
    v = 0.5 * (x + 1); wv = 0.5 * w
    return hi - (hi - lo) * v**2, 2 * (hi - lo) * v * wv


def comp_nodes(top, cut=5.0, sqrt_end=True):
    """composite nodes on [0, top]: fine on [0, min(cut,top)], then [cut, top] (sqrt-endpoint substitution)."""
    c = min(cut, top)
    t1, w1 = seg_nodes(0.0, c, gA, endpoint_sqrt=(sqrt_end and top <= cut))
    t2, w2 = seg_nodes(c, top, gB, endpoint_sqrt=sqrt_end)
    return np.concatenate([t1, t2]), np.concatenate([w1, w2])


def conv(tau, F, G):
    """(F*G)(tau) = int d^4w F(tau_xw) G(tau_wy); F, G callables of proper time."""
    if tau <= 0:
        return 0.0
    tot = 0.0
    T2, W2 = comp_nodes(tau, sqrt_end=False)
    for t2, w2 in zip(T2, W2):
        top = tau - t2
        if top <= 0:
            continue
        T1, W1 = comp_nodes(top, sqrt_end=True)
        s1 = T1 * T1; s2 = t2 * t2
        tt = (tau**2 + s1 - s2) / (2 * tau)
        r = np.sqrt(np.maximum(tt * tt - s1, 0))
        tot += w2 * np.sum(W1 * (np.pi * r / tau) * 4 * T1 * t2 * F(t2) * G(T1))
    return tot


P1 = lambda t: np.exp(-np.pi * t**4 / 24)


def march(taus, rhs_fn, coef, kern):
    """solve X(tau) = rhs(tau) + coef * (kern * X)(tau) by marching (Volterra)."""
    X = np.zeros_like(taus)
    for i, tau in enumerate(taus):
        Xi = (lambda t, i=i: np.interp(t, taus[:i], X[:i]) if i > 0 else 0 * t)
        X[i] = rhs_fn(tau) + (coef * conv(tau, kern, Xi) if i > 0 else 0.0)
    return X


def analyse(T, m):
    taus = np.unique(np.concatenate([np.linspace(0, min(T, 6), 121), np.linspace(min(T, 6), T, int(4 * T) + 1)]))
    b = -m * m
    # exact mean: Kbar = a P1 + a b (P1 * Kbar)
    K = march(taus, lambda t: A * P1(t), A * b, P1)
    K2 = K - A * P1(taus)                       # Kbar_{>=2}
    Kf = lambda t: np.interp(t, taus, K2)
    S = lambda t: A * A * P1(t) + np.interp(t, taus, K2)**2
    seed = A * A * b * b * conv(T, P1, lambda t: Kf(t)**2)     # one end
    EL2 = conv(T, P1, P1)
    # renewal W = S + b^2 rho (S * W)
    W = march(taus, S, b * b, S)
    var_ren = W[-1] - K[-1]**2
    return dict(Kbar=K[-1], EL2=EL2, floor=A**4 * b * b * EL2, seed=seed, var_ren=var_ren)


if __name__ == "__main__":
    for f in sorted(glob.glob("../out/massive4d_T*_s*.npz"), key=lambda s: float(s.split("_T")[1].split("_")[0])):
        d = np.load(f)
        T = float(d["T"]); mT = d["mT"]; Kt = d["Kt"]; L2 = d["L2"]
        varL2 = L2.var(ddof=1)
        print(f"\n=== T = {T:.0f}, n = {len(L2)};  Var(L^2) sim = {varL2:.3f}")
        print("   mT   m*ell | Kbar_exact/<K>_sim | Var_sim | floor(simVarL2) | +2 seeds | renewal(overlap-free) | ratio sim/renewal | sd/envelope (sim)")
        for k in range(len(mT)):
            if mT[k] == 0 or mT[k] > 12:
                continue
            m = mT[k] / T
            r = analyse(T, m)
            vs = Kt[:, k].var(ddof=1); mu = Kt[:, k].mean()
            fl = A**4 * m**4 * varL2
            env = (m / (4 * np.pi * T)) * np.sqrt(2 / (np.pi * m * T)) if mT[k] >= 2 else abs((m / (4 * np.pi * T)) * j1(m * T))
            print(f"  {mT[k]:5.2f} {m:6.3f} |   {r['Kbar']/mu:7.3f}          | {vs:.3e} | {fl:.3e}       | {fl+2*r['seed']:.3e} | {r['var_ren']:.3e}"
                  f"            | {vs/r['var_ren']:6.3f}          | {np.sqrt(vs)/env:7.3f}", flush=True)
