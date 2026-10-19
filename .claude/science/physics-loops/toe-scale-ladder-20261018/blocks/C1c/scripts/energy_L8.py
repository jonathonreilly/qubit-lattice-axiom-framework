#!/usr/bin/env python3
"""L=8 single-beta thermal energy (one-sided check of the 8^3 ground energy: <H>_beta >= E0 for all beta).
usage: energy_L8.py TAG [TAG...]"""
import os, sys, glob
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
for tag in sys.argv[1:]:
    fs = sorted(glob.glob(os.path.join(HERE, "..", "data", "raw", tag + "_c*.npz")))
    ms = [np.load(f)["m"][:, 0, :] for f in fs]
    k = list(np.load(fs[0])["keys"])
    m = np.concatenate(ms)
    m = m[int(0.2 * len(m)):]
    E = m[:, k.index("E")]
    W = m[:, [k.index("Wx"), k.index("Wy"), k.index("Wz")]].astype(int)
    for nb in (10, 20, 40):
        n = len(E) // nb
        b = E[: n * nb].reshape(nb, n).mean(1)
        print(f"{tag}: nb={nb} E = {E.mean():.3f} +- {b.std(ddof=1) / np.sqrt(nb):.3f}")
    n = len(E) // 5
    print(f"{tag}: fifths {[round(E[i * n:(i + 1) * n].mean(), 3) for i in range(5)]}  W visited {sorted(set(map(tuple, W)))[:5]}  nmeas={len(E)}  E/Np={E.mean() / (3 * 8 ** 3):.5f}")
