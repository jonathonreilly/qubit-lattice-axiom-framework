"""Structure factors of flippability / circulation from DMC snapshots (mixed distribution). No claim."""
import os, sys, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, chk
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pat = sys.argv[1] if len(sys.argv) > 1 else "results/*e0.00*.npz"
for fn in sorted(glob.glob(pat)):
    d = np.load(fn); L = int(d["L"]); lat = chk.Lat((L, L, L))
    S = d["SNAP"][d["SNAP"].shape[0] // 4:].reshape(-1, lat.np_).astype(float)  # drop first quarter
    if S.shape[0] == 0: continue
    f = (S != 0).astype(float)
    qs = [np.array(q) * 2 * np.pi / L for q in np.ndindex(L, L, L)]
    best = []
    for name, X in (("flip", f - f.mean()), ("circ", S)):
        sq = {}
        for q in qs:
            ph = np.exp(1j * (lat.root @ q))
            for o in range(3):
                m = lat.ori == o
                A = X[:, m] @ ph[m]
                sq[(tuple(np.round(q / np.pi, 2)), o)] = float((np.abs(A) ** 2).mean() / m.sum())
        top = sorted(sq.items(), key=lambda kv: -kv[1])[:3]
        best.append((name, top))
    print(f"{fn}: <f>={f.mean():.4f}  " + "  ".join(f"{n}: " + ", ".join(f"q/pi={k[0]} o{k[1]} S={v:.2f}" for k, v in t) for n, t in best))
