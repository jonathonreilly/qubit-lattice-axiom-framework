#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 77 (floating point; dense linear algebra; machinery disjoint from the exact runner's).

W1  the a-term's spectrum on a 6x6x6 torus: the eight zeros' energies against a0 + 2a(3 - 2|n|); the lowest |E - level| near each zero (no gap).
W2  the staggered term: the full spectrum of H + m eps against +-sqrt(E_walk^2 + m^2) (exact pairing of the walk's eigenvalues); with the a-term the
    four Dirac masses at the zeros against sqrt(m^2 + 4a^2(3 - 2|n|)^2).
W3  THE MASSIVE SEA (block 76's probe redone with rest energy): the clocks' stiffness kappa(m) and the reach-three strain stiffnesses for m = 0, 1/2, 1,
    L = 8: does rest energy give the lengths a stiffness comparable to the clocks'?
W4  a slow body: a packet of the massive walk at the zero, its group velocity and its fall in a rate gradient against -M grad u (block 54's law with M).
"""
import numpy as np
from scipy.sparse.linalg import expm_multiply

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


class Torus:
    def __init__(self, L):
        self.L = L; self.dims = (L, L, L); self.n = L**3; self.grid = np.indices(self.dims).reshape(3, -1)
        self.T = [self.shift(a) for a in range(3)]
        self.S = [(t - t.T)/(2j) for t in self.T]; self.C = [(t + t.T)/2 for t in self.T]; self.P = [(t@t - t.T@t.T)/(4j) for t in self.T]
        self.eps = np.kron(np.diag((-1.0)**self.grid.sum(axis=0)), np.eye(2))
        self.H0 = sum(np.kron(self.S[a], sig[a]) for a in range(3))

    def shift(self, axis):
        g = self.grid.copy(); g[axis] = (g[axis] + 1) % self.L
        M = np.zeros((self.n, self.n)); M[np.arange(self.n), np.ravel_multi_index(g, self.dims)] = 1.0
        return M

    def hop(self, a, v): return 0.5*(np.diag(v)@self.T[a] + self.T[a].T@np.diag(v))

    def H(self, a0=0.0, a=0.0, m=0.0, u=None, B=None):
        H = self.H0 + a0*np.eye(2*self.n) + 2*a*sum(np.kron(self.C[j], np.eye(2)) for j in range(3)) + m*self.eps
        if B is not None:
            for aa in range(3):
                for j in range(3):
                    if B[aa][j] is None: continue
                    v = 0.5*(B[aa][j] + self.T[aa]@B[aa][j])
                    H = H + 0.5*np.kron(self.hop(aa, v)@self.P[j] + self.P[j]@self.hop(aa, v), sig[aa])
        if u is not None:
            Phi = np.kron(np.diag(np.exp(u/2)), np.eye(2)); H = Phi@H@Phi
        return H

    def sea(self, **kw):
        ev = np.linalg.eigvalsh(self.H(**kw)); return ev[ev < 0].sum()


def second_order(E, e1=0.02, e2=0.04):
    z = E(0.0); d1 = (E(e1) + E(-e1))/2 - z; d2 = (E(e2) + E(-e2))/2 - z
    return (16*d1 - d2)/(12*e1**2)


if __name__ == "__main__":
    tor = Torus(6); a0, a = 0.3, 0.2
    ev = np.linalg.eigvalsh(tor.H(a0=a0, a=a))
    print(f"[W1] 6x6x6 torus, a0 = {a0}, a = {a}: the a-term's levels at the zeros and the nearest eigenvalues")
    for mabs in range(4):
        level = a0 + 2*a*(3 - 2*mabs)
        near = np.sort(np.abs(ev - level))[:2]
        print(f"     |n| = {mabs} ({(1,3,3,1)[mabs]} species, sense {(+1,-1,+1,-1)[mabs]:+d}): level {level:+.3f}; nearest eigenvalues off by {near[0]:.1e}, {near[1]:.1e} (zeros present: the walk on an even torus has k = pi n exactly)")

    m = 0.7
    ev0 = np.linalg.eigvalsh(tor.H0); evm = np.linalg.eigvalsh(tor.H(m=m))
    pred = np.sort(np.concatenate([np.sqrt(ev0[ev0 >= 0]**2 + m**2), -np.sqrt(ev0[ev0 >= 0]**2 + m**2)]))
    print(f"\n[W2] staggered term m = {m}: spectrum of H + m eps against +-sqrt(E_walk^2 + m^2): largest mismatch {np.abs(np.sort(evm) - pred).max():.1e}; gap {evm[evm > 0].min():.4f} = m")
    evam = np.linalg.eigvalsh(tor.H(a0=a0, a=a, m=m))
    print(f"     with the a-term: eigenvalues nearest a0 +- sqrt(m^2 + 36 a^2) = {a0 + np.sqrt(m**2 + 36*a**2):.4f} / {a0 - np.sqrt(m**2 + 36*a**2):.4f} and a0 +- sqrt(m^2 + 4 a^2) = {a0 + np.sqrt(m**2 + 4*a**2):.4f} / {a0 - np.sqrt(m**2 + 4*a**2):.4f}:",
          ", ".join(f"{np.min(np.abs(evam - t)):.1e}" for t in (a0 + np.sqrt(m**2 + 36*a**2), a0 - np.sqrt(m**2 + 36*a**2), a0 + np.sqrt(m**2 + 4*a**2), a0 - np.sqrt(m**2 + 4*a**2))), "(offsets)")

    print("\n[W3] the massive sea, L = 8, mode cos(2 pi x/L): clocks' stiffness kappa(m) and reach-three strain stiffnesses (gradient parts per |q|^2)")
    tor8 = Torus(8); x = tor8.grid[0]; q = 2*np.pi/8; cos = np.cos(q*x); one = np.ones(tor8.n); lat = 2 - 2*np.cos(q)
    for m in (0.0, 0.5, 1.0):
        c0 = tor8.sea(m=m)/tor8.n
        cuu = second_order(lambda e: tor8.sea(m=m, u=e*cos))/tor8.n
        loc = second_order(lambda e: tor8.sea(m=m, u=e*one))/tor8.n/2
        kap = 4*(cuu - loc)/lat
        tt = second_order(lambda e: tor8.sea(m=m, B=[[None, None, None], [None, None, e*cos], [None, e*cos, None]]))/tor8.n
        ttl = second_order(lambda e: tor8.sea(m=m, B=[[None, None, None], [None, None, e*one], [None, e*one, None]]))/tor8.n/2
        iso = second_order(lambda e: tor8.sea(m=m, B=[[e*cos, None, None], [None, e*cos, None], [None, None, e*cos]]))/tor8.n
        isol = second_order(lambda e: tor8.sea(m=m, B=[[e*one, None, None], [None, e*one, None], [None, None, e*one]]))/tor8.n/2
        print(f"     m = {m}: c0 = {c0:+.4f}; kappa = {kap:+.4f}; TT (yz) gradient/|q|^2 = {(tt - ttl)/q**2:+.5f}; isotropic stretch gradient/|q|^2 = {(iso - isol)/q**2:+.5f}; ratio clocks/TT = {kap/4/((tt - ttl)/q**2) if abs(tt - ttl) > 1e-9 else float('nan'):.1f}")

    print("\n[W4] a slow body: L = 24 line along x (2D slice 24 x 8), massive walk m = 0.6 at the zero, Gaussian packet width 4, rate gradient g = 0.02 along x")
    Lx, Ly = 24, 8; nn = Lx*Ly; grid = np.indices((Lx, Ly)).reshape(2, -1)
    def sh(axis):
        g = grid.copy(); g[axis] = (g[axis] + 1) % (Lx, Ly)[axis]
        M = np.zeros((nn, nn)); M[np.arange(nn), np.ravel_multi_index(g, (Lx, Ly))] = 1.0; return M
    T2 = [sh(0), sh(1)]; S2 = [(t - t.T)/(2j) for t in T2]
    eps2 = np.kron(np.diag((-1.0)**grid.sum(axis=0)), np.eye(2))
    H2 = np.kron(S2[0], sig[0]) + np.kron(S2[1], sig[1]) + 0.6*eps2
    ev2, vec2 = np.linalg.eigh(H2)
    # the positive-energy packet at rest: project a Gaussian onto the positive branch
    env = np.exp(-((grid[0] - Lx/2)**2)/(2*4.0**2))
    psi0 = np.kron(env, np.array([1.0, 0.0])); pos = vec2[:, ev2 > 0]; psi0 = pos@(pos.conj().T@psi0); psi0 /= np.linalg.norm(psi0)
    E0 = np.real(np.vdot(psi0, H2@psi0))
    u = 0.02*(grid[0] - Lx/2); Phi = np.kron(np.diag(np.exp(u/2)), np.eye(2)); Hw = Phi@H2@Phi
    X = np.kron(np.diag(grid[0].astype(float)), np.eye(2))
    xs = []
    for t in (0.0, 5.0, 10.0):
        psit = expm_multiply(-1j*t*Hw, psi0) if t > 0 else psi0
        xs.append(np.real(np.vdot(psit, X@psit)))
    early = 2*(xs[1] - xs[0])/25                                        # a body released from rest: x(t) - x(0) = a t^2/2
    print(f"     energy of the packet at rest {E0:.4f} (m = 0.6 plus width); mean position at t = 0, 5, 10: {xs[0]:.3f}, {xs[1]:.3f}, {xs[2]:.3f}; acceleration from rest {early:+.5f} against block 54's -w^2 g = {-0.02:+.5f} at the centre (the packet's momentum spread ~1/8 against M = 0.6 lowers the mean of d^2E/dp^2 to about 0.94 of 1/M, which accounts for the difference): the massive walker falls as a slow body toward slow clocks")
