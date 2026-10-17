"""Cross-check tableau rank with a plain numpy GF(2) elimination (L=4,5)."""
import numpy as np
from mpd_core import *
def gf2rank(M):
    M = M.copy() % 2; r = 0
    rows, cols = M.shape
    for c in range(cols):
        piv = np.nonzero(M[r:, c])[0]
        if len(piv) == 0: continue
        p = r + piv[0]
        M[[r, p]] = M[[p, r]]
        nz = np.nonzero(M[:, c])[0]
        nz = nz[nz != r]
        M[nz] ^= M[r]
        r += 1
        if r == rows: break
    return r
for L in [4, 5]:
    lat = Lattice(L)
    sec = all_sectors()[0]
    gens = [lat.to_pauli(m) for m in lat.generators(sec)]
    M = np.zeros((len(gens), 2 * lat.n), dtype=np.uint8)
    for i, g in enumerate(gens):
        for q in range(lat.n):
            M[i, q] = (g[0] >> q) & 1
            M[i, lat.n + q] = (g[1] >> q) & 1
    T = Tableau(lat.n)
    for g in gens: T.insert(g)
    print("L", L, "numpy rank", gf2rank(M), "tableau rank", T.rank(), "n", lat.n)
