"""E2 (4): table of mean stiffness per present site (pooled L = 8, 10, 12, weighted by 1/SE^2) and noise sd*sqrt(N)
(pooled mean over boxes) for each p, coupling, functional."""
import numpy as np
import e23_core as c
for mode in ['pd', 'nn']:
    z = np.load(f"E2_1_{mode}.npz")
    for k, fn in enumerate(['boson m2=1', 'boson m2=0.04', 'fermion sea']):
        print(f"[{mode}] {fn}")
        for p in [1.0, 0.9, 0.7, 0.5, 0.3116, 0.3, 0.2, 0.1]:
            row = f"  p={p:<6}"
            for ch, idx in c.CH.items():
                ms, ws, sdn = [], [], []
                for Lb in [8, 10, 12]:
                    A = z[f"p{p}_L{Lb}"][:, k, idx, 1]; N = z[f"p{p}_L{Lb}_N"].mean()
                    if len(A) == 1: ms, ws, sdn = [A.mean()], [1.0], [0.0]; break
                    se = A.mean(1).std(ddof=1) / np.sqrt(len(A)); ms.append(A.mean()); ws.append(1 / se**2); sdn.append(A.std(ddof=1) * np.sqrt(N))
                ms, ws = np.array(ms), np.array(ws); m = (ms * ws).sum() / ws.sum(); se = 1 / np.sqrt(ws.sum()) if len(ms) > 1 else 0
                row += f" | {ch}: {m:+.4f}+-{se:.4f} sdN {np.mean(sdn):.3f}"
            print(row)
