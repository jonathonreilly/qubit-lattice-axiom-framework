"""Finite-range test walks for C5b (all Laurent polynomial unitaries on Z^3)."""
import itertools
import numpy as np
from scipy.linalg import expm
import lib5b as L

I2 = np.eye(2, dtype=complex)


def cshift_axis(a, sig, m=1):
    """cos(m k_a) + i sin(m k_a) sig = P_+ e^{i m k_a} + P_- e^{-i m k_a}, P_pm=(1 pm sig)/2."""
    e = [0, 0, 0]; e[a] = m
    Pp = (I2 + sig) / 2; Pm = (I2 - sig) / 2
    return L.Laurent({tuple(e): Pp, tuple(-x for x in e): Pm}, f'S{"xyz"[a]}{m}')


def Q_product(m=(1, 1, 1)):
    """Q = S_x S_y S_z with S_a = cos(m_a k_a) + i sin(m_a k_a) sigma_a (one-qubit, SU(2))."""
    W = cshift_axis(0, L.SX, m[0])
    W = L.lmul(W, cshift_axis(1, L.SY, m[1]))
    W = L.lmul(W, cshift_axis(2, L.SZ, m[2]))
    W.name = f'Q{m}'
    return W


def dariano_perinotti_weyl():
    """BCC Weyl QCA A = e^{-i q_x sx} e^{-i q_y sy} e^{-i q_z sz}, q = k_BCC (neighbours at
    (+-1,+-1,+-1) in units where q.h is the phase).  Written on Z^3 through the primitive
    vectors a1=(1,1,1), a2=(1,1,-1), a3=(1,-1,1): theta_j = q.a_j.
    Form recalled from D'Ariano-Perinotti PRA 90, 062106 (2014) (d = cxcycz - sxsysz ...);
    only its structure (product of three half conditional shifts on BCC) is used."""
    A = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1]], float)
    out = {}
    for sx, sy, sz in itertools.product((1, -1), repeat=3):
        # e^{-i q_a sigma_a} = P^a_+ e^{-i q_a} + P^a_- e^{+i q_a}
        M = ((I2 + sx * L.SX) / 2) @ ((I2 + sy * L.SY) / 2) @ ((I2 + sz * L.SZ) / 2)
        h = -np.array([sx, sy, sz], float)        # phase e^{i q.h}
        n = np.linalg.solve(A.T, h)               # h = sum_j n_j a_j
        assert np.allclose(n, np.round(n))
        key = tuple(int(round(x)) for x in n)
        out[key] = out.get(key, 0) + M
    W = L.Laurent(out, 'DP-Weyl-QCA(BCC)')
    W.Abcc = A
    return W


# ---- C7 two-qubit Clifford walk (formulas copied from blocks/C7/scripts/c7_numeric.py)
t1 = np.array([[0, 1], [1, 0]], complex); t2 = np.array([[0, -1j], [1j, 0]]); t3 = np.diag([1.0, -1.0]).astype(complex)
TAU = [np.kron(t1, I2), np.kron(t2, I2)]
TS = [np.kron(t3, x) for x in (L.SX, L.SY, L.SZ)]


def Gmat(b0, b1, b2):
    return np.array([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
                     [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
                     [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
                     [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])


def c7_walk(b, name):
    b = np.array(b, float)
    G = Gmat(*b)
    ev, V = np.linalg.eigh(G)
    keep = ev > 1e-13
    F = (V[:, keep] * np.sqrt(ev[keep])).T
    if F.shape[0] < 3:
        F = np.vstack([F, np.zeros((3 - F.shape[0], 4))])
    phi0 = np.array([1.0, 3, 3, 1]); wv = np.array([0.0, 1, 2, 1])
    e = F @ phi0
    Q = np.linalg.qr(np.column_stack([e, np.eye(3)]))[0][:, :3]
    if Q[:, 0] @ e < 0:
        Q[:, 0] *= -1
    F = Q.T @ F
    W = F[1:] @ wv
    if np.linalg.norm(W) > 1e-12:
        ang = np.arctan2(W[1], W[0])
        R = np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])
        F[1:] = R @ F[1:]

    def U0(K):
        c, s = np.cos(K), np.sin(K)
        ph = np.stack([np.ones(K.shape[:-1]), c.sum(-1), c[..., 0]*c[..., 1] + c[..., 0]*c[..., 2] + c[..., 1]*c[..., 2], c.prod(-1)], -1)
        f, h1, h2 = np.moveaxis(ph @ F.T, -1, 0)
        g = [s[..., i]*(b[0] + b[1]*(c[..., (i+1) % 3] + c[..., (i+2) % 3]) + b[2]*c[..., (i+1) % 3]*c[..., (i+2) % 3]) for i in range(3)]
        out = f[..., None, None]*np.eye(4) + 1j*(h1[..., None, None]*TAU[0] + h2[..., None, None]*TAU[1]
                                                + sum(g[i][..., None, None]*TS[i] for i in range(3)))
        return out
    # exact Laurent coefficients by FFT (degree <= 3 per axis, so an 8-point grid is exact)
    N = 8
    k = 2*np.pi*np.arange(N)/N
    K = np.stack(np.meshgrid(k, k, k, indexing='ij'), -1)
    Ug = U0(K)
    Fc = np.fft.fftn(Ug, axes=(0, 1, 2)) / N**3
    coeffs = {}
    for n in itertools.product(range(-3, 4), repeat=3):
        Mx = Fc[n[0] % N, n[1] % N, n[2] % N]
        if np.abs(Mx).max() > 1e-13:
            coeffs[n] = Mx
    Wl = L.Laurent(coeffs, name)
    Kt = np.random.default_rng(0).uniform(0, 2*np.pi, (50, 3))
    assert np.abs(Wl(Kt) - U0(Kt)).max() < 1e-12
    return Wl


r5 = np.sqrt(5)
B_GOLD = ((9*r5 - 5)/38, (5*r5 - 7)/19, (71 - 29*r5)/38)


def conj_coin(W, K, eta, name):
    """exp(i eta K/2) W exp(i eta K/2) (constant coins: finite range preserved)."""
    Mh = expm(0.5j*eta*K)
    out = L.lmul(L.lmul(L.lconst(Mh), W), L.lconst(Mh))
    out.name = name
    return out


def coupled(blocks, eta, seed, name):
    out = blocks[0]
    for b in blocks[1:]:
        out = L.ldirect(out, b)
    n = out.n
    rng = np.random.default_rng(seed)
    Kh = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); Kh = (Kh + Kh.conj().T)/2
    out = L.lmul(L.lconst(expm(1j*eta*Kh)), out)
    out.name = name
    return out


def phase_const(E):
    return L.Laurent({(0, 0, 0): np.array([[np.exp(-1j*E)]])}, f'e^(-i{E})')


def monomial(m):
    return L.Laurent({tuple(m): np.array([[1.0 + 0j]])}, f'z^{m}')
