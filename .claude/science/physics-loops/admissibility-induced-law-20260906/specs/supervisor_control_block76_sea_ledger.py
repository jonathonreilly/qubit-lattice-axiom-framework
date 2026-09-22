#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 76 (floating point; dense linear algebra; machinery disjoint from the exact runner's).

THE READING PROBED: every negative-energy state of the walk occupied; E_sea = sum of the negative eigenvalues of H_w = phi H phi (with strains through
the reach-three coupling) booked as the field's term of the ledger. Second-order response to a mode cos(q.x) of the rates u (phi = e^{u/2}) and of
strains B (bond value = mean of the two ends), by symmetric differences with two amplitudes (quartic removed); the LOCAL part is the same mode's
uniform second derivative times the mode's mean square; the remainder is the gradient part.
W1  the volume term c0 = E_sea/site and the rates' polarisation Pi(q): gradient part / lattice |q|^2 for several q, directions and L (the clocks' stiffness kappa).
W2  the strains' polarisation under reach three: transverse-traceless modes and the isotropic stretch.
W3  the chessboard of clocks at finite amplitude (exact zero, by the runner's T1) and the corner-type modes.
W4  the linearised static law with the measured c0 and kappa: the clock at a unit body, volume term kept and removed; gamma_ind = 1/kappa.
"""
import numpy as np

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


class Torus:
    def __init__(self, L):
        self.L = L; self.dims = (L, L, L); self.n = L**3; self.grid = np.indices(self.dims).reshape(3, -1)
        self.T = [self.shift(a) for a in range(3)]
        self.S = [(t - t.T)/(2j) for t in self.T]; self.P = [(t@t - t.T@t.T)/(4j) for t in self.T]
        self.H0 = sum(np.kron(self.S[a], sig[a]) for a in range(3))

    def shift(self, axis):
        g = self.grid.copy(); g[axis] = (g[axis] + 1) % self.L
        M = np.zeros((self.n, self.n)); M[np.arange(self.n), np.ravel_multi_index(g, self.dims)] = 1.0
        return M

    def hop(self, a, v): return 0.5*(np.diag(v)@self.T[a] + self.T[a].T@np.diag(v))

    def H(self, u=None, B=None):
        H = self.H0.copy()
        if B is not None:
            for a in range(3):
                for j in range(3):
                    if B[a][j] is None: continue
                    v = 0.5*(B[a][j] + self.T[a]@B[a][j])
                    H = H + 0.5*np.kron(self.hop(a, v)@self.P[j] + self.P[j]@self.hop(a, v), sig[a])
        if u is not None:
            Phi = np.kron(np.diag(np.exp(u/2)), np.eye(2)); H = Phi@H@Phi
        return H

    def sea(self, **kw):
        ev = np.linalg.eigvalsh(self.H(**kw)); return ev[ev < 0].sum()


def second_order(E, e1=0.02, e2=0.04):
    d1 = (E(e1) + E(-e1))/2 - E(0.0); d2 = (E(e2) + E(-e2))/2 - E(0.0)
    return (16*d1 - d2)/(12*e1**2)


if __name__ == "__main__":
    print("[W1] volume term and the rates' polarisation (reach three absent: pure rates); per site; gradient part = total - c0 * (mean square)/2")
    kappas = []
    for L, modes in ((6, [(1, 0, 0)]), (8, [(1, 0, 0), (2, 0, 0)]), (10, [(1, 0, 0), (2, 0, 0)]), (12, [(1, 0, 0), (2, 0, 0), (3, 0, 0), (1, 1, 0), (1, 1, 1), (2, 2, 0)])):
        tor = Torus(L); E00 = tor.sea(); c0 = E00/tor.n
        line = []
        for mvec in modes:
            q = 2*np.pi*np.array(mvec)/L; cos = np.cos(q@tor.grid)
            c2 = second_order(lambda e: tor.sea(u=e*cos))/tor.n
            lat_q2 = float(sum(2 - 2*np.cos(qi) for qi in q))
            grad = c2 - c0/4
            line.append(f"{mvec}: Pi = {c2:+.5f}, gradient/|q|^2_lat = {grad/lat_q2:+.5f}")
            if L == 12: kappas.append(4*grad/lat_q2)
        print(f"     L = {L}: c0 = {c0:.5f}; " + "; ".join(line))
    kappa = float(np.mean(kappas)); c0_12 = Torus(12).sea()/12**3
    print(f"     clocks' stiffness kappa (coefficient of (1/2) sum_bonds (u_x - u_y)^2), L = 12, mean over six modes: {kappa:.4f} (spread {np.ptp(kappas):.4f})")

    print("\n[W2] strains under reach three, L = 8, q = 2 pi (1,0,0)/8: second order per site, local part, gradient part / |q|^2")
    tor = Torus(8); E00 = tor.sea(); x = tor.grid[0]; q = 2*np.pi/8; cos = np.cos(q*x); one = np.ones(tor.n)
    for label, mk in (("TT cross (yz)", lambda f: [[None, None, None], [None, None, f], [None, f, None]]), ("TT plus (yy - zz)", lambda f: [[None, None, None], [None, f, None], [None, None, -f]]), ("isotropic stretch", lambda f: [[f, None, None], [None, f, None], [None, None, f]])):
        c2 = second_order(lambda e: tor.sea(B=mk(e*cos)))/tor.n
        loc = second_order(lambda e: tor.sea(B=mk(e*one)))/tor.n/2
        print(f"     {label:18s}: total {c2:+.6f}; local {loc:+.6f}; gradient/|q|^2 = {(c2 - loc)/q**2:+.6f}")

    print("\n[W3] chessboard of clocks u = eps (-1)^(x+y+z), L = 8: E_sea(eps) - E_sea(0) at eps = 0.25, 0.5, 1.0 (exactly zero by T1); corner-type modes' second order")
    tor = Torus(8); E00 = tor.sea(); chess = np.cos(np.pi*tor.grid.sum(axis=0))
    print("     chessboard:", [f"{tor.sea(u=e*chess) - E00:+.2e}" for e in (0.25, 0.5, 1.0)])
    for label, u in (("cos(pi x)", np.cos(np.pi*tor.grid[0])), ("cos(pi(x + y))", np.cos(np.pi*(tor.grid[0] + tor.grid[1])))):
        c2 = second_order(lambda e: tor.sea(u=e*u))/tor.n
        print(f"     {label:15s}: second order {c2:+.5f}; local part c0/2 = {E00/tor.n/2:+.5f}; gradient part {c2 - E00/tor.n/2:+.5f} (= |c0|/2 x |q|^2_lat/12 = {abs(E00/tor.n)/2*(4 if 'x)' in label else 8)/12:+.5f})")

    print(f"\n[W4] linearised static law (c0 + kappa q^2_lat) u_q = -m/N with c0 = {c0_12:.4f}, kappa = {kappa:.4f}, L = 12, unit body at the origin:")
    L = 12; ks = 2*np.pi*np.fft.fftfreq(L)*L/L
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing="ij"); q2 = (2 - 2*np.cos(KX)) + (2 - 2*np.cos(KY)) + (2 - 2*np.cos(KZ))
    for label, c in (("volume term kept", c0_12), ("volume term removed", 0.0)):
        with np.errstate(divide="ignore"):
            uq = np.where(q2 > 1e-12, -1.0/(c + kappa*q2), 0.0)
        u = np.real(np.fft.ifftn(uq))
        print(f"     {label:20s}: u at the body {u[0,0,0]:+.4f}, neighbour {u[1,0,0]:+.4f}, distance 3 {u[3,0,0]:+.4f} -> " + ("clock FASTER at the body (repulsion)" if u[0,0,0] > 0 else "clock SLOWER at the body (attraction)"))
    print(f"     c0 + 12 kappa = {c0_12 + 12*kappa:+.4f} (the zone corner; exactly zero for the true second variation by T1); induced coupling with the volume term removed: gamma_ind = 1/kappa = {1/kappa:.2f}")
