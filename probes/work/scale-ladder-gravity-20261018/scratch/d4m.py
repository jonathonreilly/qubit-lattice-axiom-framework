"""Site-cell metric L: 72 D4-cone edge lengths -> 10 metric components per site cell, invariant under moving non-site vertices."""
import sys, itertools, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from d4e import C
HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
pairs = list(itertools.combinations(range(4), 2))
def eidx(v1, v2):
    key, anc = RG._key_pair(v1, v2); return C.ekey[key], np.array(anc, float)
def L(k):
    """rows: h components of the cell at the origin; columns: Bloch edge variables (delta l)."""
    k = np.asarray(k, complex); Lm = np.zeros((10, C.E), complex)
    Ei = np.eye(4, dtype=int)
    def add(row, v1, v2, coef):
        c, anc = eidx(v1, v2); Lm[row, c] += coef*np.exp(1j*k @ anc)
    for mu in range(4):                      # h_mumu = 2 delta l(axis)  (length 1)
        add(HC.index((mu, mu)), ((0,0,0,0), 0), (tuple(Ei[mu]), 0), 2.0)
    for h, (m, n) in enumerate(pairs):       # face diagonal 0 -> e_m+e_n through the hole (e_m+e_n)/2, type 2+h
        row = HC.index((m, n))
        add(row, ((0,0,0,0), 0), ((0,0,0,0), 2+h), np.sqrt(2.0))      # 2 sqrt2 dl_diag / 2
        add(row, ((0,0,0,0), 2+h), (tuple(Ei[m]+Ei[n]), 0), np.sqrt(2.0))
        add(row, ((0,0,0,0), 0), (tuple(Ei[m]), 0), -1.0)             # - h_mm/2 = - dl_axis(m)
        add(row, ((0,0,0,0), 0), (tuple(Ei[n]), 0), -1.0)
    return Lm
# checks: (1) L G_optical = 0 ; (2) L acting on line-map image of constant metric reproduces it at k -> 0
for k in [np.array([0.3, -0.2, 0.1, 0.25]), np.zeros(4)]:
    G = C.gauge(k); Lk = L(k)
    nt = len(C.types); Ga = sum(G[:, 4*t:4*t+4] for t in range(nt))
    opt = np.hstack([G[:, 4*t:4*t+4] - G[:, 0:4]*0 for t in range(1, nt)])
    print("k=", k, " |L G_nonsite| =", np.abs(Lk @ np.hstack([G[:, 4*t:4*t+4] for t in range(1, nt)])).max(), " |L M(0) - 1| =", np.abs(L(np.zeros(4)) @ C.line_map(np.zeros(4)) - np.eye(10)).max())
