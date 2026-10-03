"""Vectorized Bloch builder for layer-list cycles (one-excitation sector, 2x2x2 cell).

A cycle is a list of layers (axis, par, theta); the first listed acts first.
signed=True puts the Kogut-Susskind signs eta_y=(-1)^{s_x}, eta_z=(-1)^{s_x+s_y} on the gates.
"""
import numpy as np

def _pairs(axis, signed):
    out = []
    for pz in (0, 1):
        for py in (0, 1):
            for px in (0, 1):
                p = [px, py, pz]
                if p[axis] != 0:
                    continue
                q = list(p); q[axis] = 1
                i0 = p[0] + 2 * p[1] + 4 * p[2]
                i1 = q[0] + 2 * q[1] + 4 * q[2]
                if not signed or axis == 0:
                    e = 1.0
                elif axis == 1:
                    e = (-1.0) ** p[0]
                else:
                    e = (-1.0) ** (p[0] + p[1])
                out.append((i0, i1, e))
    return out

PAIRS = {(a, sg): _pairs(a, sg) for a in range(3) for sg in (False, True)}

def layers_U(K, layers, signed):
    """K: (N,3) array. Returns (N,8,8) cycle matrices."""
    K = np.atleast_2d(K)
    N = K.shape[0]
    U = np.broadcast_to(np.eye(8, dtype=complex), (N, 8, 8)).copy()
    for (a, par, th) in layers:
        c, s = np.cos(th), np.sin(th)
        L = np.zeros((N, 8, 8), complex)
        for (i0, i1, e) in PAIRS[(a, signed)]:
            L[:, i0, i0] = c
            L[:, i1, i1] = c
            if par == 0:
                L[:, i0, i1] = -1j * e * s
                L[:, i1, i0] = -1j * e * s
            else:
                L[:, i1, i0] = -1j * e * s * np.exp(1j * K[:, a])
                L[:, i0, i1] = -1j * e * s * np.exp(-1j * K[:, a])
        U = np.exp(1j * th) * (L @ U)
    return U

def plain6(th, order=(0, 1, 2)):
    return [(a, p, th) for a in order for p in (0, 1)]

def strang9(th, order=(0, 1, 2)):
    out = []
    for a in order:
        out += [(a, 0, th / 2), (a, 1, th), (a, 0, th / 2)]
    return out

def nu3(layers, signed, N=20, h=1e-4):
    """3D winding number (1/24 pi^2) int eps_ijk tr(U^-1 d_i U U^-1 d_j U U^-1 d_k U), midpoint grid."""
    g = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    KK = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T
    U0 = layers_U(KK, layers, signed)
    Ui = np.conj(np.transpose(U0, (0, 2, 1)))
    Ad = []
    for i in range(3):
        d = np.zeros(3); d[i] = h
        dU = (layers_U(KK + d, layers, signed) - layers_U(KK - d, layers, signed)) / (2 * h)
        Ad.append(Ui @ dU)
    # eps_ijk tr(A_i A_j A_k) = 3 tr(A_x[A_y,A_z]) (cyclic)
    X, Y, Z = Ad
    dens = 3 * np.trace(X @ (Y @ Z - Z @ Y), axis1=1, axis2=2)
    vol = (2 * np.pi / N) ** 3
    return (dens.sum() * vol / (24 * np.pi ** 2))
