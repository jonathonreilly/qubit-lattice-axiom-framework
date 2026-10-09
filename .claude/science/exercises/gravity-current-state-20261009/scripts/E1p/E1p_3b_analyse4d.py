"""Analyse E1' (c) 4D massive runs: means vs continuum, per-realization relative noise, two-link floor law.
Laws compared (rho = 1, a = 1/(2 pi sqrt6)):
  continuum point-to-point (timelike):  Gm(tau) = -(m/(4 pi tau)) J1(m tau)
  two-link term: a^2 b L^2(x,y);  E L^2 -> 3 pi (tau >> ell);  floor sd_L2 = a^2 m^2 sqrt(Var L^2)
  exact finite-tau E L^2(tau) = (pi/tau) int int r e^{-pi(s1^2+s2^2)/24} ds1 ds2   (Mecke + Jacobian)
"""
import glob, sys
import numpy as np
from scipy.special import j1
from scipy import integrate

A = 1.0 / (2 * np.pi * np.sqrt(6))


def EL2(tau, n=400):
    s = np.linspace(0, 12, n + 1); s = 0.5 * (s[1:] + s[:-1]); ds = 12 / n
    S1, S2 = np.meshgrid(s, s, indexing="ij")
    t = (tau**2 + S1 - S2) / (2 * tau)
    r2 = t * t - S1
    ok = (r2 > 0) & (t > 0) & (t < tau)
    r = np.sqrt(np.where(ok, r2, 0))
    return (np.pi / tau) * np.sum(np.where(ok, r, 0) * np.exp(-np.pi * (S1**2 + S2**2) / 24)) * ds * ds


def KJ_cont(T, m, w, tc, nt=500, nr=500):
    """continuum phi(top) = int d^4y J(y) G_R(top - y), J Euclidean Gaussian truncated to the diamond."""
    # delta part: int_0^{T/2} r J(T-r, r) dr  (top's past cone inside the diamond: r < T/2 at t = T - r > r)
    rr = np.linspace(0, T / 2, 4000)
    Jc = np.exp(-((T - rr - tc)**2 + rr**2) / (2 * w * w))
    dpart = np.trapezoid(rr * Jc, rr)
    if m == 0:
        return dpart
    t = (np.arange(nt) + 0.5) / nt * T
    tot = 0.0
    for ti in t:
        rmax = min(ti, T - ti)
        r = (np.arange(nr) + 0.5) / nr * rmax
        tau = np.sqrt(np.maximum((T - ti)**2 - r**2, 1e-300))
        Jv = np.exp(-((ti - tc)**2 + r**2) / (2 * w * w))
        tot += np.sum(r * r * Jv * j1(m * tau) / tau) * (rmax / nr)
    tot *= (T / nt)
    return dpart - m * tot


rows = []
for f in sorted(glob.glob("../out/massive4d_T*_s*.npz"), key=lambda s: float(s.split("_T")[1].split("_")[0])):
    d = np.load(f)
    T = float(d["T"]); mT = d["mT"]; m = d["m"]; Kt = d["Kt"]; KJt = d["KJt"]; L2 = d["L2"]; n = len(L2)
    el2 = EL2(T)
    print(f"\n=== T = {T:.0f} (tau/ell), n = {n} realizations, <N> = {d['Nel'].mean():.0f}, <past links of top> = {d['nlk'].mean():.0f}")
    print(f"  L^2(top,bottom): mean {L2.mean():.3f} (exact finite-tau E L^2 = {el2:.3f}; continuum 3pi = {3*np.pi:.3f}); "
          f"Var {L2.var(ddof=1):.3f}; Fano {L2.var(ddof=1)/L2.mean():.3f}")
    print("   mT    m*ell   <K>/Gm_cont   (se)     sd(K)/|Gm_cont|  sd(K)/(a^2 m^2 sqrt(3pi))   <KJ>/KJ_cont  sd(KJ)/|<KJ>|")
    for k in range(len(m)):
        if m[k] == 0:
            continue
        g = -(m[k] / (4 * np.pi * T)) * j1(m[k] * T)
        mu = Kt[:, k].mean(); sd = Kt[:, k].std(ddof=1); se = sd / np.sqrt(n)
        floor = A * A * m[k]**2 * np.sqrt(3 * np.pi)
        kjc = KJ_cont(T, m[k], float(d["w"]), float(d["tc"])) if T >= 10 else np.nan
        mj = KJt[:, k].mean(); sj = KJt[:, k].std(ddof=1)
        print(f"  {mT[k]:5.2f}  {m[k]:6.3f}   {mu/g:8.3f}    ({se/abs(g):.3f})   {sd/abs(g):9.3f}        {sd/floor:7.3f}"
              f"                 {mj/kjc if np.isfinite(kjc) else np.nan:7.3f}      {sj/abs(mj):8.4f}")
        rows.append((T, mT[k], m[k], mu, g, sd, se, mj, sj, kjc, L2.mean(), L2.var(ddof=1), el2))
np.save("../out/massive4d_summary.npy", np.array(rows))
