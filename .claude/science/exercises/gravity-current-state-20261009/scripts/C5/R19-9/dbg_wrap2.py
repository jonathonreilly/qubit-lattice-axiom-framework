import numpy as np, lib199 as L
rng = np.random.default_rng(3)
for l in range(3):
    k1 = rng.uniform(-np.pi, np.pi, 3); k1[l] = np.pi - 1e-7; k2 = rng.uniform(-np.pi, np.pi, 3)
    k1b = k1.copy(); k1b[l] = -np.pi + 1e-7
    T = np.ones(6); T[l] = -1; T[3:] = -1; T[3+l] = 1
    Ma = L.piece_B(k1, k2, L.spatial_VW(k1, k2)); Mb = L.piece_B(k1b, k2, L.spatial_VW(k1b, k2))
    D = np.abs(Ma - np.einsum('a,mnab->mnab', T, Mb)).max(axis=(2,3)); print('l', l); print(np.array2string(D, precision=2))
    print(' divdiff', L.divdiff(k1, k2), L.divdiff(k1b, k2), 'q', L.wrap(k1-k2), L.wrap(k1b-k2))
