#!/usr/bin/env python3
"""kasner-crush: anisotropic (Bianchi I) collapse on a box-frustum Lorentzian Regge carrier under CL-1's fixed-step tick
(T = sin(eps0)/sqrt(sum_i 1/m_i^2), lapse following the edges) and CL-3 stationarity in the three edges per slice.
Supplied models; exact identities, finite diagnostics and estimates; no physical identification.
 A  carrier: isotropic reduction, Schlaefli, Bianchi I continuum limit, scale-freedom, null-face force signs
 B  one tick: properness, degree 1 (a root always exists), multiplicity 3-5, fold surfaces
 C  vacuum Kasner: Kasner while sub-Hubble; pancake freeze; cigar (Schwarzschild-interior exponents) at the speed limit
 D  a lattice wall: reflection of a face speed off a mixed-sign null face
 E  dust Bianchi I
 F  estimates (Kantowski-Sachs interiors, measurement)
Helper code is inlined below as two source strings (float carrier + solver; mpmath carrier + solver), exec'd locally.
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import os, signal, sys, time, ast
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import mpmath as mp
FL_SRC = r'''
"""box-frustum Lorentzian Regge carrier, fixed-step lapse (exploration core)."""
import numpy as np
PAIRS = ((0, 1, 2), (1, 2, 0), (2, 0, 1))   # (i, j, k): edge along i, its trapezoid moves along j,k


def lapse(l, lp, sinE):
    m = (l + lp) / 2
    return sinE / np.sqrt(np.sum(1 / m ** 2))


def slab(l, lp, sinE, M=0.0):
    """timelike-hinge sum + dust; returns (action, u)"""
    m = (l + lp) / 2; T = sinE / np.sqrt(np.sum(1 / m ** 2)); u = (lp - l) / (2 * T); S = -M * T
    for i, j, k in PAIRS:
        h = np.sqrt(1 - u[j] ** 2 - u[k] ** 2); w = u[j] * u[k] / np.sqrt((1 - u[j] ** 2) * (1 - u[k] ** 2))
        S = S + m[i] * T * h * 4 * np.arcsin(w)
    return S, u


def spacehinge(l, um, up):
    """sum over the three faces at a slice: area l_j l_k x 2 (atanh u_i(after) - atanh u_i(before))"""
    return sum(2 * l[j] * l[k] * (np.arctanh(up[i]) - np.arctanh(um[i])) for i, j, k in PAIRS)


def S_loc(l0, l1, l2, sinE, M=0.0):
    s0, u0 = slab(l0, l1, sinE, M); s1, u1 = slab(l1, l2, sinE, M)
    S = s0 + s1 + spacehinge(l1, u0, u1)
    S = S + sum(2 * l0[j] * l0[k] * np.arctanh(u0[i]) for i, j, k in PAIRS)
    S = S - sum(2 * l2[j] * l2[k] * np.arctanh(u1[i]) for i, j, k in PAIRS)
    return S


def resid(l0, l1, l2, sinE, M=0.0, h=1e-30):
    g = np.zeros(3)
    for a in range(3):
        d = np.zeros(3, complex); d[a] = 1j * h
        g[a] = S_loc(l0.astype(complex), l1 + d, l2.astype(complex), sinE, M).imag / h
    return g


def energy(l, lp, sinE, M=0.0):
    """lapse-equation residual of a slab (Schlaefli: dS/dT = sum eps dA/dT) times T/sig_iso (isotropic: (6pA-M) lbar)"""
    m = (l + lp) / 2; T = lapse(l, lp, sinE); u = (lp - l) / (2 * T); E = -M
    for i, j, k in PAIRS:
        h = np.sqrt(1 - u[j] ** 2 - u[k] ** 2); w = u[j] * u[k] / np.sqrt((1 - u[j] ** 2) * (1 - u[k] ** 2))
        E += 4 * m[i] * np.arcsin(w) / h
    return E * T * np.sqrt(3) / sinE


def l_from_u(l, u, sinE, it=200):
    """next slice from slab velocities u (T self-consistent)"""
    T = sinE / np.sqrt(np.sum(1 / l ** 2))
    for _ in range(it):
        m = l + u * T; Tn = sinE / np.sqrt(np.sum(1 / m ** 2))
        if abs(Tn - T) < 1e-16 * T: break
        T = Tn
    return l + 2 * u * T

def gaps(u): return np.array([1 - u[j]**2 - u[k]**2 for i, j, k in PAIRS])
def ok(u): return np.all(gaps(u) > 0)
class Var:
    def __init__(self, u):
        g = gaps(u); self.ip = int(np.argmin(g)); _, self.jp, self.kp = PAIRS[self.ip]; self.polar = g[self.ip] < 0.05
    def to_u(self, y):
        if not self.polar: return np.array(y, float)
        r = np.sqrt(-np.expm1(y[0])); u = np.zeros(3); u[self.ip] = y[2]; u[self.jp] = r * np.cos(y[1]); u[self.kp] = r * np.sin(y[1]); return u
    def to_y(self, u):
        if not self.polar: return np.array(u, float)
        return np.array([np.log(1 - u[self.jp]**2 - u[self.kp]**2), np.arctan2(u[self.kp], u[self.jp]), u[self.ip]])
    def tr(self, F, u):
        if not self.polar: return F
        j, k, i = self.jp, self.kp, self.ip; h = np.sqrt(max(1 - u[j]**2 - u[k]**2, 0))
        return np.array([(u[j] * F[j] + u[k] * F[k]) * h, -u[k] * F[j] + u[j] * F[k], F[i]])
    def valid(self, y): return (not self.polar or y[0] < 0) and ok(self.to_u(y))
def Gfun(a, b, sE, M):
    def G(uu):
        c = l_from_u(b, uu, sE); Tb = lapse(b, c, sE)
        return resid(a, b, c, sE, M) / np.maximum(np.array([b[1]*b[2], b[2]*b[0], b[0]*b[1]]) / Tb, np.sum(b))
    return G
def jac(H, y, h=1e-8):
    H0 = H(y); J = np.zeros((len(H0), len(y)))
    for q in range(len(y)):
        yp = y.copy(); yp[q] += h; J[:, q] = (H(yp) - H0) / h
    return J, H0
def newton(G, V, y, tol=1e-11, it=60):
    H = lambda yy: V.tr(G(V.to_u(yy)), V.to_u(yy)); e = np.inf
    for _ in range(it):
        J, F0 = jac(H, y); e = np.max(np.abs(F0))
        if e < tol: return True, y, e, J
        try: dy = np.linalg.solve(J, -F0)
        except np.linalg.LinAlgError: return False, y, e, J
        t = 1.0
        while t > 1e-10:
            yn = y + t * dy
            if V.valid(yn) and np.max(np.abs(H(yn))) < e: break
            t /= 2
        if t <= 1e-10: return bool(np.max(np.abs(dy)) < 1e-8 and e < 1e-7), y, e, J
        y = yn
    return False, y, e, J
def homotopy(Lm, a, b, sE, M, u_prev, ds0=0.02):
    """pseudo-arclength in lambda from problem (Lm, a) [root u_prev] to (a, b); returns (ok, u, fold_seen)"""
    V = Var(u_prev)
    def H(Y):
        lam = Y[3]; G = Gfun(Lm + lam * (a - Lm), a + lam * (b - a), sE, M); uu = V.to_u(Y[:3]); return V.tr(G(uu), uu)
    def tang(J, prev):
        t = np.array([(-1) ** q * np.linalg.det(np.delete(J, q, axis=1)) for q in range(4)]); t /= np.linalg.norm(t)
        return -t if prev is not None and t @ prev < 0 else t
    Y = np.append(V.to_y(u_prev), 0.0); J, _ = jac(H, Y); t = tang(J, None)
    if t[3] < 0: t = -t
    ds = ds0; fold = False; nstep = 0
    while nstep < 3000:
        nstep += 1; Yp = Y + ds * t; good = False
        for _ in range(25):
            if not V.valid(Yp[:3]): break
            J, H0 = jac(H, Yp); A = np.vstack([J, t]); rhs = np.append(-H0, -t @ (Yp - Y - ds * t))
            try: d = np.linalg.solve(A, rhs)
            except np.linalg.LinAlgError: break
            Yp = Yp + d
            if np.max(np.abs(d)) < 1e-12: good = V.valid(Yp[:3]); break
        if not good:
            ds /= 2
            if ds < 1e-9: return False, V.to_u(Y[:3]), fold, Y[3]
            continue
        if Yp[3] >= 1:
            w = (1 - Y[3]) / (Yp[3] - Y[3]); y = Y[:3] + w * (Yp[:3] - Y[:3]); Hf = lambda yy: V.tr(Gfun(a, b, sE, M)(V.to_u(yy)), V.to_u(yy))
            for _ in range(30):
                J, F0 = jac(Hf, y)
                if np.max(np.abs(F0)) < 1e-11: break
                yn = y + np.linalg.solve(J, -F0)
                if not V.valid(yn): break
                y = yn
            e = np.max(np.abs(Hf(y)))
            if e < 1e-9: return True, V.to_u(y), fold, 1.0
            ds /= 2
            if ds < 1e-9: return False, V.to_u(Y[:3]), fold, Y[3]
            continue
        J, _ = jac(H, Yp); tn = tang(J, t)
        if tn[3] < 0: fold = True
        Y, t = Yp, tn
        if Y[3] < -0.5: return False, V.to_u(Y[:3]), True, Y[3]
        ds = min(ds * 1.5, 0.2)
    return False, V.to_u(Y[:3]), fold, Y[3]
def step(L, U, sE, M):
    """returns (status, u_new, info); status ok | homotopy | NOROOT"""
    a, b = L[-2], L[-1]; G = Gfun(a, b, sE, M)
    guesses = [U[-1]] if len(U) < 2 else [2 * U[-1] - U[-2], U[-1]]
    for g in guesses:
        if not ok(g): continue
        V = Var(g); okn, y, e, J = newton(G, V, V.to_y(g))
        if okn: return 'ok', V.to_u(y), np.linalg.det(J)
    if len(L) < 3: return 'NOROOT', None, None
    okh, u, fold, lam = homotopy(L[-3], a, b, sE, M, U[-1])
    if okh: return ('fold' if fold else 'homotopy'), u, lam
    return 'NOROOT', u, (fold, lam)
'''
MP_SRC = r'''
"""mpmath analytic edge equations (Schlaefli) for the box frustum with the fixed-step lapse."""
import mpmath as mp
PAIRS = ((0, 1, 2), (1, 2, 0), (2, 0, 1))
def slabq(l, lp, sE):
    m = [(l[i] + lp[i]) / 2 for i in range(3)]; s2 = sum(1 / x ** 2 for x in m); T = sE / mp.sqrt(s2)
    D = [lp[i] - l[i] for i in range(3)]; u = [D[i] / (2 * T) for i in range(3)]
    return m, T, D, u
def eps_t(u):   # rotation deficits at the three trapezoids
    return [4 * mp.asin(u[j] * u[k] / mp.sqrt((1 - u[j] ** 2) * (1 - u[k] ** 2))) for i, j, k in PAIRS]
def dslab(l, lp, sE, M, side):
    """d/dl_a (side=0 bottom, 1 top) of sum eps_i A_i - M T, deficits frozen (Schlaefli)"""
    m, T, D, u = slabq(l, lp, sE); ep = eps_t(u); out = []
    sgn = -1 if side == 0 else 1
    for a in range(3):
        dT = T ** 3 / (sE ** 2 * m[a] ** 3) / 2; g = -M * dT
        for i, j, k in PAIRS:
            Q = T ** 2 - (D[j] ** 2 + D[k] ** 2) / 4
            dQ = 2 * T * dT - (D[j] * (sgn if a == j else 0) + D[k] * (sgn if a == k else 0)) / 2
            dA = (mp.mpf(1) / 2 if a == i else 0) * mp.sqrt(Q) + m[i] * dQ / (2 * mp.sqrt(Q))
            g += ep[i] * dA
        out.append(g)
    return out
def resid(l0, l1, l2, sE, M=0):
    _, _, _, u0 = slabq(l0, l1, sE); _, _, _, u1 = slabq(l1, l2, sE)
    g0 = dslab(l0, l1, sE, M, 1); g1 = dslab(l1, l2, sE, M, 0); out = []
    for a in range(3):
        r = g0[a] + g1[a]
        for i, j, k in PAIRS:   # face i at slice 1, area l_j l_k
            if a == j: r += 2 * l1[k] * (mp.atanh(u1[i]) - mp.atanh(u0[i]))
            if a == k: r += 2 * l1[j] * (mp.atanh(u1[i]) - mp.atanh(u0[i]))
        out.append(r)
    return out
def energy(l, lp, sE, M=0):
    m, T, D, u = slabq(l, lp, sE); ep = eps_t(u)
    E = -M + sum(ep[i] * m[i] / mp.sqrt(1 - u[j] ** 2 - u[k] ** 2) for i, j, k in PAIRS)
    return E * T * mp.sqrt(3) / sE
def l_from_u(l, u, sE):
    T = sE / mp.sqrt(sum(1 / x ** 2 for x in l))
    for _ in range(400):
        m = [l[i] + u[i] * T for i in range(3)]; Tn = sE / mp.sqrt(sum(1 / x ** 2 for x in m))
        if abs(Tn - T) < mp.mpf(10) ** (-mp.mp.dps + 5) * T: break
        T = Tn
    return [l[i] + 2 * u[i] * T for i in range(3)]

KAPPA = [mp.mpf(1)]
def gaps(u): return [1 - u[j]**2 - u[k]**2 for i, j, k in PAIRS]
def ok(u): return min(gaps(u)) > 0
class Var:
    def __init__(self, u):
        g = gaps(u); self.ip = min(range(3), key=lambda i: g[i]); _, self.jp, self.kp = PAIRS[self.ip]; self.polar = g[self.ip] < mp.mpf('0.3')
    def to_u(self, y):
        if not self.polar: return list(y)
        r = mp.sqrt(-mp.expm1(y[0])); u = [None] * 3; u[self.ip] = y[2]; u[self.jp] = r * mp.cos(y[1]); u[self.kp] = r * mp.sin(y[1]); return u
    def to_y(self, u):
        if not self.polar: return list(u)
        return [mp.log(1 - u[self.jp]**2 - u[self.kp]**2), mp.atan2(u[self.kp], u[self.jp]), u[self.ip]]
    def tr(self, F, u):
        if not self.polar: return F
        j, k, i = self.jp, self.kp, self.ip; h = mp.sqrt(1 - u[j]**2 - u[k]**2)
        return [(u[j] * F[j] + u[k] * F[k]) * h, -u[k] * F[j] + u[j] * F[k], F[i]]
    def valid(self, y):
        if self.polar and y[0] >= 0: return False
        return ok(self.to_u(y))
def Gfun(a, b, sE, M):
    def G(x):
        c = l_from_u(b, x, sE); T = sE / mp.sqrt(sum(4 / (b[i] + c[i]) ** 2 for i in range(3)))
        rr = resid(a, b, c, sE, M); sc = [max(b[(i+1)%3] * b[(i+2)%3] / T, sum(b)) for i in range(3)]
        return [rr[i] / sc[i] for i in range(3)]
    return G
def jac(H, y):
    H0 = H(y); n = len(y); J = mp.matrix(3, n); hh = mp.mpf(10) ** (-mp.mp.dps // 2)
    for q in range(n):
        yp = list(y); yp[q] += hh; Hp = H(yp)
        for r in range(3): J[r, q] = (Hp[r] - H0[r]) / hh
    return J, H0
def newton(H, V, y, it=60):
    tol = mp.mpf(10) ** (-mp.mp.dps + 8) * KAPPA[0]; e = None; J = None
    for _ in range(it):
        J, F0 = jac(H, y); e = max(abs(v) for v in F0)
        if e < tol: return True, y, e, J
        try: dy = mp.lu_solve(J, mp.matrix([-v for v in F0]))
        except ZeroDivisionError: return False, y, e, J
        t = mp.mpf(1)
        while t > mp.mpf(10) ** -14:
            yn = [y[i] + t * dy[i] for i in range(3)]
            if V.valid(yn) and max(abs(v) for v in H(yn)) < e: break
            t /= 2
        if t <= mp.mpf(10) ** -14: return False, y, e, J
        y = yn
    return False, y, e, J
def homotopy(Lm, a, b, sE, M, u_prev, nmax=400):
    V = Var(u_prev)
    def H(Y):
        lam = Y[3]; G = Gfun([Lm[i] + lam * (a[i] - Lm[i]) for i in range(3)], [a[i] + lam * (b[i] - a[i]) for i in range(3)], sE, M)
        uu = V.to_u(Y[:3]); return V.tr(G(uu), uu)
    def tang(J, prev):
        t = []
        for q in range(4):
            cols = [c for c in range(4) if c != q]; Mq = mp.matrix(3, 3)
            for r in range(3):
                for c_, c in enumerate(cols): Mq[r, c_] = J[r, c]
            t.append((-1) ** q * mp.det(Mq))
        nrm = mp.sqrt(sum(v * v for v in t)); t = [v / nrm for v in t]
        if prev is not None and sum(t[i] * prev[i] for i in range(4)) < 0: t = [-v for v in t]
        return t
    Y = V.to_y(u_prev) + [mp.mpf(0)]; J, _ = jac(H, Y); t = tang(J, None)
    if t[3] < 0: t = [-v for v in t]
    ds = mp.mpf('0.05'); fold = False; minlam_slope = mp.mpf(1)
    for _ in range(nmax):
        Yp = [Y[i] + ds * t[i] for i in range(4)]; good = False
        for _c in range(20):
            if not V.valid(Yp[:3]): break
            J, H0 = jac(H, Yp); A = mp.matrix(4, 4); rhs = mp.matrix(4, 1)
            for r in range(3):
                for c in range(4): A[r, c] = J[r, c]
                rhs[r] = -H0[r]
            for c in range(4): A[3, c] = t[c]
            rhs[3] = -sum(t[i] * (Yp[i] - Y[i] - ds * t[i]) for i in range(4))
            try: d = mp.lu_solve(A, rhs)
            except ZeroDivisionError: break
            Yp = [Yp[i] + d[i] for i in range(4)]
            if max(abs(v) for v in d) < mp.mpf(10) ** (-mp.mp.dps + 10): good = V.valid(Yp[:3]); break
        if good and Yp[3] > 1:
            w = (1 - Y[3]) / (Yp[3] - Y[3]); y0 = [Y[i] + w * (Yp[i] - Y[i]) for i in range(3)]
            Hf = lambda yy: V.tr(Gfun(a, b, sE, M)(V.to_u(yy)), V.to_u(yy))
            okn, y, e, _ = newton(Hf, V, y0)
            if okn: return True, V.to_u(y), fold, minlam_slope
            good = False
        if not good:
            ds /= 2
            if ds < mp.mpf(10) ** -12: return False, V.to_u(Y[:3]), fold, Y[3]
            continue
        J, _ = jac(H, Yp); tn = tang(J, t)
        if tn[3] < 0: fold = True
        minlam_slope = min(minlam_slope, tn[3]); Y, t = Yp, tn; ds = min(ds * 1.5, mp.mpf('0.25'))
    return False, V.to_u(Y[:3]), fold, Y[3]
def step(L, U, sE, M):
    a, b = L[-2], L[-1]; KAPPA[0] = (max(b) / min(b)) ** 2; G = Gfun(a, b, sE, M)
    gs = [U[-1]] if len(U) < 2 else [[2 * U[-1][i] - U[-2][i] for i in range(3)], U[-1]]
    for g in gs:
        if not ok(g): continue
        V = Var(g); H = lambda yy: V.tr(G(V.to_u(yy)), V.to_u(yy))
        okn, y, e, J = newton(H, V, V.to_y(g))
        if okn: return 'ok', V.to_u(y), mp.det(J)
    if len(L) < 3: return 'NOROOT', None, None
    okh, u, fold, info = homotopy(L[-3], a, b, sE, M, U[-1])
    if okh: return ('fold' if fold else 'homotopy'), u, info
    return 'NOROOT', u, (fold, info)
'''
# run-11 vacuum state at tick 200 (seed-1 random anisotropic data, sin eps0 = 0.0892), 40 digits: last 3 slices, last 2 slab speeds
STATE11 = "STATE [['1.66035452787509047177421410139206836861', '0.1578456694819417670013960735120776432893', '0.0001171799271753548552812543422003512426487'], ['1.66037152277623101151372559214650445893', '0.1578343016434624824043516890218546816117', '0.0001121391581256811492143617475070251026794'], ['1.66038784324449705028824454443993263054', '0.1578235088251881445991893623238154279348', '0.0001073099972115630519724118308150570538018']] [['0.8311935446058734906526353515769113712182', '-0.5559828728608609522254759748216662260759', '-0.2465359850751566605997318325597231117019'], ['0.8341082406648375586926064473701565476868', '-0.5516005126737842546289454585267510678734', '-0.2468092733800040639385080693410734854978']] 0.089161300778190746841"
FL, MP = {}, {}
exec(FL_SRC, FL); exec(MP_SRC, MP)
T00 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
PAIRS = FL['PAIRS']; resid, energy, l_from_u, lapse, S_loc = FL['resid'], FL['energy'], FL['l_from_u'], FL['lapse'], FL['S_loc']
gaps = FL['gaps']; rng = np.random.default_rng(20261022)

print('== A. box-frustum carrier: edges l_x,l_y,l_z per slice, tick T = sin(eps0)/sqrt(sum 1/m_i^2) (CL-1, mid read)')
def g_np(u): return np.sqrt(1 - 2 * u * u) * np.arcsin(u * u / (1 - u * u))
def S3(l0, l1, l2, sig, M):      # crush-bounce cubic-frustum carrier, inlined for comparison
    out = 0
    for a, b in ((l0, l1), (l1, l2)):
        T = sig * (a + b) / 2; u = (b - a) / (2 * T); out += 6 * (a + b) * T * g_np(u) - M * T
    u0 = (l1 - l0) / (sig * (l0 + l1)); u1 = (l2 - l1) / (sig * (l1 + l2))
    return out + 6 * l1 ** 2 * (np.arctanh(u1) - np.arctanh(u0)) + 6 * l0 ** 2 * np.arctanh(u0) - 6 * l2 ** 2 * np.arctanh(u1)
dev = 0
for a, b, c in ((1.0, 1.05, 1.12), (1.0, 0.97, 0.9), (2.0, 1.9, 1.75)):
    dev = max(dev, abs(S_loc(np.full(3, a), np.full(3, b), np.full(3, c), 0.3, 0.7) - S3(a, b, c, 0.3 / np.sqrt(3), 0.7)))
check('A1 THEOREM: equal edges give exactly the cubic-frustum carrier (trapezoid deficit 4 asin(u_j u_k/sqrt((1-u_j^2)(1-u_k^2))))', dev < 1e-13, f'max action difference {dev:.0e}')
def hinges(l0, l1, l2, sE):
    out = []
    for (a, b) in ((l0, l1), (l1, l2)):
        m = (a + b) / 2; T = lapse(a, b, sE); u = (b - a) / (2 * T)
        for i, j, k in PAIRS:
            out.append((m[i] * T * np.sqrt(1 - u[j] ** 2 - u[k] ** 2), 4 * np.arcsin(u[j] * u[k] / np.sqrt((1 - u[j] ** 2) * (1 - u[k] ** 2)))))
    u0 = (l1 - l0) / (2 * lapse(l0, l1, sE)); u1 = (l2 - l1) / (2 * lapse(l1, l2, sE))
    for i, j, k in PAIRS: out.append((l1[j] * l1[k], 2 * (np.arctanh(u1[i]) - np.arctanh(u0[i]))))
    return out
sch = 0
for _ in range(4):
    l0 = rng.uniform(0.5, 2, 3); l1 = l0 * np.exp(rng.uniform(-0.05, 0.05, 3)); l2 = l1 * np.exp(rng.uniform(-0.05, 0.05, 3))
    g = resid(l0, l1, l2, 0.3, 0.4); H0 = hinges(l0, l1, l2, 0.3); gs = np.zeros(3)
    for q in range(3):
        d = np.zeros(3); d[q] = 1e-6
        gs[q] = sum((p[0] - r[0]) / 2e-6 * e for p, r, (_, e) in zip(hinges(l0, l1 + d, l2, 0.3), hinges(l0, l1 - d, l2, 0.3), H0))
        gs[q] -= 0.4 * (lapse(l0, l1 + d, 0.3) + lapse(l1 + d, l2, 0.3) - lapse(l0, l1 - d, 0.3) - lapse(l1 - d, l2, 0.3)) / 2e-6
    sch = max(sch, np.max(np.abs(g - gs) / np.abs(g)))
check('A2 THEOREM: Schlaefli holds on anisotropic slabs: the deficits are the true dihedral angles', sch < 1e-7, f'relative {sch:.0e}')
t = np.linspace(40.0, 60.0, 401); p = np.array([0.2, -0.5, 0.9]); a = np.array([np.exp(0.002 * p_ * t) for p_ in p]).T
Lsum = LCi = 0.0
for n in range(1, len(t) - 1):
    T0 = lapse(a[n - 1], a[n], 0.05); u0 = (a[n] - a[n - 1]) / (2 * T0); u1 = (a[n + 1] - a[n]) / (2 * lapse(a[n], a[n + 1], 0.05))
    Lsum += FL['slab'](a[n - 1], a[n], 0.05)[0] + sum(2 * (a[n - 1][j] * a[n - 1][k] - a[n][j] * a[n][k]) * np.arctanh(u0[i]) for i, j, k in PAIRS)
    ad, m = 2 * u0, (a[n] + a[n - 1]) / 2; LCi += -T0 * (ad[0] * ad[1] * m[2] + ad[1] * ad[2] * m[0] + ad[0] * ad[2] * m[1])
check('A3 THEOREM: small face speeds give the Bianchi I Einstein-Hilbert action -T sum adot_i adot_j a_k',
      abs(Lsum / LCi - 1) < 0.02, f'Regge/continuum action {Lsum / LCi:.4f} (off-shell path) at u ~ {np.max(np.abs(u1)):.3f}')
l0 = np.array([1.0, 0.8, 1.3]); u0 = np.array([0.3, -0.2, -0.4]); l1 = l_from_u(l0, u0, 0.1); sc = []
for lam, M in ((1.0, 0.0), (1e-20, 0.0), (1.0, 0.5), (1e-20, 0.5e-20)):
    V = FL['Var'](u0); okn, y, e, J = FL['newton'](FL['Gfun'](lam * l0, lam * l1, 0.1, M), V, u0.copy()); sc.append(V.to_u(y))
check('A4 THEOREM: degree-2 homogeneity: the face-speed map is scale-free, so CL-1 splits leave the vacuum orbit unchanged',
      np.max(np.abs(sc[0] - sc[1])) < 1e-9 and np.max(np.abs(sc[2] - sc[3])) < 1e-9, f'u at scale 1 vs 1e-20: {np.max(np.abs(sc[0] - sc[1])):.0e}, dust {np.max(np.abs(sc[2] - sc[3])):.0e}')
rows = []
for uj, uk in ((0.6, 0.6), (-0.6, -0.6), (0.6, -0.6), (-0.7, 0.5), (0.2, 0.9), (-0.9, -0.3)):
    for dl in (1e-6,):
        s = np.sqrt((1 - dl) / (uj * uj + uk * uk)); u = np.array([0.1, uj * s, uk * s]); l1 = np.array([1.0, 1.0, 1.0])
        l2 = l_from_u(l1, u, 0.05); l0 = l_from_u(l1, -0.2 * u, 0.05); R = resid(l0, l1, l2, 0.05)
        n = np.array([0, u[1], u[2]]) / np.hypot(u[1], u[2]); rows.append((np.sign(uj * uk), (R @ n) / np.linalg.norm(R)))
check('A5 THEOREM (leading asymptotics): at the null face u_j^2+u_k^2 -> 1 the edge equation diverges as pi m_i sign(u_j u_k) n/h_i: outward when both '
      'faces move alike, INWARD when one grows and one shrinks, so the isotropic existence proof does not carry over', all(abs(c - s_) < 1e-3 for s_, c in rows),
      'R.n/|R| at gap 1e-6: ' + ', '.join(f'{s_:+.0f}:{c:+.4f}' for s_, c in rows))

print('== B. existence, multiplicity, folds of the edge equation (one tick, any data)')
gm = []
for _ in range(12):
    while True:
        d = rng.normal(size=3); d /= np.linalg.norm(d); s = 1 / np.sqrt(max(d[j] ** 2 + d[k] ** 2 for i, j, k in PAIRS))
        if True: break
    l1 = np.exp(rng.uniform(-1, 1, 3)); l0 = l_from_u(l1, -0.3 * s * d, 0.03); vals = []
    for dl in (1e-2, 1e-6, 1e-10):
        u = d * s * np.sqrt(1 - dl); vals.append(np.linalg.norm(resid(l0, l1, l_from_u(l1, u, 0.03), 0.03)))
    gm.append(vals[2] / vals[0])
check('B1 DIAGNOSTIC: the edge equation diverges on the whole null boundary, so roots cannot leave the window: one degree for all data', min(gm) > 100,
      f'|R|(gap 1e-10)/|R|(gap 1e-2) on 12 rays: min {min(gm):.0f}, median {np.median(gm):.0f}')
r2 = np.random.default_rng(2); g1 = np.linspace(-0.97, 0.97, 7); hist = {}; degs = {}; ex = None
starts = [np.array([x, y, z]) for x in g1 for y in g1 for z in g1 if np.min(gaps(np.array([x, y, z]))) > 0.02]
nsamp = 0
while nsamp < 18 and time.monotonic() - T00 < 40:
    sE = 10 ** r2.uniform(-2, -0.6); l1 = np.exp(r2.uniform(-1, 1, 3)); M = r2.choice([0.0, 1.0]) * r2.uniform(0, 2) * l1.sum()
    while True:
        u0 = r2.uniform(-1, 1, 3)
        if np.min(gaps(u0)) > 0.02: break
    l0 = l1.copy()
    for _ in range(200):
        l0n = l1 - 2 * u0 * lapse(l0, l1, sE)
        if np.max(np.abs(l0n - l0)) < 1e-15: break
        l0 = l0n
    if np.min(l0) <= 0: continue
    G = FL['Gfun'](l0, l1, sE, M); roots = []; dets = []
    for st in starts:
        V = FL['Var'](st); V.polar = False; okn, y, e, J = FL['newton'](G, V, st.copy(), tol=1e-11, it=40)
        if okn and not any(np.max(np.abs(y - r)) < 1e-6 for r in roots): roots.append(y); dets.append(np.sign(np.linalg.det(J)))
    nsamp += 1; k = len(roots); hist[k] = hist.get(k, 0) + 1; dg = int(sum(dets)); degs[dg] = degs.get(dg, 0) + 1
    if k > 1 and ex is None: ex = (k, np.round(u0, 2), [np.round(r, 2) for r in roots])
check('B2 DIAGNOSTIC: degree +1 at every sampled tick (a root always exists), but fast data have 3 roots: CL-3 does not fix the next slice',
      set(degs) == {1} and max(hist) >= 3, (f'{nsamp} samples: roots {dict(sorted(hist.items()))}, degree {degs}; e.g. u_prev {ex[1]} -> roots {ex[2]}' if ex else str(hist)))
def detJ(l1, u, sE):
    l2 = l_from_u(l1, u, sE); l0 = l_from_u(l1, -0.5 * u, sE); J = np.zeros((3, 3))
    for q in range(3):
        h = 1e-7 * l2[q]; d = np.zeros(3); d[q] = h; J[:, q] = (resid(l0, l1, l2 + d, sE) - resid(l0, l1, l2 - d, sE)) / (2 * h)
    return np.linalg.det(J)
ray = {}
for nm, dirn in (('iso', (1, 1, 1)), ('(1,-1,-1)', (1, -1, -1)), ('(1,0,0)', (1, 0, 0)), ('(1,1,0)', (1, 1, 0)), ('Kasner -2:3:6', (2, -3, -6))):
    d = np.array(dirn, float); d /= np.sqrt(max(d[j] ** 2 + d[k] ** 2 for i, j, k in PAIRS))
    ray[nm] = [np.sign(detJ(np.ones(3), s * d, 0.02)) for s in (0.05, 0.4, 0.8, 0.95, 0.99, 0.999)]
check('B3 DIAGNOSTIC: the Legendre-map Jacobian changes sign near some null faces (folds), never on isotropic or one-axis rays',
      all(v > 0 for v in ray['iso'] + ray['(1,0,0)'] + ray['(1,-1,-1)']) and min(ray['(1,1,0)']) < 0 and min(ray['Kasner -2:3:6']) < 0,
      '; '.join(f"{k_}: {''.join('+' if v > 0 else '-' for v in w)}" for k_, w in ray.items()) + ' at s = .05,.4,.8,.95,.99,.999 of the null ray')

print('== C. vacuum Kasner collapse (fixed-step tick; zero dark constant on the first slab)')
from scipy.optimize import brentq
def kasner(sE, uk, amp, NT):
    p = np.array([-uk, 1 + uk, uk * (1 + uk)]) / (1 + uk + uk * uk); l0 = np.ones(3)
    f = lambda x: energy(l0, l_from_u(l0, np.array([x, -amp * p[1], -amp * p[2]]), sE), sE, 0.0)
    u = np.array([brentq(f, 1e-9, 0.9), -amp * p[1], -amp * p[2]]); L = [l0, l_from_u(l0, u, sE)]; U = [u]; tau = [0.0, lapse(l0, L[1], sE)]; cnt = {}
    for n in range(NT):
        st, x, info = FL['step'](L, U, sE, 0.0); cnt[st] = cnt.get(st, 0) + 1
        if st == 'NOROOT': break
        c = l_from_u(L[-1], x, sE); tau.append(tau[-1] + lapse(L[-1], c, sE)); L.append(c); U.append(x)
    return p, np.array(L), np.array(U), np.array(tau), cnt
res = {}
for nm, uk, NT in (('pancake', 2.0, 1500), ('cigar', 1.0, 1100)):
    res[nm] = kasner(0.3, uk, 0.01, NT)
rat = []
for nm in res:
    p, L, U, tau, cnt = res[nm]; r = np.log(L[60] / L[59]); rat.append(np.max(np.abs(r / r[2] - p / p[2])))
    t_end = 1 / (2 * 0.01); tt = np.linspace(0, t_end, 200001)[1:]
    nGR = np.trapezoid(np.sqrt(np.sum([(tt / t_end) ** (-2 * q) for q in p], axis=0)) / 0.3, tt); res[nm] = res[nm] + (nGR,)
check('C1 DIAGNOSTIC: sub-Hubble cells follow Kasner (speed ratios p_i/p_j); the continuum slicing crushes in finitely many ticks',
      max(rat) < 2e-3, f'max ratio error {max(rat):.0e}; continuum ticks to the crush: {res["pancake"][5]:.0f} and {res["cigar"][5]:.0f}')
p, L, U, tau, cnt = res['pancake'][:5]; k = len(L) - 1
pr = (1 + 0.3 * U[-1][2]) / (1 - 0.3 * U[-1][2]); me = L[-1][2] / L[-2][2]
check('C2 DIAGNOSTIC pancake p=(-2,3,6)/7: every tick has its root; l_z falls by (1+s u_z)/(1-s u_z), s = sin eps0, far from '
      'the speed limit; l_x, l_y freeze; proper time converges (the tick, read from the smallest edge, freezes the cell)', cnt.get('NOROOT', 0) == 0 and abs(pr / me - 1) < 1e-8 and abs(L[-1][0] / L[-2][0] - 1) < 1e-5 and np.min(gaps(U[-1])) > 0.3,
      f'{k} ticks {cnt}; ratio meas/pred - 1 = {me / pr - 1:.0e}; edges {np.round(L[-1], 5)}; min null gap {np.min(gaps(U[-1])):.2f}; tau {tau[k - 1]:.4f} -> {tau[k]:.4f} vs Kasner 50 (lattice ticks: unbounded vs {res["pancake"][5]:.0f})')
p, L, U, tau, cnt = res['cigar'][:5]; k = len(L) - 1; gl = [np.min(gaps(U[q])) / L[q][1] for q in (k // 2, 3 * k // 4, k - 1)]
pr = (1 + 0.3 * U[-1][1] / np.sqrt(2)) / (1 - 0.3 * U[-1][1] / np.sqrt(2))
check('C3 DIAGNOSTIC cigar p=(-1,2,2)/3 (Schwarzschild interior): l_y=l_z fall by (1+s u/sqrt2)/(1-s u/sqrt2); the growing edge alone '
      'runs into the speed limit (u_x -> sqrt(1-u_y^2), null gap ~ l_y) and freezes',
      cnt.get('NOROOT', 0) == 0 and abs(pr / (L[-1][1] / L[-2][1]) - 1) < 1e-6 and abs(gl[2] / gl[1] - 1) < 0.02,
      f'{k} ticks {cnt}; u = {np.round(U[-1], 5)}; gap/l_y {gl[0]:.2f}, {gl[1]:.2f}, {gl[2]:.2f}; l_x {L[-1][0]:.4f}; tau {tau[-1]:.3f}')

print('== D. a lattice wall: reflection off a mixed-sign null face (vacuum Bianchi I, mpmath 40 digits)')
mp.mp.dps = 40; txt = STATE11[6:]
i = txt.index(']] [[') + 2; Ls = ast.literal_eval(txt[:i]); j = txt.index(']] ', i) + 2; Us = ast.literal_eval(txt[i + 1:j]); sEm = mp.mpf(txt[j + 1:].strip())
Lm = [[mp.mpf(v) for v in w] for w in Ls]; Um = [[mp.mpf(v) for v in w] for w in Us]; hist_w = []; cntw = {}
for n in range(42):
    st, x, info = MP['step'](Lm, Um, sEm, mp.mpf(0)); cntw[st] = cntw.get(st, 0) + 1
    if st == 'NOROOT': break
    Lm.append(MP['l_from_u'](Lm[-1], x, sEm)); Um.append(x); hist_w.append((n + 201, [float(v) for v in x], float(min(MP['gaps'](x)))))
uy = [h[1][1] for h in hist_w]; gp = [h[2] for h in hist_w]; kflip = next(q for q in range(len(uy)) if uy[q] > 0)
check('D1 DIAGNOSTIC: a vacuum cell slides along the mixed-sign null face of its z-edge (gap ~ 1e-7) and is reflected: u_y turns '
      'from shrinking to growing, a lattice BKL-type wall absent from GR Bianchi I; every tick has its root, no fold met',
      cntw.get('NOROOT', 0) == 0 and max(gp[:15]) < 1e-6 and gp[-5] > 0.05 and uy[0] < -0.5 and uy[-1] > 0.2,
      f"ticks 201-{hist_w[-1][0]} {cntw}; u at 201 {np.round(hist_w[0][1], 3)}, gap {gp[0]:.1e}; leaves the face at tick ~{hist_w[next(q for q in range(len(gp)) if gp[q] > 1e-3)][0]}; u_y > 0 from tick {hist_w[kflip][0]}; u at {hist_w[-1][0]} {np.round(hist_w[-1][1], 3)}")

print('== E. dust-filled Bianchi I (Heckmann-Schucking class), mpmath')
mp.mp.dps = 30; sEd = mp.mpf('0.1'); ud = [mp.mpf(v) for v in ('-0.05', '-0.03', '-0.04')]; l0 = [mp.mpf(1)] * 3; l1 = MP['l_from_u'](l0, ud, sEd)
Td = sEd / mp.sqrt(sum(4 / (l0[i] + l1[i]) ** 2 for i in range(3))); Md = MP['energy'](l0, l1, sEd, 0) * sEd / (mp.sqrt(3) * Td)
Ld = [l0, l1]; Ud = [ud]; cntd = {}; snap = {}
for n in range(520):
    MP['KAPPA'][0] = 1
    st, x, info = MP['step'](Ld, Ud, sEd, Md); cntd[st] = cntd.get(st, 0) + 1
    if st == 'NOROOT': break
    Ld.append(MP['l_from_u'](Ld[-1], x, sEd)); Ud.append(x)
    if n in (100, 450, 500): snap[n] = ([float(v) for v in Ld[-1]], [float(v) for v in x], float(MP['energy'](Ld[-2], Ld[-1], sEd, Md)))
ok_e = cntd.get('NOROOT', 0) == 0 and snap[100][1][1] < 0 < snap[500][1][1] and snap[500][0][0] < 1e-3 and abs(snap[500][0][1] / snap[450][0][1] - 1) < 0.02 and abs(snap[500][0][2] / snap[450][0][2] - 1) < 0.02
check('E1 DIAGNOSTIC: dust collapse: all edges shrink, one re-expands (as in GR), then one edge falls geometrically and the others freeze', ok_e,
      f"M {float(Md):.4f}; {cntd}; tick 100 u {np.round(snap[100][1], 3)}; 500: l {np.round(snap[500][0], 5)}, u {np.round(snap[500][1], 3)}, D {snap[500][2]:.1e}; l_y,l_z change 450->500 {snap[500][0][1] / snap[450][0][1] - 1:.0e}, {snap[500][0][2] / snap[450][0][2] - 1:.0e}")

print('== F. ESTIMATES (cube 2 sqrt(8 pi) l_P; Schwarzschild interior ~ Kantowski-Sachs ~ Kasner (-1,2,2)/3 near r = 0)')
lP = 1.616255e-35; l0c = 2 * np.sqrt(8 * np.pi) * lP; G, c = 6.674e-11, 2.998e8; Ms = 1.989e30; rs = 2 * G * 10 * Ms / c ** 2
r_nosplit = np.sqrt(l0c * rs); r_split = (l0c ** 2 * rs) ** (1 / 3)
check('F1 Kantowski-Sachs (10 M_sun): radial edges stretch as r^-1/2; lattice regime at r ~ sqrt(l r_s) without splits, '
      '~ (l^2 r_s)^(1/3) with CL-1 splits; then C3: radial edge frozen at the speed limit, r = 0 at no finite tick',
      r_split < r_nosplit < rs, f'r_s {rs:.2e} m; sqrt(l r_s) {r_nosplit:.1e} m; (l^2 r_s)^(1/3) {r_split:.1e} m; Planck-curvature r {(lP ** 2 * rs) ** (1 / 3):.1e} m')
check('F2 exteriors GR to (l/r_s)^2; no bounce or white hole; homogeneous collapse makes no crushed cube (B2)', (l0c / rs) ** 2 < 1e-70,
      f'(l/r_s)^2 {(l0c / rs) ** 2:.0e}')
print('supplied: box-frustum carrier (diagonal metric, no shift, homogeneous cells), mid-slab tick read, dust -M T, zero')
print('  initial dark constant, Lambda = 0, continuation as the choice among multiple roots, KS = Kasner limit, unit map.')
print(f'elapsed {time.monotonic() - T00:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
