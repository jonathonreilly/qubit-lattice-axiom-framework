"""A10 shared toy: cycling brickwork of partner pairs on Z^3, one qubit per site.

One-excitation sector, 2x2x2 cell, Bloch form.  In-cell index i = px + 2 py + 4 pz.
Bloch convention: psi(2n + p) = exp(i K.n) phi_p  (K = cell momentum, period 2 pi).

Layer (a, par): partner pairs (s, s+e_a) with s_a = par mod 2, gate on the pair's
one-excitation block  u = exp(i th) [[c, -i eta s], [-i eta s, c]]   (c=cos th, s=sin th)
which is the one-excitation block of the partial swap exp(-i th SWAP) (eta=+1),
relative to the vacuum phase.  eta = staggered sign of the bond (eta=1 for the plain cycle;
KS signs eta_x=1, eta_y=(-1)^{s_x}, eta_z=(-1)^{s_x+s_y} for the signed cycle).
"""
import numpy as np

def idx(p):
    return p[0] + 2 * p[1] + 4 * p[2]

def eta(axis, p, signed):
    if not signed:
        return 1.0
    if axis == 0:
        return 1.0
    if axis == 1:
        return (-1.0) ** p[0]
    return (-1.0) ** (p[0] + p[1])

def layer(K, axis, par, th, signed=False):
    """8x8 Bloch matrix of one brickwork layer."""
    c, s = np.cos(th), np.sin(th)
    L = np.zeros((8, 8), complex)
    for pz in (0, 1):
        for py in (0, 1):
            for px in (0, 1):
                p = [px, py, pz]
                if p[axis] != 0:
                    continue
                q = list(p); q[axis] = 1           # partner inside cell (par=0) or the
                i0, i1 = idx(p), idx(q)            # p_a=1 site of the cell to the left (par=1)
                e = eta(axis, p, signed)           # eta does not depend on s_a
                if par == 0:
                    L[i0, i0] += c; L[i1, i1] += c
                    L[i0, i1] += -1j * e * s; L[i1, i0] += -1j * e * s
                else:
                    # bond (2n + q, 2(n+e_a) + p): site q of cell n with site p of cell n+e_a
                    L[i0, i0] += c; L[i1, i1] += c
                    L[i1, i0] += -1j * e * s * np.exp(1j * K[axis])   # row q(cell n) <- p(cell n+e_a)
                    L[i0, i1] += -1j * e * s * np.exp(-1j * K[axis])  # row p(cell n) <- q(cell n-e_a)
    return np.exp(1j * th) * L

def cycle(K, th_e, th_o=None, signed=False, order=(0, 1, 2), pars=(0, 1)):
    """U = product of layers; the first listed layer acts first."""
    if th_o is None:
        th_o = th_e
    U = np.eye(8, dtype=complex)
    for a in order:
        for par in pars:
            th = th_e if par == 0 else th_o
            U = layer(K, a, par, th, signed) @ U
    return U

def W1(K, th_e, th_o=None):
    """1D brickwork walk W = w_o w_e on the 2-site cell (a=even, b=odd)."""
    if th_o is None:
        th_o = th_e
    ce, se, co, so = np.cos(th_e), np.sin(th_e), np.cos(th_o), np.sin(th_o)
    we = np.exp(1j * th_e) * np.array([[ce, -1j * se], [-1j * se, ce]])
    wo = np.exp(1j * th_o) * np.array([[co, -1j * so * np.exp(-1j * K)],
                                       [-1j * so * np.exp(1j * K), co]])
    return wo @ we

def phases(U):
    """sorted eigenphases in (-pi, pi]"""
    return np.sort(np.angle(np.linalg.eigvals(U)))
