#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 72 (floating point; machinery disjoint from the exact runner's).

W1  STATIONARY STATES, SITE BY SITE (dense matrices, 5 x 6 x 7 torus, random smooth-free rate field): for eigenvectors of H_w = phi H phi the
    lattice divergence of the two-step current K[phi psi] equals minus the two-step force density fP at every site (T1(d)), and the same for block
    66's one-step pair (J, f).
W2  PACKETS OF TWO SPECIES IN A SMOOTH RATE FIELD (a ring of 2048 sites, coin along sigma_3, wave number pi n + q): the total force of each
    relabelling against the total weight sum_x e(x) (u(x+1) - u(x)):  reach two: F/W = cos k = D cos q;  reach three: FP/W = cos 2k = cos 2q.
W3  the same ratio site by site (where the weight is not small): its spread.
"""
import numpy as np

rng = np.random.default_rng(72)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def w1():
    dims = (5, 6, 7); n = int(np.prod(dims)); grid = np.indices(dims).reshape(3, -1)
    def shift(axis, step=1):
        g = grid.copy(); g[axis] = (g[axis] + step) % dims[axis]
        M = np.zeros((n, n)); M[np.arange(n), np.ravel_multi_index(g, dims)] = 1.0
        return M
    T = [shift(a) for a in range(3)]
    S = [(t - t.T)/(2j) for t in T]; P = [(t@t - t.T@t.T)/(4j) for t in T]
    H = sum(np.kron(S[a], sig[a]) for a in range(3))
    phi = 1 + 0.3*rng.random(n); Phi = np.kron(np.diag(phi), np.eye(2)); Hw = Phi@H@Phi
    ev, vec = np.linalg.eigh(Hw)
    def div_current(chi, mom, j):
        c = chi.reshape(n, 2); m = (np.kron(mom[j], np.eye(2))@chi).reshape(n, 2); out = np.zeros(n)
        for a in range(3):
            cur = 0.5*np.real(np.einsum("xi,ij,xj->x", (T[a]@c).conj(), sig[a], m) + np.einsum("xi,ij,xj->x", (T[a]@m).conj(), sig[a], c))
            out += cur - T[a].T@cur
        return out
    def force(psi, j, steps):
        p = psi.reshape(n, 2); g = (H@(Phi@psi)).reshape(n, 2)
        Tj = T[j] if steps == 1 else T[j]@T[j]
        w = Tj@phi - phi
        hop = lambda f: (np.diag(w)@(Tj@f) + Tj.T@(np.diag(w)@f))/(2*steps)
        return np.real(np.einsum("xi,xi->x", hop(p).conj(), g) + np.einsum("xi,xi->x", p.conj(), hop(g)))
    worst2 = worst3 = 0.0; size = 0.0
    for col in rng.choice(2*n, size=10, replace=False):
        psi = vec[:, col]; chi = Phi@psi
        for j in range(3):
            worst2 = max(worst2, np.abs(div_current(chi, S, j) + force(psi, j, 1)).max())
            worst3 = max(worst3, np.abs(div_current(chi, P, j) + force(psi, j, 2)).max())
            size = max(size, np.abs(force(psi, j, 2)).max())
    print(f"[W1] 5x6x7 torus, random rate field, 10 eigenvectors of H_w, j = 1, 2, 3: largest |div J[phi psi] + f| = {worst2:.1e}; largest |div K[phi psi] + fP| = {worst3:.1e} (largest |fP| at a site {size:.1e})")


def w2():
    N = 2048; x = np.arange(N)
    u = 0.2*np.sin(2*np.pi*x/N); phi = np.exp(u/2)
    print("\n[W2] ring of 2048 sites, u = 0.2 sin(2 pi x/N), packets of width 60 at the steepest point, coin along sigma_3 (H = S on the upper component):")
    for q in (0.2, 0.5, 0.9):
        for species in (0, 1):
            k = np.pi*species + q
            psi = np.exp(-((x - N/2)**2)/(4*60.0**2))*np.exp(1j*k*x); psi /= np.linalg.norm(psi)
            chi = phi*psi
            g = (np.roll(chi, -1) - np.roll(chi, 1))/(2j)                                    # H (phi psi)
            e = np.real(np.conj(chi)*g)                                                       # energy density Re psi^* (H_w psi) = Re (phi psi)^* H (phi psi)
            weight = e*(np.roll(u, -1) - u)
            def force(steps):
                w = np.roll(phi, -steps) - phi
                hop = lambda f: (w*np.roll(f, -steps) + np.roll(w*f, steps))/(2*steps)
                return np.real(np.conj(hop(psi))*g + np.conj(psi)*hop(g))
            f2, f3 = force(1), force(2)
            mask = np.abs(weight) > 0.2*np.abs(weight).max()
            r2, r3 = f2[mask]/weight[mask], f3[mask]/weight[mask]
            print(f"     q = {q}, species {species}: energy {e.sum():+.4f}; reach two F/W = {f2.sum()/weight.sum():+.4f} (cos k = {np.cos(k):+.4f}); reach three FP/W = {f3.sum()/weight.sum():+.4f} (cos 2k = {np.cos(2*k):+.4f}); [W3] site by site: f/(e du) in [{r2.min():+.3f}, {r2.max():+.3f}], fP/(e du) in [{r3.min():+.3f}, {r3.max():+.3f}]")


if __name__ == "__main__":
    w1()
    w2()
