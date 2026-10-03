#!/usr/bin/env python3
"""A19: track velocity vs packet momentum K0 (m = 0.6), coarse vs sharp registrations at g = 0.03, T = 600.
Track velocity = least-squares slope of record place vs tick (preparation point included); also the late-half slope.
Theory: coarse (sigma_s K0 >> 1, N_reg << (sigma_s K0)^2): slope -> v(K0).  Sharp: the first record resets the mover;
the mean velocity of segment k is v0 (1-sin m) r^(k-1) (r = exact direction correlation), late slope -> 0."""
import numpy as np
from core1d import step, packet, vgroup, Registrar, ls_slope
from exact_sharp import sharp_stats

M, j0, w0, T, B, m, g = 2048, 700, 20.0, 600, 120, 0.6, 0.03
ex = sharp_stats(m, g)
print(f"m={m} g={g} T={T} B={B}; exact sharp-cut r = {ex['r']:.4f}, 1 - sin m = {1-np.sin(m):.4f}")
print("K0     v(K0)   | coarse sig=64 sites: slope (s.e.)  late-half slope | sharp site: slope (s.e.)  late-half slope")
for K0 in (-0.3, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2):
    v0 = vgroup(K0, m)
    row = f"{K0:+.2f} {v0:+.4f} |"
    for kw in (dict(kind="gauss", sig=64.0), dict(kind="gauss", sig=0.0)):
        rng = np.random.default_rng(int(1000 * (K0 + 2)))
        a0, b0 = packet(M, m, K0, w0, j0)
        a = np.repeat(a0[None], B, 0); b = np.repeat(b0[None], B, 0)
        reg = Registrar(B, M, g, rng=rng, x0_cells=j0, **kw)
        for t in range(1, T + 1):
            a, b = step(a, b, m); a, b = reg.apply(a, b, t)
        sl, s2 = [], []
        for tr in reg.tracks:
            tt = np.array([p[0] for p in tr], float); yy = np.array([p[1] for p in tr])
            sl.append(ls_slope(tt, yy))
            h = tt > T / 2
            s2.append(ls_slope(tt[h], yy[h]))
        sl, s2 = np.array(sl), np.array(s2)
        row += (f" {np.nanmean(sl):+.4f} ({np.nanstd(sl)/np.sqrt(np.isfinite(sl).sum()):.4f})"
                f"  {np.nanmean(s2):+.4f} ({np.nanstd(s2)/np.sqrt(np.isfinite(s2).sum()):.4f}) |")
    print(row, flush=True)
