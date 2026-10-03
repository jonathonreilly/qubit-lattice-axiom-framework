"""A41 common: the covariant charged-triplet hop family through light's links, in closed form (own code).

Closed form (derived in the report, checked against A34 c13's numerical null space in d1):
  M^(a)(theta) = alpha e_-^(a) e_a^T - conj(alpha) e_a e_-^(a)T,  alpha = t e^{i theta},
  e_-^(a) = (e_b - i e_c)/sqrt2 with (a, b, c) cyclic.  Normalization t = 1 (M^(a) has singular values 1, 1, 0).
Hop: psi^dag_x [u_{x,a} M^(a)] psi_{x+e_a} + h.c., classical link value u (zero flux: u = 1; pi flux: KS signs).
Bloch convention psi_x ~ e^{i k.x}, true displacements: one direction's block h_a(k) = e^{i k_a} M^(a) + h.c.
  zero flux: H0(k) = sum_a h_a(k)                       (3 bands)
  pi flux, 2x2x2 KS cell: H24(k) = sum_a P_a (x) h_a(k)  (24 bands; P_a = 8x8 signed shift, anticommuting)
  pi flux reduced form: H6(k) = sum_a sigma_a (x) h_a(k) (6 bands); H24 ~ 2 H6 + 2 (-H6) (checked in d1).
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import numpy as np

E3 = np.eye(3)
CYC = {0: (1, 2), 1: (2, 0), 2: (0, 1)}
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
# spin-1 in the Cartesian (vector) basis: (S^a)_{jk} = -i eps_{ajk}
SP1 = []
for a in range(3):
    m = np.zeros((3, 3), complex)
    for j in range(3):
        for k in range(3):
            m[j, k] = -1j * np.linalg.det(np.array([E3[a], E3[j], E3[k]]))
    SP1.append(m)


def e_minus(a):
    b, c = CYC[a]
    return (E3[b] - 1j * E3[c]) / np.sqrt(2)


def M_family(theta, t=1.0):
    al = t * np.exp(1j * theta)
    return [al * np.outer(e_minus(a), E3[a]) - np.conj(al) * np.outer(E3[a], e_minus(a)) for a in range(3)]


def blocks(K, M):
    """K: (..., 3) momenta; returns list of 3 arrays (..., 3, 3): h_a(k) = e^{ik_a} M^(a) + h.c."""
    out = []
    for a in range(3):
        ph = np.exp(1j * K[..., a])[..., None, None]
        out.append(ph * M[a] + np.conj(ph) * M[a].conj().T)
    return out


def H0(K, M):
    h = blocks(K, M)
    return h[0] + h[1] + h[2]


def H6(K, M):
    h = blocks(K, M)
    return sum(np.einsum("ij,...kl->...ikjl", SIG[a], h[a]).reshape(h[a].shape[:-2] + (6, 6)) for a in range(3))


CELL8 = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]


def eta(a, s):
    x, y, z = s
    return [1, (-1) ** x, (-1) ** (x + y)][a]


def H24(k, M):
    """2x2x2 KS cell, true-displacement Bloch phases; site order CELL8, internal index fastest."""
    H = np.zeros((24, 24), complex)
    for i, s in enumerate(CELL8):
        for a in range(3):
            s2 = list(s); s2[a] = (s2[a] + 1) % 2; j = CELL8.index(tuple(s2))
            T = eta(a, s) * np.exp(1j * k[a]) * M[a]
            H[3 * i:3 * i + 3, 3 * j:3 * j + 3] += T
            H[3 * j:3 * j + 3, 3 * i:3 * i + 3] += T.conj().T
    return H


CELL4 = [(x, y) for x in range(2) for y in range(2)]


def H12(k, M):
    """2x2x1 KS cell (the minimal magnetic cell; c14's layout), true-displacement Bloch phases."""
    H = np.zeros((12, 12), complex)
    for i, (x, y) in enumerate(CELL4):
        for a, (dx, dy) in enumerate(((1, 0), (0, 1), (0, 0))):
            j = CELL4.index(((x + dx) % 2, (y + dy) % 2))
            T = eta(a, (x, y, 0)) * np.exp(1j * k[a]) * M[a]
            H[3 * i:3 * i + 3, 3 * j:3 * j + 3] += T
            H[3 * j:3 * j + 3, 3 * i:3 * i + 3] += T.conj().T
    return H


def grid(n, lo=-np.pi, hi=np.pi, off=0.37):
    g = lo + (np.arange(n) + off) * (hi - lo) / n
    return np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)
