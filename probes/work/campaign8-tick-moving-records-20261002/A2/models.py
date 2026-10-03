"""Step operators used in the checks.

E1  2x2 strictly local product walk  U = Sx Sy Sz,  S_j = exp(-i k_j sigma_j)
    (each S_j = spin-conditional shift: spin up along j hops +e_j, spin down hops -e_j).
E3  2x2 quasi-local covariant map     U = (d4 + i d.sigma)/|d|,
    d = (sin kx, sin ky, sin kz), d4 = m - cos kx - cos ky - cos kz  (m=2).  NOT strictly local.
E4  2x2 strictly local but NON-unitary  M = i d4 + d.sigma   (inverse is not strictly local).
"""
import numpy as np
from wlib import s0, sx, sy, sz, SIG


def E1(K):
    K = np.atleast_2d(K)
    c = np.cos(K)
    s = np.sin(K)
    S = [c[:, j, None, None] * s0 - 1j * s[:, j, None, None] * SIG[j] for j in range(3)]
    dS = [-s[:, j, None, None] * s0 - 1j * c[:, j, None, None] * SIG[j] for j in range(3)]
    U = S[0] @ S[1] @ S[2]
    dU = np.stack([dS[0] @ S[1] @ S[2], S[0] @ dS[1] @ S[2], S[0] @ S[1] @ dS[2]])
    return U, dU


def _d(K, m):
    K = np.atleast_2d(K)
    d = np.sin(K)  # (M,3)
    d4 = m - np.cos(K).sum(1)
    dd = np.cos(K)  # d d_a / d k_a (diagonal)
    dd4 = np.sin(K)  # d d4 / d k_j
    return d, d4, dd, dd4


def E3(K, m=2.0, sign=+1):
    """sign=-1 gives the mirror-image map (d.sigma -> -d.sigma)."""
    d, d4, dd, dd4 = _d(K, m)
    Nm = d4[:, None, None] * s0 + sign * 1j * np.einsum("ma,aij->mij", d, SIG)
    r = np.sqrt(d4 ** 2 + (d ** 2).sum(1))
    U = Nm / r[:, None, None]
    dU = []
    for j in range(3):
        dN = dd4[:, j, None, None] * s0 + sign * 1j * dd[:, j, None, None] * SIG[j]
        dr = (d4 * dd4[:, j] + d[:, j] * dd[:, j]) / r
        dU.append(dN / r[:, None, None] - Nm * (dr / r ** 2)[:, None, None])
    return U, np.stack(dU)


def E4(K, m=2.0):
    d, d4, dd, dd4 = _d(K, m)
    M = 1j * d4[:, None, None] * s0 + np.einsum("ma,aij->mij", d, SIG)
    dM = np.stack([1j * dd4[:, j, None, None] * s0 + dd[:, j, None, None] * SIG[j] for j in range(3)])
    return M, dM
