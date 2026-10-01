#!/usr/bin/env python3
"""Node count of the supplied composite-network comparator versus the odd term kappa at the fixed anisotropic coupling (Jx, Jy, Jz) = (6/5, 4/5, 1).

Supplied model (nothing here is an axiom of the framework): four-site Bloch matrix H(f) = i M(f), M[a,b] += t z^n, M[b,a] -= t z^(-n), z_j = exp(2 pi i f_j), couplings
(Jx, Jy, Jz) = (6/5, 4/5, 1), odd amplitude 2 kappa, kappa > 0.  Zeros of det M on the torus are the middle-band touchings.  For Jx != Jy,  |d_x|^2 det M = s1^2 + s2^2 + s3^2
with |d_x|^2 >= (2Jx - 2Jy)^2 > 0, so the touchings are the common zeros of three real trigonometric polynomials s_i (kappa a parameter).  s : T^3 -> R^3 is a vector field on T^3,
so the signs of det(ds/df) at its simple zeros sum to chi(T^3) = 0 (charge conservation; sign det(ds/df) equals the chirality sign at every node tested, a FLOAT observation).

TIERS.  EXACT: sympy / Fractions / exact number-field gcds.  INTERVAL-CERTIFIED: float intervals with one-ulp outward steps after every IEEE operation, mpmath.iv (100 bit) cos/sin
tables rounded outward, exact Fraction coefficient intervals and exact Hessian-type bounds.  FLOAT: Newton searches, tracking, sweeps, the chirality triple product; no claim attached.
EVENTS (kappa-values where something happens to the nodes):
 E1  count 2 -> 6: the Jacobian of s at the two line nodes (x, 1-x, 0) vanishes exactly at kappa_c^2 = (18 sqrt(91) - 108)/1375 (shared root of the line polynomial q and F_c; exact).
     The line node index flips (+1 -> -1 at x < 1/2), emitting two off-plane nodes of the same sign as the old index (pitchfork; FLOAT scaling f3^2 ~ kappa - kappa_c).
 E2  an off-plane orbit (4 nodes) crosses the coordinate planes f2 = 0 and f1 = 0 at kappa^2 = 99/100 (complete exact elimination on the plane, exact solution); no count change.
 E3, E4, E5  coincidence planes without a symmetry reason: f1 - f2 = 1/2, f1 - f3 = 1/2, f2 - f3 = 0 at algebraic kappa^2 in quadratic fields (identified by PSLQ, exact real solution
     verified in the number field, location certified by a Krawczyk box); no count change.
CERTIFIED INTERVALS (cells of width 0.0025-0.01, Krawczyk existence/uniqueness in node cubes + hierarchical clearing of the rest of the torus): exactly 2 zeros for every kappa in I1,
exactly 6 in I2..I6; I2, I4, I5, I6 straddle E2, E3, E4, E5.
Run: python3 <this script>  (single process, about 1.5 minutes, under 600 MB; APHASE_VERBOSE=1 prints per-cell lines)."""
AUDIT_TIMEOUT_SEC = 900
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import time
import itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
VERBOSE = os.environ.get("APHASE_VERBOSE") == "1"
PASS = 0
FAIL = 0
OUT_BYTES = 0

def emit(s):
    global OUT_BYTES
    OUT_BYTES += len(s) + 1
    print(s, flush=True)

def check(ok, label, detail):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    emit("[%s] %s: %s" % ("PASS" if ok else "FAIL", label, detail))

def info(tag, s):
    emit("[%s] %s" % (tag, s))

# ============================================================================ embedded data
TERMS = [(0, 1, (-1, 0, 0), "y"), (0, 1, (0, 0, 0), "x"), (0, 3, (0, 0, -1), "z"), (1, 1, (-1, 0, 0), "odd"), (1, 3, (1, 0, -1), "odd"),
         (3, 1, (0, 0, 1), "odd"), (0, 0, (1, 0, 0), "odd"), (0, 2, (-1, 0, 0), "odd"), (2, 0, (0, 0, 0), "odd"), (2, 3, (0, -1, 0), "y"),
         (2, 3, (0, 0, 0), "x"), (2, 1, (0, 0, 0), "z"), (3, 3, (0, -1, 0), "odd"), (3, 1, (0, 1, 0), "odd"), (1, 3, (0, 0, 0), "odd"),
         (2, 2, (0, 1, 0), "odd"), (2, 0, (0, -1, 1), "odd"), (0, 2, (0, 0, -1), "odd")]
JX, JY, JZ = Fr(6, 5), Fr(4, 5), Fr(1, 1)
# certified intervals: name, kappa_start, kappa_end, cell width, expected number of zeros
INTERVALS = [("I1", Fr(1, 10), Fr(3, 25), Fr(1, 200), 2),
             ("I2", Fr(99, 100), Fr(1), Fr(1, 200), 6),
             ("I3", Fr(6, 5), Fr(61, 50), Fr(1, 100), 6),
             ("I4", Fr(103, 200), Fr(21, 40), Fr(1, 400), 6),
             ("I5", Fr(77, 200), Fr(79, 200), Fr(1, 400), 6),
             ("I6", Fr(913, 2000), Fr(933, 2000), Fr(1, 400), 6)]
# plane events: label, plane description, z-substitution kind, free-variable map f = F0 + B (a, b), seed (a, b, kappa), candidate polynomial for kappa^2 (None = exact rational given)
EVENTS = {
    "E2": dict(desc="f2 = 0", F0=(0, 0, 0), B=((1, 0), (0, 0), (0, 1)), seed=(0.663868, 0.304087, 0.9949874), poly=(100, -99), root="rational"),
    "E3": dict(desc="f1 - f2 = 1/2", F0=(-0.5, 0, 0), B=((1, 0), (1, 0), (0, 1)), seed=(0.849182, 0.757161, 0.518998), poly=(625, -302, 36), root="plus"),
    "E4": dict(desc="f1 - f3 = 1/2", F0=(0.5, 0, 0), B=((1, 0), (0, 1), (1, 0)), seed=(0.103127, 0.218810, 0.388850), poly=(825, 530, -99), root="plus"),
    "E5": dict(desc="f2 - f3 = 0", F0=(0, 0, 0), B=((1, 0), (0, 1), (0, 1)), seed=(0.632117, 0.184517, 0.461609), poly=(50403125, -11680400, 200376), root="plus"),
}

# ============================================================================ exact derivation (sympy)
def build_exact():
    kap = sp.symbols("kappa", positive=True)
    z1, z2, z3 = sp.symbols("z1 z2 z3")
    Jx, Jy, Jz = (sp.Rational(q.numerator, q.denominator) for q in (JX, JY, JZ))
    amp = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kap}
    M = sp.zeros(4, 4)
    for (a, b, n, kind) in TERMS:
        t = amp[kind]; mon = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
        M[a, b] += t * mon; M[b, a] -= t / mon
    conj = lambda e: sp.expand(e.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True).subs(sp.I, -sp.I))
    sg = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    dag = lambda Mx: Mx.T.applyfunc(conj)
    vec = lambda Mx: [sp.expand((s_ * Mx).trace() / 2) for s_ in sg]
    hx = M[:2, :2] * sp.I; hy = M[2:, 2:] * sp.I; Wm = M[:2, 2:]
    e = vec(dag(Wm) * hx * Wm)
    dxv = vec(hx); dyv = vec(hy)
    dx2 = sp.expand(sum(q * q for q in dxv))
    s = [sp.expand(dx2 * dyv[i] - e[i]) for i in range(3)]
    D = sp.expand(M.det(method="berkowitz"))
    mu = sp.symbols("mu")
    cp = sp.Poly(sp.expand((mu * sp.eye(4) - M).det(method="berkowitz")), mu)
    co = {ee[0]: sp.expand(c) for ee, c in cp.terms()}
    ah = sp.expand(M + M.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True).T) == sp.zeros(4, 4)
    return dict(kap=kap, z=(z1, z2, z3), M=M, s=s, D=D, dx2=dx2, A2=co[2], co=co, ah=ah)

def tcoeffs(expr, kap, z):
    z1, z2, z3 = z
    P = sp.Poly(sp.expand(sp.expand(expr) * z1 ** 3 * z2 ** 3 * z3 ** 3), z1, z2, z3)
    out = {}
    for (a, b, c), cf in P.terms():
        pk = sp.Poly(cf, kap)
        out[(a - 3, b - 3, c - 3)] = {m[0]: (Fr(int(sp.re(c_).p), int(sp.re(c_).q)), Fr(int(sp.im(c_).p), int(sp.im(c_).q))) for m, c_ in pk.terms()}
    return out

def half_real_form(d):
    """Hermitian Laurent family {k: {m: (re, im)}} -> c0(kappa) + sum_{k in half space} a_k cos(2 pi k.f) + b_k sin(2 pi k.f); polynomials in kappa as Fraction lists."""
    deg = max(m for v in d.values() for m in v)
    c0 = [Fr(0)] * (deg + 1); half = {}
    for k, v in d.items():
        if k == (0, 0, 0):
            for m, (re, im) in v.items():
                assert im == 0; c0[m] += re
        elif k > tuple(-q for q in k):
            a = [Fr(0)] * (deg + 1); b = [Fr(0)] * (deg + 1)
            for m, (re, im) in v.items():
                a[m] += 2 * re; b[m] += -2 * im
            half[k] = (a, b)
    return c0, half

def dpoly(p): return [m * p[m] for m in range(1, len(p))] or [Fr(0)]

class Family:
    """real trigonometric family with polynomial-in-kappa coefficients (Fractions)"""
    def __init__(self, c0, half):
        self.c0 = c0; self.ks = sorted(half.keys()); self.a = [half[k][0] for k in self.ks]; self.b = [half[k][1] for k in self.ks]
        self.K = np.array(self.ks, float)
    def coef_float(self, kappa):
        pw = lambda p: sum(float(c) * kappa ** m for m, c in enumerate(p))
        return pw(self.c0), np.array([pw(p) for p in self.a]), np.array([pw(p) for p in self.b])
    def valgrad_float(self, F, kappa):
        F = np.atleast_2d(F); c0, a, b = self.coef_float(kappa)
        ph = 2 * np.pi * F @ self.K.T
        co, si = np.cos(ph), np.sin(ph)
        v = c0 + co @ a + si @ b
        g = np.stack([(-si * a + co * b) @ (2 * np.pi * self.K[:, j]) for j in range(3)], axis=1)
        return v, g
    def dk_float(self, F, kappa):
        F = np.atleast_2d(F)
        pw = lambda p: sum(float(c) * kappa ** m for m, c in enumerate(dpoly(p)))
        a1 = np.array([pw(p) for p in self.a]); b1 = np.array([pw(p) for p in self.b])
        ph = 2 * np.pi * F @ self.K.T
        return pw(self.c0) + np.cos(ph) @ a1 + np.sin(ph) @ b1

# ============================================================================ outward-rounded interval arithmetic (float, vectorised)
INF = np.inf
def dn(x): return np.nextafter(x, -INF)
def up(x): return np.nextafter(x, INF)
def f_dn(q): return float(np.nextafter(float(q), -INF))        # float(Fraction) is correctly rounded
def f_up(q): return float(np.nextafter(float(q), INF))
def iadd(a, b): return (dn(a[0] + b[0]), up(a[1] + b[1]))
def isub(a, b): return (dn(a[0] - b[1]), up(a[1] - b[0]))
def imul(a, b):
    p0 = a[0] * b[0]; p1 = a[0] * b[1]; p2 = a[1] * b[0]; p3 = a[1] * b[1]
    lo = np.minimum(np.minimum(p0, p1), np.minimum(p2, p3)); hi = np.maximum(np.maximum(p0, p1), np.maximum(p2, p3))
    return (dn(lo), up(hi))
def imag(a): return np.maximum(np.abs(a[0]), np.abs(a[1]))
def imig(a): return np.maximum(np.maximum(a[0], -a[1]), 0.0)
INFL = 1 + 1e-12                    # inflation of sums of nonnegative terms (relative rounding error <= 10 u << 1e-12)

def pi_bounds():
    iv = mp.iv; old = iv.prec; iv.prec = 120
    p = iv.pi; lo = float(p.a); hi = float(p.b); iv.prec = old
    return float(dn(lo)), float(up(hi))
_TP = []
def two_pi():
    if not _TP:
        lo, hi = pi_bounds(); _TP.append((2 * lo, 2 * hi))
    return _TP[0]

def fr_imul(a, b):
    ps = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]); return (min(ps), max(ps))
def poly_interval(p, klo, khi):
    acc = (Fr(p[-1]), Fr(p[-1]))
    for c in reversed(p[:-1]):
        acc = fr_imul(acc, (klo, khi)); acc = (acc[0] + c, acc[1] + c)
    return acc

class AxisTables:
    """cos/sin(2 pi m a), m = 1, 2, as outward-rounded float intervals for exact float a (mpmath.iv, 100 bit)"""
    def __init__(self): self.cache = {}
    def lookup(self, vals):
        u, inv = np.unique(vals, return_inverse=True)
        miss = [v for v in u if v not in self.cache]
        if miss:
            iv = mp.iv; old = iv.prec; iv.prec = 100
            for v in miss:
                th = 2 * iv.pi * iv.mpf(float(v)); out = []
                for m in (1, 2):
                    for fn in (iv.cos, iv.sin):
                        r = fn(m * th); out.append((float(dn(float(r.a))), float(up(float(r.b)))))
                self.cache[v] = out
            iv.prec = old
        return np.array([self.cache[v] for v in u])[inv]            # (N, 4, 2)

def cmul(a, b):
    c1, s1 = a; c2, s2 = b
    return (isub(imul(c1, c2), imul(s1, s2)), iadd(imul(c1, s2), imul(s1, c2)))

def axis_phase(T, k):
    N = T.shape[0]
    if k == 0: return ((np.ones(N), np.ones(N)), (np.zeros(N), np.zeros(N)))
    base = 0 if abs(k) == 1 else 2
    c = (T[:, base, 0], T[:, base, 1]); s = (T[:, base + 1, 0], T[:, base + 1, 1])
    if k < 0: s = (-s[1], -s[0])
    return (c, s)

def phases_for(ks, C, tabs):
    T = [tabs[j].lookup(C[:, j]) for j in range(3)]
    ax = [{k: axis_phase(T[j], k) for k in range(-2, 3)} for j in range(3)]
    p12 = {}; out = {}
    for k in ks:
        key = (k[0], k[1])
        if key not in p12:
            if k[0] == 0: p12[key] = ax[1][k[1]]
            elif k[1] == 0: p12[key] = ax[0][k[0]]
            else: p12[key] = cmul(ax[0][k[0]], ax[1][k[1]])
        out[k] = p12[key] if k[2] == 0 else (cmul(p12[key], ax[2][k[2]]) if key != (0, 0) else ax[2][k[2]])
    return out

def sum_iv(lo, hi):
    n = lo.shape[0]
    sl = lo.sum(0); sh = hi.sum(0)
    el = (n * 2.3e-16) * np.abs(lo).sum(0); eh = (n * 2.3e-16) * np.abs(hi).sum(0)     # (n-1) u sum|x| bound for recursive summation
    return (dn(sl - el), up(sh + eh))

def smul(clo, chi, alo, ahi):
    p0 = clo * alo; p1 = clo * ahi; p2 = chi * alo; p3 = chi * ahi
    lo = np.minimum(np.minimum(p0, p1), np.minimum(p2, p3)); hi = np.maximum(np.maximum(p0, p1), np.maximum(p2, p3))
    return dn(lo), up(hi)

class FamTables:
    """float-interval coefficient tables of a Family over a rational kappa interval [klo, khi]"""
    def __init__(self, fam, klo, khi):
        self.fam = fam
        def ivf(p):
            lo, hi = poly_interval(p, klo, khi); return (f_dn(lo), f_up(hi))
        arr = lambda polys: np.array([ivf(p) for p in polys])
        self.c0 = ivf(fam.c0); self.c0d = ivf(dpoly(fam.c0))
        self.a = arr(fam.a); self.b = arr(fam.b)
        self.ad = arr([dpoly(p) for p in fam.a]); self.bd = arr([dpoly(p) for p in fam.b])
        tp = two_pi(); self.AG = []; self.BG = []
        for j in range(3):
            kj = fam.K[:, j]
            f = (np.array([tp[0] * kk if kk >= 0 else tp[1] * kk for kk in kj]), np.array([tp[1] * kk if kk >= 0 else tp[0] * kk for kk in kj]))
            f = (dn(f[0]), up(f[1]))
            ag = imul(f, (-self.a[:, 1], -self.a[:, 0])); bg = imul(f, (self.b[:, 0], self.b[:, 1]))
            self.AG.append(np.stack(ag, 1)); self.BG.append(np.stack(bg, 1))

def _stack(ft, ph):
    ks = ft.fam.ks
    cl = np.stack([ph[k][0][0] for k in ks]); ch = np.stack([ph[k][0][1] for k in ks]); sl = np.stack([ph[k][1][0] for k in ks]); sh = np.stack([ph[k][1][1] for k in ks])
    return cl, ch, sl, sh

def eval_S(ft, ph):
    cl, ch, sl, sh = _stack(ft, ph)
    t1 = smul(ft.a[:, 0:1], ft.a[:, 1:2], cl, ch); t2 = smul(ft.b[:, 0:1], ft.b[:, 1:2], sl, sh)
    return iadd(sum_iv(np.concatenate([t1[0], t2[0]]), np.concatenate([t1[1], t2[1]])), ft.c0)

def eval_G(ft, ph):
    cl, ch, sl, sh = _stack(ft, ph); out = []
    for j in range(3):
        t1 = smul(ft.AG[j][:, 0:1], ft.AG[j][:, 1:2], sl, sh); t2 = smul(ft.BG[j][:, 0:1], ft.BG[j][:, 1:2], cl, ch)
        out.append(sum_iv(np.concatenate([t1[0], t2[0]]), np.concatenate([t1[1], t2[1]])))
    return out

def eval_Sk(ft, ph):
    cl, ch, sl, sh = _stack(ft, ph)
    t1 = smul(ft.ad[:, 0:1], ft.ad[:, 1:2], cl, ch); t2 = smul(ft.bd[:, 0:1], ft.bd[:, 1:2], sl, sh)
    return iadd(sum_iv(np.concatenate([t1[0], t2[0]]), np.concatenate([t1[1], t2[1]])), ft.c0d)

def crude_bounds(fam, khi):
    """upper bounds (floats) of sup |d_j d_l| (Hff) and sup |d_l d_kappa| (Hk) of the family over the torus and kappa in [0, khi]"""
    tp = two_pi()[1]
    def bnd(p, order):
        q = p
        for _ in range(order): q = dpoly(q)
        return sum(abs(c) * khi ** m for m, c in enumerate(q))
    Hff = [[Fr(0)] * 3 for _ in range(3)]; Hk = [Fr(0)] * 3
    for k, a, b in zip(fam.ks, fam.a, fam.b):
        w0 = bnd(a, 0) + bnd(b, 0); w1 = bnd(a, 1) + bnd(b, 1)
        for j in range(3):
            for l in range(3): Hff[j][l] += w0 * abs(k[j] * k[l])
            Hk[j] += w1 * abs(k[j])
    Hf = np.array([[f_up(Hff[j][l]) * tp * tp * INFL for l in range(3)] for j in range(3)]); Hkk = np.array([f_up(Hk[j]) * tp * INFL for j in range(3)])
    return Hf, Hkk

NAMES = ("s1", "s2", "s3")

def sdet_sign(Y):
    m = [[Fr(float(Y[i][j])) for j in range(3)] for i in range(3)]
    d = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    return (d > 0) - (d < 0)

def lincomb_iv(y, ivs):
    acc = None
    for m in range(3):
        t = imul((np.asarray(float(y[m])), np.asarray(float(y[m]))), ivs[m])
        acc = t if acc is None else iadd(acc, t)
    return acc

class Cell:
    """kappa-cell [klo, khi] (Fractions): mean-value forms about the cell midpoint km, natural kappa-intervals for the first derivatives, crude second-derivative bounds"""
    def __init__(self, fams, klo, khi, tabs):
        self.fams = fams; self.klo = klo; self.khi = khi
        self.km = (klo + khi) / 2; self.dK = f_up((khi - klo) / 2)
        self.ks = sorted(set(k for n in NAMES for k in fams[n].ks)); self.tabs = tabs
        self.ftp = {n: FamTables(fams[n], self.km, self.km) for n in NAMES}
        self.ftk = {n: FamTables(fams[n], klo, khi) for n in NAMES}
        bnd = {n: crude_bounds(fams[n], khi) for n in NAMES}
        self.Hff = np.stack([bnd[n][0] for n in NAMES]); self.Hk = np.stack([bnd[n][1] for n in NAMES])
    def eval_point(self, C):
        ph = phases_for(self.ks, C, self.tabs)
        return [eval_S(self.ftp[n], ph) for n in NAMES], ph
    def eval_K(self, C, ph):
        return [eval_G(self.ftk[n], ph) for n in NAMES], [eval_Sk(self.ftk[n], ph) for n in NAMES]
    def krawczyk(self, c, rho, Y, mf=16, mk=16):
        """parametric Krawczyk test on the cube c +- rho for every kappa in the cell: T(f) = f - Y s(f, kappa) maps the cube into its interior and contracts (row sums of |I - Y J| < 1)"""
        c = np.asarray(c, float)
        g = (2 * np.arange(mf) + 1 - mf) / mf
        B = c + np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T * rho
        rs = rho / mf
        ph = phases_for(self.ks, B, self.tabs)
        JXlo = np.full((3, 3), np.inf); JXhi = np.full((3, 3), -np.inf); Sklo = np.full(3, np.inf); Skhi = np.full(3, -np.inf)
        for q in range(mk):
            qlo = self.klo + (self.khi - self.klo) * Fr(q, mk); qhi = self.klo + (self.khi - self.klo) * Fr(q + 1, mk)
            for i, n in enumerate(NAMES):
                ft = FamTables(self.fams[n], qlo, qhi)
                G = eval_G(ft, ph); Sk = eval_Sk(ft, ph)
                for j in range(3):
                    JXlo[i, j] = min(JXlo[i, j], G[j][0].min()); JXhi[i, j] = max(JXhi[i, j], G[j][1].max())
                Sklo[i] = min(Sklo[i], Sk[0].min()); Skhi[i] = max(Skhi[i], Sk[1].max())
        addJ = up(self.Hff.sum(2) * rs * INFL); addK = up(self.Hk.sum(1) * rs * INFL)
        JX = (dn(JXlo - addJ), up(JXhi + addJ)); SkX = (dn(Sklo - addK), up(Skhi + addK))
        S0, _ = self.eval_point(c[None, :])
        S0 = [(np.array(a[0][0]), np.array(a[1][0])) for a in S0]
        Emag = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                acc = (np.array(1.0 if i == j else 0.0), np.array(1.0 if i == j else 0.0))
                for m in range(3):
                    acc = isub(acc, imul((np.array(float(Y[i, m])), np.array(float(Y[i, m]))), (JX[0][m, j], JX[1][m, j])))
                Emag[i, j] = max(abs(acc[0]), abs(acc[1]))
        YS0 = [lincomb_iv(Y[i], S0) for i in range(3)]
        YSk = [lincomb_iv(Y[i], [(np.array(SkX[0][m]), np.array(SkX[1][m])) for m in range(3)]) for i in range(3)]
        img = np.array([(imag(YS0[i]) + imag(YSk[i]) * self.dK + Emag[i].sum() * rho) * INFL for i in range(3)])
        rows = Emag.sum(1) * INFL
        return dict(ok=bool((img < rho).all() and (rows < 1).all()), img=float((img / rho).max()), rows=float(rows.max()), det=sdet_sign(Y))

def periodic_inside(C, r, lo, hi):
    ok = np.ones(len(C), bool)
    for j in range(3):
        a = C[:, j] - r; b = C[:, j] + r; axis_ok = np.zeros(len(C), bool)
        for sh in (-1.0, 0.0, 1.0): axis_ok |= (lo[j] <= a + sh) & (b + sh <= hi[j])
        ok &= axis_ok
    return ok

def periodic_dist(C, c):
    d = C - c; d = d - np.round(d)
    return np.abs(d).max(1)

def clear_cell(cell, cubes, Ys, maxlevel=15, cap=250000, chunk=8192, rows_radius=0.3):
    """hierarchical clearing of the torus minus the node cubes: each dyadic box is either inside a cube or some row y.s (y = unit rows, or rows of the node matrices Y) has zero outside its enclosure over box x [klo,khi]."""
    g0 = (np.arange(8) + 0.5) / 8
    C = np.array(np.meshgrid(g0, g0, g0, indexing="ij")).reshape(3, -1).T
    r = 1.0 / 16; level = 3; total = 0
    cens = [0.5 * (lo + hi) for lo, hi in cubes]
    def rowtest(y, S, G, Sk, r):
        gv = lincomb_iv(y, S)
        Gg = [lincomb_iv(y, [G[m][j] for m in range(3)]) for j in range(3)]
        Gk = lincomb_iv(y, Sk)
        absy = np.abs(y)
        Hg = [float((absy * cell.Hff[:, j, :].sum(1)).sum()) * r * INFL for j in range(3)]
        Hk = float((absy * cell.Hk.sum(1)).sum()) * r * INFL
        bound = up((sum((imag(Gg[j]) + Hg[j]) * r for j in range(3)) + (imag(Gk) + Hk) * cell.dK) * INFL)
        return imig(gv) > bound
    while len(C):
        if level > maxlevel or len(C) > cap: return dict(ok=False, level=level, remaining=len(C), total=total)
        nxt = []; total += len(C)
        for a in range(0, len(C), chunk):
            Cb = C[a:a + chunk]
            S, ph = cell.eval_point(Cb); G, Sk = cell.eval_K(Cb, ph)
            cleared = np.zeros(len(Cb), bool)
            for i in range(3):
                e = np.zeros(3); e[i] = 1.0
                cleared |= rowtest(e, S, G, Sk, r)
            for cc, Y in zip(cens, Ys):
                idx = np.where((periodic_dist(Cb, cc) < rows_radius) & ~cleared)[0]
                if len(idx):
                    Sn = [(s_[0][idx], s_[1][idx]) for s_ in S]; Gn = [[(g_[0][idx], g_[1][idx]) for g_ in G[m]] for m in range(3)]; Skn = [(s_[0][idx], s_[1][idx]) for s_ in Sk]
                    for i in range(3): cleared[idx] |= rowtest(Y[i], Sn, Gn, Skn, r)
            keep = Cb[~cleared]
            if len(keep):
                ins = np.zeros(len(keep), bool)
                for lo, hi in cubes: ins |= periodic_inside(keep, r, lo, hi)
                keep = keep[~ins]
            if len(keep): nxt.append(keep)
        if not nxt: break
        keep = np.concatenate(nxt); r2 = r / 2
        off = np.array([[a_, b_, c_] for a_ in (-1, 1) for b_ in (-1, 1) for c_ in (-1, 1)]) * r2
        C = (keep[:, None, :] + off[None, :, :]).reshape(-1, 3); r = r2; level += 1
    return dict(ok=True, level=level, total=total)

# ============================================================================ float helpers
def make_float_tools(fams):
    def Sf(F, kappa): return np.stack([fams[n].valgrad_float(F, kappa)[0] for n in NAMES], axis=1)
    def Jf(F, kappa): return np.stack([fams[n].valgrad_float(F, kappa)[1] for n in NAMES], axis=1)
    def newton1(c, kappa, it=60):
        c = np.array(c, float)
        for _ in range(it):
            try: step = np.linalg.solve(Jf(c[None], kappa)[0], Sf(c[None], kappa)[0])
            except np.linalg.LinAlgError: return None
            c = c - step
            if np.linalg.norm(step) < 1e-15: break
        return c if np.linalg.norm(Sf(c[None], kappa)[0]) < 1e-9 else None
    def all_nodes(kappa, n=12, it=50):
        g = (np.arange(n) + 0.5) / n
        F = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T.copy()
        for _ in range(it):
            v = Sf(F, kappa); Jm = Jf(F, kappa)
            try: step = np.linalg.solve(Jm, v[:, :, None])[:, :, 0]
            except np.linalg.LinAlgError: step = np.einsum("nij,nj->ni", np.linalg.pinv(Jm), v)
            nr = np.linalg.norm(step, axis=1, keepdims=True)
            step = np.where(nr > 0.1, step * 0.1 / np.maximum(nr, 1e-300), step)
            F = F - step; F = np.where(np.isfinite(F), F, 0.5)
        keep = np.linalg.norm(Sf(F, kappa), axis=1) < 1e-10
        out = []
        for p in F[keep] - np.floor(F[keep]):
            for q in out:
                d = p - q; d -= np.round(d)
                if np.linalg.norm(d) < 1e-6: break
            else: out.append(p)
        pts = []
        for p in out:
            r_ = newton1(p, kappa)
            if r_ is not None: pts.append(r_ - np.floor(r_))
        return sorted(pts, key=lambda t: tuple(np.round(t, 6)))
    return Sf, Jf, newton1, all_nodes

def chirality(f, kappa):
    """FLOAT: Im Tr(P d1H P d2H P d3H), P the projector on the two middle eigenvectors of H = iM (net chirality sign of the node)"""
    amp = {"x": 2 * float(JX), "y": 2 * float(JY), "z": 2 * float(JZ), "odd": 2 * kappa}
    f = np.asarray(f, float)
    M = np.zeros((4, 4), complex); dM = [np.zeros((4, 4), complex) for _ in range(3)]
    for (a, b, n, kind) in TERMS:
        t = amp[kind]; ph = np.exp(2j * np.pi * (np.array(n, float) @ f))
        M[a, b] += t * ph; M[b, a] -= t * np.conj(ph)
        for l in range(3):
            dM[l][a, b] += t * ph * 2j * np.pi * n[l]; dM[l][b, a] -= t * np.conj(ph) * (-2j * np.pi * n[l])
    H0 = 1j * M; dH = [1j * d for d in dM]
    w, V = np.linalg.eigh(H0)
    P = V[:, 1:3] @ V[:, 1:3].conj().T
    return float(np.imag(np.trace(P @ dH[0] @ P @ dH[1] @ P @ dH[2]))), w

# ============================================================================ checks A: exact structure
def check_A(ex):
    kap = ex["kap"]; z1, z2, z3 = ex["z"]
    co = ex["co"]
    ok = ex["ah"] and co.get(3, 0) == 0 and co.get(1, 0) == 0 and co[4] == 1
    sos = sp.expand(ex["dx2"] * ex["D"] - sum(q ** 2 for q in ex["s"])) == 0
    a = 2 * sp.Rational(JX.numerator, JX.denominator); b = 2 * sp.Rational(JY.numerator, JY.denominator); k = 2 * kap
    c1 = (z1 + 1 / z1) / 2; s1sq = -(z1 - 1 / z1) ** 2 / 4
    dx2f = (a - b) ** 2 + 2 * a * b * (1 + c1) + 4 * k ** 2 * s1sq
    dx2_ok = sp.expand(ex["dx2"] - dx2f) == 0
    D = ex["D"]
    sym = sp.expand(D - D.subs({z1: z2, z2: z1}, simultaneous=True)) == 0 and sp.expand(D - D.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True)) == 0
    check(ok and sos and dx2_ok and sym, "A structure",
          "M anti-Hermitian; char poly mu^4+a2 mu^2+D (no mu^3, mu^1; kappa symbolic); |d_x|^2 det M = s1^2+s2^2+s3^2; |d_x|^2 >= 16/25 > 0, so zeros of det M = zeros of s; det M symmetric under f1<->f2 and f->-f")

# ============================================================================ checks B: event E1 (exact)
def check_E1(ex):
    kap = ex["kap"]; z1, z2, z3 = ex["z"]
    zz, u, c = sp.symbols("zz u c")
    Jx, Jy, Jz = (sp.Rational(q.numerator, q.denominator) for q in (JX, JY, JZ))
    P = Jx * Jy; S = Jx ** 2 + Jy ** 2 - Jz ** 2
    sub = {z1: zz, z2: 1 / zz, z3: sp.Integer(1)}
    cz = (zz + 1 / zz) / 2
    qz = 4 * kap ** 2 * cz ** 2 - 2 * P * cz - (4 * kap ** 2 + S)
    ok1 = sp.expand(ex["D"].subs(sub, simultaneous=True) - 16 * qz ** 2) == 0
    Fc = lambda cc, shift=0: P * (Jx + Jy + Jz) * cc ** 2 + (Jx + Jy) * (Jx ** 2 + Jy ** 2 + Jz * (Jx + Jy)) * cc + (Jx + Jz) * (Jy + Jz) * (Jx + Jy - Jz) + shift
    Dj = lambda e, zv: sp.expand(sp.I * zv * sp.diff(e, zv))
    Jm = sp.Matrix(3, 3, lambda i, j: Dj(ex["s"][i], (z1, z2, z3)[j]))
    W = sp.together(Jm.subs(sub, simultaneous=True).applyfunc(sp.expand).det(method="berkowitz"))
    sinth = (zz - 1 / zz) / (2 * sp.I)
    qprime = 8 * kap ** 2 * cz - 2 * P
    qzz = sp.Poly(sp.expand(zz ** 2 * qz), zz)
    def remainder(shift):
        R = sp.together(W + 1024 * kap * sinth * qprime * Fc(cz, shift))
        return sp.rem(sp.Poly(sp.expand(sp.numer(R)), zz), qzz)
    ok2 = remainder(0).is_zero and qzz.degree() == 4
    ctl = not remainder(1).is_zero                              # negative control: F_c + 1 must fail
    qc = 4 * u * c ** 2 - 2 * P * c - (4 * u + S)
    res = sp.resultant(sp.Poly(qc, c), sp.Poly(Fc(c), c))
    R2 = 34375 * u ** 2 + 5400 * u - 324
    ratio = sp.simplify(res / R2)
    up_ = (18 * sp.sqrt(91) - 108) / 1375; um_ = (-18 * sp.sqrt(91) - 108) / 1375
    cF = (-17 + sp.sqrt(91)) / 12
    ok3 = ratio.is_number and ratio != 0 and len(sp.factor_list(R2)[1]) == 1 and sp.Poly(R2, u).discriminant() > 0 and not sp.sqrt(sp.Poly(R2, u).discriminant()).is_rational
    ok4 = sp.simplify(R2.subs(u, up_)) == 0 and sp.simplify(R2.subs(u, um_)) == 0 and sp.simplify(Fc(cF)) == 0 and sp.simplify(qc.subs({u: up_, c: cF})) == 0 and um_ < 0 < up_ and -1 < sp.N(cF) < 1
    check(ok1 and ok2 and ctl and ok3 and ok4, "B E1 exact",
          "det M|line = 16 q^2; det(ds/df)|line = -8192 pi^3 kappa sin(th) q'(c) F_c(c) mod q (control F_c+1 fails); Res_c(q,F_c) ~ 34375u^2+5400u-324 irreducible; kappa_c^2 = (18 sqrt91-108)/1375 = %s" % sp.N(up_, 10))
    sgn = []
    for uv in (sp.Rational(1, 100), sp.Rational(1, 4)):
        cmv = (2 * P - sp.sqrt(4 * P ** 2 + 16 * uv * (4 * uv + S))) / (8 * uv)
        sgn.append(int(sp.sign(sp.N(Fc(cmv), 30))))
    check(sgn == [1, -1] and sp.Rational(1, 100) < up_ < sp.Rational(1, 4), "B E1 sign", "x<1/2 line-node index = sign F_c(c_-): %+d at kappa^2=1/100, %+d at 1/4 (x>1/2 node opposite): flips once, at kappa_c = %s" % (sgn[0], sgn[1], sp.N(sp.sqrt(up_), 10)))
    return float(sp.sqrt(up_))

# ============================================================================ checks C: plane events (exact elimination / exact number-field solutions / Krawczyk boxes)
from mpmath.libmp import to_rational

def Zt(t): return (1 + sp.I * t) / (1 - sp.I * t)

def real_plane_polys(ex, subs, gens, u):
    """numerators of s_i on the plane described by `subs` (tan-half-angle parametrisation z = (1+it)/(1-it)): real polynomials in gens and u = kappa^2 (an overall kappa is stripped)."""
    kap = ex["kap"]; out = []
    for si in ex["s"]:
        e = sp.together(sp.expand(si).subs(subs, simultaneous=True))
        num, den = sp.fraction(e); num = sp.expand(num)
        P = sp.Poly(num, *gens, kap)
        d = {}
        for m, c in P.terms():
            assert sp.im(c) == 0
            d[m] = sp.Rational(sp.re(c))
        c0, fl = sp.factor_list(sp.factor(sp.Poly.from_dict(d, *gens, kap).as_expr()))
        keep = sp.Mul(*[f ** m for f, m in fl if f != kap])
        e2 = sp.expand(c0 * keep)
        assert not e2.has(kap) or all(p % 2 == 0 for (*_, p) in sp.Poly(e2, *gens, kap).monoms()), "odd kappa power"
        out.append(sp.expand(e2.subs(kap ** 2, u)) if e2.has(kap) else e2)
    return out

def plane_subs(ev_name, z, x, y):
    z1, z2, z3 = z
    return {"E2": {z1: Zt(x), z2: sp.Integer(1), z3: Zt(y)}, "E3": {z1: -Zt(x), z2: Zt(x), z3: Zt(y)},
            "E4": {z1: -Zt(x), z2: Zt(y), z3: Zt(x)}, "E5": {z1: Zt(y), z2: Zt(x), z3: Zt(x)}}[ev_name]

def check_E2_exact(ex):
    """complete exact elimination on the plane f2 = 0: the real torus zeros of s there"""
    kap = ex["kap"]; x, y = sp.symbols("x y", real=True); u = sp.symbols("u")
    z1, z2, z3 = ex["z"]
    p1, p2, p3 = real_plane_polys(ex, plane_subs("E2", ex["z"], x, y), (x, y), u)
    # branch x != 0 (p3 = 32 x (4 u x^2 - 3 x^2 - 3)): u = 3 (1 + x^2) / (4 x^2)
    usub = sp.solve(sp.cancel(p3 / (32 * x)), u)[0]
    q1 = sp.numer(sp.together(sp.factor(p1.subs(u, usub)))); q2 = sp.numer(sp.together(sp.factor(p2.subs(u, usub))))
    Rr = sp.factor(sp.resultant(sp.Poly(q1, y), sp.Poly(q2, y)))
    xs = sp.Poly(Rr, x).real_roots()
    sol = []
    for x0 in set(xs):
        x0 = sp.simplify(x0)
        for y0 in sp.solve(sp.expand(q1.subs(x, x0)), y):
            y0 = sp.simplify(y0)
            if y0.is_real and sp.simplify(q2.subs({x: x0, y: y0})) == 0:
                uv = sp.simplify(usub.subs(x, x0))
                if all(sp.simplify(p.subs({x: x0, y: y0, u: uv})) == 0 for p in (p1, p2, p3)): sol.append((x0, y0, uv))
    # branch x = 0, and the cases z1 = -1, z3 = -1 (t = infinity)
    b0 = sp.Poly(p1.subs(x, 0), y).as_expr(), sp.Poly(p2.subs(x, 0), y).as_expr()
    ok_x0 = sp.simplify(b0[0].subs(y, 0)) == 0 and sp.simplify(b0[1].subs(y, 0)) != 0 and sp.factor(b0[0]) == -160 * y
    PB = real_plane_polys(ex, {z1: sp.Integer(-1), z2: sp.Integer(1), z3: Zt(y)}, (y,), u)
    PC = real_plane_polys(ex, {z1: Zt(x), z2: sp.Integer(1), z3: sp.Integer(-1)}, (x,), u)
    PD = [sp.expand(si.subs({z1: -1, z2: 1, z3: -1})) for si in ex["s"]]
    # B: y(4u+1) = 0 -> y = 0 (u > 0) and then second polynomial nonzero; C: second polynomial has all terms positive; D: second component nonzero
    okB = sp.factor(PB[0]) == -32 * y * (4 * u + 1) and sp.simplify(PB[1].subs(y, 0)) == -16 * (-20 * u - 1)
    okC = all(c > 0 for c in sp.Poly(PC[1] / -16, x, u).coeffs())
    okD = sp.simplify(PD[1]) != 0 and sp.simplify(PD[1] / (-16 * (20 * ex["kap"] ** 2 + 9) / 25)) == 1
    rat = all(s[2] == sp.Rational(99, 100) for s in sol) and len(sol) == 2
    # direct exact verification of the torus point: z1 = (-17 + 20 sqrt2 i)/33, z2 = 1, z3 = (-1 - 2 sqrt2 i)/3, kappa = 3 sqrt11/10
    s2, s11 = sp.sqrt(2), sp.sqrt(11)
    Z1 = (-17 + 20 * s2 * sp.I) / 33; Z3 = (-1 - 2 * s2 * sp.I) / 3
    # Laurent terms: replace inverses by exact conjugates (unit circle)
    def ev(e):
        e = sp.expand(e)
        tot = 0
        for term in sp.Add.make_args(e):
            tot += term.subs({z1: Z1, z3: Z3, ex["kap"]: 3 * s11 / 10, z2: 1}, simultaneous=True)
        return sp.simplify(sp.expand(tot))
    direct = all(ev(si) == 0 for si in ex["s"])
    check(len(sol) == 2 and rat and ok_x0 and okB and okC and okD and direct, "C E2 exact",
          "on f2=0 (cases t1=0, z1=-1, z3=-1 treated) s has exactly 2 real zeros, both at kappa^2 = 99/100 (cos 2pi f1 = -17/33, cos 2pi f3 = -1/3); exact substitution gives s=0; f1=0 by symmetry")
    return sp.Rational(99, 100)

def iv_coef(p, kv):
    iv = mp.iv; acc = iv.mpf(0)
    for c in reversed(p): acc = acc * kv + iv.mpf(c.numerator) / iv.mpf(c.denominator)
    return acc

def iv_family(fam, f, kv):
    iv = mp.iv; TP = 2 * iv.pi
    v = iv_coef(fam.c0, kv); dk = iv_coef(dpoly(fam.c0), kv); g = [iv.mpf(0), iv.mpf(0), iv.mpf(0)]
    for k, a, b in zip(fam.ks, fam.a, fam.b):
        phi = TP * (k[0] * f[0] + k[1] * f[1] + k[2] * f[2])
        co, si = iv.cos(phi), iv.sin(phi)
        A = iv_coef(a, kv); Bc = iv_coef(b, kv)
        v = v + A * co + Bc * si
        dk = dk + iv_coef(dpoly(a), kv) * co + iv_coef(dpoly(b), kv) * si
        for j in range(3):
            if k[j]: g[j] = g[j] + TP * k[j] * (Bc * co - A * si)
    return v, g, dk

def plane_system(fams, ev, w):
    iv = mp.iv; B = ev["B"]; F0 = ev["F0"]
    f = [iv.mpf(F0[j]) + B[j][0] * w[0] + B[j][1] * w[1] for j in range(3)]
    vals = []; J = []
    for n in NAMES:
        v, g, dk = iv_family(fams[n], f, w[2])
        vals.append(v); J.append([sum(B[j][c] * g[j] for j in range(3)) for c in range(2)] + [dk])
    return vals, J

def mid(x): return 0.5 * (float(x.a) + float(x.b))

def plane_box(fams, ev, rho=1e-9):
    """Krawczyk existence and uniqueness of a zero (a, b, kappa) of the plane system s(F0 + B (a,b); kappa) = 0 in a box of radius rho (mpmath.iv, 100 bit)"""
    iv = mp.iv; old = iv.prec; iv.prec = 100
    w = np.array(ev["seed"], float)
    for _ in range(14):
        vals, J = plane_system(fams, ev, [iv.mpf(float(t)) for t in w])
        Jm = np.array([[mid(J[i][j]) for j in range(3)] for i in range(3)]); vm = np.array([mid(vals[i]) for i in range(3)])
        w = w - np.linalg.solve(Jm, vm)
    W = [iv.mpf(float(t)) for t in w]
    vals0, J0 = plane_system(fams, ev, W)
    Y = np.linalg.inv(np.array([[mid(J0[i][j]) for j in range(3)] for i in range(3)]))
    X = [iv.mpf([float(w[i]) - rho, float(w[i]) + rho]) for i in range(3)]
    JX = plane_system(fams, ev, X)[1]
    dX = [X[j] - W[j] for j in range(3)]
    ok = True; Kx = []
    for i in range(3):
        t = W[i]
        for m in range(3): t = t - iv.mpf(float(Y[i, m])) * vals0[m]
        for j in range(3):
            e = iv.mpf(1 if i == j else 0)
            for m in range(3): e = e - iv.mpf(float(Y[i, m])) * JX[m][j]
            t = t + e * dX[j]
        Kx.append(t); ok &= bool(t.a > X[i].a and t.b < X[i].b)
    kl = Fr(*to_rational(X[2]._mpi_[0])); kh = Fr(*to_rational(X[2]._mpi_[1]))
    iv.prec = old
    return ok, kl, kh, w

def number_field_solution(ex, evn, poly, root):
    """exact setup for the plane system at kappa^2 = u0 (root of a u^2 + b u + c = 0, a number in K = Q(sqrt m)): Q = the three real tan-half-angle polynomials (gens y, x) with u = u0, G = gcd over K of the pairwise
    y-resultants, facs = factors of G other than x^2 + 1.  Returns (Q, G, facs, u0, K, sqrt m); exact_solution_at completes the existence proof."""
    x, y = sp.symbols("x y", real=True); u = sp.symbols("u")
    Ps = real_plane_polys(ex, plane_subs(evn, ex["z"], x, y), (x, y), u)
    A, B_, C_ = (sp.Integer(t) for t in poly)
    disc = B_ ** 2 - 4 * A * C_
    r = sp.sqrt(disc); sq = sp.simplify(r)
    m = sp.Integer(1)
    for f_, e_ in sp.factorint(int(disc)).items():
        if e_ % 2: m *= f_
    rt = sp.sqrt(m)
    u0 = (-B_ + (1 if root == "plus" else -1) * sq) / (2 * A)
    K = sp.QQ.algebraic_field(rt)
    Q = []
    for p in Ps:
        pu = sp.Poly(p, u)
        a_ = sp.Poly(pu.coeff_monomial(u), y, x, domain=K); b_ = sp.Poly(pu.coeff_monomial(1), y, x, domain=K)
        Q.append(a_.mul_ground(K.from_sympy(u0)).add(b_))
    R12 = Q[0].resultant(Q[1]); R13 = Q[0].resultant(Q[2])
    G = sp.gcd(R12, R13)
    facs = [(f, mult) for f, mult in G.factor_list()[1] if f.degree() >= 1 and f.as_expr() != x ** 2 + 1]
    return Q, G, facs, u0, K, rt

def poly_coeffs_in_x(Qi, x, K, deg_y=2):
    """coefficient polynomials (in x, domain K) of y^e, e = 0..deg_y, of a Poly in gens (y, x)"""
    dct = {e: {} for e in range(deg_y + 1)}
    for (ey, ex_), cf in Qi.as_dict().items(): dct[ey][(ex_,)] = cf
    return [sp.Poly.from_dict(dct[e], x, domain=K) if dct[e] else sp.Poly(0, x, domain=K) for e in range(deg_y + 1)]

def exact_solution_at(ex, evn, poly, root):
    """exact real torus solutions of the plane system at kappa^2 = u0 (u0 the stated root of poly), in the number field K = Q(sqrt m).  The pairwise resultants in y of the three plane polynomials (Q_i, gens (y, x)) have a gcd G(x)
    over K; for each factor h(x) of G other than x^2 + 1 the common y0 is produced exactly: either (degree <= 2 in y) y0 = -L0/L1 with all remainders modulo h zero, or (h = x^2 - r) as the gcd in y over L = K(sqrt r) of the three
    polynomials Q_i(x0, y).  Returns dict(ok, u0, pts = [(x0, y0) numeric], h)."""
    x, y = sp.symbols("x y", real=True)
    Q, G, facs, u0, K, rt = number_field_solution(ex, evn, poly, root)
    pts = []; okall = len(facs) > 0; hs = []
    mp.mp.dps = 40
    for h, mult in facs:
        hs.append(h.as_expr())
        if all(Qi.degree(0) <= 2 for Qi in Q):
            a = poly_coeffs_in_x(Q[0], x, K); b = poly_coeffs_in_x(Q[1], x, K); c = poly_coeffs_in_x(Q[2], x, K)
            L1 = b[2] * a[1] - a[2] * b[1]; L0 = b[2] * a[0] - a[2] * b[0]
            Fi = lambda t: t[2] * L0 ** 2 - t[1] * L0 * L1 + t[0] * L1 ** 2
            okall &= bool(all(Fi(t).rem(h).is_zero for t in (a, b, c)) and sp.gcd(L1, h).degree() == 0)
            hco = [sp.N(cc, 45) for cc in sp.Poly(h.as_expr(), x).all_coeffs()]
            L0f = sp.lambdify(x, L0.as_expr(), "mpmath"); L1f = sp.lambdify(x, L1.as_expr(), "mpmath")
            for r_ in mp.polyroots([mp.mpf(str(sp.re(cc))) + 1j * mp.mpf(str(sp.im(cc))) for cc in hco], maxsteps=300, extraprec=300):
                if abs(mp.im(r_)) < mp.mpf(10) ** -25:
                    x0 = mp.re(r_); pts.append((x0, -L0f(x0) / L1f(x0)))
        else:
            hx = sp.Poly(h.as_expr(), x)
            cs = hx.all_coeffs()
            if hx.degree() != 2 or sp.simplify(cs[1]) != 0:
                okall = False; continue
            rexpr = sp.simplify(-cs[2] / cs[0])
            if not sp.N(rexpr) > 0: okall = False; continue
            for sgn in (1, -1):
                x0e = sgn * sp.sqrt(rexpr)
                L = sp.QQ.algebraic_field(rt, sp.sqrt(rexpr))
                Qy = []
                for Qi in Q:
                    d_ = {}
                    for (ey, ex_), cf in Qi.as_dict().items():
                        v = L.from_sympy(cf) * L.from_sympy(x0e) ** ex_
                        d_[(ey,)] = d_.get((ey,), L.zero) + v
                    Qy.append(sp.Poly.from_dict(d_, y, domain=L))
                g_ = sp.gcd(sp.gcd(Qy[0], Qy[1]), Qy[2])
                if g_.degree() < 1: okall = False; continue
                for yr in sp.Poly(g_.as_expr(), y).nroots(n=30):
                    if abs(sp.im(yr)) < 1e-20: pts.append((mp.mpf(str(sp.N(x0e, 40))), mp.mpf(str(sp.re(yr)))))
    return dict(ok=okall and len(pts) > 0, u0=u0, pts=pts, h=hs)

def torus_ab(evn, x0, y0):
    """(a, b) coordinates (mod 1) of the plane solution from the tangent half-angles"""
    f = lambda t: float((mp.atan(t) / mp.pi) % 1)
    return {"E2": (f(x0), f(y0)), "E3": (f(x0), f(y0)), "E4": (f(x0), f(y0)), "E5": (f(y0), f(x0))}[evn]

def circ_close(p, q, tol):
    d = (p - q) % 1.0
    return min(d, 1 - d) < tol

def check_plane_events(ex, fams):
    out = {}
    rho = 1e-9
    for evn in ("E2", "E3", "E4", "E5"):
        ev = EVENTS[evn]
        t1 = time.time()
        okb, kl, kh, w = plane_box(fams, ev, rho)
        u_lo, u_hi = kl * kl, kh * kh
        if evn == "E2":
            u0 = sp.Rational(99, 100); pts_ab = None
            ex_ok = True
        else:
            r = exact_solution_at(ex, evn, ev["poly"], ev["root"])
            u0 = r["u0"]; ex_ok = r["ok"]
            pts_ab = [torus_ab(evn, x0, y0) for (x0, y0) in r["pts"]]
        inbox = (sp.Rational(u_lo.numerator, u_lo.denominator) < u0 < sp.Rational(u_hi.numerator, u_hi.denominator))
        # coordinates of an exact solution inside the box (E3-E5; E2 coordinates from the exact solution list are in check_E2_exact)
        if pts_ab is None:
            a_ex = float(mp.acos(mp.mpf(-17) / 33) / (2 * mp.pi)); a_ex = 1 - a_ex            # f1 = 0.66387 (inverse image of the node f1 = 0.33613)
            b_ex = float(mp.acos(mp.mpf(-1) / 3) / (2 * mp.pi))                                # f3 = 0.30409
            near = circ_close(a_ex, w[0], 1e-8) and circ_close(b_ex, w[1], 1e-8)
        else:
            near = any(circ_close(a, w[0], 1e-8) and circ_close(b, w[1], 1e-8) for (a, b) in pts_ab)
        out[evn] = dict(kappa=float(np.sqrt(float(u0))), box=(float(kl), float(kh)), w=w)
        check(okb and inbox and ex_ok and near, "C %s" % evn,
              "plane %s: Krawczyk box +-1e-9 at kappa = %.9f has a unique zero; exact kappa^2 = %s = %.10f inside [%.10f, %.10f]; exact real solution there (%s) lies in the box"
              % (ev["desc"], w[2], "99/100" if evn == "E2" else str(sp.nsimplify(u0)), float(u0), float(u_lo), float(u_hi), "exact elimination" if evn == "E2" else "number field"))
    return out

# ============================================================================ checks D: certified intervals
def a2_family(ex):
    d = tcoeffs(ex["A2"], ex["kap"], ex["z"]); c0, half = half_real_form(d)
    return Family(c0, half)

def a2_lower(cell, a2fam, c, rho):
    ft = FamTables(a2fam, cell.klo, cell.khi)
    ph = phases_for(a2fam.ks, c[None, :], cell.tabs)
    lo = float(eval_S(ft, ph)[0][0])
    tp = two_pi()[1]
    def bnd(p): return sum(abs(cc) * cell.khi ** m for m, cc in enumerate(p))
    L = sum(float(f_up((bnd(a) + bnd(b)) * abs(k[j]))) for k, a, b in zip(a2fam.ks, a2fam.a, a2fam.b) for j in range(3)) * tp * INFL
    return float(dn(lo - L * rho * INFL))

def run_interval(name, ka, kb, w, nexp, fams, tools, tabs, a2fam, negctl=False):
    Sf, Jf, newton1, all_nodes = tools
    k = ka; prev = []; nodes = all_nodes(float(ka + w / 2))
    n_float = len(nodes)
    res = dict(name=name, ok=True, cells=0, boxes=0, ps=[], dets=[], a2=np.inf, nfloat=n_float, chir=[0, 0], first=None, reason="")
    t0 = time.time()
    while k < kb:
        cell = Cell(fams, k, k + w, tabs); km = float(cell.km)
        cubes = []; Ys = []; dets = []; pos = []; ps = []
        for n0 in nodes:
            n = newton1(n0, km)
            if n is None: res.update(ok=False, reason="Newton"); return res
            Y = np.linalg.inv(Jf(n[None], km)[0])
            hint = None
            for (pn, pp) in prev:
                d = np.abs((n - pn) - np.round(n - pn)).max()
                if d < 0.05: hint = pp
            order = ([hint, hint - 1, hint + 1] if hint else []) + list(range(6, 15))
            found = None; seen = set()
            for p in order:
                if p in seen or p < 4 or p > 16: continue
                seen.add(p)
                rho = 2.0 ** -p; cs = np.round(n * 2 ** (p + 4)) / 2 ** (p + 4)
                r = cell.krawczyk(cs, rho, Y)
                if r["ok"]: found = (p, cs, r); break
            if not found: res.update(ok=False, reason="Krawczyk at kappa=%s" % k); return res
            p, cs, r = found
            cubes.append((cs - 2.0 ** -p, cs + 2.0 ** -p)); Ys.append(Y); dets.append(r["det"]); pos.append(n); ps.append(p)
            res["a2"] = min(res["a2"], a2_lower(cell, a2fam, cs, 2.0 ** -p))
        for i in range(len(cubes)):
            for j in range(i + 1, len(cubes)):
                ci = 0.5 * (cubes[i][0] + cubes[i][1]); cj = 0.5 * (cubes[j][0] + cubes[j][1])
                if not np.abs((ci - cj) - np.round(ci - cj)).max() > (cubes[i][1][0] - cubes[i][0][0]) / 2 + (cubes[j][1][0] - cubes[j][0][0]) / 2:
                    res.update(ok=False, reason="cubes overlap"); return res
        out = clear_cell(cell, cubes, Ys)
        if not out["ok"]: res.update(ok=False, reason="clearing failed at kappa=%s level %d" % (k, out["level"])); return res
        if len(cubes) != nexp or sum(dets) != 0: res.update(ok=False, reason="count %d / index sum %d at kappa=%s" % (len(cubes), sum(dets), k)); return res
        if res["first"] is None:
            res["first"] = (km, list(pos), list(dets))
            for n, dsg in zip(pos, dets):
                T, _ = chirality(n, km); res["chir"][0 if np.sign(T) == dsg else 1] += 1
            if negctl:
                ok_nc1 = not clear_cell(cell, cubes[:-1], Ys[:-1], maxlevel=12, cap=60000)["ok"]
                ok_nc2 = not cell.krawczyk(0.5 * (cubes[0][0] + cubes[0][1]), 0.5 * (cubes[0][1][0] - cubes[0][0][0]), np.eye(3))["ok"]
                res["negctl"] = (ok_nc1, ok_nc2)
        res["cells"] += 1; res["boxes"] += out["total"]; res["ps"] += ps; res["dets"] = dets
        if VERBOSE: info("CELL", "%s [%s, %s]: %d zeros, index %s, p=%s, boxes %d (t=%.0f s)" % (name, k, k + w, len(cubes), "".join("+" if d > 0 else "-" for d in dets), ps, out["total"], time.time() - T0))
        prev = list(zip(pos, ps)); nodes = pos; k = k + w
    res["time"] = time.time() - t0
    return res

# ============================================================================ checks E: FLOAT diagnostics
def float_sweep(tools):
    Sf, Jf, newton1, all_nodes = tools
    counts = {}; badq = 0; agree = 0; tot = 0
    for j in range(1, 61):
        kappa = j / 30.0
        nodes = all_nodes(kappa, n=11)
        qs = []
        for n in nodes:
            T, _ = chirality(n, kappa); qs.append(np.sign(T))
            tot += 1; agree += int(np.sign(np.linalg.det(Jf(n[None], kappa)[0])) == np.sign(T))
        if sum(qs) != 0: badq += 1
        counts.setdefault(len(nodes), []).append(j)
    return counts, badq, agree, tot

def pitchfork_float(tools, kc):
    Sf, Jf, newton1, all_nodes = tools
    nodes = all_nodes(0.30, n=11)
    off = [n for n in nodes if 1e-3 < n[2] < 0.5]
    n = min(off, key=lambda t: t[2])
    ks = []; f3 = []
    for kappa in np.concatenate([np.arange(0.30, 0.23, -0.002), np.arange(0.23, 0.2162, -0.0004)]):
        n = newton1(n, kappa)
        if n is None: return None
        if kappa < 0.226: ks.append(kappa); f3.append(n[2] if n[2] < 0.5 else n[2] - 1)
    ks = np.array(ks); y = np.array(f3) ** 2
    A = np.polyfit(ks, y, 1)
    return -A[1] / A[0], float(np.abs(np.array(f3)).min())

def mp_family(fam, f, kappa):
    TP = 2 * mp.pi
    pv = lambda p: sum(mp.mpf(c.numerator) / mp.mpf(c.denominator) * kappa ** m for m, c in enumerate(p))
    v = pv(fam.c0); dk = pv(dpoly(fam.c0)); g = [mp.mpf(0)] * 3
    for k, a, b in zip(fam.ks, fam.a, fam.b):
        phi = TP * (k[0] * f[0] + k[1] * f[1] + k[2] * f[2]); co, si = mp.cos(phi), mp.sin(phi)
        A = pv(a); Bc = pv(b)
        v += A * co + Bc * si; dk += pv(dpoly(a)) * co + pv(dpoly(b)) * si
        for j in range(3): g[j] += TP * k[j] * (Bc * co - A * si)
    return v, g, dk

def selftest_enclosures(fams, tabs):
    """every interval enclosure (value at kappa_m, gradient and kappa-derivative over [klo, khi]) must contain 40-digit mpmath values at random dyadic centres"""
    mp.mp.dps = 40
    rng = np.random.default_rng(12345)
    C = rng.integers(0, 4096, (60, 3)) / 4096.0 + 1 / 8192.0
    klo, khi = Fr(6, 5), Fr(121, 100)
    cell = Cell(fams, klo, khi, tabs)
    S, ph = cell.eval_point(C); G, Sk = cell.eval_K(C, ph)
    bad = 0; wmax = 0.0
    for t in range(len(C)):
        for i, n in enumerate(NAMES):
            v, _, _ = mp_family(fams[n], [mp.mpf(float(q)) for q in C[t]], mp.mpf(241) / 200)
            if not (mp.mpf(float(S[i][0][t])) <= v <= mp.mpf(float(S[i][1][t]))): bad += 1
            wmax = max(wmax, float(S[i][1][t] - S[i][0][t]))
            for kk in (mp.mpf(6) / 5, mp.mpf(1205) / 1000, mp.mpf(121) / 100):
                _, g, dk = mp_family(fams[n], [mp.mpf(float(q)) for q in C[t]], kk)
                for j in range(3):
                    if not (mp.mpf(float(G[i][j][0][t])) <= g[j] <= mp.mpf(float(G[i][j][1][t]))): bad += 1
                if not (mp.mpf(float(Sk[i][0][t])) <= dk <= mp.mpf(float(Sk[i][1][t]))): bad += 1
    return bad, wmax

def main():
    ex = build_exact()
    check_A(ex)
    kc = check_E1(ex)
    check_E2_exact(ex)
    fams = {}
    for n, e in zip(NAMES, ex["s"]):
        d = tcoeffs(e, ex["kap"], ex["z"]); c0, half = half_real_form(d); fams[n] = Family(c0, half)
    tabs = [AxisTables() for _ in range(3)]
    bad, wmax = selftest_enclosures(fams, tabs)
    check(bad == 0, "D0 intervals", "enclosures (value at kappa_m; grad, d/dkappa over the cell) contain 40-digit mpmath values at 60 centres: violations %d, max width %.1e" % (bad, wmax))
    evres = check_plane_events(ex, fams)
    tools = make_float_tools(fams); a2fam = a2_family(ex)
    for (name, ka, kb, w, nexp) in INTERVALS:
        r = run_interval(name, ka, kb, w, nexp, fams, tools, tabs, a2fam, negctl=(name == "I3"))
        ok = r["ok"] and r["a2"] > 0 and r["nfloat"] == nexp
        check(ok, "D %s" % name, "kappa in [%s, %s]: exactly %d zeros for every kappa (%d cells, cubes 2^-%d..2^-%d, %d boxes), simple zeros of s, index sum 0, a2 >= %.3g; FLOAT count %d, index = chirality %d/%d%s"
              % (ka, kb, nexp, r["cells"], max(r["ps"]) if r["ps"] else 0, min(r["ps"]) if r["ps"] else 0, r["boxes"], r["a2"], r["nfloat"], r["chir"][0], sum(r["chir"]), "" if r["ok"] else " FAILED: " + r["reason"]))
        if "negctl" in r: check(all(r["negctl"]), "D neg", "controls fail as they must: clearing without one node cube (%s), Krawczyk with identity preconditioner (%s)" % (r["negctl"][0], r["negctl"][1]))
    counts, badq, agree, tot = float_sweep(tools)
    desc = "; ".join("%d nodes at j/30 for j in %s" % (n, "%d..%d" % (min(js), max(js)) if len(js) == max(js) - min(js) + 1 else js) for n, js in sorted(counts.items()))
    info("FLOAT", "Newton sweep kappa = j/30, j = 1..60: %s; chirality sum != 0 at %d kappa; sign det(ds/df) = sign(chirality) for %d of %d nodes" % (desc, badq, agree, tot))
    pf = pitchfork_float(tools, kc)
    if pf: info("FLOAT", "pitchfork: off-plane node continued from kappa = 0.30 to 0.2162; f3^2 linear in kappa, extrapolated zero kappa = %.5f vs exact kappa_c = %.5f; smallest |f3| = %.4f" % (pf[0], kc, pf[1]))
    info("INFO", "runtime %.1f s (AUDIT_TIMEOUT_SEC = %d), stdout so far %d chars" % (time.time() - T0, AUDIT_TIMEOUT_SEC, OUT_BYTES))
    if VERBOSE: info("INFO", "verbose mode: stdout-size check skipped")
    else: check(OUT_BYTES < 4900, "stdout", "under 5000 characters (%d)" % OUT_BYTES)
    emit("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))

if __name__ == "__main__":
    main()
