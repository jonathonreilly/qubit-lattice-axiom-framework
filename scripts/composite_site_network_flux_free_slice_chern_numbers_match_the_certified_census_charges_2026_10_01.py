#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: Chern numbers of the two lowest bands on 2D torus slices of the Brillouin zone, and their jumps
against the node charges of the touching census.

Setting. Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings
J = (J_x, J_y, J_z), odd term kappa, four-site Bloch matrix H(f) = i M(f) over the fractional zone [0,1)^3; "occupied" = the two lowest bands,
middle gap = eps_3 - eps_2. Nothing here is adopted framework premise. Couplings are the exact decimals written: the interval code brackets each
amplitude 2J, 2 kappa that is not exactly 2 one ulp either side of its double.
Couplings: B = (6/5, 4/5, 1; 3/10) and H1 = (6/5, 4/5, 1; 1/5).

Slices. A slice is the 2-torus {f : n.f = c (mod 1)}, n a primitive integer vector, parametrised f(s,t) = c w + s e_a + t e_b, (s,t) in [0,1)^2,
with integer e_a, e_b, e_a x e_b = n (so the plaquette orientation (s,t) counterclockwise is the orientation seen from +n) and n.w = 1.
Families: "f3" (n = (0,0,1)), "f1" (n = (1,0,0)), "f1-f2" (n = (1,-1,0), e_a = (1,1,0)). Slice constants c are dyadic, so every phase is exact.
The planned slices put at least one constant c in every gap between the node layers {n.f_node} of the family (checked: "gaps k/k").

Per-slice certificate (computer-assisted; interval parts round OUTWARD), the method of the anisotropic-touchings Chern-certificate runner
(composite_site_network_flux_free_anisotropic_touchings_certified_by_lattice_chern_numbers_2026_10_01) with the cube surface replaced by the torus:
(A) Gap [INTERVAL]. Adaptive quadtree on the parameter square: a cell (dyadic centre, half-width h) is cleared when two outward-rounded interval
    LDL^T inertias of H(c) - x1 and H(c) - x2 (floats x1 < x2 around the float middle gap at the centre) each give exactly two negative pivots and
    the lower bound x2 - x1 - 2 r(h) >= g_target, with r(h) = h rho(E_a + E_b) (Weyl; E the entrywise bound of |dH/d(s,t)|, rho by Collatz-Wielandt).
    The cleared cells tile the square (area exactly 1); g = the minimum of the cell lower bounds is an interval-certified lower bound of the
    middle gap on the whole slice.
(B) Admissibility [INTERVAL] (the lemma of that note, applied to a closed torus; its proof is local to plaquettes and edges, and closedness is
    used to cancel the edge terms): with Fro >= ||d H||_F, Op >= ||d H||_op, Op2 >= ||d^2 H||_op along the two parameters (outward rounded) and g, a
    plaquette of side h has flux |Phi_p| <= 2 h^2 Fro_a Fro_b / g^2 and each edge a transport-versus-overlap phase mismatch
    |delta_e| <= alpha b2 h^3/6 + x^2/(1-x), alpha = Fro/g, x = alpha^2 h^2/2, b2 = sqrt2 (Op2/g + 8 Op^2/(pi g^2)) + (Op/g) alpha.
    If |Phi_p| + sum_e |delta_e| < pi (mpmath intervals; the mesh m is the smallest power of two with bound <= 1), the Fukui-Hatsugai-Suzuki lattice Chern
    number of the two lowest bands (principal phases of the four-link products of det(u_v^dag u_w), v0=(i,j), v1=(i+1,j), v2=(i+1,j+1), v3=(i,j+1),
    periodic) equals the Chern number of the occupied bundle on the slice.
(C) Lattice integer [FLOAT, not interval-verified]: eigenvectors and the phase sum in double precision. Checks: the integer at mesh m and m/2 agree, the
    observed max |principal phase| <= the certified bound, the certified g <= the float minimum gap of a 256^2 grid, a float sampling control of the cell
    bounds with a negative control (gap controls), and a 30-digit mpmath recomputation of the plaquette phases on one slice (last check).
Sign convention. charge = sign T = sign det V (landed chirality, T = Im Tr(P d1H P d2H P d3H) = 2 det V of the kernel Pauli vector); the Chern-certificate
note's convention is C_sphere = -sign det V (sphere oriented outward). For slices c1 < c2 (normal +n), Stokes on the occupied bundle gives
C(c2) - C(c1) = sum over the nodes between of C_sphere = -(sum of their charges). The runner compares every certified slice-to-slice jump with this.
Particle-hole: H(-f) = -conj(H(f)) gives C(-c) = C(c); slices at c and 1 - c are certified independently and compared.
Node data (positions, charges, |T|) are embedded from the certified touching census runners (B: ..._with_charges_at_five_anisotropic_couplings_2026_10_01;
H1: ..._across_coupling_regimes_2026_10_01), interval-certified there; here they predict which
nodes lie between two slices and are checked against det V. Completeness of the node list is the census result and is not re-proved here.
Prints TOTAL: PASS=N FAIL=M. Run with -v for the per-slice table (g, bound, mesh, lattice integers, max phase).
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"

import sys
import time

import numpy as np
from mpmath import iv, mp, mpc, mpf
import mpmath

AUDIT_TIMEOUT_SEC = 300

RESULTS = []
T0 = time.time()
JUMPS = []                 # (observed slice jump, sum of census charges crossed)
VERBOSE = "-v" in sys.argv


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

    def levels(self, F, chunk=50000):
        F = np.atleast_2d(F)
        if len(F) <= chunk:
            return np.linalg.eigvalsh(self.H(F))
        return np.concatenate([np.linalg.eigvalsh(self.H(F[s:s + chunk])) for s in range(0, len(F), chunk)])


# ------------------------------------------------------------------------------------------------ float node refinement, chirality
def kernel_basis(B, f, nker=2):
    ev, V = np.linalg.eigh(B.H(np.asarray(f)[None, :])[0])
    idx = np.argsort(np.abs(ev))[:nker]
    return ev[idx], V[:, idx]


def _pauli(Mat, W):
    h = W.conj().T @ Mat @ W
    return (h[0, 0] + h[1, 1]).real / 2, np.array([h[0, 1].real, -h[0, 1].imag, (h[0, 0] - h[1, 1]).real / 2])


def refine_node(B, f0, iters=14):
    """Newton iteration on the Pauli vector d(f) of the 2x2 kernel block (kernel re-chosen each step). Returns (f, |d|)."""
    f = np.asarray(f0, dtype=float).copy()
    for _ in range(iters):
        ev, W = kernel_basis(B, f)
        t, d = _pauli(B.H(f[None, :])[0], W)
        Vj = np.array([_pauli(B.dH(f[None, :], i)[0], W)[1] for i in range(3)])
        f = f + np.linalg.solve(Vj.T, -d)
    ev, W = kernel_basis(B, f)
    t, d = _pauli(B.H(f[None, :])[0], W)
    return f, float(np.linalg.norm(d))


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


_PH = {}


def phase_table(values):
    """Rigorous enclosures of cos and sin of 2 pi v for exactly representable floats v (converted exactly), one extra ulp outward (cached)."""
    out = {}
    for v in values:
        v = float(v)
        if v not in _PH:
            x = iv.mpf(mpf(v))
            a = 2 * iv.pi * x
            cc, ss = iv.cos(a), iv.sin(a)
            _PH[v] = (float(rd(float(cc.a))), float(ru(float(cc.b))), float(rd(float(ss.a))), float(ru(float(ss.b))))
        out[v] = _PH[v]
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
    """Upper-triangle complex-interval entries of H(c) = i M(c) at dyadic points Cs (Cs @ n exact in floating point)."""
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


# ------------------------------------------------------------------------------------------------ slices
SLICES = {
    "f3": dict(n=(0, 0, 1), w=(0, 0, 1), ea=(1, 0, 0), eb=(0, 1, 0)),
    "f1": dict(n=(1, 0, 0), w=(1, 0, 0), ea=(0, 1, 0), eb=(0, 0, 1)),
    "f1-f2": dict(n=(1, -1, 0), w=(1, 0, 0), ea=(1, 1, 0), eb=(0, 0, 1)),
}
for _k, _s in SLICES.items():
    assert tuple(np.cross(_s["ea"], _s["eb"])) == _s["n"] and np.dot(_s["n"], _s["ea"]) == 0 and np.dot(_s["n"], _s["eb"]) == 0 and np.dot(_s["n"], _s["w"]) == 1


def slice_points(fam, c, S, T):
    """f(s, t) = c w + s e_a + t e_b for dyadic c, s, t (exact in floating point); returns (..., 3)."""
    sp = SLICES[fam]
    return float(c) * np.array(sp["w"], float) + np.asarray(S, float)[..., None] * np.array(sp["ea"], float) + np.asarray(T, float)[..., None] * np.array(sp["eb"], float)


IVPI = iv.pi


def E_dir(Tm, e, order):
    """Entrywise upper bounds E[a, b] >= sum over terms |t| (2 pi |n.e|)^order (diagonal terms counted twice), floats rounded up."""
    E = [[iv.mpf(0) for _ in range(4)] for _ in range(4)]
    for (a, b, n, t) in Tm:
        k = abs(sum(int(n[i]) * int(e[i]) for i in range(3)))
        tt = iv.mpf(t_interval(float(t))[1])
        w = tt * (2 * IVPI * k) ** order
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
    """Certified derivative constants along the two parameters (s, t) of a slice family."""

    def __init__(self, B, fam):
        sp = SLICES[fam]
        self.E1 = [E_dir(B.T, sp["ea"], 1), E_dir(B.T, sp["eb"], 1)]
        E2 = [E_dir(B.T, sp["ea"], 2), E_dir(B.T, sp["eb"], 2)]
        self.Fro1 = [fro_upper(E) for E in self.E1]
        self.Op1 = [min(cw_upper(E), fro_upper(E)) for E in self.E1]
        self.Op2 = [cw_upper(E) for E in E2]
        self.rho = cw_upper(ru(self.E1[0] + self.E1[1]))

    def lip(self, h):
        """Bound of ||H(f) - H(c)||_op for |s - s_c|, |t - t_c| <= h (h a power of two)."""
        return float(ru(self.rho * h))


def bound_iv(K, g, h):
    """Outward-rounded upper bound of flux + four edge mismatches for a plaquette of side h with middle gap >= g; inf if x >= 1."""
    G = iv.mpf(float(g)); hh = iv.mpf(float(h))
    flux = 2 * hh ** 2 * iv.mpf(K.Fro1[0]) * iv.mpf(K.Fro1[1]) / G ** 2
    edges = []
    for j in (0, 1):
        Fj, Oj, O2 = iv.mpf(K.Fro1[j]), iv.mpf(K.Op1[j]), iv.mpf(K.Op2[j])
        al = Fj / G; ap = Oj / G
        pp = O2 / G + 8 * Oj ** 2 / (iv.pi * G ** 2)
        b2 = iv.sqrt(iv.mpf(2)) * pp + ap * al
        x = al ** 2 * hh ** 2 / 2
        if not (x.b < 1):
            return float("inf")
        edges.append(al * b2 * hh ** 3 / 6 + x ** 2 / (1 - x))
    return float(ru(float((flux + 2 * edges[0] + 2 * edges[1]).b)))


# ------------------------------------------------------------------------------------------------ (A) interval gap on a slice (quadtree)
def certify_gap(B, K, fam, c, g_target, n0=32, hmin=2.0 ** -16, frac=0.999, chunk=40000):
    """Adaptive quadtree. Returns dict(g=certified lower bound of the middle gap over the slice (0 if failed), area, cells, levels, left, rec)
    where rec = arrays (s, t, h, lower bound) of the cleared cells."""
    a_, b_, n_, t_ = build(B.T)
    h = 0.5 / n0
    g1 = (np.arange(n0) + 0.5) / n0
    S0, T0 = np.meshgrid(g1, g1, indexing="ij")
    ST = np.stack([S0.ravel(), T0.ravel()], axis=1)
    area = 0.0; gmin = np.inf; ncell = 0; lev = 0; rec = []
    while True:
        r = K.lip(h)
        keep = []
        for s0 in range(0, len(ST), chunk):
            sub = ST[s0:s0 + chunk]
            F = slice_points(fam, c, sub[:, 0], sub[:, 1])
            ev = B.levels(F)
            e2, e3 = ev[:, 1], ev[:, 2]
            mu = 0.5 * (e2 + e3); rho = frac * 0.5 * (e3 - e2)
            pre = 2 * rho > (g_target + 2 * r) * (1 + 1e-9)
            cleared = np.zeros(len(sub), dtype=bool)
            if pre.any():
                idx = np.nonzero(pre)[0]
                A = H_intervals(F[idx], a_, b_, n_, t_)
                x1 = mu[idx] - rho[idx]; x2 = mu[idx] + rho[idx]
                n1, ok1 = inertia_neg(A, x1); n2, ok2 = inertia_neg(A, x2)
                gl = rd(rd(x2 - x1) - 2 * r)
                good = ok1 & ok2 & (n1 == 2) & (n2 == 2) & (gl >= g_target)
                cleared[idx[good]] = True
                if good.any():
                    gmin = min(gmin, float(gl[good].min()))
                    ig = idx[good]
                    rec.append(np.stack([sub[ig, 0], sub[ig, 1], np.full(len(ig), h), gl[good]], axis=1))
            nc = int(cleared.sum())
            ncell += nc
            area += nc * (2 * h) ** 2
            keep.append(sub[~cleared])
        ST = np.concatenate(keep) if keep else np.zeros((0, 2))
        if len(ST) == 0:
            break
        if h <= hmin:
            break
        off = np.array([(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]) * h
        ST = (ST[:, None, :] + off[None, :, :]).reshape(-1, 2)
        h /= 2
        lev += 1
    left = len(ST)
    ok = left == 0 and area == 1.0 and np.isfinite(gmin)
    return dict(g=gmin if ok else 0.0, area=area, cells=ncell, levels=lev, left=left, ok=ok,
                rec=np.concatenate(rec) if rec else np.zeros((0, 4)))


# ------------------------------------------------------------------------------------------------ (C) lattice Chern number on the slice torus
def frames(B, pts, chunk=50000):
    U = np.empty((len(pts), 4, 2), dtype=complex)
    for s0 in range(0, len(pts), chunk):
        e, W = np.linalg.eigh(B.H(pts[s0:s0 + chunk]))
        U[s0:s0 + chunk] = W[:, :, :2]
    return U


def _link(Ua, Ub):
    O = np.einsum("...ia,...ib->...ab", Ua.conj(), Ub)
    return O[..., 0, 0] * O[..., 1, 1] - O[..., 0, 1] * O[..., 1, 0]


def lattice_chern(B, fam, c, m, rows=32, keep=False):
    """Fukui-Hatsugai-Suzuki lattice Chern number of the two lowest bands on the m x m periodic mesh of the slice (streamed in row blocks),
    max |principal plaquette phase|, and (keep=True) the m x m array of principal plaquette phases."""
    g = np.arange(m) / m
    tot = 0.0; mx = 0.0; blocks = []
    for r0 in range(0, m, rows):
        R = min(rows, m - r0)
        S, T = np.meshgrid(np.arange(r0, r0 + R + 1) % m / m, g, indexing="ij")
        U = frames(B, slice_points(fam, c, S, T).reshape(-1, 3)).reshape(R + 1, m, 4, 2)
        L1 = _link(U[:-1], U[1:])
        L2 = _link(U, np.roll(U, -1, axis=1))
        ph = np.angle(L1 * L2[1:] * np.conj(np.roll(L1, -1, axis=1)) * np.conj(L2[:-1]))
        tot += float(ph.sum()); mx = max(mx, float(np.abs(ph).max()))
        if keep:
            blocks.append(ph)
    return tot / (2 * np.pi), mx, (np.concatenate(blocks) if keep else None)


# ------------------------------------------------------------------------------------------------ census data (embedded) and slice plans
# charge = sign T from the interval-certified census runners (five-couplings census for B, across-regimes census for H1)
TB_OFF, TB_LINE, TH1_LINE = 143.863060903176832, 106.494170705382777, 11.1880437


def node_data():
    xl = float(np.arccos(-2.0 / 3.0) / (2 * np.pi))                       # B line nodes: cos 2 pi x = -2/3 exactly
    xh = float(np.arccos(6.0 - 2.5 * np.sqrt(7.0)) / (2 * np.pi))         # H1 line nodes: 4c^2 - 48c - 31 = 0 root in [-1,1]
    B = [((0.25505692926694, 0.58994705039569, 0.042638569171718), +1, TB_OFF),
         ((0.58994705039569, 0.25505692926694, 0.042638569171718), -1, TB_OFF),
         ((0.74494307073306, 0.41005294960431, 0.95736143082828), -1, TB_OFF),
         ((0.41005294960431, 0.74494307073306, 0.95736143082828), +1, TB_OFF),
         ((xl, 1 - xl, 0.0), -1, TB_LINE), ((1 - xl, xl, 0.0), +1, TB_LINE)]
    H1 = [((xh, 1 - xh, 0.0), +1, TH1_LINE), ((1 - xh, xh, 0.0), -1, TH1_LINE)]
    return B, H1


COUPLINGS = {"B": ((1.2, 0.8, 1.0), 0.3), "H1": ((1.2, 0.8, 1.0), 0.2)}
# (coupling, family, [(c, g_target)]) ; c dyadic; one slice in every gap between the node layers of the family
PLAN = [
    ("B", "f3", [(5 / 256, 0.075), (1 / 16, 0.13), (0.5, 1.5), (15 / 16, 0.13), (251 / 256, 0.075)]),
    ("B", "f1", [(0.0, 0.6), (5 / 16, 0.09), (25 / 64, 0.085), (0.5, 0.6), (39 / 64, 0.085), (11 / 16, 0.09)]),
    ("B", "f1-f2", [(0.0, 1.5), (5 / 16, 0.062), (0.5, 0.6), (11 / 16, 0.062)]),
    ("H1", "f3", [(0.25, 1.5), (0.5, 2.0)]),
    ("H1", "f1", [(0.0, 0.4), (0.5, 0.4)]),
    ("H1", "f1-f2", [(0.0, 1.5), (0.5, 0.4)]),
]
MESHES = (64, 128, 256, 512, 1024)
BOUND_MAX = 1.0


def node_coord(fam, f):
    return float(np.mod(np.dot(SLICES[fam]["n"], np.asarray(f, float)), 1.0))


def between_charges(fam, cs, nodes):
    """Sum of the census charges of the nodes whose coordinate n.f lies between c_k and c_{k+1} (cyclically; the last interval wraps to c_0 + 1)."""
    out = []
    for k in range(len(cs)):
        lo, hi = cs[k], cs[(k + 1) % len(cs)]
        if hi <= lo:
            hi += 1.0
        tot = 0
        for (f, q, _) in nodes:
            x = node_coord(fam, f)
            for xx in (x, x + 1.0):
                if lo < xx < hi:
                    tot += q
        out.append(tot)
    return out


def gaps_covered(fam, cs, nodes):
    """(covered, total): the node layers (distinct coordinates n.f) cut the circle into total gaps; covered = gaps containing a slice constant."""
    xs = sorted({round(node_coord(fam, f), 6) % 1.0 for (f, _, _) in nodes})
    cov = 0
    for k in range(len(xs)):
        lo, hi = xs[k], xs[(k + 1) % len(xs)]
        if hi <= lo:
            hi += 1.0
        cov += any(lo < c < hi or lo < c + 1.0 < hi for c in cs)
    return cov, len(xs)


def min_dist(fam, cs, nodes):
    d = 1.0
    for (f, q, _) in nodes:
        x = node_coord(fam, f)
        for c in cs:
            dd = abs(x - c)
            d = min(d, dd, 1 - dd)
    return d


def float_gap_min(B, fam, c, m=256):
    g = (np.arange(m) + 0.5) / m
    S, T = np.meshgrid(g, g, indexing="ij")
    ev = B.levels(slice_points(fam, c, S, T).reshape(-1, 3))
    return float((ev[:, 2] - ev[:, 1]).min())


def certify_slice(B, K, fam, c, g_target):
    """Full per-slice certificate. Returns dict with the certified integer C (None if any step fails)."""
    gr = certify_gap(B, K, fam, c, g_target)
    res = dict(c=c, gap=gr, C=None, bound=float("inf"), m=0, Cf=float("nan"), Cf2=float("nan"), maxph=float("nan"), fmin=float_gap_min(B, fam, c))
    if not gr["ok"]:
        return res
    g = gr["g"]
    for m in MESHES:
        bnd = bound_iv(K, g, 1.0 / m)
        if bnd <= BOUND_MAX:
            break
    res["bound"], res["m"] = bnd, m
    if not bnd < float(iv.pi.a):
        return res
    Cf, mx, _ = lattice_chern(B, fam, c, m)
    Cf2, _, _ = lattice_chern(B, fam, c, m // 2)
    res.update(Cf=Cf, Cf2=Cf2, maxph=mx)
    ok = abs(Cf - round(Cf)) < 1e-6 and abs(Cf2 - round(Cf)) < 1e-6 and res["maxph"] <= bnd and g <= res["fmin"]
    if ok:
        res["C"] = int(round(Cf))
    return res


def frac_str(c):
    from fractions import Fraction
    f = Fraction(c).limit_denominator(1024)
    return str(f)


# ------------------------------------------------------------------------------------------------ checks
def check_interval_sanity():
    """Interval Bloch entries contain 40-digit values at slice points; interval inertia = float counts."""
    B = Bloch(*COUPLINGS["B"])
    a, b, n, t = build(B.T)
    rng = np.random.default_rng(0)
    S = np.floor(rng.random(400) * 2 ** 14) / 2 ** 14; T = np.floor(rng.random(400) * 2 ** 14) / 2 ** 14
    pts = slice_points("f1-f2", 5 / 16, S, T)
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
    agree = []; defin = []
    for m_ in (-1.0, 0.0, 0.37, 2.5):
        ng, ok = inertia_neg(A, m_)
        defin.append(float(ok.mean()))
        agree.append(float(np.mean((ng == (ev < m_).sum(axis=1))[ok])))      # where no pivot interval meets 0 (else the cell is subdivided)
    check("interval Bloch entries contain 40-digit values; interval inertia = float counts (B, slice f1-f2 = 5/16)",
          miss == 0 and min(agree) == 1.0 and min(defin) > 0.99,
          f"missed {miss}/320 entries at 20 pts; inertia agreement {min(agree):.3f} on the {min(defin):.3f}+ of 400 pts with definite pivots, 4 shifts")


def check_convention(name, nodes):
    """det V (float, Newton-refined node) has the sign of the census charge and 2 det V = T."""
    B = Bloch(*COUPLINGS[name])
    rows = []; ok = True
    for (f0, q, Tabs) in nodes:
        f, resid = refine_node(B, f0)
        dV, nker = det_V(B, f)
        s = int(np.sign(dV))
        good = (s == q) and nker == 2 and resid < 1e-12 and abs(2 * abs(dV) - Tabs) < 1e-6 * Tabs and float(np.abs(f - np.asarray(f0)).max()) < 1e-7
        ok &= good
        rows.append(f"{'+' if s > 0 else '-'}")
    check(f"{name}: node chirality sign det V = census charge, 2|det V| = |T|, Newton from embedded positions", ok,
          f"{len(nodes)} nodes, sign det V = {''.join(rows)} vs census {''.join('+' if q > 0 else '-' for _, q, _ in nodes)}; sum charges {sum(q for _, q, _ in nodes):+d}")


def family_check(name, fam, plan, nodes, K_cache, B_cache):
    t0 = time.time()
    B = B_cache[name]
    K = K_cache[(name, fam)]
    cs = [c for c, _ in plan]
    res = [certify_slice(B, K, fam, c, gt) for c, gt in plan]
    Cs = [r["C"] for r in res]
    certified = all(C is not None for C in Cs)
    chg = between_charges(fam, cs, nodes)
    pred = [-q for q in chg]                                   # convention: C(c2) - C(c1) = -(sum of charges between)
    obs = [(Cs[(k + 1) % len(cs)] - Cs[k]) if certified else None for k in range(len(cs))]
    jumps_ok = certified and obs == pred and sum(obs) == 0
    if certified:
        JUMPS.extend(zip(obs, chg))
    sep = min_dist(fam, cs, nodes)
    gmin = min((r["gap"]["g"] for r in res if r["gap"]["ok"]), default=0.0)
    mfs = sorted({r["m"] for r in res if r["m"]})
    bmax = max(r["bound"] for r in res)
    cov, ngap = gaps_covered(fam, cs, nodes)
    # particle-hole consistency: H(-f) = -conj(H(f)) gives C(-c) = C(c); compare the independently certified slices c and 1 - c
    pairs = [(i, j) for i, c in enumerate(cs) for j, c2 in enumerate(cs) if i < j and abs(c + c2 - 1.0) < 1e-12]
    ph_ok = certified and all(Cs[i] == Cs[j] for i, j in pairs)
    ok = certified and jumps_ok and sep > 0.01 and all(r["gap"]["ok"] for r in res) and cov == ngap and ph_ok
    sg = lambda L: ",".join("?" if v is None else f"{v:+d}" if v else "0" for v in L)
    check(f"{name} {fam}: slice Chern numbers, gap + admissibility, jumps = -(node charges)", ok,
          f"c={','.join(frac_str(c) for c in cs)} C={sg(Cs)} jumps obs {sg(obs)} pred {sg(pred)} g>={gmin:.3g} bound<={bmax:.2g} m={mfs[0]}..{mfs[-1]} "
          f"gaps {cov}/{ngap} C(c)=C(1-c) on {len(pairs)} pairs {ph_ok} node dist>={sep:.3f} {time.time() - t0:.0f}s")
    if VERBOSE:
        for r in res:
            gp = r["gap"]
            print(f"   {name} {fam} c={frac_str(r['c']):>7} g>={gp['g']:.4f} (float min {r['fmin']:.4f}) cells {gp['cells']} levels {gp['levels']} "
                  f"bound {r['bound']:.3f} m={r['m']} Cf={r['Cf']:+.9f} Cf(m/2)={r['Cf2']:+.9f} max|phase| {r['maxph']:.4f} C={r['C']}")
    return res


def gap_controls(B_cache, K_cache):
    """(a) FLOAT sampling: the certified cell bounds lie below the float gap at random points of the cells (hardest slice, lowest-bound cells and random cells);
    (b) negative control: a target above the true minimum gap must NOT be certified."""
    B = B_cache["B"]; K = K_cache[("B", "f3")]
    c = 5 / 256
    gr = certify_gap(B, K, "f3", c, 0.075)
    rec = gr["rec"]
    rng = np.random.default_rng(1)
    order = np.argsort(rec[:, 3])
    sel = np.unique(np.concatenate([order[:2000], rng.choice(len(rec), min(2000, len(rec)), replace=False)]))
    npt = 8
    s = rec[sel, 0][:, None] + (rng.random((len(sel), npt)) * 2 - 1) * rec[sel, 2][:, None]
    t = rec[sel, 1][:, None] + (rng.random((len(sel), npt)) * 2 - 1) * rec[sel, 2][:, None]
    ev = B.levels(slice_points("f3", c, s, t).reshape(-1, 3))
    margin = ((ev[:, 2] - ev[:, 1]).reshape(len(sel), npt) - rec[sel, 3][:, None]).min()
    neg = certify_gap(B, K, "f3", c, 0.11, hmin=2.0 ** -11)
    check("interval gap controls (B, f3 = 5/256): cell bounds below float gaps at random points; target 0.11 above the minimum is not certified",
          gr["ok"] and margin >= -1e-12 and (not neg["ok"]) and neg["left"] > 0,
          f"{len(sel)} cells x {npt} pts, min(float gap - bound) = {margin:.2e}; target 0.075 certified in {gr['cells']} cells, target 0.11 left {neg['left']} cells uncleared at h=2^-11")


def constants_control(B_cache, K_cache):
    """FLOAT sampling control of the certified constants along the slice parameters: max over random slice points of ||d H||_F, ||d H||_op, ||d^2 H||_op
    (central differences) and of ||H(f) - H(c)||_op over random points of cells of half-width 2^-8 against Fro1, Op1, Op2 and lip(2^-8)."""
    rng = np.random.default_rng(2)
    worst = 0.0; ok = True; n = 0; TOL = 1e-9       # the Frobenius bound is attained (one term per entry), so allow float noise
    for nm in B_cache:
        for fam in SLICES:
            B = B_cache[nm]; K = K_cache[(nm, fam)]; sp = SLICES[fam]
            pts = slice_points(fam, 0.3, rng.random(2000), rng.random(2000))
            H0 = B.H(pts)
            for ax, e in enumerate((sp["ea"], sp["eb"])):
                ev = np.array(e, float)
                d1 = sum(e[j] * B.dH(pts, j) for j in range(3))
                hs = 1e-4
                d2 = (B.H(pts + hs * ev) - 2 * H0 + B.H(pts - hs * ev)) / hs ** 2
                rt = [np.linalg.norm(d1, axis=(1, 2)).max() / K.Fro1[ax], np.linalg.norm(d1, ord=2, axis=(1, 2)).max() / K.Op1[ax],
                      np.linalg.norm(d2, ord=2, axis=(1, 2)).max() / K.Op2[ax]]
                worst = max(worst, max(rt)); ok &= max(rt) <= 1.0 + TOL; n += 3
            h = 2.0 ** -8
            s0, t0 = rng.random(2000), rng.random(2000)
            Hc = B.H(slice_points(fam, 0.3, s0, t0))
            Hf = B.H(slice_points(fam, 0.3, s0 + (rng.random(2000) * 2 - 1) * h, t0 + (rng.random(2000) * 2 - 1) * h))
            rt = np.linalg.norm(Hf - Hc, ord=2, axis=(1, 2)).max() / K.lip(h)
            worst = max(worst, rt); ok &= rt <= 1.0 + TOL; n += 1
    check("certified derivative constants and Lipschitz radius dominate float samples (2 couplings x 3 families)", ok,
          f"{n} ratios sample/certified, largest {worst:.6f} (must be <= 1 + 1e-9; the Frobenius bounds are attained)")


def sign_summary():
    nz = [(o, q) for (o, q) in JUMPS if q != 0]
    ok = len(JUMPS) > 0 and all(o == -q for (o, q) in JUMPS) and len(nz) > 0
    check("sign convention: every slice jump equals minus the census charge crossed (C = -sign T per node, slices oriented by +n)", ok,
          f"{len(JUMPS)} slice-to-slice jumps, {len(nz)} nonzero (|jump| 1 or 2), all obs = -charge; the opposite convention would contradict {len(nz)} of {len(nz)}")


def mp_check():
    """30-digit recomputation of the plaquette phases on one slice (B, f1-f2 = 1/2, mesh 64, exact decimal couplings)."""
    t0 = time.time()
    B = Bloch(*COUPLINGS["B"])
    fam, c, m = "f1-f2", 0.5, 64
    g = np.arange(m) / m
    S, T = np.meshgrid(g, g, indexing="ij")
    V = slice_points(fam, c, S, T).reshape(-1, 3)
    mpmath.mp.dps = 30
    Tm = [(a, b, n, mpmath.mpf(str(round(float(t), 12)))) for (a, b, n, t) in B.T]
    fr = []
    for v in V:
        fv = [mpmath.mpf(float(x)) for x in v]
        M = mpmath.matrix(4, 4)
        for (a, b, n, t) in Tm:
            e = mpmath.expj(2 * mpmath.pi * sum(fv[j] * int(n[j]) for j in range(3)))
            M[a, b] += t * e; M[b, a] -= t * mpmath.conj(e)
        E, Q = mpmath.eigh(mpmath.mpc(0, 1) * M)
        fr.append((Q[:, 0], Q[:, 1]))
    cache = {}

    def link(i, j):
        if (i, j) not in cache:
            A_, B_ = fr[i], fr[j]
            mm = [[sum(mpmath.conj(A_[x][r]) * B_[y][r] for r in range(4)) for y in range(2)] for x in range(2)]
            cache[(i, j)] = mm[0][0] * mm[1][1] - mm[0][1] * mm[1][0]
        return cache[(i, j)]
    idx = lambda i, j: (i % m) * m + (j % m)
    ph_mp = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            v0, v1, v2, v3 = idx(i, j), idx(i + 1, j), idx(i + 1, j + 1), idx(i, j + 1)
            ph_mp[i, j] = float(mpmath.arg(link(v0, v1) * link(v1, v2) * link(v2, v3) * link(v3, v0)))
    Cd, _, ph_d = lattice_chern(B, fam, c, m, keep=True)
    d = (ph_d - ph_mp + np.pi) % (2 * np.pi) - np.pi
    Cmp = ph_mp.sum() / (2 * np.pi)
    check("30-digit mpmath recomputation of the plaquette phases (B, f1-f2 = 1/2, mesh 64, exact decimal couplings)",
          abs(Cmp - round(Cmp)) < 1e-10 and round(Cmp) == round(Cd) and np.abs(d).max() < 1e-10,
          f"C_mp={Cmp:.10f} C_double={Cd:.10f} max phase diff {np.abs(d).max():.1e} over {m * m} plaquettes {time.time() - t0:.0f}s")


# ------------------------------------------------------------------------------------------------ main
if __name__ == "__main__":
    nodesB, nodesH1 = node_data()
    NODES = {"B": nodesB, "H1": nodesH1}
    check_interval_sanity()
    check_convention("B", nodesB)
    check_convention("H1", nodesH1)
    B_cache = {k: Bloch(*v) for k, v in COUPLINGS.items()}
    K_cache = {(nm, fam): Consts(B_cache[nm], fam) for nm in B_cache for fam in SLICES}
    constants_control(B_cache, K_cache)
    for (nm, fam, plan) in PLAN:
        family_check(nm, fam, plan, NODES[nm], K_cache, B_cache)
    gap_controls(B_cache, K_cache)
    sign_summary()
    mp_check()
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}  runtime {time.time() - T0:.0f}s")
