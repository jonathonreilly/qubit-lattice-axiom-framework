#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 70 (floating point; dense matrices; machinery disjoint from the exact runner's).

The exact runner applies operators to one rational state with the campaign's torus class. Here every generator is a dense matrix on a 6 x 6 x 6 torus
(432 x 432) with random real fields, and the exchange identities are tested as MATRIX identities (every state at once).
W1  V_n H[field] V_n - det(D_n) H[field'] for the five kinds of field and all eight species (largest matrix entry), and the same with the field
    left unchanged (to show which fields the maps move).
W2  spectra: multiplicities of the levels and the symmetry of the spectrum about zero, for rates + reach-three strains, for a frame, for a reach-two strain.
W3  the cubic trace of the walk in the runner's rational reach-two strain field on a 4 x 4 x 4 torus, against the runner's exact -735/8192.
W4  twins: for an odd species, A_n = Theta V_n applied to a solution is a solution in the same fields (rates + reach-three strain): the norm of
    A_n exp(-iHt) psi - exp(-iHt) A_n psi, and the site densities of the two movies.
"""
import itertools
from collections import Counter
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(70)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


class Lattice:
    def __init__(self, dims):
        self.dims = dims; self.n = int(np.prod(dims)); self.grid = np.indices(dims).reshape(3, -1)
        self.T = [self.shift(a) for a in range(3)]
        self.S = [(t - t.T)/(2j) for t in self.T]; self.P = [(t@t - t.T@t.T)/(4j) for t in self.T]
        self.H0 = sum(np.kron(self.S[a], sig[a]) for a in range(3))

    def shift(self, axis):
        g = self.grid.copy(); g[axis] = (g[axis] + 1) % self.dims[axis]
        M = np.zeros((self.n, self.n)); M[np.arange(self.n), np.ravel_multi_index(g, self.dims)] = 1.0
        return M                                                   # (T psi)(x) = psi(x + e)

    def hop(self, a, v):                                          # symmetric hop weighted by the bond function v (bond from x to x + e_a stored at x)
        return 0.5*(np.diag(v)@self.T[a] + self.T[a].T@np.diag(v))

    def rates(self, phi):
        f = np.kron(np.diag(phi), np.eye(2)); return f@self.H0@f

    def frame(self, E):
        return sum(0.5*np.kron(np.diag(E[a][j])@self.S[j] + self.S[j]@np.diag(E[a][j]), sig[a]) for a in range(3) for j in range(3))

    def strain(self, B, reach):
        mom = self.S if reach == 2 else self.P
        return self.H0 + sum(0.5*np.kron(self.hop(a, B[a][j])@mom[j] + mom[j]@self.hop(a, B[a][j]), sig[a]) for a in range(3) for j in range(3))

    def twist(self, th):
        H = self.H0.copy()
        for a, b, j in itertools.permutations(range(3)):
            sign = np.linalg.det(np.eye(3)[[a, b, j]])
            H = H + sign*0.5*np.kron(np.diag(th[b])@self.S[j] + self.S[j]@np.diag(th[b]), sig[a])
        for a in range(3):
            H = H + 0.5*np.kron(self.hop(a, self.T[a]@th[a] - th[a]), np.eye(2))
        return H

    def exchange(self, nvec):
        D = np.array([(-1)**k for k in nvec]); s = int(np.prod(D)); rho = s*D
        U = np.diag(np.prod([(-1.0)**(nvec[a]*self.grid[a]) for a in range(3)], axis=0))
        R = np.eye(2, dtype=complex) if tuple(rho) == (1, 1, 1) else sig[[i for i in range(3) if rho[i] == 1][0]]
        return np.kron(U, R), D, s, rho


if __name__ == "__main__":
    L = Lattice((6, 6, 6)); n = L.n
    fld = lambda: [[0.3*rng.normal(size=n) for _ in range(3)] for _ in range(3)]
    E = fld(); E = [[E[a][j] + (1.0 if a == j else 0.0) for j in range(3)] for a in range(3)]
    B = fld(); th = [0.3*rng.normal(size=n) for _ in range(3)]; phi = 1 + 0.3*rng.random(n)
    print("[W1] 6x6x6 torus, random real fields, dense matrices: largest entry of V_n H[field] V_n - det(D) H[field'] (in brackets: with the field left unchanged)")
    for nvec in itertools.product((0, 1), repeat=3):
        V, D, s, rho = L.exchange(nvec)
        conj = lambda H: V@H@V.conj().T
        rE = [[rho[a]*E[a][j]*rho[j] for j in range(3)] for a in range(3)]
        BD = [[B[a][j]*D[j] for j in range(3)] for a in range(3)]
        rth = [rho[b]*th[b] for b in range(3)]
        rows = [("rates", L.rates(phi), L.rates(phi)), ("frame", L.frame(E), L.frame(rE)), ("twist", L.twist(th), L.twist(rth)),
                ("reach2", L.strain(B, 2), L.strain(BD, 2)), ("reach3", L.strain(B, 3), L.strain(B, 3))]
        print(f"     n = {nvec}, det D = {s:+d}, rho = {tuple(int(r) for r in rho)}: " + "; ".join(f"{name} {np.abs(conj(H) - s*Hp).max():.1e} ({np.abs(conj(H) - s*H).max():.2f})" for name, H, Hp in rows))

    def levels(H):
        ev = np.linalg.eigvalsh(H); groups = np.split(ev, np.where(np.diff(ev) > 1e-9)[0] + 1)
        return dict(Counter(len(g) for g in groups)), np.abs(ev + ev[::-1]).max()
    f = np.kron(np.diag(phi), np.eye(2))
    print("\n[W2] multiplicities of the levels {multiplicity: number of levels} and the largest |E_i + E_(N-i)|:")
    for name, H in [("rates + reach-three strain", f@L.strain(B, 3)@f), ("frame", L.frame(E)), ("twist", L.twist(th)), ("reach-two strain", L.strain(B, 2))]:
        mult, asym = levels(H); print(f"     {name:28s}: {mult}, asymmetry {asym:.2e}")

    small = Lattice((4, 4, 4))
    def detB(a, j, x): return ((7*a + 3*j + 3*x[0]*x[0] + 5*x[1] + x[2]*x[1] + (a + 1)*x[0] + j*x[2]) % 5 - 2)/4
    Bs = [[np.array([detB(a, j, tuple(small.grid[:, i])) for i in range(small.n)]) for j in range(3)] for a in range(3)]
    H2 = small.strain(Bs, 2); t3 = np.trace(H2@H2@H2).real
    print(f"\n[W3] 4x4x4 torus, the runner's rational reach-two strain field: tr H^3 = {t3:.13f}; the runner's exact value -735/8192 = {-735/8192:.13f}")
    ev = np.linalg.eigvalsh(H2); print(f"     its spectrum: largest {ev[-1]:.6f}, smallest {ev[0]:.6f}")

    print("\n[W4] twins (rates + reach-three strain, 6x6x6, t = 7): A_n = Theta V_n, Theta = sigma_2 x conjugation")
    H = f@L.strain(B, 3)@f; Ut = expm(-7j*H)
    psi = rng.normal(size=2*n) + 1j*rng.normal(size=2*n); psi /= np.linalg.norm(psi)
    s2 = np.kron(np.eye(n), sig[1])
    for nvec in [(1, 0, 0), (0, 1, 0), (1, 1, 1)]:
        V = L.exchange(nvec)[0]
        A = lambda v: s2@np.conj(V@v)
        left, right = A(Ut@psi), Ut@A(psi)
        dens = lambda v: (np.abs(v.reshape(n, 2))**2).sum(axis=1)
        print(f"     n = {nvec}: |A U psi - U A psi| = {np.linalg.norm(left - right):.1e}; largest difference of site densities between the movies = {np.abs(dens(Ut@psi) - dens(right)).max():.1e}; energies {np.vdot(psi, H@psi).real:+.6f} and {np.vdot(A(psi), H@A(psi)).real:+.6f}; contrast, V_n alone: |V U psi - U V psi| = {np.linalg.norm(V@(Ut@psi) - Ut@(V@psi)):.2f}")
