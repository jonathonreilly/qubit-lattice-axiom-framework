#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 79 (floating point; dense linear algebra; machinery disjoint from the exact runner's).

W1  the walker on a 3D torus with a staggered mass that changes sign along x across two walls: number of exact zero modes (|E| < 1e-9) for defect
    layers of thickness 0, 1, 2, 3 at each wall; their localisation; the in-gap energies of the gapped (even) walls.
W2  transverse dispersion of the wall modes (Bloch reduction along y, z; the mass depends on x only): the smallest |E| at transverse momentum (q, 0)
    for q = 0.05 .. 0.4, giving the wall modes' transverse speed against the bulk's 1; its dependence on m.
W3  the count per wall and per transverse corner on a 24 x 6 x 6 torus (16 = 2 walls x 4 corners x 2).
"""
import numpy as np

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def torus(dims):
    n = int(np.prod(dims)); grid = np.indices(dims).reshape(3, -1)
    def shift(axis):
        g = grid.copy(); g[axis] = (g[axis] + 1) % dims[axis]
        M = np.zeros((n, n)); M[np.arange(n), np.ravel_multi_index(g, dims)] = 1.0; return M
    T = [shift(a) for a in range(3)]
    return n, grid, [(t - t.T)/(2j) for t in T]


def profile(x, Lx, m0, thickness):
    m = m0*np.where((x >= Lx//4) & (x < 3*Lx//4), 1.0, -1.0)
    for wall in (Lx//4, 3*Lx//4):
        for z in range(thickness):
            m[x == wall + z] = 0.0
    return m


if __name__ == "__main__":
    dims = (16, 6, 6); n, grid, S = torus(dims); eps = np.diag((-1.0)**grid.sum(axis=0)); x = grid[0]
    H0 = sum(np.kron(S[a], sig[a]) for a in range(3))
    print("[W1] 16x6x6 torus, staggered mass m = 0.6 changing sign at x = 4 and x = 12, defect layers of thickness z (sites with no staggered term):")
    for z in (0, 1, 2, 3):
        m = profile(x, 16, 0.6, z)
        H = H0 + np.kron(np.diag(m)@eps, np.eye(2)); ev, vec = np.linalg.eigh(H)
        zero = np.abs(ev) < 1e-9
        dens = (np.abs(vec[:, zero].reshape(n, 2, -1))**2).sum(axis=1) if zero.any() else None
        near = (np.abs(x - 4) <= 1 + z//2) | (np.abs(x - 12) <= 1 + z//2)
        loc = f"; weight within {1 + z//2} sites of a wall: min {dens[near].sum(axis=0).min():.3f}" if zero.any() else ""
        print(f"     z = {z}: exact zero modes {zero.sum()}; smallest |E| {np.round(np.sort(np.abs(ev))[:3], 4)}{loc}")

    print("\n[W2] transverse dispersion of the wall modes (Bloch in y, z; ring of 48 along x; one zero site per wall):")
    Lx = 48; xx = np.arange(Lx); T = np.roll(np.eye(Lx), -1, axis=1); Sx = (T - T.T)/(2j); epsx = np.diag((-1.0)**xx)
    for m0 in (0.3, 0.6, 1.2):
        m = m0*np.where((xx >= 12) & (xx < 36), 1.0, -1.0); m[12] = 0.0; m[36] = 0.0
        def Hx(ky, kz):
            return np.kron(Sx, sig[0]) + np.kron(np.eye(Lx), np.sin(ky)*sig[1] + np.sin(kz)*sig[2]) + np.kron(np.diag(m)@epsx, np.eye(2))
        line = []
        for q in (0.05, 0.1, 0.2, 0.4):
            e = np.sort(np.abs(np.linalg.eigvalsh(Hx(q, 0.0))))[:4]
            line.append(f"q = {q}: |E| = {e[0]:.4f} (speed {e[0]/np.sin(q):.3f})")
        print(f"     m = {m0}: " + "; ".join(line))

    dims = (24, 6, 6); n, grid, S = torus(dims); eps = np.diag((-1.0)**grid.sum(axis=0)); x = grid[0]
    m = profile(x, 24, 0.6, 1)
    H = sum(np.kron(S[a], sig[a]) for a in range(3)) + np.kron(np.diag(m)@eps, np.eye(2)); ev, vec = np.linalg.eigh(H)
    zero = np.where(np.abs(ev) < 1e-9)[0]
    print(f"\n[W3] 24x6x6 torus, one zero site per wall: {len(zero)} exact zero modes (2 walls x 4 transverse corners x 2 = 16)")
    # transverse momentum content of the zero modes: Fourier transform over y, z at each x, weight at the four corners
    counts = {(0, 0): 0.0, (1, 0): 0.0, (0, 1): 0.0, (1, 1): 0.0}
    for i in zero:
        v = vec[:, i].reshape(dims[0], dims[1], dims[2], 2)
        ft = np.fft.fft2(v, axes=(1, 2))/np.sqrt(dims[1]*dims[2])
        for c in counts:
            counts[c] += float((np.abs(ft[:, c[0]*dims[1]//2, c[1]*dims[2]//2, :])**2).sum())
    print("     total zero-mode weight at each transverse corner (four per corner expected):", {k: round(v, 3) for k, v in counts.items()})
