#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 65 (floating point; machinery disjoint from the exact runner's).

W1  FINITE rotations: psi -> U(x) psi with U = exp(-i s theta(x).sigma/2), dense matrices on a 4x3x3 torus.  Is U H U^dagger - H[s theta] of second
    order in s (with the scalar hop) and of first order without it?
W2  the spectrum: H[vartheta] against H for a random rotation field of size s: shift of the eigenvalues with and without the scalar hop.
W3  the torque on stationary states found numerically (degenerate eigenspaces of H on a 6x4x4 torus): response to a rotation at each site, with and
    without the hop.
W4  what the hop does at long wavelength: for vartheta_a = g x_a (uniform twist g) on the infinite lattice the hop adds (g/2) sum_a cos k_a to both
    branches: a coin-independent shift; compare with a numerical spectrum on a ring with a linear twist is not periodic, so use vartheta_a = A sin(q x_a)
    and first-order perturbation theory for a plane wave."""
import itertools
import numpy as np
from scipy.linalg import expm

sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
eps = np.zeros((3,3,3)); eps[0,1,2]=eps[1,2,0]=eps[2,0,1]=1; eps[0,2,1]=eps[2,1,0]=eps[1,0,2]=-1
rng = np.random.default_rng(8)

class Lat:
    def __init__(self, dims):
        self.dims = dims; self.sites = list(itertools.product(*(range(d) for d in dims))); self.idx = {s:i for i,s in enumerate(self.sites)}; self.N = len(self.sites)
    def sh(self, x, a, s=1): return tuple((x[i] + (s if i == a else 0)) % self.dims[i] for i in range(3))
    def S(self, j):
        M = np.zeros((self.N, self.N), complex)
        for x in self.sites: M[self.idx[x], self.idx[self.sh(x,j)]] += 1/(2j); M[self.idx[x], self.idx[self.sh(x,j,-1)]] -= 1/(2j)
        return M
    def C(self, a, w):
        M = np.zeros((self.N, self.N), complex)
        for x in self.sites: M[self.idx[x], self.idx[self.sh(x,a)]] += 0.5*w[x]; M[self.idx[x], self.idx[self.sh(x,a,-1)]] += 0.5*w[self.sh(x,a,-1)]
        return M
    def walk(self, vartheta=None, hop=True):
        Ss = [self.S(j) for j in range(3)]
        H = sum(np.kron(Ss[a], sig[a]) for a in range(3))
        if vartheta is not None:
            for j in range(3):
                for d in range(3):
                    v = np.array([sum(eps[c,j,d]*vartheta[c][x] for c in range(3)) for x in self.sites])
                    D = np.diag(v)
                    H = H + np.kron(0.5*(D@Ss[j] + Ss[j]@D), sig[d])
            if hop:
                for a in range(3):
                    w = {x: vartheta[a][self.sh(x,a)] - vartheta[a][x] for x in self.sites}
                    H = H + np.kron(0.5*self.C(a, w), np.eye(2))
        return H
    def rotation(self, theta, s):
        U = np.zeros((2*self.N, 2*self.N), complex)
        for x in self.sites:
            i = self.idx[x]; U[2*i:2*i+2, 2*i:2*i+2] = expm(-0.5j*s*sum(theta[c][x]*sig[c] for c in range(3)))
        return U

if __name__ == "__main__":
    L = Lat((4,3,3)); theta = [{x: rng.standard_normal() for x in L.sites} for _ in range(3)]
    H0 = L.walk()
    print("[W1] finite rotation of the coin at every site, size s: |U H U^dagger - H[s theta]| (largest entry), with and without the scalar hop:")
    for s in (0.2, 0.1, 0.05):
        U = L.rotation(theta, s); st = [{x: s*theta[c][x] for x in L.sites} for c in range(3)]
        d1 = np.abs(U@H0@U.conj().T - L.walk(st, True)).max(); d0 = np.abs(U@H0@U.conj().T - L.walk(st, False)).max()
        print(f"     s = {s}: with the hop {d1:.3e} (/s^2 = {d1/s**2:.3f});  without {d0:.3e} (/s = {d0/s:.3f})")

    print("\n[W2] eigenvalues of H[vartheta] against those of H (largest shift), random vartheta of size s:")
    base = np.linalg.eigvalsh(H0)
    for s in (0.1, 0.05):
        st = [{x: s*theta[c][x] for x in L.sites} for c in range(3)]
        e1 = np.abs(np.linalg.eigvalsh(L.walk(st, True)) - base).max(); e0 = np.abs(np.linalg.eigvalsh(L.walk(st, False)) - base).max()
        print(f"     s = {s}: with the hop {e1:.3e} (/s^2 = {e1/s**2:.3f});  without {e0:.3e} (/s = {e0/s:.3f})")
    print("     (with the hop the rotation field is a change of coin basis at first order: the spectrum moves at second order; without it, at first)")

    print("\n[W3] stationary states found numerically: a random vector in one degenerate eigenspace of H on a 6x4x4 torus; response to a rotation at a site:")
    L2 = Lat((6,4,4)); H2 = L2.walk(); w, v = np.linalg.eigh(H2)
    target = w[np.argmin(np.abs(w - 1.0))]; sel = np.abs(w - target) < 1e-9
    coeff = rng.standard_normal(sel.sum()) + 1j*rng.standard_normal(sel.sum()); psi = v[:, sel]@coeff; psi /= np.linalg.norm(psi)
    print(f"     energy {target:.6f}, degeneracy {sel.sum()}, |H psi - E psi| = {np.abs(H2@psi - target*psi).max():.1e}")
    worst_with, without = 0, []
    for x in L2.sites[::7]:
        for c in range(3):
            b = [{y: (1.0 if (y == x and cc == c) else 0.0) for y in L2.sites} for cc in range(3)]
            r1 = np.real(psi.conj()@(L2.walk(b, True) - H2)@psi); r0 = np.real(psi.conj()@(L2.walk(b, False) - H2)@psi)
            worst_with = max(worst_with, abs(r1)); without.append(abs(r0))
    without = np.array(without)
    print(f"     largest |response| with the hop: {worst_with:.1e};  without it: largest {without.max():.3e}, {np.sum(without > 1e-6)} of {len(without)} samples above 1e-6")
    print("     (in this eigenspace some sites and axes have no torque by accident; the exact runner's state has it at every sampled site)")

    print("\n[W4] a plane wave in a slowly varying twist vartheta_a = A sin(q x_a): first-order energy shift of the hop term, averaged over the torus, is zero;")
    print("     its local value is (A q/2) cos(q x_a) cos k_a to leading order in q: a coin-independent potential (1/2) div vartheta times cos k_a.")
    n = 48; A, q, k = 0.1, 2*np.pi/n, 2*np.pi*5/n
    xs = np.arange(n); w = A*np.sin(q*(xs+1)) - A*np.sin(q*xs)
    local = 0.5*0.5*(w*np.cos(k) + np.roll(w,1)*np.cos(k))                     # Re psi^*(x) (1/2) C[w] psi(x) for psi = exp(i k x), per unit density
    pred = 0.5*A*q*np.cos(q*xs)*np.cos(k)
    print(f"     largest difference between the hop's local energy and (1/2) d(vartheta)/dx cos k on a ring of {n}: {np.abs(local-pred).max():.2e} (the values are of size {np.abs(pred).max():.2e})")
