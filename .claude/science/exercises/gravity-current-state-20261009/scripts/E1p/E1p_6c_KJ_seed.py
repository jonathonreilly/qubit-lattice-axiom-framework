"""E1' (c): smeared-source field psi = (G_m J)(top) at a single element: simulated variance vs first-order law.
Source: Euclidean Gaussian, width w = 1.5 ell, centre (tc = 4.5, 0) (compact-ish: m w <= 0.8 here). Charge Q = int_diamond J.
Predicted variance (pair-of-paths expansion, first order, point-source approximation for the x-end):
   Var ~ Var_2L(m)  +  c_end * Q^2 a^2 b^2 (P1 * Kbar_{>=2}^2)(tau_eff),   tau_eff = T - tc,  c_end in [1, 2]
   Var_2L(m) = smeared two-link term, measured at the smallest m and scaled as m^4 (it is O(b) in amplitude).
"""
import glob
import numpy as np
from scipy import integrate
from E1p_6_renewal4d import march, conv, P1, A


def Q_trunc(T, w, tc):
    f = lambda r, t: 4 * np.pi * r * r * np.exp(-((t - tc)**2 + r * r) / (2 * w * w))
    val, _ = integrate.dblquad(f, 0, T, lambda t: 0, lambda t: min(t, T - t))
    return val


for f in sorted(glob.glob("../out/massive4d_T*_s*.npz"), key=lambda s: float(s.split("_T")[1].split("_")[0])):
    d = np.load(f)
    T = float(d["T"])
    if T < 14:
        continue
    mT = d["mT"]; KJ = d["KJt"]; w = float(d["w"]); tc = float(d["tc"]); n = KJ.shape[0]
    Q = Q_trunc(T, w, tc)
    te = T - tc
    k0 = 1  # smallest nonzero m
    m0 = mT[k0] / T
    r2abs0 = KJ[:, k0].var(ddof=1)
    print(f"\n=== T={T:.0f}, n={n}, Q={Q:.1f}, tau_eff={te:.1f}; smeared two-link rel noise at m tau={mT[k0]}: "
          f"{np.sqrt(r2abs0)/abs(KJ[:,k0].mean()):.4f}")
    print("   mT    m*ell  m*tau_eff | sd_sim/|mean_sim| | Var_sim | Var_2L(scaled) | +1 x-end seed | +2 end seeds | Var_sim/(2L+1 end)")
    for k in range(1, len(mT)):
        m = mT[k] / T
        if m * T > 12:
            continue
        b = -m * m
        taus = np.unique(np.concatenate([np.linspace(0, 6, 121), np.linspace(6, te, int(4 * te) + 1)]))
        K = march(taus, lambda t: A * P1(t), A * b, P1)
        K2 = K - A * P1(taus)
        seed = Q * Q * A * A * b * b * conv(te, P1, lambda t: np.interp(t, taus, K2)**2)
        v2l = r2abs0 * (m / m0)**4
        vs = KJ[:, k].var(ddof=1); mu = KJ[:, k].mean()
        print(f"  {mT[k]:5.2f} {m:6.3f}   {m*te:6.2f}   |   {np.sqrt(vs)/abs(mu):8.3f}        | {vs:.3e} | {v2l:.3e}      | {v2l+seed:.3e}     | {v2l+2*seed:.3e}    | {vs/(v2l+seed):6.3f}")
