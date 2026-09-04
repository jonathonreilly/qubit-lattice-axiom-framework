"""C4 -- Bloch decomposition validated against a direct dense L^4 x L^4 assembly
(kuhn.dense_eigs) with no translation-invariance assumption, at small L."""
import math
import numpy as np
from kx_base import (build, _bands, bloch_eigs, dense_eigs, CH_P, N_MODE, fmte)
import kuhn

n = N_MODE
print("=== C4  Bloch spectrum vs dense L^4 assembly ===")
for L in (4, 6, 8):
    kk = 2 * math.pi * n / L
    for name, P in CH_P.items():
        for eps in (0.0, 0.10):
            for imp in (True, False):
                r = build(L, eps, P, kk)
                bd = _bands(L, r['stencil'])
                qs = kuhn.all_momenta(L)
                ev, herm = bloch_eigs(L, bd, r['mass'], qs,
                                      C=(r['C'] if imp else None), improve=imp)
                blo = np.sort(ev.ravel())
                den, M = dense_eigs(L, eps, P, kk,
                                    C=(r['C'] if imp else None), improve=imp)
                dm = float(np.max(np.abs(np.repeat(r['mass'], L ** 3) - M)))
                d = float(np.max(np.abs(blo - den)))
                rel = d / max(1.0, float(np.max(np.abs(den))))
                print(f"  L={L} {name:13s} eps={eps:.2f} {'IMPR ' if imp else 'plain'}"
                      f"  max|dlambda| {d:.3e}  rel {rel:.3e}  max|dM| {dm:.3e}")
