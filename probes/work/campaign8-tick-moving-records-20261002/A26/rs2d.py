"""A26 rs2d: real-space 2D stepper for A10's time-symmetric KS-signed partial-swap cycle (one excitation) with FIXED
field couplings read from static site fields (supplied toy; nothing adopted).
Site fields: N (lapse), hxx, hyy (diagonal frame), beta (frame rotation of the x-block, per cell), imx/imy (period-2).
Bond (p, q), amplitude t: p' = cos|t| p - i sin|t|/|t| t q ;  q' = -i sin|t|/|t| conj(t) p + cos|t| q.
Couplings for bond angles (rule):
  'field'  : th0 * Nb * eb            (lapse x frame;  Nb = endpoint mean, eb = 1 - (h+h')/4)
  'lapse'  : th0 * Nb                 (A18's OR rule)
  'frame'  : th0 * eb
  'and'    : th0 * N N'               (A18's product rule, for reference)
Two-site mass (staggered angle part delta on x-bonds): mode 'os' (operator support: whole angle x Nb eb) or
'st' (stress: frame only on the uniform part, angle = Nb (th0 eb +- delta)).
One-site mass: phase exp(-i (mu/2) N eps) before and after the bond blocks.
"""
import numpy as np


def gate(p, q, t):
    a = np.abs(t)
    c = np.cos(a)
    s = np.where(a > 0, np.sin(a) / np.where(a > 0, a, 1.0), 1.0) * t
    return c * p - 1j * s * q, -1j * np.conj(s) * p + c * q


class Walk2D:
    def __init__(self, Lx, Ly, th0, N=None, hxx=None, hyy=None, mu=0.0, delta=0.0, mode='os', rule='field',
                 beta=None, imx=0.0, imy=0.0):
        self.Lx, self.Ly = Lx, Ly
        one = np.ones((Lx, Ly))
        N = one if N is None else N
        hxx = 0 * one if hxx is None else hxx
        hyy = 0 * one if hyy is None else hyy
        x = np.arange(Lx)[:, None] * np.ones((1, Ly))
        y = np.ones((Lx, 1)) * np.arange(Ly)[None, :]
        eps = (-1.0) ** (x + y)
        self.mh = np.exp(-0.5j * mu * N * eps)
        # x bonds from site (x,y) to (x+1,y)
        Nx = 0.5 * (N + np.roll(N, -1, 0)); ex = 1 - 0.25 * (hxx + np.roll(hxx, -1, 0))
        Ny = 0.5 * (N + np.roll(N, -1, 1)); ey = 1 - 0.25 * (hyy + np.roll(hyy, -1, 1))
        prodx = N * np.roll(N, -1, 0); prody = N * np.roll(N, -1, 1)
        def fac(Nb, eb, prod):
            return {'field': Nb * eb, 'lapse': Nb, 'frame': eb, 'and': prod}[rule]
        fx, fy = fac(Nx, ex, prodx), fac(Ny, ey, prody)
        par_x = (-1.0) ** x                     # +1 on even x-bonds, -1 on odd x-bonds
        if mode == 'os':
            ax = (th0 + par_x * delta) * fx
        else:                                   # stress coupling: frame only on the uniform (momentum-carrying) part
            Nb = {'field': Nx, 'lapse': Nx, 'frame': 1.0, 'and': np.sqrt(prodx)}[rule]
            eb = {'field': ex, 'lapse': 1.0, 'frame': ex, 'and': np.sqrt(prodx)}[rule]
            ax = Nb * (th0 * eb + par_x * delta)
        ay = th0 * fy * (-1.0) ** x             # KS sign eta_y = (-1)^x
        # period-2 staggered Peierls phases (taste-graded shear, s1_span patterns)
        ax = ax - 1j * imx * th0 * fx * (-1.0) ** (x + y)
        ay = ay + 1j * imy * th0 * fy * (-1.0) ** y
        self.tx_e = 0.5 * ax[0::2, :]; self.tx_o = ax[1::2, :]
        self.ty_e = 0.5 * ay[:, 0::2]; self.ty_o = ay[:, 1::2]
        self.beta = None
        if beta is not None:
            # R(beta) = S P(beta) S^dag on each cell: S = exp(-i pi/4 X_y) (unsigned intra-cell y-gate),
            # P = exp(-i beta Z_y X_x) (intra-cell x-gate, sign (-1)^y); beta given per site, use the cell's (even,even) site
            b = beta[0::2, 0::2]
            self.Pt = np.repeat(b, 2, axis=1) * ((-1.0) ** np.arange(Ly))[None, :]   # shape (Lx/2, Ly)
            self.beta = True

    # ---- layers
    def lx(self, psi, te, to):
        p, q = gate(psi[0::2, :], psi[1::2, :], te)
        psi[0::2, :], psi[1::2, :] = p, q
        p, q = gate(psi[1::2, :], np.roll(psi[0::2, :], -1, 0), to)
        psi[1::2, :] = p; psi[0::2, :] = np.roll(q, 1, 0)
        p, q = gate(psi[0::2, :], psi[1::2, :], te)
        psi[0::2, :], psi[1::2, :] = p, q
        return psi

    def ly(self, psi, te, to):
        p, q = gate(psi[:, 0::2], psi[:, 1::2], te)
        psi[:, 0::2], psi[:, 1::2] = p, q
        p, q = gate(psi[:, 1::2], np.roll(psi[:, 0::2], -1, 1), to)
        psi[:, 1::2] = p; psi[:, 0::2] = np.roll(q, 1, 1)
        p, q = gate(psi[:, 0::2], psi[:, 1::2], te)
        psi[:, 0::2], psi[:, 1::2] = p, q
        return psi

    def R(self, psi, sign):
        # matrix R(+-beta) = S P(+-beta) S^dag  =>  time order: S^dag (gate -pi/4), P, S (gate +pi/4)
        s = np.pi / 4
        p, q = gate(psi[:, 0::2], psi[:, 1::2], -s); psi[:, 0::2], psi[:, 1::2] = p, q
        p, q = gate(psi[0::2, :], psi[1::2, :], sign * self.Pt); psi[0::2, :], psi[1::2, :] = p, q
        p, q = gate(psi[:, 0::2], psi[:, 1::2], s); psi[:, 0::2], psi[:, 1::2] = p, q
        return psi

    def step(self, psi):
        psi = psi * self.mh
        if self.beta:
            psi = self.R(psi, -1.0)            # R^dag first (rightmost in R Ux R^dag)
        psi = self.lx(psi, self.tx_e, self.tx_o)
        if self.beta:
            psi = self.R(psi, +1.0)
        psi = self.ly(psi, self.ty_e, self.ty_o)
        return psi * self.mh


# ---------------- Bloch (flat medium) for packet preparation: must match Walk2D with uniform fields
def bloch_batch(K, th0, mu=0.0, delta=0.0, beta=0.0, imx=0.0, imy=0.0, fx=1.0, fy=1.0, N=1.0, mode='os'):
    """K: (n,2) cell momenta; returns (n,4,4) cycle matrices. internal index 2i+j for site (2cx+i, 2cy+j)."""
    n = K.shape[0]
    def layer(bonds):
        U = np.tile(np.eye(4, dtype=complex), (n, 1, 1))
        for p, q, d, t in bonds:
            a = abs(t); c = np.cos(a); s = (np.sin(a) / a if a > 0 else 1.0) * t
            ph = np.exp(1j * (K[:, 0] * d[0] + K[:, 1] * d[1]))
            U[:, p, p] = c; U[:, q, q] = c
            U[:, p, q] = -1j * s * ph; U[:, q, p] = -1j * np.conj(s * ph)
        return U
    st = lambda i, j: 2 * i + j
    if mode == 'os':
        axe, axo = (th0 + delta) * fx * N, (th0 - delta) * fx * N
    else:
        axe, axo = N * (th0 * fx + delta), N * (th0 * fx - delta)
    # x bonds: even (x even), odd (x odd); imaginary pattern (-1)^(x+y)
    xe = layer([(st(0, j), st(1, j), (0, 0), 0.5 * (axe - 1j * imx * th0 * fx * N * (-1.0) ** j)) for j in (0, 1)])
    xo = layer([(st(1, j), st(0, j), (1, 0), (axo + 1j * imx * th0 * fx * N * (-1.0) ** j)) for j in (0, 1)])
    ye = layer([(st(i, 0), st(i, 1), (0, 0), 0.5 * (th0 * fy * N * (-1.0) ** i + 1j * imy * th0 * fy * N)) for i in (0, 1)])
    yo = layer([(st(i, 1), st(i, 0), (0, 1), (th0 * fy * N * (-1.0) ** i - 1j * imy * th0 * fy * N)) for i in (0, 1)])
    Ux = xe @ xo @ xe
    Uy = ye @ yo @ ye
    if beta != 0.0:
        S = layer([(st(i, 0), st(i, 1), (0, 0), np.pi / 4) for i in (0, 1)])
        Sd = layer([(st(i, 0), st(i, 1), (0, 0), -np.pi / 4) for i in (0, 1)])
        P = layer([(st(0, j), st(1, j), (0, 0), beta * (-1.0) ** j) for j in (0, 1)])
        Rm = S @ P @ Sd
        Ux = Rm @ Ux @ np.conj(np.transpose(Rm, (0, 2, 1)))
    epsd = np.array([(-1.0) ** (i + j) for i in (0, 1) for j in (0, 1)])
    Mh = np.diag(np.exp(-0.5j * mu * N * epsd))
    return Mh @ Uy @ Ux @ Mh


def to_cells(psi):
    """site array (Lx,Ly) -> (Lx/2, Ly/2, 4) with internal index 2i+j"""
    out = np.empty((psi.shape[0] // 2, psi.shape[1] // 2, 4), complex)
    for i in (0, 1):
        for j in (0, 1):
            out[:, :, 2 * i + j] = psi[i::2, j::2]
    return out


def from_cells(c):
    psi = np.empty((2 * c.shape[0], 2 * c.shape[1]), complex)
    for i in (0, 1):
        for j in (0, 1):
            psi[i::2, j::2] = c[:, :, 2 * i + j]
    return psi


def packet(Lx, Ly, c0, K0, sig, th0, chi=None, upper=True, cut=1e-10, **kw):
    """positive-band (upper=True) Gaussian packet centred at cell c0 with carrier cell momentum K0 (relative K*)"""
    Lcx, Lcy = Lx // 2, Ly // 2
    cx = np.arange(Lcx)[:, None]; cy = np.arange(Lcy)[None, :]
    dxc = (cx - c0[0] + Lcx / 2) % Lcx - Lcx / 2
    dyc = (cy - c0[1] + Lcy / 2) % Lcy - Lcy / 2
    env = np.exp(-(dxc ** 2 + dyc ** 2) / (4 * sig ** 2)) * np.exp(1j * ((np.pi + K0[0]) * cx + (np.pi + K0[1]) * cy))
    chi = np.array([1, 0.3 + 0.2j, -0.4j, 0.5]) if chi is None else chi
    cells = env[:, :, None] * chi[None, None, :]
    ft = np.fft.fft2(cells, axes=(0, 1))
    kx = 2 * np.pi * np.fft.fftfreq(Lcx)[:, None] * np.ones((1, Lcy))
    ky = 2 * np.pi * np.fft.fftfreq(Lcy)[None, :] * np.ones((Lcx, 1))
    # fft convention: ft[k] = sum_c f[c] e^{-i k c}; the Bloch phase convention psi(c) ~ e^{+iKc} => K = +k
    mag = np.linalg.norm(ft, axis=2)
    sel = mag > cut * mag.max()
    Ks = np.column_stack([kx[sel], ky[sel]])
    U = bloch_batch(Ks, th0, **kw)
    w, V = np.linalg.eig(U)
    om = -np.angle(w)
    keep = (om > 0) if upper else (om < 0)
    Vi = np.linalg.inv(V)
    Pp = np.einsum('nij,nj,njk->nik', V, keep.astype(float), Vi)
    vecs = ft[sel]
    ft2 = np.zeros_like(ft)
    ft2[sel] = np.einsum('nij,nj->ni', Pp, vecs)
    c2 = np.fft.ifft2(ft2, axes=(0, 1))
    psi = from_cells(c2)
    return psi / np.linalg.norm(psi)


def centroid(psi):
    p = np.abs(psi) ** 2
    x = np.arange(psi.shape[0]); y = np.arange(psi.shape[1])
    return (p.sum(1) @ x) / p.sum(), (p.sum(0) @ y) / p.sum(), p.sum()
