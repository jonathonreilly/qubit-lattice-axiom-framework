"""R19-16 Z2': Neumann series vs eigen-sum Sylvester on the FULL 6x6 blocks (not only the physical block), both sides,
soft leg |k| in (1e-6 .. 1) x r/8, hard leg outside r/2: they are the same matrix (unique solution with the stated support)."""
import numpy as np, lib1916 as R
L = R.L; rng = np.random.default_rng(5)
for r in (0.1, 0.05):
    ag = 0.0; n = 0
    while n < 200:
        v = rng.normal(size=3); ks = v/np.linalg.norm(v)*r/8*10**rng.uniform(-6, 0); kh = rng.uniform(-np.pi, np.pi, 3)
        if np.linalg.norm(kh) < r/2: continue
        for left in (True, False):
            k1, k2 = (ks, kh) if left else (kh, ks)
            Msp = L.spatial_VW(k1, k2)
            A = R.piece_A(k1, k2, Msp, left, series=True); B = R.piece_A(k1, k2, Msp, left, series=False)
            ag = max(ag, np.abs(A - B).max()/max(np.abs(A).max(), 1e-300))
        n += 1
    print(f'r={r}: 200 x both sides: max |Neumann - eigen-sum| / max|M| on the full 4x4x6x6 kernel = {ag:.1e}')
