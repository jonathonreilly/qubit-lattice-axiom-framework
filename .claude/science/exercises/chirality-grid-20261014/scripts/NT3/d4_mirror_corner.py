"""PREREG follow-up A3, D4: single-particle spectral gap at the mirror corner k_m = floor(L/2) (W = infinity)."""
import numpy as np
import scipy.sparse.linalg as sla
from ed_core import Model, ring, lowest
from analyze import chain
from filters import ring_fvals

out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

for name in ("C1", "F_lo", "F_star", "F_hi"):
    for L in (4, 5, 6, 7):
        m = Model(ring(L), ring_fvals(name, L))
        b0 = chain(m, (0, 0, 0, 0), 0); e0, v0 = lowest(m.build_H(b0), k=2); g0 = v0[:, 0]; E0 = e0[0]
        km = L // 2; j = m.jof[km]
        res = []
        for lab, dag, d in (("particle", True, (1, 0, 0, 0)), ("hole", False, (-1, 0, 0, 0))):
            K = (km if dag else (-km) % L)
            b = chain(m, d, K)
            vec = m.apply_op_sum([(1.0, [(dag, m.p(0, j))])], b0, g0, b)
            nv = vec @ vec
            H = m.build_H(b)
            nlev = min(8, len(b) - 2) if len(b) > 600 else len(b)
            e, V = lowest(H, k=nlev)
            w = (V.T @ vec) ** 2 / nv
            cap = w.sum()
            eavg = (w * (e - E0)).sum() / cap
            first = next(((e[i] - E0, w[i]) for i in range(len(e)) if w[i] >= 0.1), (np.nan, np.nan))
            # exact first moment of the full spectral function (no truncation): <v|H|v>/<v|v> - E0
            m1 = (vec @ (H @ vec)) / nv - E0
            res.append(f"{lab}: lowest-in-sector {e[0]-E0:.4f}; first level with w>=0.1: E={first[0]:.4f} (w={first[1]:.3f}); "
                       f"captured w(8 lowest) = {cap:.3f}, E_avg = {eavg:.4f}; exact 1st moment = {m1:.4f}")
        P(f"{name} L={L} k_m={km} (f={m.f[j]:.4f}): " + " | ".join(res))
open(__file__.replace(".py", ".out"), "w").write("\n".join(out) + "\n")
