"""Exact ensemble propagation for Bell's minimal jump law (probe-5 protocol).

Two walkers, each on an L-site ring with a 2-component coin, H = sin k sigma_z per ring.
The record ensemble rho_t on the L*L joint site configurations obeys the master equation with
Bell's minimal rates max(0, J_yx)/P(x); no sampling.
"""
import numpy as np
import scipy.sparse as sp
from scipy.integrate import solve_ivp

SZ = np.array([1.0, -1.0])


def ring_H(L):
    H = np.zeros((2 * L, 2 * L), complex)
    for x in range(L):
        xp = (x + 1) % L
        for c in range(2):
            H[x * 2 + c, xp * 2 + c] += -1j * SZ[c] / 2
            H[xp * 2 + c, x * 2 + c] += +1j * SZ[c] / 2
    assert np.allclose(H, H.conj().T)
    return H


class Ring:
    def __init__(self, L):
        self.L = L
        self.H = ring_H(L)
        self.E, self.V = np.linalg.eigh(self.H)

    def U4(self, t):
        U = (self.V * np.exp(-1j * self.E * t)) @ self.V.conj().T
        return U.reshape(self.L, 2, self.L, 2)


def rot_y(theta):
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -s], [s, c]], complex)  # exp(-i theta sigma_y / 2)


def initial_wave(L, thA, thB, width=1.5, centre=12):
    x = np.arange(L)
    g = np.exp(-((x - centre) ** 2) / (2 * width ** 2))
    singlet = np.zeros((2, 2), complex)
    singlet[0, 1] = 1 / np.sqrt(2)
    singlet[1, 0] = -1 / np.sqrt(2)
    coin = rot_y(thA) @ singlet @ rot_y(thB).T
    psi = g[:, None, None, None] * g[None, :, None, None] * coin[None, None, :, :]
    psi = psi / np.sqrt((np.abs(psi) ** 2).sum())
    return psi


class Bell2:
    """Two independent rings; psi_t = (U x U) psi_0; Bell minimal rates on (xA, xB)."""

    def __init__(self, L, thA, thB, ring=None, width=1.5, centre=12):
        self.L = L
        self.ring = ring or Ring(L)
        self.psi0 = initial_wave(L, thA, thB, width, centre)

    def wave(self, t):
        U = self.ring.U4(t)
        return np.einsum('aixj,bkyl,xyjl->abik', U, U, self.psi0, optimize=True)

    def P(self, t):
        return (np.abs(self.wave(t)) ** 2).sum(axis=(2, 3))

    def currents(self, psi):
        """T_A[a,b] = J_{(a+1,b),(a,b)}, T_B[a,b] = J_{(a,b+1),(a,b)}."""
        sz = SZ[:, None, None]
        # A-direction: pair (a, a+1)
        psi_up = np.roll(psi, -1, axis=0)
        TA = np.real(np.einsum('abik,i,abik->ab', psi_up.conj(), SZ, psi))
        psi_upB = np.roll(psi, -1, axis=1)
        TB = np.real(np.einsum('abik,k,abik->ab', psi_upB.conj(), SZ, psi))
        return TA, TB

    cap = None   # optional rate cap (documented when used)

    def rates(self, t, gamma=0.0, floor=1e-300):
        psi = self.wave(t)
        P = (np.abs(psi) ** 2).sum(axis=(2, 3))
        TA, TB = self.currents(psi)
        Pinv = np.where(P > floor, 1.0 / np.maximum(P, floor), 0.0)
        rpA = np.maximum(TA, 0) * Pinv                       # (a,b)->(a+1,b)
        rmA = np.maximum(-np.roll(TA, 1, axis=0), 0) * Pinv  # (a,b)->(a-1,b)
        rpB = np.maximum(TB, 0) * Pinv
        rmB = np.maximum(-np.roll(TB, 1, axis=1), 0) * Pinv
        if self.cap is not None:
            rpA, rmA, rpB, rmB = [np.minimum(r, self.cap) for r in (rpA, rmA, rpB, rmB)]
        if gamma > 0:
            def met(Pn):
                return gamma * np.minimum(1.0, Pn * Pinv)
            rpA = rpA + met(np.roll(P, -1, axis=0))
            rmA = rmA + met(np.roll(P, 1, axis=0))
            rpB = rpB + met(np.roll(P, -1, axis=1))
            rmB = rmB + met(np.roll(P, 1, axis=1))
        return P, rpA, rmA, rpB, rmB

    def gen(self, t, gamma=0.0):
        """Sparse generator W(t) acting on flattened rho[a*L+b]."""
        L = self.L
        P, rpA, rmA, rpB, rmB = self.rates(t, gamma)
        idx = np.arange(L * L).reshape(L, L)
        rows, cols, vals = [], [], []
        def add(dst, src, v):
            rows.append(dst.ravel()); cols.append(src.ravel()); vals.append(v.ravel())
        add(np.roll(idx, -1, axis=0), idx, rpA)   # (a,b)->(a+1,b)
        add(np.roll(idx, 1, axis=0), idx, rmA)
        add(np.roll(idx, -1, axis=1), idx, rpB)
        add(idx, idx, -(rpA + rmA + rpB + rmB))
        add(np.roll(idx, 1, axis=1), idx, rmB)
        W = sp.csc_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(L * L, L * L))
        return P, W

    def evolve(self, rho0, t_eval, gamma=0.0, rtol=1e-9, atol=1e-13):
        L = self.L
        def f(t, y):
            return self.gen(t, gamma)[1] @ y
        def jac(t, y):
            return self.gen(t, gamma)[1]
        sol = solve_ivp(f, (0, t_eval[-1]), rho0.ravel(), method='Radau', jac=jac,
                        t_eval=t_eval, rtol=rtol, atol=atol)
        assert sol.success, sol.message
        return sol.y.T.reshape(len(t_eval), L, L)


def kl(rho, P):
    m = rho > 1e-300
    return float((rho[m] * np.log(rho[m] / np.maximum(P[m], 1e-300))).sum())


def tv(a, b):
    return 0.5 * float(np.abs(a - b).sum())
