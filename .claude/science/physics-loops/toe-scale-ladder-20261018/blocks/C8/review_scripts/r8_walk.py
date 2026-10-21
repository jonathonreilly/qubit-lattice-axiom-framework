"""Reviewer's own implementation of the supplied walk (parent note Theorems 1-3) by a generic
matrix route: build the 4x4 unitary U(k) explicitly, diagonalise it, take the principal-branch
generator H = V diag(omega) V^dag (U = exp(-i H)), read off the spin part of H by traces, and
evaluate second-order vacuum-energy bubbles by explicit band sums (no Clifford trace formula).
Nothing is imported from the author's scripts."""
from __future__ import annotations
import numpy as np

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2)
TAU = [np.kron(s1, I2), np.kron(s2, I2), np.kron(s3, I2)]          # flavour (x) spin
T3S = [np.kron(s3, s) for s in (s1, s2, s3)]                        # tau3 sigma_a  (alpha_a = - tau3 sigma_a)


def Gram(b0, b1, b2):   # parent Theorem 2
    return np.array([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
                     [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
                     [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
                     [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])


def bstar():
    """b0 = 11/30, b2 = 3/20, b1 = sqrt(u*), u* smallest positive root of det G (parent Theorem 3).
    Root found here by sampling det G on a fine u grid and bisection (own route)."""
    b0, b2 = 11/30, 3/20
    dg = lambda u: np.linalg.det(Gram(b0, np.sqrt(u), b2))
    us = np.linspace(1e-6, 0.2, 20001); vals = np.array([dg(u) for u in us])
    i = np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0][0]
    lo, hi = us[i], us[i+1]
    for _ in range(200):
        mid = 0.5*(lo + hi)
        if np.sign(dg(mid)) == np.sign(dg(lo)): lo = mid
        else: hi = mid
    return np.array([b0, np.sqrt(0.5*(lo+hi)), b2])


r5, r6, r15 = np.sqrt(5), np.sqrt(6), np.sqrt(15)
B_GOLD = np.array([(9*r5 - 5)/38, (5*r5 - 7)/19, (71 - 29*r5)/38])
B_ISO = np.array([(r6 + 2*r15)/27, (5*r6 - 2*r15)/27, (2*r15 - 2*r6)/27])
PHI0 = np.array([1.0, 3, 3, 1])


class Walk:
    def __init__(self, b, theta=0.0, hhat=(0.0, 1.0)):
        self.b = np.asarray(b, float)
        self.s = self.b[0] + 2*self.b[1] + self.b[2]
        G = Gram(*self.b)
        ev = np.linalg.eigvalsh(G)
        assert ev.min() > -1e-12 and np.sum(ev > 1e-10) == 3, ev
        F0 = G @ PHI0                                   # f row is fixed: F^T e_f = G phi0
        assert abs(F0 @ PHI0 - 1) < 1e-12
        Rm = G - np.outer(F0, F0)
        w, V = np.linalg.eigh(Rm)
        assert w.min() > -1e-12 and np.sum(w > 1e-10) == 2
        idx = np.argsort(w)[-2:]
        self.Fh = (V[:, idx]*np.sqrt(np.clip(w[idx], 0, None))).T   # h rows (any O(2) frame)
        self.F0 = F0
        hh = np.asarray(hhat, float)
        Mh = hh[0]*TAU[0] + hh[1]*TAU[1]
        self.M = np.cos(theta/2)*np.eye(4) + 1j*np.sin(theta/2)*Mh   # exp(i theta hhat.tau/2)
        self.theta = theta

    def U(self, k):
        c = np.cos(k); s = np.sin(k)
        phi = np.stack([np.ones(len(k)), c.sum(1), c[:, 0]*c[:, 1] + c[:, 0]*c[:, 2] + c[:, 1]*c[:, 2],
                        c[:, 0]*c[:, 1]*c[:, 2]], 1)
        f = phi @ self.F0; h = phi @ self.Fh.T
        b0, b1, b2 = self.b
        g = np.stack([s[:, a]*(b0 + b1*(c[:, (a+1) % 3] + c[:, (a+2) % 3]) + b2*c[:, (a+1) % 3]*c[:, (a+2) % 3])
                      for a in range(3)], 1)
        U = f[:, None, None]*np.eye(4) + 1j*(h[:, 0, None, None]*TAU[0] + h[:, 1, None, None]*TAU[1])
        U = U + 1j*sum(g[:, a, None, None]*T3S[a] for a in range(3))
        if self.theta != 0.0:
            U = self.M[None] @ U @ self.M[None]
        return U

    def bands(self, k):
        """omega (n,4) and eigenvectors (n,4,4) of the principal generator H, U = exp(-iH)."""
        U = self.U(k)
        A = (U - np.conj(np.transpose(U, (0, 2, 1))))/(2j)          # Hermitian, eigenvalues +-|x|
        lam, V = np.linalg.eigh(A)
        d = np.einsum('nji,njk,nki->ni', np.conj(V), U, V)            # <v|U|v> = exp(-i omega)
        om = -np.angle(d)
        return om, V

    def H(self, k):
        om, V = self.bands(k)
        return np.einsum('nij,nj,nkj->nik', V, om, np.conj(V))


def vertex(walk, k, eps, kind):
    """Perturbation symbol at the midpoint k."""
    H = walk.H(k)
    if kind == 'M1':
        P = np.stack([-np.real(np.einsum('nij,ji->n', H, T3S[j]))/4 for j in range(3)], 1)   # H_spin = alpha_j P_j
        w = P @ np.asarray(eps).T                                    # w_b = eps_bi P_i
        # delta H = -(1/2) h_bi alpha_b P_i = +(1/2) eps_bi tau3 sigma_b P_i
        return 0.5*sum(w[:, b, None, None]*T3S[b] for b in range(3))
    if kind == 'L1':
        return H
    raise ValueError(kind)


def bubble(walk, Vm, ka, kb, ba=None, bb=None):
    """sum over (unocc a, occ b) and (occ a, unocc b) of |<i_a|V|j_b>|^2 / gap: the author's F(k,t)."""
    oa, Va = walk.bands(ka) if ba is None else ba
    ob, Vb = walk.bands(kb) if bb is None else bb
    Mx = np.einsum('nji,njk,nkl->nil', np.conj(Va), Vm, Vb)
    m2 = np.abs(Mx)**2
    occa = oa < 0; occb = ob < 0
    gap = oa[:, :, None] - ob[:, None, :]
    w = np.where((~occa)[:, :, None] & occb[:, None, :], 1/np.where(gap == 0, 1, gap), 0.0)
    w = w + np.where(occa[:, :, None] & (~occb)[:, None, :], -1/np.where(gap == 0, 1, gap), 0.0)
    return np.sum(m2*w, axis=(1, 2))


def tt_basis(qh):
    qh = np.asarray(qh, float); qh = qh/np.linalg.norm(qh)
    tmp = np.array([1.0, 0, 0]) if abs(qh[0]) < 0.9 else np.array([0, 1.0, 0])
    u1 = np.cross(qh, tmp); u1 /= np.linalg.norm(u1); u2 = np.cross(qh, u1)
    eA = (np.outer(u1, u1) - np.outer(u2, u2))/np.sqrt(2)
    eB = (np.outer(u1, u2) + np.outer(u2, u1))/np.sqrt(2)
    return qh, eA, eB
