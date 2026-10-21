#!/usr/bin/env python3
"""POST HOC diagnostics (not pre-declared criteria): per beta on the ladder, dF1 (TI and direct), dF2 direct,
sector-conditional energy E_{W=(0,0,0)}, S2/S1 local exponent. usage: posthoc.py L"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from analyze import load
import ti
L = int(sys.argv[1])
tags = [f"L{L}_s{s}" for s in os.environ.get("SEEDS", "1,2").split(",")]
print("TI/direct dF1 along the ladder:")
d0 = load(tags[0]); betas = d0["betas"]
sel = [b for b in betas if b >= 0.99 or abs(b - betas[0]) < 1e-9][::2] + [float(L), max(betas)]
ti.main(tags, sorted(set(sel)))
for t in tags:
    d = load(t)
    m = d["m"][int(0.2 * len(d["m"])):]
    k = d["keys"]
    W = m[:, :, [k.index("Wx"), k.index("Wy"), k.index("Wz")]]
    E = m[:, :, k.index("E")]
    print(f"--- {t}")
    for bb in (L / 2, float(L), max(betas)):
        i = int(np.argmin(np.abs(betas - bb)))
        w = W[:, i]
        p0 = (w == 0).mean(); p1 = (np.abs(w) == 1).mean(); p2 = (np.abs(w) == 2).mean()
        z0 = (w == 0).all(1)
        e0 = E[z0, i].mean() if z0.any() else np.nan
        n = len(E); nb = 20; ns = n // nb
        eb = np.array([E[j * ns:(j + 1) * ns, i][z0[j * ns:(j + 1) * ns]].mean() for j in range(nb)])
        df1 = -np.log(p1 / (2 * p0)) / betas[i]
        df2 = -np.log(p2 / (2 * p0)) / betas[i] if p2 > 0 else np.nan
        s = ""
        if "S1" in k:
            S1 = m[:, i, k.index("S1")]; S2 = m[:, i, k.index("S2")]
            if np.isfinite(S1).all() and np.isfinite(S2).all():
                s = f" S2/S1={S2.mean() / S1.mean():.4f} (local p={np.log(S2.mean() / S1.mean()) / np.log(2):.3f})"
        print(f"beta={betas[i]:.4g}: P0={p0:.4f} P1={p1:.4f} P2={p2:.5f} dF1={df1:.4f} dF2={df2:.4f} dF2/dF1={df2 / df1:.3f}"
              f"  E|W=000 = {e0:.4f} +- {np.nanstd(eb, ddof=1) / np.sqrt(nb):.4f} (frac {z0.mean():.3f})" + s)
