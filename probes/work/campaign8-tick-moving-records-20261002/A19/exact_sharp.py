#!/usr/bin/env python3
"""A19 exact reduction for SHARP site registrations (EXACT, series summed numerically).

A sharp cut resets the mover to |y>: the record track is a Markov additive process.  Gaps n ~ Geometric(g)
(total registration chance per tick is exactly g in the one-excitation sector).  From a right-sublattice site
(even, chirality c=+1) the next record lands at displacement xi (cells) with law sum_n g(1-g)^(n-1) |<y|U^n|0>|^2;
from a left-sublattice site the law is mirrored (the round is symmetric under x -> 1-x).  With f = 1 if the next
record is on the other sublattice:
    q = P(f=1),  r = 1-2q  (direction correlation per registration),
    mu = E[xi],  M2 = E[xi^2],  kappa = E[xi (1-2f)],
    Var(Y after N records)/N -> M2 + kappa*mu/q,   D_track = g (M2 + kappa mu / q)  [cells^2 per tick].
Also: E[c_{i+1}] = r E[c_i], so the mean track velocity decays by r per registration.
"""
import numpy as np
from core1d import step

PI = np.pi


def sharp_stats(m, g, tol=1e-13):
    nmax = int(np.ceil(np.log(tol) / np.log(1 - g))) if g < 1 else 1
    M = 2 * nmax + 64
    a = np.zeros((1, M), complex); b = np.zeros((1, M), complex)
    c0 = M // 2
    a[0, c0] = 1.0
    x = (np.arange(M) - c0).astype(float)
    q = mu_s = mu_f = M2 = 0.0
    wsum = 0.0
    for n in range(1, nmax + 1):
        a, b = step(a, b, m)
        w = g * (1 - g) ** (n - 1)
        pa, pb = np.abs(a[0]) ** 2, np.abs(b[0]) ** 2
        q += w * pb.sum()
        mu_s += w * np.dot(pa, x)
        mu_f += w * np.dot(pb, x + 0.5)
        M2 += w * (np.dot(pa, x ** 2) + np.dot(pb, (x + 0.5) ** 2))
        wsum += w
    mu = mu_s + mu_f
    kappa = mu_s - mu_f
    out = dict(q=q, r=1 - 2 * q, mu=mu, M2=M2, kappa=kappa, wsum=wsum)
    out["Dreg"] = M2 + kappa * mu / q if q > 0 else np.inf
    out["D"] = g * out["Dreg"]
    out["tau_p"] = 1.0 / (2 * g * q) if q > 0 else np.inf     # direction persistence time (ticks)
    out["speed"] = g * mu                                     # mean speed while direction persists (cells/tick)
    return out


if __name__ == "__main__":
    print("Sharp site registrations: exact Markov-additive reduction (cells, ticks; light speed = 1)")
    print(" m     g      q        r=1-2q   mu(cells)  g*mu     D_track   tau_p   [checks]")
    for m in (0.15, 0.3, 0.6, 1.0, 1.4):
        for g in (0.01, 0.03, 0.1, 0.3, 1.0):
            s = sharp_stats(m, g)
            extra = ""
            if g == 1.0:
                extra = f"  D(g=1) = cot^2 m = {1/np.tan(m)**2:.6f}; q = sin^2 m = {np.sin(m)**2:.6f}"
            if g == 0.01:
                extra = f"  r(g->0) = 1 - sin m = {1-np.sin(m):.5f}; mu*g -> 1-sin m"
            print(f"{m:4.2f} {g:5.2f}  {s['q']:.6f}  {s['r']:+.6f}  {s['mu']:9.4f}  {s['speed']:.5f}  "
                  f"{s['D']:9.4f}  {s['tau_p']:7.2f}  wsum={s['wsum']:.12f}{extra}")
