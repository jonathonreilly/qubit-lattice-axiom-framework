#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 78 (floating point; dense linear algebra; machinery disjoint from the exact runner's).

W1  full spectra (not traces) of the five two-record generators on rings of 4..8: the hard-core sectors against the free antisymmetric and free
    symmetric pairs - number of distinct eigenvalues, extreme eigenvalues, and the spectral distance (sorted-eigenvalue L2) between hard-core
    antisymmetric and symmetric.
W2  a two-dimensional torus 4x4 with the walk H = sigma_1 S_x + sigma_2 S_y (complex): the same comparison (dimensions 496/528 free, 480 hard-core).
W3  three records on a ring of 6 under exclusion: the dimension of the hard-core antisymmetric sector against the free one, and tr H^2/dim.
"""
import itertools
import numpy as np

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def ring_H(N):
    T = np.roll(np.eye(N), -1, axis=1); D = (T - T.T)/(2j)
    return np.kron(D, sig[2]), np.repeat(np.arange(N), 2)


def torus_H(L):
    n = L*L; idx = np.arange(n).reshape(L, L)
    def sh(axis):
        g = np.indices((L, L)).reshape(2, -1).copy(); g[axis] = (g[axis] + 1) % L
        M = np.zeros((n, n)); M[np.arange(n), np.ravel_multi_index(g, (L, L))] = 1.0; return M
    S = [(t - t.T)/(2j) for t in (sh(0), sh(1))]
    return np.kron(S[0], sig[0]) + np.kron(S[1], sig[1]), np.repeat(np.arange(n), 2)


def two_body(H, site_of, which):
    d = H.shape[0]
    H2 = np.kron(H, np.eye(d)) + np.kron(np.eye(d), H)
    vecs = []
    for i in range(d):
        for j in range(d):
            if which.startswith("hard") and site_of[i] == site_of[j]: continue
            if which.endswith("anti") and j <= i: continue
            if which.endswith("sym") and j < i: continue
            if which == "hard_none": pass
            elif which.endswith("anti") or which.endswith("sym"):
                pass
            v = np.zeros(d*d); v[i*d + j] = 1.0
            if which.endswith("anti"): v[j*d + i] -= 1.0
            elif which.endswith("sym"): v[j*d + i] += 1.0
            if which.endswith("sym") and i == j: v[i*d + j] = 1.0
            vecs.append(v/np.linalg.norm(v))
    B = np.array(vecs).T
    return np.linalg.eigvalsh(B.conj().T@H2@B)


if __name__ == "__main__":
    print("[W1] rings: spectra of the two-record generators")
    for N in (4, 5, 6, 7, 8):
        H, site_of = ring_H(N)
        spec = {w: two_body(H, site_of, w) for w in ("free_anti", "free_sym", "hard_anti", "hard_sym", "hard_none")}
        fa, fs, ha, hs = spec["free_anti"], spec["free_sym"], spec["hard_anti"], spec["hard_sym"]
        dist = lambda a, b: np.linalg.norm(np.sort(a) - np.sort(b))/np.sqrt(len(a)) if len(a) == len(b) else float("nan")
        print(f"     N = {N}: dims free anti/sym {len(fa)}/{len(fs)}, hard anti/sym/none {len(ha)}/{len(hs)}/{len(spec['hard_none'])}; largest |E|: free anti {np.abs(fa).max():.4f}, hard anti {np.abs(ha).max():.4f}; distinct eigenvalues hard anti {len(np.unique(np.round(ha, 9)))} vs hard sym {len(np.unique(np.round(hs, 9)))}; spectral distance hard anti-sym {dist(ha, hs):.2e}; mean E^2: free anti {np.mean(fa**2):.4f}, free sym {np.mean(fs**2):.4f}, hard {np.mean(ha**2):.4f}")
    print("\n[W2] 4x4 torus with the two-dimensional walk")
    H, site_of = torus_H(4)
    spec = {w: two_body(H, site_of, w) for w in ("free_anti", "free_sym", "hard_anti", "hard_sym")}
    for w, s in spec.items():
        print(f"     {w:10s}: dim {len(s)}, mean E^2 {np.mean(s**2):.5f}, mean E^4 {np.mean(s**4):.5f}, largest |E| {np.abs(s).max():.4f}")
    print(f"     spectral distance hard anti - hard sym: {np.linalg.norm(np.sort(spec['hard_anti']) - np.sort(spec['hard_sym']))/np.sqrt(len(spec['hard_anti'])):.2e}")
    print("\n[W3] three records on a ring of 6 under exclusion (antisymmetric): dimension and mean E^2 against the free antisymmetric triple")
    H, site_of = ring_H(6); d = H.shape[0]
    idx3 = [(i, j, k) for i in range(d) for j in range(i+1, d) for k in range(j+1, d)]
    def triple_spectrum(hard):
        keep = [t for t in idx3 if not hard or len({site_of[i] for i in t}) == 3]
        pos = {t: p for p, t in enumerate(keep)}
        M = np.zeros((len(keep), len(keep)), complex)
        for t, p in pos.items():
            for slot in range(3):
                for k in range(d):
                    if H[k, t[slot]] == 0: continue
                    new = list(t); new[slot] = k
                    if len(set(new)) < 3: continue
                    perm = sorted(range(3), key=lambda s: new[s]); sgn = np.linalg.det(np.eye(3)[perm])
                    key = tuple(sorted(new))
                    if key in pos: M[pos[key], p] += sgn*H[k, t[slot]]
        return np.linalg.eigvalsh(M)
    f3, h3 = triple_spectrum(False), triple_spectrum(True)
    print(f"     free antisymmetric triple: dim {len(f3)}, mean E^2 {np.mean(f3**2):.4f}; hard-core: dim {len(h3)}, mean E^2 {np.mean(h3**2):.4f}")
