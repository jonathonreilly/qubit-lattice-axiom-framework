"""Independent re-implementation (B4b adversarial check).

Built from the fine-lattice real-space staggered operator
    (D chi)(x) = m chi(x) + sum_mu eta_mu(x)/2 [chi(x+mu) - chi(x-mu)],  eta_mu(x) = (-1)^{x_0+..+x_{mu-1}}
blocked onto 2^4 hypercubes x = 2X + A.  D(P)_{AB} = sum_X D[(0,A),(X,B)] e^{i P.X},
Vel_mu(P) = dD/dP_mu = sum_X i X_mu D[(0,A),(X,B)] e^{iP.X}  (block-coordinate current).
No code shared with B4b stag_kernel.py.
"""
import itertools
import numpy as np

CORN = list(itertools.product((0, 1), repeat=4))
CI = {c: i for i, c in enumerate(CORN)}


def build_hops():
    """Return list of (Xoffset(4,), 16x16 amplitude matrix) for D(P) = m + sum_X H_X e^{iP.X}."""
    hops = {}
    for A in CORN:
        x = np.array(A)
        eta = [(-1) ** int(x[:mu].sum()) for mu in range(4)]
        for mu in range(4):
            for s in (+1, -1):
                y = x.copy(); y[mu] += s
                X = tuple(int(v) for v in np.floor_divide(y, 2))
                B = tuple(int(v) for v in np.mod(y, 2))
                hops.setdefault(X, np.zeros((16, 16)))
                hops[X][CI[A], CI[B]] += 0.5 * s * eta[mu]
    return [(np.array(X, float), H) for X, H in hops.items()]


HOPS = build_hops()
XS = np.array([h[0] for h in HOPS])          # (nh,4)
HS = np.array([h[1] for h in HOPS])          # (nh,16,16)


def D(P, m):
    ph = np.exp(1j * P @ XS.T)                # (n,nh)
    return m * np.eye(16)[None] + np.einsum('nh,hab->nab', ph, HS)


def Vel(P):
    ph = np.exp(1j * P @ XS.T)
    return np.einsum('nh,hm,hab->mnab', ph, 1j * XS, HS)


def Delta(P, m):
    return m * m + np.sum(np.sin(P / 2) ** 2, axis=-1)


def G(P, m):
    Dm = D(P, m)
    return np.conj(np.swapaxes(Dm, 1, 2)) / Delta(P, m)[:, None, None]


def grid(N, shift=0.0):
    p = -np.pi + (np.arange(N) + shift) * 2 * np.pi / N
    return np.stack(np.meshgrid(p, p, p, p, indexing='ij'), -1).reshape(-1, 4)


def bubble(K, N, m, f=np.sin, chunk=4096, shift=0.0):
    """Pi[mu,nu,rho,sig](K) = N^-4 sum_P tr[G(P) V_mn(Pb) G(P+K) V_rs(Pb)], V_mn=1/2(Vel_m f_n+Vel_n f_m)."""
    K = np.asarray(K, float)
    Pg = grid(N, shift)
    J = np.zeros((4, 4, 4, 4), complex)   # J[m,n,r,s] = sum tr[G0 Vel_m G1 Vel_r] f_n f_s
    for s in range(0, len(Pg), chunk):
        P = Pg[s:s + chunk]; Pb = P + K / 2
        G0, G1, V = G(P, m), G(P + K, m), Vel(Pb)
        A = np.einsum('nab,mnbc->mnac', G0, V)
        B = np.einsum('nab,mnbc->mnac', G1, V)
        t = np.einsum('mnab,rnba->nmr', A, B)
        F = f(Pb)
        J += np.einsum('nmr,nx,ny->mxry', t, F, F)
    J /= len(Pg)
    T = 0.25 * (J + J.transpose(1, 0, 2, 3) + J.transpose(0, 1, 3, 2) + J.transpose(1, 0, 3, 2))
    return T


def tadpole_contact(K, N, m, f=np.sin, chunk=4096):
    """My analytic reduction of khat.Pi_bubble to one-propagator (tadpole-type) loops:
       khat_m V_mn = 1/2 f_n [D(P+K)-D(P)] + 1/2 Ssc Vel_n,  Ssc = 2[Delta(P+K)-Delta(P)]
       => khat.Pi_{n,rs} = sum tr{ 1/2 f_n [G(P)-G(P+K)] V_rs + [G(P) Vel_n Ddag(P+K) - Ddag(P) Vel_n G(P+K)] V_rs }."""
    K = np.asarray(K, float)
    Pg = grid(N)
    R = np.zeros((4, 4, 4), complex)
    for s in range(0, len(Pg), chunk):
        P = Pg[s:s + chunk]; Pb = P + K / 2
        G0, G1, V = G(P, m), G(P + K, m), Vel(Pb)
        D0d = np.conj(np.swapaxes(D(P, m), 1, 2)); D1d = np.conj(np.swapaxes(D(P + K, m), 1, 2))
        F = f(Pb)
        Vrs = 0.5 * (np.einsum('rnab,ns->rsnab', V, F) + np.einsum('snab,nr->rsnab', V, F))
        t1 = 0.5 * np.einsum('nx,nab,rsnba->xrs', F, G0 - G1, Vrs)
        X = np.einsum('nab,xnbc,ncd->xnad', G0, V, D1d) - np.einsum('nab,xnbc,ncd->xnad', D0d, V, G1)
        t2 = np.einsum('xnab,rsnba->xrs', X, Vrs)
        R += t1 + t2
    return R / len(Pg)


def khat(K):
    return 2 * np.sin(np.asarray(K) / 2)


def ward(T, K):
    return np.einsum('m,mnrs->nrs', khat(K), T)


def tt_pol(K):
    """unit TT (4D-transverse, traceless) polarisation orthogonal to K (generic K)."""
    k = khat(K); k = k / np.linalg.norm(k)
    Q = np.linalg.qr(np.column_stack([k, np.eye(4)[:, :3]]))[0]
    a, b = Q[:, 1], Q[:, 2]
    e = (np.outer(a, b) + np.outer(b, a)) / np.sqrt(2)
    return e
