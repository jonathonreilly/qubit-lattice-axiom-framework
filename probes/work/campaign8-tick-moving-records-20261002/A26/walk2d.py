"""A26 walk2d: A10's 2D time-symmetric KS-signed partial-swap cycle, one excitation, with FIXED field couplings
(supplied toy; nothing adopted).

Cell = 2x2 sites, internal index n = 2*i + j for site (2cx+i, 2cy+j); operators are kron(x-bit op, y-bit op).
Bond generator on (p, q) with amplitude t = phr - 1j*phi :  t |p><q| e^{iK.d} + h.c.   (d = cell offset of q)
Gate = exp(-i * generator); bonds of one layer are disjoint, so a layer is the exp of its summed generator.
KS signs (A10 S8): eta_x = 1, eta_y = (-1)^{s_x}.  One-site mass: phase exp(-i (mu/2) N eps), eps = (-1)^{x+y}.
Cycle (A10 S9 time-symmetric blocks): Mh, [xe th/2, xo th, xe th/2], [ye th/2, yo th, ye th/2], Mh.
Field couplings (task 1): one-site terms x N ; bond terms x N_b * e_b (frame), e_b = 1 - h_aa/2 on an a-bond;
shear frame: x-block conjugated by R(beta) = S P(beta) S^dag (S = exp(-i pi/4 X_y) unsigned intra-cell y-gate,
P(beta) = exp(-i beta Z_y X_x) intra-cell x-gate with sign (-1)^y), which equals exp(i beta X_x Y_y).
"""
import numpy as np
from scipy.linalg import expm

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1.0 + 0j, -1.0])
kr = np.kron


def site(i, j):
    return 2 * i + j


def bond_gen(K, bonds):
    """bonds: list of (p, q, d, t) with p, q internal indices, d = (dx, dy) cell offset of q, t complex amplitude"""
    H = np.zeros((4, 4), complex)
    for p, q, d, t in bonds:
        ph = np.exp(1j * (K[0] * d[0] + K[1] * d[1]))
        H[p, q] += t * ph
        H[q, p] += np.conj(t * ph)
    return H


def layer(K, kind, amp):
    """kind in {'xe','xo','ye','yo'}; amp(i_or_j) -> complex amplitude for the bond in row j (x-bonds) / column i (y-bonds),
    KS sign NOT included (caller includes it)."""
    bonds = []
    if kind == 'xe':
        for j in (0, 1):
            bonds.append((site(0, j), site(1, j), (0, 0), amp(j)))
    elif kind == 'xo':
        for j in (0, 1):
            bonds.append((site(1, j), site(0, j), (1, 0), amp(j)))
    elif kind == 'ye':
        for i in (0, 1):
            bonds.append((site(i, 0), site(i, 1), (0, 0), amp(i)))
    elif kind == 'yo':
        for i in (0, 1):
            bonds.append((site(i, 1), site(i, 0), (0, 1), amp(i)))
    return expm(-1j * bond_gen(K, bonds))


EPS = np.diag([(-1.0) ** (i + j) for i in (0, 1) for j in (0, 1)]).astype(complex)


def cycle(K, th=0.3, mu=0.0, N=1.0, ex=1.0, ey=1.0, dx=0.0, dy=0.0, st=False,
          imx=0.0, imy=0.0, beta=0.0, ks=True):
    """Uniform-field Bloch cycle.
    th: base dose; N: lapse; ex, ey: frame factors on x/y bonds; dx, dy: two-site (staggered) mass parts of the angles;
    st: if True, frame factor multiplies only the uniform part (stress coupling), else whole angle (operator support);
    imx, imy: period-2 imaginary-hop (taste-graded shear) amplitudes, relative to th;
    beta: frame-rotation angle of the x-block (R(beta) sandwich)."""
    sy = (lambda i: (-1.0) ** i) if ks else (lambda i: 1.0)
    def ang(e, dlt, par):           # par = +1 even bonds, -1 odd bonds
        return N * ((th * e + par * dlt) if st else (th + par * dlt) * e)
    axe, axo = ang(ex, dx, +1), ang(ex, dx, -1)
    aye, ayo = ang(ey, dy, +1), ang(ey, dy, -1)
    # x-block: real part sign +1; imaginary period-2 part with (-1)^y pattern
    # period-2 staggered Peierls phases (s1_span): x-bonds imaginary amplitude pattern (-1)^(x+y) of the lower site
    Lxe = layer(K, 'xe', lambda j: 0.5 * (axe - 1j * imx * th * N * (-1.0) ** j))
    Lxo = layer(K, 'xo', lambda j: (axo + 1j * imx * th * N * (-1.0) ** j))
    Ux = Lxe @ Lxo @ Lxe
    # y-block: real part with KS sign (-1)^x; imaginary period-2 part WITHOUT the KS sign
    # y-bonds: imaginary pattern -(-1)^y of the lower site, no KS sign
    Lye = layer(K, 'ye', lambda i: 0.5 * (aye * sy(i) + 1j * imy * th * N))
    Lyo = layer(K, 'yo', lambda i: (ayo * sy(i) - 1j * imy * th * N))
    Uy = Lye @ Lyo @ Lye
    if beta != 0.0:
        S = expm(-1j * (np.pi / 4) * kr(I2, X))
        P = expm(-1j * beta * kr(X, Z))
        R = S @ P @ S.conj().T
        Ux = R @ Ux @ R.conj().T
    Mh = np.diag(np.exp(-0.5j * mu * N * np.diag(EPS)))
    return Mh @ Uy @ Ux @ Mh


def quasi(U):
    w = np.linalg.eigvals(U)
    return np.sort(-np.angle(w))


KSTAR = np.array([np.pi, np.pi])
