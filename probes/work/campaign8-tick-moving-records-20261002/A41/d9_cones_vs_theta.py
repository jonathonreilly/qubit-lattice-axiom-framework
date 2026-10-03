"""A41 d9: do the pi-flux isotropic cones of theta = pi/2 survive at other theta? For theta in a grid, at the 16
points (TRIMs and (+-pi/2)^3) and over all 64 points of (pi/2)Z^3: number of H6 zero modes, and |slope| range over
300 directions where zero modes exist. Same for zero flux (H0)."""
import os, signal, itertools
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(38)
import numpy as np
from common import *
rng = np.random.default_rng(37)
dirs = rng.normal(size=(300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
P64 = [np.array(p) * np.pi / 2 for p in itertools.product(range(4), repeat=3)]
for th in (0.0, np.pi / 8, np.pi / 4, 3 * np.pi / 8, 7 * np.pi / 16, 0.49 * np.pi, np.pi / 2):
    M = M_family(th); rows = []
    for name, Hf in (("pi", H6), ("zero", H0)):
        nz = 0; iso = []; mins = []
        for k in P64:
            e = np.linalg.eigvalsh(Hf(k, M)); n0 = int(np.sum(np.abs(e) < 1e-9)); mins.append(np.sort(np.abs(e))[0])
            if n0:
                nz += 1
                sl = np.array([np.sort(np.abs(np.linalg.eigvalsh(Hf(k + 1e-6 * u, M))))[:n0] / 1e-6 for u in dirs])
                if sl.max() - sl.min() < 1e-3: iso.append(round(sl.max(), 4))
        rows.append(f"{name} flux: {nz}/64 points with zero modes, {len(iso)} isotropic (slopes {sorted(set(iso))}), "
                    f"min |E| over the 64 points without zeros {min([m for m in mins if m >= 1e-9], default=np.nan):.3f}")
    print(f"theta={th/np.pi:.4f} pi | " + " | ".join(rows))
