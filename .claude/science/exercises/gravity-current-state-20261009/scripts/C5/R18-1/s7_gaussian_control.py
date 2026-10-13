"""R18-1 s7 (written before running). Physical control for the pinch diagnostic, same observable and stencil:
Gaussian labels n_s in R with weight exp(-1/2 sum n^2 - (lam/2) sum_edges (G n)^2) on the same slots and N0914 stencil.
Exact: S(k) = (1 + lam G(k)^dag G(k))^{-1} (slot basis with the slot-position phases), then r = S_V/S_TT along the axis,
xi^2(q) = (1/r - 1)/q^2. lam = infinity: S = projector onto ker G(k) (a Coulomb phase of the vector law: known pinch point)."""
import numpy as np
from mc import OFFS, channel_pols, cvec
from common import G_entries, TYPES
def Gk(k):
    """3x6 symbol of G acting on slot amplitudes n_s(k) defined with slot-position phases"""
    M = np.zeros((3, 6), complex)
    for t in range(6):
        for (e, j), c in G_entries((0, 0, 0), t):
            # row j at edge base e (position e + e_j/2); slot t at OFFS[t]; amplitude phase relative to slot position
            ej = np.eye(3)[j]
            M[j, t] += c*np.exp(-1j*k @ (np.array(e) + ej/2 - OFFS[t]))
    return M
for L in [6, 8, 12, 16, 32]:
    for lam in [0.3, 3.0, 30.0, np.inf]:
        out = []
        for m in [1, 2]:
            k = np.array([0, 0, 2*np.pi*m/L]); g = Gk(k)
            if np.isinf(lam):
                u, s, vh = np.linalg.svd(g); ker = vh[np.sum(s > 1e-12):].conj().T; S = ker @ ker.conj().T
            else:
                S = np.linalg.inv(np.eye(6) + lam*g.conj().T @ g)
            pols = channel_pols(k); val = {ch: np.mean([np.real(cvec(e) @ S @ cvec(e)) for e in lst]) for ch, lst in pols.items()}
            q2 = float((4*np.sin(k/2)**2).sum()); r = val['V']/val['TT']
            out.append((q2, r, (1/r - 1)/q2 if r > 0 else np.inf))
        print("L=%2d lam=%5s: r(qmin)=%.4f  xi^2(q1)=%s xi^2(q2)=%s  xi(q1)/L=%s" % (L, lam, out[0][1], np.round(out[0][2], 3), np.round(out[1][2], 3),
              np.round(np.sqrt(out[0][2])/L, 3) if np.isfinite(out[0][2]) else "inf"))
# Identity V on the symbol: along z, |G_x| = q |n_xz| etc.
k = np.array([0, 0, 0.3]); print("symbol check along z: |G(k)| rows vs 2|sin(k/2)| =", np.round(np.abs(Gk(k)), 4).tolist(), round(2*np.sin(0.15), 4))
