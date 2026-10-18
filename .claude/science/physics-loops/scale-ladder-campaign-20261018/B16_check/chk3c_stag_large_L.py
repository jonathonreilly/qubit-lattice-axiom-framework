"""B16 check 3c: staggered timing, B/Lead at larger L (follow-up of chk3b; measurement only, no PASS criterion)."""
import numpy as np
from chk3b_scaling import em_run
rows = []
for L in (16, 24, 32, 40, 48, 56):
    D, lead, B, R = em_run("STAG", L)
    rows.append((L, B / lead))
    print(f"  STAG L={L:3d}  B/Lead={B / lead:.6f}  D={D:.2e}", flush=True)
Ls = np.array([r[0] for r in rows], float); y = np.array([r[1] for r in rows])
for deg in (1, 2):
    V = np.vander(1 / Ls, deg + 1)
    c, *_ = np.linalg.lstsq(V, y, rcond=None)
    print(f"  fit B/Lead = poly(1/L) deg {deg}: coeffs (highest power first) {np.round(c, 4)}; extrapolated L->inf value {c[-1]:.4f}")
