"""bb8n_defect: raw root-row defects of the framed DD8 chain (informational; criteria checks/bb8n_defect_criteria.md)."""
import os
import time

import numpy as np

T0 = time.time()
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bb8n_lip.py")).read()
exec(_src.split("\nout = []\n")[0])
out = []
b = rng8.standard_normal((TK, TK, 2, 3))
h = rng8.standard_normal((TK, TK, 4))
h /= np.linalg.norm(h, axis=-1, keepdims=True)
worst = 0.0
for target in (0.10, 0.05):
    V = qexp(scaled_field(b, target))
    Vh = np.stack([qmul(qmul(h, V[:, :, a]), qinv(sh(h, *((1, 0) if a == 0 else (0, 1))))) for a in range(2)], axis=2)
    for tag, W in (("ungauged", V), ("Haar gauge", Vh)):
        levs = chain(W, NA, 3)
        vals = []
        for m in (1, 2, 3):
            Zc, Zf = levs[m - 1], levs[m]
            mx = 0.0
            for a in range(2):
                e = (1, 0) if a == 0 else (0, 1)
                row = NA.one(Zf.shape[:2])
                for i in range(3):
                    row = qmul(row, sh(Zf[:, :, a], i * e[0], i * e[1]))
                d = qlog(qmul(qinv(row[0::3, 0::3]), Zc[:, :, a]))
                mx = max(mx, np.linalg.norm(d, axis=-1).max())
            vals.append(mx)
            worst = max(worst, mx)
        out.append(f"f_k = {target:.2f}, {tag}: max own |d_j| (m = 1, 2, 3) = " + ", ".join(f"{v:.2e}" for v in vals))
out.append(f"D-a d_j = 0 to round-off (<= 1e-13): {'PASS' if worst <= 1e-13 else 'FAIL'} (worst {worst:.2e})")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
