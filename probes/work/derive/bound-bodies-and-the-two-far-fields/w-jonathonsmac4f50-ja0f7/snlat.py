"""Lattice Schrodinger-Newton at leading order for a heavy self-bound walker (floating point).

Reduction (ATTEMPT step 7): the positive branch of the massive walk at leading order in the rate field and in
1/m has energy m + S^2/(2m) + m u on one parity class of sites, with u = -(m/(4K)) G rho the weak rate field
of block 60 T3 (Delta u = e/(4K), e = m rho).  With beta = m^3/(2K) the stationary state solves
    [S^2 - beta (G rho)] psi = lam psi,   rho = |psi|^2 normalised,
S^2 = sum_a S_a^2 = (1/4)(-Delta_coarse) on the class (coarse spacing 2), G the lattice Green function of -Delta.
The virial defect is v = (2<S^2> - (beta/2) D)/((beta/2) D), D = sum rho G rho: v = (2 E_kin + W)/|W|.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import ive, erf
from scipy.fft import dstn, idstn
from scipy.sparse import diags, kron, identity
from scipy.sparse.linalg import eigsh


def G_exact(pts, T=4.0e4, n=1500):
    """infinite simple-cubic lattice Green function of -Delta, int_0^oo prod_i ive(|x_i|, 2t) dt"""
    pts = np.abs(np.asarray(pts, dtype=float))
    xs, ws = leggauss(n)
    a, b = np.log(1e-8), np.log(T)
    s = 0.5 * (b - a) * xs + 0.5 * (b + a)
    t = np.exp(s)
    wt = 0.5 * (b - a) * ws * t
    out = np.empty(len(pts))
    for i in range(0, len(pts), 256):
        P = pts[i:i + 256]
        f = ive(P[:, 0:1], 2 * t[None, :]) * ive(P[:, 1:2], 2 * t[None, :]) * ive(P[:, 2:3], 2 * t[None, :])
        r = np.sqrt((P ** 2).sum(1))
        rr = np.maximum(r, 1e-300)
        tail = np.where(r > 0, erf(rr / (2 * np.sqrt(T))) / (4 * np.pi * rr), 2 * (4 * np.pi) ** -1.5 / np.sqrt(T))
        out[i:i + 256] = f @ wt + tail
    return out


def G_asym(pts):
    p = np.asarray(pts, dtype=float)
    r2 = (p ** 2).sum(1)
    r = np.sqrt(r2)
    return 1 / (4 * np.pi * r) + (5 * (p ** 4).sum(1) / r2 ** 2 - 3) / (32 * np.pi * r ** 3)


_cache = {}


def _kernel(Wc, rcut=24):
    if Wc not in _cache:
        n = 4 * Wc + 1
        d = np.arange(-2 * Wc, 2 * Wc + 1)
        D = np.array(np.meshgrid(d, d, d, indexing='ij'))
        key = np.sort((2 * np.abs(D)).reshape(3, -1).T, axis=1)
        uniq, inv = np.unique(key, axis=0, return_inverse=True)
        r = np.sqrt((uniq ** 2).sum(1))
        vals = np.empty(len(uniq))
        ex = r <= rcut
        vals[ex] = G_exact(uniq[ex])
        vals[~ex] = G_asym(uniq[~ex])
        g = vals[inv.ravel()].reshape(n, n, n)
        m = 6 * Wc + 2
        gk = np.zeros((m, m, m))
        gk[:n, :n, :n] = g
        _cache[Wc] = (np.fft.rfftn(gk), m)
    return _cache[Wc]


def _potential_inf(rho, Wc):
    Gk, m = _kernel(Wc)
    s = 2 * Wc + 1
    rp = np.zeros((m, m, m))
    rp[:s, :s, :s] = rho
    conv = np.fft.irfftn(np.fft.rfftn(rp) * Gk, s=(m, m, m), axes=(0, 1, 2))
    return conv[2 * Wc:2 * Wc + s, 2 * Wc:2 * Wc + s, 2 * Wc:2 * Wc + s]


def _kinetic(s):
    L1 = diags([2 * np.ones(s), -np.ones(s - 1), -np.ones(s - 1)], [0, 1, -1], shape=(s, s))
    I = identity(s)
    return 0.25 * (kron(kron(L1, I), I) + kron(kron(I, L1), I) + kron(kron(I, I), L1)).tocsr()


def solve_infinite(beta, Wc, R0, iters=1000, mix=0.5, tol=1e-10):
    """no walls: the coarse class of the centre, (2Wc+1)^3 coarse sites, infinite-lattice G by convolution."""
    s = 2 * Wc + 1
    X = np.arange(-Wc, Wc + 1)
    A, B, C = np.meshgrid(X, X, X, indexing='ij')
    r2 = (4 * (A ** 2 + B ** 2 + C ** 2)).ravel()
    psi = np.exp(-r2 / (2 * R0 ** 2))
    psi /= np.linalg.norm(psi)
    rho = psi ** 2
    Kin = _kinetic(s)
    d = 1.0
    for it in range(iters):
        V = -beta * _potential_inf(rho.reshape(s, s, s), Wc).ravel()
        w, v = eigsh(Kin + diags(V), k=1, which='SA', v0=psi, tol=1e-12)
        new = np.abs(v[:, 0])
        new /= np.linalg.norm(new)
        d = np.abs(new ** 2 - rho).max()
        rho = (1 - mix) * rho + mix * new ** 2
        psi = new
        if d < tol:
            break
    rho = psi ** 2
    Dq = rho @ _potential_inf(rho.reshape(s, s, s), Wc).ravel()
    kin = psi @ (Kin @ psi)
    return dict(v=(2 * kin - (beta / 2) * Dq) / ((beta / 2) * Dq), R=float(np.sqrt(rho @ r2)), resid=d,
                edge=float(rho.reshape(s, s, s)[[0, -1]].sum()))


def solve_box(beta, L, R0, iters=1000, mix=0.5, tol=1e-10):
    """walls held: Dirichlet box of L^3 fine sites, G_D by the sine transform; the centre's class."""
    k = np.pi * np.arange(1, L + 1) / (L + 1)
    lam1 = 2 - 2 * np.cos(k)
    den = lam1[:, None, None] + lam1[None, :, None] + lam1[None, None, :]
    G = lambda f: idstn(dstn(f, type=1) / den, type=1)
    c = L // 2
    x = np.arange(L) - c
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    par = ((X % 2 == 0) & (Y % 2 == 0) & (Z % 2 == 0)).ravel()
    sub = np.where(par)[0]
    s = int(round(len(sub) ** (1 / 3)))
    Kin = _kinetic(s)          # truncated S_a^2 on the class: the same stencil with Dirichlet ends
    r2 = (X ** 2 + Y ** 2 + Z ** 2).ravel()
    psi = np.zeros(L ** 3)
    psi[sub] = np.exp(-r2[sub] / (2 * R0 ** 2))
    psi /= np.linalg.norm(psi)
    rho = psi ** 2
    d = 1.0
    for it in range(iters):
        V = -beta * G(rho.reshape(L, L, L)).ravel()
        w, v = eigsh(Kin + diags(V[sub]), k=1, which='SA', v0=psi[sub], tol=1e-12)
        new = np.zeros(L ** 3)
        new[sub] = np.abs(v[:, 0])
        new /= np.linalg.norm(new)
        d = np.abs(new ** 2 - rho).max()
        rho = (1 - mix) * rho + mix * new ** 2
        psi = new
        if d < tol:
            break
    rho = psi ** 2
    Dq = rho @ G(rho.reshape(L, L, L)).ravel()
    kin = psi[sub] @ (Kin @ psi[sub])
    return dict(v=(2 * kin - (beta / 2) * Dq) / ((beta / 2) * Dq), R=float(np.sqrt(rho @ r2)), resid=d)
