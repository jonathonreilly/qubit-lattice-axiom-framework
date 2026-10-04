#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: interval gap/admissibility certificates and numerical Chern diagnostics, isotropic and anisotropic couplings.

Setting. Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings
J = (J_x, J_y, J_z), odd term kappa, four-site Bloch matrix H(f) = i M(f) over the fractional zone [0,1)^3; "occupied" = the two lowest bands,
middle gap = eps_3 - eps_2. Nothing here is adopted framework premise; couplings are the exact decimals written (the interval code encloses each
amplitude 2J, 2 kappa that is not exactly 2 one ulp either side of its double).

Certificate (computer-assisted; interval parts round OUTWARD).
(A) Whole-zone clearing: a cube (dyadic centre c, half-width h) is cleared when interval LDL^T inertias of H(c) - x1 and H(c) - x2 (floats x1 < x2
    around the float middle gap) both have exactly two negative pivots (eps_2(c) < x1, eps_3(c) >= x2) and x2 - x1 > 2 r(h), r(h) = h rho(E_x+E_y+E_z)
    (Weyl: ||H(f) - H(c)||_op <= r; E_j the entrywise bound of |dH/df_j| from the hopping terms, rho by Collatz-Wielandt). The cleared plus uncleared
    volume is exactly 1. Uncleared cubes form clusters; each cluster must lie strictly inside a cube Sigma around its float node.
(B) On every one of the 6 m_f^2 patches of the cube surface Sigma the same interval inertia (patch Lipschitz radius (h_f/2) rho(E_a+E_b)) certifies a
    lower bound g_patch of the middle gap; g = min over patches.
(C) Admissibility (the lemma stated and proved in the paired note): with Fro_j >= ||d_j H||_F, Op_j >= ||d_j H||_op, Op2_j >= ||d_j^2 H||_op (outward rounded) and
    g, a plaquette of side h whose edges lie along a, b has flux |Phi_p| <= 2 h^2 Fro_a Fro_b / g^2 and each edge a transport-versus-overlap phase mismatch
    |delta_e| <= alpha b2 h^3/6 + x^2/(1-x), alpha = Fro/g, x = alpha^2 h^2/2, b2 = sqrt2 (Op2/g + 8 Op^2/(pi g^2)) + (Op/g) alpha. If
    |Phi_p| + sum_e |delta_e| < pi for every plaquette (evaluated in mpmath intervals), the Fukui-Hatsugai-Suzuki lattice Chern number of the two lowest
    bands (principal phases of the four-link products of det(u_v^dag u_w)) equals the true Chern number of the occupied bundle on Sigma (outward orientation).
(D) A nonzero C on Sigma means the middle gap closes inside the solid cube; the clusters' Chern numbers must sum to zero (the occupied bundle exists
    on the complement). Convention: C = -sign det V, with sign det V = sign Im Tr(P d1H P d2H P d3H) the landed chirality (checked on isotropic nodes).
FLOAT (not interval-verified): node positions (Newton on the Pauli vector of the kernel block), det V, eigenvectors and the evaluation of the lattice
integer. The estimated float error is not an enclosure; a margin and a 30-digit repeat do not authenticate the integer. Existence/net-charge conclusions remain conditional on that authentication.
Checks: (1) interval machinery sanity at J = (1, 0.8, 1), kappa = 0.45; (2)-(3) isotropic J = 1, kappa = 3/10 and 9/20: clusters = landed exact family
nodes (1e-12) and C = -sign det V; (4)-(8) anisotropic A (1,.8,1; .45), B (1.2,.8,1; .3), C (1,.8,1; .8), E (.9,1.1,1.3; .4), D (1.2,.8,1; .2, larger
cube and finer mesh); (9) 30-digit recomputation of C on one surface (A off-plane, m_F = 32).
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"

import itertools
import time

import numpy as np
from mpmath import iv, mp, mpc, mpf
import mpmath

AUDIT_TIMEOUT_SEC = 900

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label} :: {detail}", flush=True)


# ------------------------------------------------------------------------------------------------ network and Bloch terms
AX = {"x": 0, "y": 1, "z": 2}
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


def reduce(p):
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1."""
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
                out.append((r1, r2, tuple(int(v) for v in np.subtract(n2, n1)), 2.0 * kappa))
    return out


class Bloch:
    def __init__(self, J, kappa):
        self.J, self.kappa = J, kappa
        self.T = terms(J, kappa)
        self.a = np.array([x[0] for x in self.T]); self.b = np.array([x[1] for x in self.T])
        self.n = np.array([x[2] for x in self.T], dtype=float); self.t = np.array([x[3] for x in self.T])

    def H(self, F):
        F = np.atleast_2d(F)
        ph = np.exp(2j * np.pi * F @ self.n.T)
        Mk = np.zeros((len(F), 4, 4), dtype=complex)
        for j in range(len(self.T)):
            Mk[:, self.a[j], self.b[j]] += self.t[j] * ph[:, j]
            Mk[:, self.b[j], self.a[j]] -= self.t[j] * np.conj(ph[:, j])
        return 1j * Mk

    def dH(self, F, j):
        """d H / d f_j."""
        F = np.atleast_2d(F)
        ph = np.exp(2j * np.pi * F @ self.n.T)
        Mk = np.zeros((len(F), 4, 4), dtype=complex)
        for k in range(len(self.T)):
            w = 2j * np.pi * self.n[k, j] * self.t[k]
            Mk[:, self.a[k], self.b[k]] += w * ph[:, k]
            Mk[:, self.b[k], self.a[k]] += w * np.conj(ph[:, k])
        return 1j * Mk

    def levels(self, F, vecs=False, chunk=50000):
        F = np.atleast_2d(F)
        if not vecs and len(F) <= chunk:
            return np.linalg.eigvalsh(self.H(F))
        ev = np.zeros((len(F), 4)); W = np.zeros((len(F), 4, 4), dtype=complex) if vecs else None
        for s in range(0, len(F), chunk):
            if vecs:
                ev[s:s + chunk], W[s:s + chunk] = np.linalg.eigh(self.H(F[s:s + chunk]))
            else:
                ev[s:s + chunk] = np.linalg.eigvalsh(self.H(F[s:s + chunk]))
        return (ev, W) if vecs else ev


# ------------------------------------------------------------------------------------------------ float node location, chirality
def kernel_basis(B, f, nker=2):
    ev, V = np.linalg.eigh(B.H(np.asarray(f)[None, :])[0])
    idx = np.argsort(np.abs(ev))[:nker]
    return ev[idx], V[:, idx]


def _pauli(Mat, W):
    h = W.conj().T @ Mat @ W
    return (h[0, 0] + h[1, 1]).real / 2, np.array([h[0, 1].real, -h[0, 1].imag, (h[0, 0] - h[1, 1]).real / 2])


def refine_node(B, f0, iters=14):
    """Newton iteration on the Pauli vector d(f) of the 2x2 kernel block (kernel re-chosen each step). Returns (f, tilt, |d|)."""
    f = np.asarray(f0, dtype=float).copy()
    for _ in range(iters):
        ev, W = kernel_basis(B, f)
        t, d = _pauli(B.H(f[None, :])[0], W)
        Vj = np.array([_pauli(B.dH(f[None, :], i)[0], W)[1] for i in range(3)])
        f = f + np.linalg.solve(Vj.T, -d)
    ev, W = kernel_basis(B, f)
    t, d = _pauli(B.H(f[None, :])[0], W)
    return f, t, float(np.linalg.norm(d))


def det_V(B, f, tol=1e-6):
    """Landed chirality: det V = Im Tr(P d1H P d2H P d3H)/2, P the kernel projector."""
    f = np.asarray(f, dtype=float)
    ev, V = np.linalg.eigh(B.H(f[None, :])[0])
    W = V[:, np.abs(ev) < tol]
    P = W @ W.conj().T
    D = [B.dH(f[None, :], i)[0] for i in range(3)]
    return np.trace(P @ D[0] @ P @ D[1] @ P @ D[2]).imag / 2, W.shape[1]


# ------------------------------------------------------------------------------------------------ rigorous interval tools
DN, UP = -np.inf, np.inf


def rd(x):
    return np.nextafter(x, DN)


def ru(x):
    return np.nextafter(x, UP)


class I:
    """Real interval arrays [lo, hi], outward rounded."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=float)
        self.hi = self.lo.copy() if hi is None else np.asarray(hi, dtype=float)

    def __add__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(rd(self.lo + o.lo), ru(self.hi + o.hi))

    def __sub__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(rd(self.lo - o.hi), ru(self.hi - o.lo))

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __mul__(self, o):
        o = o if isinstance(o, I) else I(o)
        p = np.stack([self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi])
        return I(rd(p.min(axis=0)), ru(p.max(axis=0)))

    def sq(self):
        a, b = self.lo * self.lo, self.hi * self.hi
        lo = np.where((self.lo <= 0) & (self.hi >= 0), 0.0, rd(np.minimum(a, b)))
        return I(lo, ru(np.maximum(a, b)))

    def div(self, o):
        p = np.stack([self.lo / o.lo, self.lo / o.hi, self.hi / o.lo, self.hi / o.hi])
        return I(rd(p.min(axis=0)), ru(p.max(axis=0)))


class CX:
    """Complex interval arrays as rectangles re + i im."""
    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re, self.im = re, im

    def __add__(self, o):
        return CX(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return CX(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return CX(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def rmul(self, r):
        return CX(self.re * r, self.im * r)

    def conj(self):
        return CX(self.re, -self.im)

    def abs2(self):
        return self.re.sq() + self.im.sq()


def phase_table(values):
    """Rigorous enclosures of cos and sin of 2 pi v for exactly representable floats v (converted exactly), one extra ulp outward."""
    out = {}
    for v in values:
        x = iv.mpf(mpf(float(v)))
        a = 2 * iv.pi * x
        cc, ss = iv.cos(a), iv.sin(a)
        out[float(v)] = (float(rd(float(cc.a))), float(ru(float(cc.b))), float(rd(float(ss.a))), float(ru(float(ss.b))))
    return out


def inertia_neg(A, mu):
    """Number of negative pivots of the interval Hermitian matrix A - mu I (mu float or float array) and the flag that no pivot interval met 0."""
    n = 4
    N = A[(0, 0)].re.lo.shape
    d = [None] * n
    L = {}
    ok = np.ones(N, dtype=bool)
    neg = np.zeros(N, dtype=np.int64)
    for k in range(n):
        dk = A[(k, k)].re - mu
        for j in range(k):
            dk = dk - L[(k, j)].abs2() * d[j]
        d[k] = dk
        pos, ng = dk.lo > 0, dk.hi < 0
        ok &= pos | ng
        neg += ng
        safe = I(np.where(pos | ng, dk.lo, 1.0), np.where(pos | ng, dk.hi, 1.0))
        for i in range(k + 1, n):
            s = A[(k, i)].conj()
            for j in range(k):
                s = s - (L[(i, j)] * L[(k, j)].conj()).rmul(d[j])
            L[(i, k)] = CX(s.re.div(safe), s.im.div(safe))
    return neg, ok


def t_interval(t):
    return (t, t) if t == 2.0 else (float(np.nextafter(t, -np.inf)), float(np.nextafter(t, np.inf)))


def build(terms_):
    a = np.array([x[0] for x in terms_]); b = np.array([x[1] for x in terms_])
    n = np.array([x[2] for x in terms_], dtype=np.int64)
    t = [t_interval(float(x[3])) for x in terms_]
    return a, b, n, t


def H_intervals(Cs, a, b, n, t):
    """Upper-triangle complex-interval entries of H(c) = i M(c) at dyadic centres Cs (Cs @ n exact in floating point)."""
    N = len(Cs)
    vals = np.mod(Cs @ n.T.astype(float), 1.0)
    uniq = np.unique(vals)
    tab = phase_table(uniq)
    look = np.array([tab[float(v)] for v in uniq])
    idx = np.searchsorted(uniq, vals)
    cl, ch, sl, sh = look[idx, 0], look[idx, 1], look[idx, 2], look[idx, 3]
    zero = lambda: I(np.zeros(N))
    Mre = {(i, j): zero() for i in range(4) for j in range(4)}
    Mim = {(i, j): zero() for i in range(4) for j in range(4)}
    for j in range(len(a)):
        tt = I(np.full(N, t[j][0]), np.full(N, t[j][1]))
        cs = I(cl[:, j], ch[:, j]); sn = I(sl[:, j], sh[:, j])
        Mre[(a[j], b[j])] = Mre[(a[j], b[j])] + tt * cs
        Mim[(a[j], b[j])] = Mim[(a[j], b[j])] + tt * sn
        Mre[(b[j], a[j])] = Mre[(b[j], a[j])] - tt * cs
        Mim[(b[j], a[j])] = Mim[(b[j], a[j])] + tt * sn
    A = {}
    for i in range(4):
        for j in range(i, 4):
            A[(i, j)] = CX(-Mim[(i, j)], Mre[(i, j)])
    return A


# ------------------------------------------------------------------------------------------------ certified derivative constants
IVPI = iv.pi


def E_matrix(T, j, order=1):
    """Entrywise upper bounds E[a, b] >= sum over terms |t| (2 pi |n_j|)^order (diagonal terms counted twice), floats rounded up."""
    E = [[iv.mpf(0) for _ in range(4)] for _ in range(4)]
    for (a, b, n, t) in T:
        tt = iv.mpf(t_interval(float(t))[1])
        w = tt * (2 * IVPI * abs(int(n[j]))) ** order
        if a == b:
            E[a][a] += 2 * w
        else:
            E[a][b] += w; E[b][a] += w
    return np.array([[float(ru(float(x.b))) for x in r] for r in E])


def cw_upper(E):
    """Upper bound of the spectral norm of a symmetric nonnegative matrix: Collatz-Wielandt max_i (E x)_i / x_i in interval arithmetic."""
    w, V = np.linalg.eigh(E)
    x = np.abs(V[:, -1]) + 1e-3
    best = iv.mpf(0)
    for i in range(4):
        num = sum((iv.mpf(float(E[i, k])) * iv.mpf(float(x[k])) for k in range(4)), iv.mpf(0))
        r = num / iv.mpf(float(x[i]))
        best = r if r.b > best.b else best
    return float(ru(float(best.b)))


def fro_upper(E):
    s = sum((iv.mpf(float(E[i, k])) ** 2 for i in range(4) for k in range(4)), iv.mpf(0))
    return float(ru(float(iv.sqrt(s).b)))


class Consts:
    def __init__(self, B):
        self.E1 = [E_matrix(B.T, j, 1) for j in range(3)]
        E2 = [E_matrix(B.T, j, 2) for j in range(3)]
        self.Fro1 = [fro_upper(E) for E in self.E1]
        self.Op1 = [min(cw_upper(E), fro_upper(E)) for E in self.E1]
        self.Op2 = [cw_upper(E) for E in E2]

    def lip_face(self, k, h):
        """Bound of ||H(f) - H(c)||_op for |f_a - c_a|, |f_b - c_b| <= h/2, f_k = c_k (h a power of two)."""
        a, b = (k + 1) % 3, (k + 2) % 3
        return float(ru(cw_upper(ru(self.E1[a] + self.E1[b])) * (h / 2)))

    def lip_cube(self, h):
        """Bound of ||H(f) - H(c)||_op for |f - c|_inf <= h."""
        return float(ru(cw_upper(ru(ru(self.E1[0] + self.E1[1]) + self.E1[2])) * h))


# ------------------------------------------------------------------------------------------------ whole-zone interval clearing
def zone_clear(B, K, n0=16, levels=11, chunk=40000, frac=0.98):
    a_, b_, n_, t_ = build(B.T)
    h = 0.5 / n0
    g = (np.arange(n0) + 0.5) / n0
    Cs = np.array(list(itertools.product(g, g, g)))
    vol = 0.0
    for lev in range(levels):
        r = K.lip_cube(h)
        keep = []; ncl = 0
        for s0 in range(0, len(Cs), chunk):
            c = Cs[s0:s0 + chunk]
            ev = B.levels(c)
            e2, e3 = ev[:, 1], ev[:, 2]
            mu = 0.5 * (e2 + e3); rho = frac * 0.5 * (e3 - e2)
            pre = rho > r * (1 + 1e-9)
            cleared = np.zeros(len(c), dtype=bool)
            if pre.any():
                idx = np.nonzero(pre)[0]
                A = H_intervals(c[idx], a_, b_, n_, t_)
                x1 = mu[idx] - rho[idx]; x2 = mu[idx] + rho[idx]
                n1, ok1 = inertia_neg(A, x1); n2, ok2 = inertia_neg(A, x2)
                good = ok1 & ok2 & (n1 == 2) & (n2 == 2) & (rd(x2 - x1) > 2 * r)
                cleared[idx[good]] = True
            ncl += int(cleared.sum())
            keep.append(c[~cleared])
        Cs = np.concatenate(keep) if keep else np.zeros((0, 3))
        vol += ncl * (2 * h) ** 3
        if len(Cs) == 0 or lev == levels - 1:
            break
        off = np.array(list(itertools.product((-0.5, 0.5), repeat=3))) * h
        Cs = (Cs[:, None, :] + off[None, :, :]).reshape(-1, 3)
        h /= 2
    vol += len(Cs) * (2 * h) ** 3
    return Cs, h, vol


def clusters(Cs, h):
    """Connected groups (touching or diagonal neighbours, periodic zone) of uncleared cubes of half-width h."""
    n = int(round(0.5 / h))
    ids = np.floor(Cs / (2 * h)).astype(np.int64) % n
    where = {tuple(x): i for i, x in enumerate(ids)}
    seen = np.zeros(len(Cs), dtype=bool)
    out = []
    offs = [d for d in itertools.product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]
    for s0 in range(len(Cs)):
        if seen[s0]:
            continue
        seen[s0] = True
        grp = [s0]; q = [s0]
        while q:
            i = q.pop()
            x = ids[i]
            for d in offs:
                k = where.get(((x[0] + d[0]) % n, (x[1] + d[1]) % n, (x[2] + d[2]) % n))
                if k is not None and not seen[k]:
                    seen[k] = True; grp.append(k); q.append(k)
        out.append(np.array(grp))
    return out


def unwrap_cluster(Cs, idx):
    c = Cs[idx]
    d = c - c[0]
    d -= np.round(d)
    return c[0] + d


# ------------------------------------------------------------------------------------------------ cube surface, patches, Fukui mesh
def dyadic(x, bits):
    return np.round(np.asarray(x, dtype=float) * 2.0 ** bits) / 2.0 ** bits


class Surface:
    """Cube surface, centre c0 on the 2^-(q+2) grid, half-side s = m_f 2^-(q+1): faces cut into m_f^2 patches of side h_f = 2^-q (interval gap) and
    m_F^2 plaquettes of side h_F = 2 s / m_F (Chern mesh). Face index 2k + (0 for -, 1 for +); in-plane axes (a, b) = (k+1, k+2) mod 3."""

    def __init__(self, c0, q, m_f, m_F):
        assert m_f % m_F == 0 and m_f % 2 == 0
        self.c0 = dyadic(c0, max(30, q + 2)); self.q = q; self.m_f = m_f; self.m_F = m_F
        self.h_f = 2.0 ** -q; self.s = m_f * 2.0 ** -(q + 1); self.h_F = 2 * self.s / m_F

    def patch_centres(self):
        m, h = self.m_f, self.h_f
        u = (np.arange(m) + 0.5 - m / 2) * h
        out = np.zeros((6, m, m, 3))
        for k in range(3):
            a, b = (k + 1) % 3, (k + 2) % 3
            for sg in (0, 1):
                f = 2 * k + sg
                out[f, :, :, k] = self.c0[k] + (self.s if sg else -self.s)
                out[f, :, :, a] = self.c0[a] + u[:, None]
                out[f, :, :, b] = self.c0[b] + u[None, :]
        return out

    def _face_points(self, k, sg):
        m = self.m_F; a, b = (k + 1) % 3, (k + 2) % 3
        ii, jj = np.meshgrid(np.arange(m + 1), np.arange(m + 1), indexing="ij")
        P = np.zeros((m + 1, m + 1, 3), dtype=np.int64)
        P[:, :, k] = m if sg else 0; P[:, :, a] = ii; P[:, :, b] = jj
        return P

    def vertices(self):
        m = self.m_F; M1 = m + 1
        keys = np.concatenate([(lambda P: P[..., 0] + M1 * (P[..., 1] + M1 * P[..., 2]))(self._face_points(k, sg)).reshape(-1)
                               for k in range(3) for sg in (0, 1)])
        keys = np.unique(keys)
        l = keys // (M1 * M1); j = (keys // M1) % M1; i = keys % M1
        return self.c0 + (np.stack([i, j, l], axis=1) - m / 2) * self.h_F, keys

    def plaquette_index(self, keys):
        """Corner vertex ids (v0, v1, v2, v3), counterclockwise seen from outside, arrays (6, m_F, m_F, 4)."""
        m = self.m_F; M1 = m + 1
        out = np.zeros((6, m, m, 4), dtype=np.int64)
        for k in range(3):
            for sg in (0, 1):
                P = self._face_points(k, sg)
                kk = P[..., 0] + M1 * (P[..., 1] + M1 * P[..., 2])
                vid = np.searchsorted(keys, kk)
                assert np.all(keys[vid] == kk)
                if sg:
                    corners = [vid[:-1, :-1], vid[1:, :-1], vid[1:, 1:], vid[:-1, 1:]]
                else:
                    corners = [vid[:-1, :-1], vid[:-1, 1:], vid[1:, 1:], vid[1:, :-1]]
                out[2 * k + sg] = np.stack(corners, axis=-1)
        return out


def certify_gap(B, Sf, K, chunk=30000, frac=0.98):
    """Certified lower bound g_patch of the middle gap on every patch (0.0 where the certificate failed): returns (g array, float minimum gap)."""
    a_, b_, n_, t_ = build(B.T)
    flat = Sf.patch_centres().reshape(-1, 3)
    N = len(flat)
    e2 = np.zeros(N); e3 = np.zeros(N)
    for s0 in range(0, N, chunk):
        e_ = B.levels(flat[s0:s0 + chunk]); e2[s0:s0 + chunk] = e_[:, 1]; e3[s0:s0 + chunk] = e_[:, 2]
    mu = 0.5 * (e2 + e3); rho = frac * 0.5 * (e3 - e2)
    r = np.repeat(np.array([K.lip_face(k, Sf.h_f) for k in range(3)]), 2 * Sf.m_f ** 2)
    g = np.zeros(N)
    for s0 in range(0, N, chunk):
        sl = slice(s0, s0 + chunk)
        A = H_intervals(flat[sl], a_, b_, n_, t_)
        x1 = mu[sl] - rho[sl]; x2 = mu[sl] + rho[sl]
        n1, ok1 = inertia_neg(A, x1); n2, ok2 = inertia_neg(A, x2)
        good = ok1 & ok2 & (n1 == 2) & (n2 == 2)
        gl = rd(rd(x2 - x1) - 2 * r[sl])
        g[sl] = np.where(good & (gl > 0), gl, 0.0)
    return g, float((e3 - e2).min())


def lattice_chern(B, Sf, nocc=2, chunk=100000):
    """Fukui-Hatsugai-Suzuki lattice Chern number of the lowest nocc bands (outward) and the principal plaquette phases (float)."""
    V, keys = Sf.vertices()
    P4 = Sf.plaquette_index(keys).reshape(-1, 4)
    U = np.zeros((len(V), 4, nocc), dtype=complex)
    for s0 in range(0, len(V), 50000):
        e, W = np.linalg.eigh(B.H(V[s0:s0 + 50000]))
        U[s0:s0 + 50000] = W[:, :, :nocc]
    ph = np.zeros(len(P4))
    det = lambda A_, B_: np.linalg.det(np.einsum("nia,nib->nab", A_.conj(), B_))
    for s0 in range(0, len(P4), chunk):
        v0, v1, v2, v3 = (P4[s0:s0 + chunk, i] for i in range(4))
        ph[s0:s0 + chunk] = np.angle(det(U[v0], U[v1]) * det(U[v1], U[v2]) * det(U[v2], U[v3]) * det(U[v3], U[v0]))
    return ph.sum() / (2 * np.pi), ph


def total_bound_iv(K, face_axes, g, hF):
    """Outward-rounded upper bound of flux + four edge mismatches for a plaquette of side hF with middle gap >= g (theorem T1-T4); inf if x >= 1."""
    a, b = face_axes
    G = iv.mpf(float(g)); h = iv.mpf(float(hF))
    flux = 2 * h ** 2 * iv.mpf(K.Fro1[a]) * iv.mpf(K.Fro1[b]) / G ** 2
    edges = []
    for j in (a, b):
        Fj, Oj, O2 = iv.mpf(K.Fro1[j]), iv.mpf(K.Op1[j]), iv.mpf(K.Op2[j])
        al = Fj / G; ap = Oj / G
        pp = O2 / G + 8 * Oj ** 2 / (iv.pi * G ** 2)
        b2 = iv.sqrt(iv.mpf(2)) * pp + ap * al
        x = al ** 2 * h ** 2 / 2
        if not (x.b < 1):
            return float("inf")
        edges.append(al * b2 * h ** 3 / 6 + x ** 2 / (1 - x))
    return float(ru(float((flux + 2 * edges[0] + 2 * edges[1]).b)))


# ------------------------------------------------------------------------------------------------ one coupling, whole zone
def pdist(a, b):
    d = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    d -= np.round(d)
    return float(np.abs(d).max())


def analyse(J, kap, q=15, m_f=128, m_F=64):
    B = Bloch(J, kap); K = Consts(B)
    Cs, h, vol = zone_clear(B, K)
    items = []
    for g in clusters(Cs, h):
        c = unwrap_cluster(Cs, g)
        lo, hi = c.min(axis=0) - h, c.max(axis=0) + h
        items.append((tuple(np.mod((lo + hi) / 2, 1.0)), (lo + hi) / 2, c))
    items.sort(key=lambda r: r[0])
    pi_lo = float(iv.pi.a)
    res = dict(vol=vol, n_uncleared=len(Cs), nodes=[])
    for _, ctr, cc in items:
        f, tilt, resid = refine_node(B, ctr)
        dV, nker = det_V(B, f)
        Sf = Surface(f, q, m_f, m_F)
        g, fgap = certify_gap(B, Sf, K)
        gmin = float(g.min())
        bound = float("inf"); Cf = float("nan"); Cf2 = float("nan")
        if gmin > 0:
            bound = max(total_bound_iv(K, ((k + 1) % 3, (k + 2) % 3), gmin, Sf.h_F) for k in range(3))
            Cf = lattice_chern(B, Sf)[0]
            Cf2 = lattice_chern(B, Surface(Sf.c0, q, m_f, m_F // 2))[0]
        Ci = int(round(Cf)) if (bound < pi_lo and abs(Cf - round(Cf)) < 1e-6 and abs(Cf2 - round(Cf)) < 1e-6) else None
        res["nodes"].append(dict(f=f, detV=float(dV), nker=nker, tilt=float(tilt), resid=resid, gmin=gmin, bound=bound, C=Ci, s=Sf.s,
                                 patches_ok=int((g > 0).sum()), patches=int(g.size), contained=bool(np.all(np.abs(cc - Sf.c0) + h < Sf.s))))
    return res


def fmt3(f):
    x = np.mod(np.asarray(f, dtype=float), 1.0)
    x[x > 1 - 5e-7] = 0.0                      # -1e-17 prints as 0.000000, not 1.000000
    return "(" + ",".join(f"{v:.6f}" for v in x) + ")"


def signs(nodes):
    return "".join("0" if n["C"] is None else ("+" if n["C"] > 0 else "-") for n in nodes)


def coupling_check(label, J, kap, expected, q=15, m_f=128, m_F=64):
    t0 = time.time()
    r = analyse(J, kap, q, m_f, m_F)
    nodes = r["nodes"]
    pos_ok = len(nodes) == len(expected) and all(min(pdist(n["f"], e) for e in expected) < 1e-8 for n in nodes) \
        and all(min(pdist(n["f"], e) for n in nodes) < 1e-8 for e in expected)
    numerical_integer_available = all(n["C"] is not None for n in nodes)
    sumC = sum(n["C"] for n in nodes if n["C"] is not None)
    sign_ok = numerical_integer_available and all(n["C"] == -int(np.sign(n["detV"])) and abs(n["C"]) == 1 for n in nodes)
    gap_ok = all(n["patches_ok"] == n["patches"] and n["contained"] for n in nodes)
    ok = r["vol"] == 1.0 and pos_ok and numerical_integer_available and sumC == 0 and sign_ok and gap_ok and all(n["nker"] == 2 and abs(n["tilt"]) < 1e-12 for n in nodes)
    off = [n for n in nodes if min(np.mod(n["f"][2], 1.0), 1 - np.mod(n["f"][2], 1.0)) > 1e-6] or nodes
    n0 = off[0]
    detail = (f"{len(nodes)} cubes (s={n0['s']:.2e}) vol={r['vol']:.1f} gaps {sum(n['patches_ok'] for n in nodes)}/{sum(n['patches'] for n in nodes)} "
              f"gmin={min(n['gmin'] for n in nodes):.2e} bound<={max(n['bound'] for n in nodes):.3g}<pi C={signs(nodes)} sum={sumC} "
              f"node{fmt3(n0['f'])} C={n0['C']} detV={n0['detV']:+.1f} {time.time() - t0:.0f}s")
    check(label, ok, detail)
    return r


# ------------------------------------------------------------------------------------------------ check 1: interval sanity
def check_interval_sanity():
    J, kap = (1.0, 0.8, 1.0), 0.45
    B = Bloch(J, kap)
    a, b, n, t = build(B.T)
    rng = np.random.default_rng(0)
    pts = np.floor(rng.random((400, 3)) * 2 ** 20) / 2 ** 20
    A = H_intervals(pts, a, b, n, t)
    mp.dps = 40
    miss = 0
    for s_ in range(20):
        f = [mpf(float(x)) for x in pts[s_]]
        M = [[mpc(0)] * 4 for _ in range(4)]
        for (aa, bb, nn, tt) in B.T:
            th = 2 * mp.pi * sum(f[j] * int(nn[j]) for j in range(3))
            tx = mpf(str(round(float(tt), 12)))              # the exact decimal amplitude
            M[aa][bb] += tx * mp.expj(th); M[bb][aa] -= tx * mp.expj(-th)
        for (i, j), e in A.items():
            hij = mpc(0, 1) * M[i][j]
            miss += not (e.re.lo[s_] <= hij.real <= e.re.hi[s_] and (i == j or e.im.lo[s_] <= hij.imag <= e.im.hi[s_]))
    ev = B.levels(pts)
    agree = []
    for m_ in (-1.0, 0.0, 0.37, 2.5):
        ng, ok = inertia_neg(A, m_)
        agree.append(bool(ok.all()) and float(np.mean(ng == (ev < m_).sum(axis=1))))
    check("interval Bloch entries contain 40-digit values; interval inertia = float counts (J=(1,.8,1), kappa=.45)", miss == 0 and min(agree) == 1.0,
          f"missed {miss}/320 entries at 20 pts; inertia agreement {min(agree):.3f} at 400 pts x 4 shifts")


# ------------------------------------------------------------------------------------------------ isotropic landed families
def landed_nodes(kap, J=1.0):
    """Landed exact families (i) line points and (ii) four points (J = 1, kappa between kappa_c and kappa_h)."""
    out = []
    for c in np.roots([4 * kap ** 2, -2.0, J ** 2 - 4 * kap ** 2 - 2]):
        if abs(c.imag) < 1e-14 and abs(c.real) < 1:
            x = np.arccos(c.real) / (2 * np.pi)
            out += [(x, 1 - x, 0.0), (1 - x, x, 0.0)]
    cx = 1 - J / (4 * kap ** 2); c3 = (J + 2) / (4 * kap ** 2) - (4 + J - J ** 2) / J
    if abs(cx) < 1 and abs(c3) < 1:
        x = np.arccos(cx) / (2 * np.pi); f3 = np.arccos(c3) / (2 * np.pi)
        out += [(x, 1 - x, f3), (x, 1 - x, -f3), (1 - x, x, f3), (1 - x, x, -f3)]
    return out


def isotropic_check(label, kap, nexp):
    t0 = time.time()
    r = analyse((1.0, 1.0, 1.0), kap)
    nodes = r["nodes"]
    ex = landed_nodes(kap)
    dmax = max(min(pdist(n["f"], e) for e in ex) for n in nodes)
    dmax2 = max(min(pdist(n["f"], e) for n in nodes) for e in ex)
    numerical_integer_available = all(n["C"] is not None for n in nodes)
    sumC = sum(n["C"] for n in nodes if n["C"] is not None)
    sign_ok = numerical_integer_available and all(n["C"] == -int(np.sign(n["detV"])) and abs(n["C"]) == 1 for n in nodes)
    gap_ok = all(n["patches_ok"] == n["patches"] and n["contained"] for n in nodes)
    ok = len(nodes) == nexp == len(ex) and max(dmax, dmax2) < 1e-12 and r["vol"] == 1.0 and numerical_integer_available and sumC == 0 and sign_ok and gap_ok
    check(label, ok, f"{len(nodes)} clusters vs {len(ex)} landed nodes, max distance {max(dmax, dmax2):.1e}; vol={r['vol']:.1f} gaps "
          f"{sum(n['patches_ok'] for n in nodes)}/{sum(n['patches'] for n in nodes)} bound<={max(n['bound'] for n in nodes):.3g}<pi C={signs(nodes)} sum={sumC} "
          f"C=-sign detV {sign_ok} {time.time() - t0:.0f}s")


# ------------------------------------------------------------------------------------------------ 30-digit recomputation of C
def mp_chern_check():
    t0 = time.time()
    J, kap = (1.0, 0.8, 1.0), 0.45
    B = Bloch(J, kap)
    f, _, _ = refine_node(B, (0.2229990424, 0.6864370506, 0.2502403395))
    Sf = Surface(f, 15, 128, 32)
    V, keys = Sf.vertices()
    P4 = Sf.plaquette_index(keys).reshape(-1, 4)
    mpmath.mp.dps = 30
    T = [(a, b, n, mpmath.mpf(str(round(float(t), 12)))) for (a, b, n, t) in B.T]
    frames = []
    for v in V:
        fv = [mpmath.mpf(float(x)) for x in v]
        M = mpmath.matrix(4, 4)
        for (a, b, n, t) in T:
            e = mpmath.expj(2 * mpmath.pi * sum(fv[j] * int(n[j]) for j in range(3)))
            M[a, b] += t * e; M[b, a] -= t * mpmath.conj(e)
        E, Q = mpmath.eigh(mpmath.mpc(0, 1) * M)
        frames.append((Q[:, 0], Q[:, 1]))
    cache = {}

    def link(i, j):
        if (i, j) not in cache:
            A_, B_ = frames[i], frames[j]
            m = [[sum(mpmath.conj(A_[x][r]) * B_[y][r] for r in range(4)) for y in range(2)] for x in range(2)]
            cache[(i, j)] = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        return cache[(i, j)]
    ph_mp = np.array([float(mpmath.arg(link(v0, v1) * link(v1, v2) * link(v2, v3) * link(v3, v0))) for v0, v1, v2, v3 in P4])
    Cd, ph_d = lattice_chern(B, Sf)
    d = (ph_d - ph_mp + np.pi) % (2 * np.pi) - np.pi
    Cmp = ph_mp.sum() / (2 * np.pi)
    check("30-digit mpmath recomputation of the lattice Chern number (A off-plane node, m_F=32, exact decimal couplings)",
          abs(Cmp - round(Cmp)) < 1e-10 and round(Cmp) == round(Cd) == -1 and np.abs(d).max() < 1e-10,
          f"{fmt3(f)} C_mp={Cmp:.12f} C_double={Cd:.12f} max phase diff {np.abs(d).max():.1e} over {len(P4)} plaquettes {time.time() - t0:.0f}s")


# ------------------------------------------------------------------------------------------------ main
if __name__ == "__main__":
    check_interval_sanity()
    isotropic_check("isotropic J=(1,1,1), kappa=3/10: clusters = landed line points, C = -sign det V", 0.3, 2)
    isotropic_check("isotropic J=(1,1,1), kappa=9/20: clusters = landed six nodes, C = -sign det V", 0.45, 6)
    coupling_check("A J=(1,.8,1) kappa=.45: zone, gaps, bound, C",
                   (1.0, 0.8, 1.0), 0.45,
                   [(0.2229990424, 0.6864370506, 0.2502403395), (0.3135629494, 0.7770009576, 0.7497596605), (0.3680037842, 0.6319962158, 0.0),
                    (0.6319962158, 0.3680037842, 0.0), (0.6864370506, 0.2229990424, 0.2502403395), (0.7770009576, 0.3135629494, 0.7497596605)])
    coupling_check("B J=(1.2,.8,1) kappa=.3: zone, gaps, bound, C",
                   (1.2, 0.8, 1.0), 0.3,
                   [(0.2550569293, 0.5899470504, 0.0426385692), (0.3661397636, 0.6338602364, 0.0), (0.4100529496, 0.7449430707, 0.9573614308),
                    (0.5899470504, 0.2550569293, 0.0426385692), (0.6338602364, 0.3661397636, 0.0), (0.7449430707, 0.4100529496, 0.9573614308)])
    coupling_check("C J=(1,.8,1) kappa=.8: zone, gaps, bound, C",
                   (1.0, 0.8, 1.0), 0.8,
                   [(0.0352628499, 0.6874758782, 0.3404884877), (0.3125241218, 0.9647371501, 0.6595115123), (0.4112126412, 0.5887873588, 0.0),
                    (0.5887873588, 0.4112126412, 0.0), (0.6874758782, 0.0352628499, 0.3404884877), (0.9647371501, 0.3125241218, 0.6595115123)])
    coupling_check("E J=(.9,1.1,1.3) kappa=.4: zone, gaps, bound, C",
                   (0.9, 1.1, 1.3), 0.4, [(0.3207616147, 0.6792383853, 0.0), (0.6792383853, 0.3207616147, 0.0)])
    coupling_check("D J=(1.2,.8,1) kappa=.2 (slow node: s=2^-7, 512^2 patches, m_F=256): zone, gaps, bound, C",
                   (1.2, 0.8, 1.0), 0.2, [(0.3552965520, 0.6447034480, 0.0), (0.6447034480, 0.3552965520, 0.0)], q=15, m_f=512, m_F=256)
    mp_chern_check()
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")

# A failed decisive check must fail the bounded execution.
if __name__ == "__main__":
    raise SystemExit(int(not all(RESULTS)))
