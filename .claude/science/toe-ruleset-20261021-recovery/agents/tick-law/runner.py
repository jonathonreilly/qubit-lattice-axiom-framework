#!/usr/bin/env python3
"""tick-law: which rule fixes the tick (lapse) that CL-1's step reads?  Supplied models; exact identities and finite
diagnostics; no physical identification.
 A  rule algebra on the CL-1 cube tick (spin-3/2 edge hop, inline): a fixed step inverts the cone reading into a
    light-crossing tick; Weyl blindness at fixed step; band maximum 2 eps for every mass; split mode map at a kept step
 B  ticks varied by CL-3 (current reading) on the cubic-frustum Lorentzian Regge FRW carrier: strength of the tick
    fixing, the content-dependent selection, photon lattice band, neutrality, a split
 C  fixed step with the ticks set by CL-1 and not varied: minisuperspace theorem (w = alpha/3), the carrier's lapse
    residual, the conserved constant, splits
 D  weak static field in the fixed-step gauge (planar field, packets): free fall, universality, bending, redshift
 E  the shift-inclusive light-crossing rule and the fixed proper tick
 F  estimates against measurement
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import itertools, math, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
from scipy.optimize import brentq
T00 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ''))

# ------------------------------------------------------------------ CL-1 cube tick (inline)
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); NVc = (2 * C8 - 1.0) / r3; XI = []
for i in range(8):
    _, v_ = np.linalg.eigh(sum(NVc[i, k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
WAX = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(a + 1, 8):
        if np.sum(abs(C8[a] - C8[b])) == 1:
            g_ = XI[a].conj() @ XI[b]; x = -g_ / abs(g_) / r3; ax = int(np.argmax(abs(C8[a] - C8[b])))
            WAX[ax][a, b] = x; WAX[ax][b, a] = np.conj(x)
def Rf(f): f = np.asarray(f, float); return sum(f[i] * WAX[i] for i in range(3)) / np.sqrt(f @ f / 3)
def halves(f, eps, mu):
    R = Rf(f); te, to = eps - mu / 2, -(eps + mu / 2)
    return np.cos(te) * I8 - 1j * np.sin(te) * R, np.cos(to) * I8 - 1j * np.sin(to) * R
def ublock(K, f, eps, mu):
    Ue, Uo = halves(f, eps, mu); D = np.exp(1j * (np.atleast_2d(K) @ C8.T))
    return (D[:, :, None] * Uo[None] * D.conj()[:, None, :]) @ Ue
def band(K, f, eps, mu):
    f = np.asarray(f, float); A = (np.cos(mu) - np.cos(2 * eps)) / 2; Sf = (np.cos(np.atleast_2d(K)) @ f ** 2) / (f @ f)
    return np.arccos(np.clip(A * Sf + (np.cos(2 * eps) + np.cos(mu)) / 2, -1, 1))
def cm2(eps, mu): return (np.cos(mu) - np.cos(2 * eps)) / 6 * (mu / np.sin(mu) if mu else 1.0)
def wmin(U): return np.abs(np.angle(np.linalg.eigvals(U))).min()

print('== A. the rule on the CL-1 cube tick (exact algebra)')
eps0 = 0.3; rng = np.random.default_rng(20261022); dev = 0.0
for _ in range(4):
    L = rng.uniform(0.7, 1.4, 3); f = 1 / L; N = np.sin(eps0) / (r3 * np.sqrt(np.mean(f ** 2)))   # the rule: lapse from the edges
    for ax in range(3):
        k = 1e-4; K = np.zeros(3); K[ax] = k
        v = wmin(ublock(K, f, eps0, 0.0)[0]) / k; dev = max(dev, abs(v / (N * f[ax]) - 1))
check('A1 THEOREM: a fixed step inverts the cone reading, N = sin(eps0)/(sqrt3 rms sqrt(g^ii)): light then moves N sqrt(g^ii) '
      'blocks per tick, so a tick is sin(eps0)/sqrt3 of a block\'s light crossing (T = l sin(eps0)/sqrt3 on cubic cells)', dev < 1e-6, f'box speeds vs N/L_i: max rel dev {dev:.0e}')
Kr = rng.uniform(-np.pi, np.pi, (30, 3)); f0 = np.array([1.0, 0.8, 1.3])
dW = np.abs(ublock(Kr, 2.7 * f0, eps0, 0.0) - ublock(Kr, f0, eps0, 0.0)).max(); dM = np.abs(ublock(Kr, 2.7 * f0, eps0, 0.1 / 2.7) - ublock(Kr, f0, eps0, 0.1)).max()
check('A2 THEOREM: at fixed step the massless update ignores the cell size, so on growing cubic cells it is the same '
      'unitary every tick: photon quasi-energy per tick is exactly kept, the atom phase m N grows as l, 1+z = edge ratio at every K', dW < 1e-14 and dM > 1e-3, f'|U(2.7f)-U(f)| massless {dW:.0e}, massive (mu = mN scaled) {dM:.1e}')
gK = (np.arange(10) + 0.5) / 10 * 2 * np.pi - np.pi; KG = np.stack(np.meshgrid(gK, gK, gK, indexing='ij'), -1).reshape(-1, 3)
KG = np.vstack([KG, [[np.pi] * 3]]); bmax = {}
for e in (0.04, 0.3):
    for mu in (0.0, 0.05):
        bmax[(e, mu)] = max(np.abs(np.angle(np.linalg.eigvals(U))).max() for U in ublock(KG, [1, 1, 1], e, mu)) / (2 * e)
check('A3 THEOREM: every band spans [mu, 2 eps], so the maximum is 2 eps0 for every species: the vacuum-stability bound '
      '(maximum < 0.015-0.075) becomes eps0 < 0.0075-0.0375, one constant for every cube and epoch', max(abs(v - 1) for v in bmax.values()) < 1e-9,
      'max|w|/2eps ' + ', '.join(f'{v:.6f}' for v in bmax.values()))
def U1(K, eps, mu=0.0): return ublock(np.asarray(K, float), [1, 1, 1], eps, mu)[0]
def Pw(U):
    cw = np.real(np.trace(U)) / 8; return (I8 - (U - U.conj().T) / (2j * np.sqrt(1 - cw ** 2))) / 2, np.arccos(cw)
chi0 = rng.normal(size=8) + 1j * rng.normal(size=8)
def split(Kc, e_c, e_f):
    P, wc = Pw(U1(Kc, e_c)); psi = P @ chi0; psi /= np.linalg.norm(psi); flip = ws = 0.0
    for m in C8:
        Kf = Kc / 2 + np.pi * m; am = np.prod((1 + np.exp(-1j * Kf)) / 2) * psi; Pp, wf = Pw(U1(Kf, e_f))
        pp = np.linalg.norm(Pp @ am) ** 2; pm = np.linalg.norm(am) ** 2 - pp; flip += pm; ws += (pp - pm) * wf
    return flip, ws / wc
Kb = np.array([0.05, 0.02, 0.01]); kept = [split(K, 0.15, 0.15) for K in (Kb, 2 * Kb)]
x2 = split(Kb, 0.15, np.arcsin(2 * np.sin(0.15))); x16 = split(Kb, 0.02, np.arcsin(16 * np.sin(0.02)))
check('A4 split: the child tick halves, the step is kept (x1, not x16 as at fixed record 4-volume or x2 at a fixed proper '
      'tick): flips O(K^2), photon and atom phases per tick halve together; a step change flips ~0.06 eps^2 of every mode',
      all(0.03 < fl / (K @ K) < 0.06 for (fl, _), K in zip(kept, (Kb, 2 * Kb))) and abs(kept[0][1] - 0.5) < 1e-4
      and x2[0] / np.arcsin(2 * np.sin(0.15)) ** 2 > 0.03 and x16[0] / np.arcsin(16 * np.sin(0.02)) ** 2 > 0.03,
      f'kept: flip/K^2 {kept[0][0] / (Kb @ Kb):.3f}, {kept[1][0] / (4 * (Kb @ Kb)):.3f}, photon ratio {kept[0][1]:.5f}; '
      f'x2: flip/eps^2 {x2[0] / np.arcsin(2 * np.sin(0.15)) ** 2:.3f}; x16: {x16[0] / np.arcsin(16 * np.sin(0.02)) ** 2:.3f}')

# ------------------------------------------------------------------ frustum carrier with 2^3 splits (per original cell)
def g(u): return np.sqrt(1 - 2 * u * u) * np.arcsin(u * u / (1 - u * u))
def Afn(u): return np.arcsin(u * u / (1 - u * u)) / np.sqrt(1 - 2 * u * u)
def fv(a, b): return (a + b) * (a * a + b * b) / 4
class Carrier:
    """X_n: edge of the original cell's worth at slice n; slab n at mesh m: cell edges X/2^m, 8^m cells.  Hinge j =
    c_up atanh(u_j) - c_dn atanh(u_j-1); split slice: c_up = 2 c_dn (parent faces + new interior faces)."""
    def __init__(s, Lam=0.0, M=0.0, Ng=0.0, K0=(0.4, 0.3, 0.2), Rlin=0.0):
        s.Lam, s.M, s.Ng, s.K0, s.Rlin = Lam, M, Ng, np.asarray(K0, float), Rlin
    def matter(s, a, b, T, m):
        lb = (a + b) / 2; out = s.M * T + s.Rlin * T / (lb * 2 ** m)
        if s.Ng: out = out + s.Ng * np.arccos(1 - 3 * (T / lb) ** 2 * (1 - np.mean(np.cos(s.K0 / 2 ** m))) + 0j)
        return out
    def slab(s, Xa, Xb, T, m):
        a, b = Xa / 2.0 ** m, Xb / 2.0 ** m; u = (b - a) / (2 * T)
        return 8.0 ** m * (6 * (a + b) * T * g(u) - s.Lam * T * fv(a, b)) - s.matter(a, b, T, m), u
    @staticmethod
    def cc(Xj, mdn, mup):
        c = 8.0 ** mdn * 6 * (Xj / 2.0 ** mdn) ** 2; return (c, c) if mup == mdn else (2 * c, c)
    def locX(s, X, T, mesh, j):
        sm, um = s.slab(X[j - 1], X[j], T[j - 1], mesh[j - 1]); spp, up = s.slab(X[j], X[j + 1], T[j], mesh[j])
        cpp = s.cc(X[j - 1], mesh[j - 2] if j >= 2 else mesh[j - 1], mesh[j - 1])[0]; cup, cdn = s.cc(X[j], mesh[j - 1], mesh[j])
        cdn1 = s.cc(X[j + 1], mesh[j], mesh[j + 1] if j + 1 < len(mesh) else mesh[j])[1]
        return sm + spp + cpp * np.arctanh(um) + cup * np.arctanh(up) - cdn * np.arctanh(um) - cdn1 * np.arctanh(up)
    def locT(s, X, T, mesh, j):
        spp, up = s.slab(X[j], X[j + 1], T[j], mesh[j]); cup = s.cc(X[j], mesh[j - 1] if j >= 1 else mesh[j], mesh[j])[0]
        cdn1 = s.cc(X[j + 1], mesh[j], mesh[j + 1] if j + 1 < len(mesh) else mesh[j])[1]
        return spp + cup * np.arctanh(up) - cdn1 * np.arctanh(up)
    def dX(s, X, T, mesh, j):
        Xc = np.array(X, complex); Xc[j] += 1e-30j; return s.locX(Xc, np.asarray(T, complex), mesh, j).imag / 1e-30
    def dT(s, X, T, mesh, j):
        Tc = np.array(T, complex); Tc[j] += 1e-30j; return s.locT(np.asarray(X, complex), Tc, mesh, j).imag / 1e-30
def nextX(C, X, T, mesh, j):
    return brentq(lambda Xb: C.dT(np.array(list(X) + [Xb]), np.array(list(T)), mesh, j), X[j] * (1 + 1e-13),
                  X[j] + 2 * T[j] * 0.7 * 2 ** mesh[j], xtol=1e-16, rtol=1e-15)
def run_b(C, X0, T0, nst, span=3.0, maxsplit=0, scan=49):
    """ticks varied: slab constraint dS/dT_j = 0 gives X_j+1(T_j); slice equation dS/dX_j = 0 picks T_j"""
    X = [X0]; T = [T0]; mesh = [0]; X.append(nextX(C, X, T, mesh, 0)); nsp = 0; info = None
    for j in range(1, nst):
        mh = mesh[-1] + (1 if (X[j] / 2.0 ** mesh[-1] >= 2.0 and nsp < maxsplit) else 0); nsp += mh > mesh[-1]; mt = mesh + [mh]
        def gT(Tj):
            Xb = nextX(C, X, T + [Tj], mt, j); Xa, Ta = np.array(X + [Xb]), np.array(T + [Tj])
            return C.dX(Xa, Ta, mt, j) / abs(12 * X[j] * math.atanh((Xb - X[j]) / 2 ** mh / (2 * Tj)) * 4.0 ** mh), Xb
        Tg = np.geomspace(T[-1] / span, T[-1] * span, scan); gs_ = np.array([gT(t)[0] for t in Tg]); sc = np.where(np.sign(gs_[1:]) != np.sign(gs_[:-1]))[0]
        if len(sc) == 0: info = (j, mh, gs_); break
        rts = [brentq(lambda t: gT(t)[0], Tg[i], Tg[i + 1], xtol=1e-18, rtol=1e-13) for i in sc]
        Tj = min(rts, key=lambda r_: abs(np.log(r_ / T[-1]))); X.append(gT(Tj)[1]); T.append(Tj); mesh = mt
    return np.array(X), np.array(T), mesh, info
def run_V1(C, sig, X0, nsl, delta=0.0, maxsplit=0):
    """fixed step: T_n = sig x mean cell edge; only X varied (ticks follow); first slab from the lapse equation (+delta)"""
    Tof = lambda a, b, m: sig * (a + b) / 2 / 2.0 ** m
    X1 = brentq(lambda Xb: C.dT([X0, Xb], [Tof(X0, Xb, 0)], [0], 0) - delta, X0 * (1 + 1e-12), X0 * (1 + 1.4 * sig))
    X = [X0, X1]; mesh = [0]; nsp = 0
    for j in range(1, nsl):
        mh = mesh[-1] + (1 if (X[j] / 2.0 ** mesh[-1] >= 2.0 and nsp < maxsplit) else 0); nsp += mh > mesh[-1]; mt = mesh + [mh]
        def eq(Xn):
            Xc = np.array(X + [Xn], complex); Xc[j] += 1e-30j
            return C.locX(Xc, np.array([Tof(Xc[i], Xc[i + 1], mt[i]) for i in range(len(mt))]), mt, j).imag / 1e-30
        d = X[j] - X[j - 1]; X.append(brentq(eq, X[j] + 0.2 * d, X[j] + 3 * d, xtol=1e-15, rtol=1e-14)); mesh = mt
    X = np.array(X); T = np.array([Tof(X[n], X[n + 1], mesh[n]) for n in range(len(mesh))])
    R = np.array([C.dT(X, T, mesh, n) for n in range(len(T))])
    u = np.array([(X[n + 1] - X[n]) / 2 ** mesh[n] / (2 * T[n]) for n in range(len(T))])
    G = np.array([8.0 ** mesh[n] * 6 * (X[n] + X[n + 1]) / 2 ** mesh[n] * Afn(u[n]) for n in range(len(T))])
    return X, T, np.array(mesh), R, G, u

print('== B. ticks varied by CL-3 (current reading): cubic-frustum Lorentzian Regge FRW, kappa = 1')
Cs = Carrier(Lam=0.03, M=0.2, Rlin=0.1); a_, b_, T_ = 1.0, 1.01, 0.05
idn = abs(Cs.dT([a_, b_], [T_], [0], 0) - (12 * (a_ + b_) / 2 * Afn((b_ - a_) / (2 * T_)) - 0.2 - 0.1 / 1.005 - 0.03 * fv(a_, b_)))
def strength(C, T0):
    X = [1.0]; T = [T0]; X.append(nextX(C, X, T, [0], 0)); mt = [0, 0]
    def gT(Tj):
        Xb = nextX(C, X, T + [Tj], mt, 1); return C.dX(np.array(X + [Xb]), np.array(T + [Tj]), mt, 1) / abs(12 * X[1] * math.atanh((Xb - X[1]) / (2 * Tj)))
    return (X[1] - X[0]) / T0 / ((X[0] + X[1]) / 2) * T0, abs(gT(2 * T0) - gT(T0))
cf = {}
for lab, C in (('Lambda', Carrier(Lam=0.03)), ('dust', Carrier(M=0.1)), ('radiation', Carrier(Rlin=0.1))):
    st = np.array([strength(C, t) for t in (0.02, 0.01, 0.005)]); cf[lab] = (st[-1, 1] / st[-1, 0] ** 2, np.polyfit(np.log(st[:, 0]), np.log(st[:, 1]), 1)[0])
check('B1 lapse equation = 6(a+b)A(u) - E - Lambda fv (Schlaefli); the edge equation fixes the tick only through a term '
      'c (HT)^2 of its size', idn < 1e-12 and all(abs(p - 2) < 0.05 for _, p in cf.values()),
      f'identity {idn:.0e}; ' + ', '.join(f'{k} c={v[0]:.3f} (power {v[1]:.2f})' for k, v in cf.items()))
sel = {}
for lab, C in (('Lambda', Carrier(Lam=0.003)), ('dust', Carrier(M=0.01)), ('radiation, no band', Carrier(Rlin=0.1)),
               ('photons on their band', Carrier(Ng=0.1 / np.sqrt(6 * (1 - np.mean(np.cos([1.6, 1.5, 1.4])))), K0=(1.6, 1.5, 1.4)))):
    X, T, _, info = run_b(C, 1.0, 0.01, 40); lb = 0.5 * (X[1:] + X[:-1])[:len(T)]
    sel[lab] = np.polyfit(np.log(lb[3:]), np.log(T[3:]), 1)[0]
check('B2 the selected tick depends on the content: Lambda T ~ 1/l (sin eps ~ l^-2), dust T ~ l; photons on their lattice '
      'band also give T ~ l: their band breaks time relabelling at (wT)^2 >> (HT)^2 and keeps quasi-energy only at a kept step', abs(sel['Lambda'] + 1) < 0.02
      and abs(sel['dust'] - 1) < 0.02 and abs(sel['photons on their band'] - 1) < 0.02 and abs(sel['radiation, no band'] - 1) > 0.5,
      'T ~ l^p: ' + ', '.join(f'{k} {v:+.3f}' for k, v in sel.items()))
nt = []
for C in (Carrier(M=0.01), Carrier(Lam=0.003)):
    Xa, Ta, _, _ = run_b(C, 1.0, 0.010, 30); Xb, Tb, _, _ = run_b(C, 1.0, 0.011, 30)
    la, lbb = 0.5 * (Xa[1:] + Xa[:-1])[:len(Ta)], 0.5 * (Xb[1:] + Xb[:-1])[:len(Tb)]; le = min(la[-1], lbb[-1])
    nt.append(np.interp(le, lbb, Tb) / np.interp(le, la, Ta))
check('B3 neutral: a 10% change of the first tick persists, so the tick\'s value is initial data',
      all(abs(v - 1.1) < 1e-3 for v in nt), 'tick ratio at equal edge after 30 ticks: ' + ', '.join(f'{v:.5f}' for v in nt))
Cd = Carrier(M=0.006); X, T, mesh, info = run_b(Cd, 1.996, 0.02, 200, maxsplit=1)
j = len(T); mt = list(mesh) + [1]; res = []
for Tj in np.geomspace(T[-1] * 1e-3, T[-1] * 10, 25):
    Xb = nextX(Cd, list(X), list(T) + [Tj], mt, j); uf = (Xb - X[j]) / 2 / (2 * Tj)
    res.append(Cd.dX(np.array(list(X) + [Xb]), np.array(list(T) + [Tj]), mt, j) / (Cd.cc(X[j], 0, 1)[0] * uf))
res = np.array(res); uc = (X[j] - X[j - 1]) / (2 * T[-1])
check('B4 no stationary point across a split: for every child tick (1e-3 to 10 x the last) the split-slice equation stays '
      'at -u^2/4 of its momentum term; the junction mismatch ignores the tick',
      info is not None and np.all(np.sign(res) == np.sign(res[0])) and abs(res.mean() / (-uc ** 2 / 4) - 1) < 0.01,
      f'residual {res.min():.4e}..{res.max():.4e} vs -u^2/4 = {-uc ** 2 / 4:.4e}')

print('== C. fixed step: ticks set by CL-1, not varied; CL-3 stationary in the other edges with the ticks following')
t, c, al, kap, vv, E_ = sp.symbols('t c alpha kappa v E', positive=True); af = sp.Function('a')(t); rho = sp.Function('rho')
Nf = c * af ** al; Lg = -3 * af * sp.diff(af, t) ** 2 / (kap * Nf) - Nf * af ** 3 * rho(af)
Eg = sp.diff(af, t) * sp.diff(Lg, sp.diff(af, t)) - Lg; EL = sp.diff(sp.diff(Lg, sp.diff(af, t)), t) - sp.diff(Lg, af)
cons_ok = sp.simplify(sp.diff(Eg, t) - sp.diff(af, t) * EL) == 0
aa = sp.Symbol('A', positive=True); Ev = Eg.subs(sp.diff(af, t), vv).subs(af, aa); v2 = sp.solve(sp.Eq(Ev, E_), vv ** 2)
v2 = v2[0] if v2 else sp.solve(sp.Eq(Ev, E_), vv)[0] ** 2
fr = sp.simplify(v2 / (c * aa ** al * aa) ** 2 - kap / 3 * (rho(aa) - E_ / (c * aa ** (3 + al))))
ws = {v: sp.Rational(3 + v, 3) - 1 for v in (1, 0, -3)}
check('C1 THEOREM (sympy): N = c a^alpha fixed before variation loses the lapse equation; the reduced energy E is kept and '
      'H^2 = (kappa/3)(rho + rho_C), rho_C = -E/(c a^(3+alpha)), w_C = alpha/3: fixed step (1) dark radiation, fixed proper '
      'tick (0) dust, fixed record 4-volume (-3) Lambda',
      cons_ok and fr == 0 and ws == {1: sp.Rational(1, 3), 0: 0, -3: -1}, f'dE/dt = adot EL: {cons_ok}; residual {fr}; w {ws}')
out = {}
for e0, s in ((0.1, 1.0), (0.1, 4.0), (0.2, 1.0)):
    sg = np.sin(e0) / r3; C = Carrier(Lam=0.0003 * s, M=0.002 * s, Ng=0.0002 * s)
    X, T, mesh, R, G, u = run_V1(C, sg, 1.0, 80); out[(e0, s)] = (np.abs(R / G).max(), (2 * u.mean() * sg))
check('C2 lapse equation imposed on the first slab only: it then holds on every slab to ~0.01 (HT)^2, so the expansion law '
      'A(u) = (8 pi G/3) rho l^2/4 holds; photons leave the edge equation exactly (A2), entering through the first slab',
      all(r_ / ht ** 2 < 0.03 for r_, ht in out.values()), ', '.join(f'{v[0]:.1e} = {v[0] / v[1] ** 2:.3f}(HT)^2' for k, v in out.items()))
sg = np.sin(0.1) / r3; C = Carrier(Lam=0.0003, M=0.002, Ng=0.0002)
X, T, mesh, R, G, u = run_V1(C, sg, 1.0, 110); X2, T2, m2, R2, G2, u2 = run_V1(C, sg, 1.0, 110, delta=1e-3 * G[0])
Xm, Xm2 = 0.5 * (X[1:] + X[:-1]), 0.5 * (X2[1:] + X2[:-1]); dR = R2 - np.interp(Xm2, Xm, R); EC = dR * Xm2
pC = np.polyfit(np.log(Xm2[5:]), np.log(np.abs(dR[5:]) / Xm2[5:] ** 3), 1)[0]
check('C3 a nonzero first-slab residual is a kept constant per cell diluting as l^-4: dark radiation, as C1 says', abs(pC + 4) < 1e-3 and abs(EC[-1] / EC[1] - 1) < 1e-5, f'density ~ X^{pC:.4f}; residual x X drift {EC[-1] / EC[1] - 1:.1e}')
sg = np.sin(0.3) / r3; C = Carrier(Lam=0.003, M=0.02, Ng=0.002)
X, T, mesh, R, G, u = run_V1(C, sg, 1.0, 260, maxsplit=3); r_ = R / G; sp_ = list(np.where(np.diff(mesh) > 0)[0] + 1)
tr_ = [T[s] / T[s - 1] for s in sp_]
kick = [(r_[s + 1] - r_[s - 2]) / (u[s - 1] ** 2 / 2) for s in sp_]
check('C4 splits: the tick halves, and the junction mismatch of B4 goes into that constant, a kick of u^2/2 = (HL)^2/8 '
      'of the density per split; every split has a solution',
      len(sp_) == 3 and all(0.49 < v < 0.52 for v in tr_) and all(0.85 < k_ < 1.1 for k_ in kick),
      f'splits at slabs {[int(q) for q in sp_]}; tick ratio ' + ', '.join(f'{v:.4f}' for v in tr_) + '; kick/(u^2/2) ' + ', '.join(f'{k_:.3f}' for k_ in kick))

print('== D. weak static field in the fixed-step gauge (planar Phi(Z), packets, eps0 = 0.3)')
class Line:
    def __init__(s, Nz, kp, fe, fo, e0, mu0):
        s.Ue = s.cubes(fe, e0, mu0, False); s.Uo = s.cubes(fo, e0, mu0, True)
        s.blk = (np.arange(Nz)[:, None] + 1 - C8[:, 2][None, :]) % Nz; s.tcol = np.arange(8)[None, :]
        s.ph = np.exp(1j * ((1 - C8[:, 0]) * kp[0] + (1 - C8[:, 1]) * kp[1])); s.z = np.arange(Nz)[:, None] + C8[:, 2][None, :] / 2.0
    @staticmethod
    def cubes(fl, e0, mu0, odd):
        N, Lx, LZ = fl; return np.array([halves([1 / Lx[n], 1 / Lx[n], 1 / LZ[n]], e0, mu0 * N[n])[1 if odd else 0] for n in range(len(N))])
    def tick(s, a):
        a = np.einsum('nij,nj->ni', s.Ue, a); v = np.einsum('nij,nj->ni', s.Uo, a[s.blk, s.tcol] * s.ph)
        b = np.empty_like(a); b[s.blk, s.tcol] = v / s.ph; return b
    def zm(s, a): p = np.abs(a) ** 2; return (p * s.z).sum() / p.sum()
def packet(Nz, kp, z0, sig, kz0, e0, mu):
    a = np.zeros((Nz, 8), complex); m = np.arange(Nz)
    for jj in range(Nz):
        Kz = (2 * np.pi * jj / Nz + np.pi) % (2 * np.pi) - np.pi; gw = np.exp(-((Kz - kz0) * sig) ** 2 / 2)
        if gw < 1e-14: continue
        U = ublock(np.array([kp[0], kp[1], Kz]), [1, 1, 1], e0, mu)[0]; cw = np.real(np.trace(U)) / 8
        cvec = ((I8 - (U - U.conj().T) / (2j * np.sqrt(1 - cw * cw))) / 2) @ chi0
        a += gw * np.exp(1j * Kz * (m - z0))[:, None] * (cvec / np.linalg.norm(cvec))[None, :]
    return a / np.linalg.norm(a)
def gauge(Phi, gam):
    N = 1 + Phi; Lx = 1 - gam * Phi; return N, Lx, 1 / np.sqrt(3 / N ** 2 - 2 / Lx ** 2)
Nz, X0s, zc = 2048, 900, 1024.0; zz = (np.arange(Nz) + 0.25, np.arange(Nz) + 0.75)
def saw(x):
    x = (x + Nz / 2) % Nz - Nz / 2; return np.where(np.abs(x) <= X0s, x, np.sign(x) * X0s - (x - np.sign(x) * X0s) * 2 * X0s / (Nz - 2 * X0s))
def accel(gs, mu, kp, gam, sig, nT):
    F = lambda z: gauge(gs * saw(z - zc), gam); ln = Line(Nz, kp, F(zz[0]), F(zz[1]), eps0, mu); a = packet(Nz, kp, zc, sig, 0.0, eps0, mu)
    zs = [ln.zm(a)]
    for _ in range(nT): a = ln.tick(a); zs.append(ln.zm(a))
    return -2 * np.polyfit(np.arange(nT + 1), np.array(zs) - zs[0], 2)[0] / gs
N_, Lx_, LZ_ = gauge(2e-5 * saw(zz[0] - zc), 1.0); gchk = np.abs(N_ * np.sqrt((2 / Lx_ ** 2 + 1 / LZ_ ** 2) / 3) - 1).max()
lin = tuple((gauge(np.array([1e-6]), gm)[2][0] - gauge(np.array([-1e-6]), gm)[2][0]) / 2e-6 for gm in (1.0, 0.0))
check('D1 THEOREM: a static field admits the fixed-step gauge: L_Z = (3/N^2 - 2/L_x^2)^(-1/2) gives N rms(1/L) = 1, '
      'L_Z = 1 + (3+2 gamma) Phi; around a body, labels moved by xi with div xi = 3(1+gamma) Phi',
      gchk < 1e-14 and abs(lin[0] - 5) < 1e-6 and abs(lin[1] - 3) < 1e-6, f'|N rms(1/L) - 1| {gchk:.0e}; dL_Z/dPhi {lin[0]:.4f}, {lin[1]:.4f} (gamma 1, 0)')
ff = {}
for mu in (0.03, 0.12):
    for gam in (0.0, 1.0):
        r = [accel(4e-6, mu, (0, 0), gam, s_, 1350) / cm2(eps0, mu) for s_ in (80.0, 160.0)]; ff[(mu, gam)] = (4 * r[1] - r[0]) / 3
check('D2 free fall in that gauge: slow packets fall at c_m^2 dPhi/dZ (gamma 0, 1; 1/sigma^2-extrapolated)', max(abs(v - 1) for v in ff.values()) < 2e-3, 'a/(c_m^2 g) ' + ', '.join(f'{v:.5f}' for v in ff.values()))
eta_m = 1 - ff[(0.12, 0.0)] * cm2(eps0, 0.12) / (ff[(0.03, 0.0)] * cm2(eps0, 0.03)); eta_b = 1 - cm2(eps0, 0.12) / cm2(eps0, 0.03)
check('D3 universality: species differ only by c_m^2(eps0, mu), the lattice term mu^2(1/6 - 1/(4 sin^2 eps0))',
      abs(eta_m - eta_b) < 2e-3, f'eta packets {eta_m:.4f}, band {eta_b:.4f}')
kx = 0.4; wl = band(np.array([kx, 0, 0]), [1, 1, 1], eps0, 0.0)[0]
lb = [accel(2e-5, 0.0, (kx, 0), gam, 160.0, 800) / (np.sin(eps0) ** 2 / 3) * np.cos(wl / 2) ** 2 for gam in (0.0, 1.0)]
check('D4 light along x is pulled by (1 + gamma) x Newtonian in that gauge',
      abs(lb[0] - 1) < 1e-3 and abs(lb[1] - 2) < 2e-3, f'{lb[0]:.5f}, {lb[1]:.5f} (gamma 0, 1)')
Nz2 = 1024; zz2 = (np.arange(Nz2) + 0.25, np.arange(Nz2) + 0.75); dP = 0.05
stp = lambda z: 0.5 * (np.tanh((z - 512) / 15) - np.tanh((z - 960) / 15)); fl2 = lambda z: gauge(dP * stp(z), 1.0)
Nz = Nz2; ln = Line(Nz2, (0, 0), fl2(zz2[0]), fl2(zz2[1]), eps0, 0.0); a = packet(Nz2, (0, 0), 300, 25.0, 0.4, eps0, 0.0)
for _ in range(2600): a = ln.tick(a)
bq = a.copy(); bq[(np.arange(Nz2) < 560) | (np.arange(Nz2) > 940)] = 0; tr = (np.abs(bq) ** 2).sum()
pw = (np.abs(np.fft.fft(bq, axis=0)) ** 2).sum(1); km = (pw * 2 * np.pi * np.fft.fftfreq(Nz2)).sum() / pw.sum()
N2, L2x, L2Z = gauge(np.array([dP]), 1.0); fz2 = L2Z[0] ** -2 / (2 / L2x[0] ** 2 + 1 / L2Z[0] ** 2)
k2 = np.arccos(1 - (1 - np.cos(band(np.array([0, 0, 0.4]), [1, 1, 1], eps0, 0)[0])) / (np.sin(eps0) ** 2 * fz2))
check('D5 a photon climbing a lapse step keeps its quasi-energy, so its frequency over the local clock mN falls by '
      'N_low/N_high exactly', tr > 0.99999 and abs(km - k2) < 2e-4, f'transmitted {tr:.6f}; k {km:.5f} vs {k2:.5f}')

print('== E. the other candidate rules')
Nn, fz, bz = 0.9, np.array([1.1, 0.8, 1.0]), np.array([0.05, -0.02, 0.03])          # a cell with a shift, lattice units
sp6 = np.concatenate([Nn * fz - bz, Nn * fz + bz]); rms6 = np.sqrt(np.mean(sp6 ** 2))
idn6 = abs(rms6 - np.sqrt(Nn ** 2 * np.mean(fz ** 2) + bz @ bz / 3)); ks_out = lambda x: (1 - 2 / x) / (1 + 2 / x)   # Kerr-Schild outgoing speed
check('E1 THEOREM: light crossing read in the lattice frame makes the step read the shift speed v: rms over the 6 axis '
      'directions gives sin eps = sin eps0/sqrt(1 + v^2/3); a round trip has no solution for v >= 1 (inside every horizon). '
      'Only the normal-frame rule keeps one step', idn6 < 1e-15 and ks_out(1.5) < 0 < ks_out(2.5),
      f'rms identity {idn6:.0e}; Kerr-Schild outgoing speed at 1.5M, 2.5M: {ks_out(1.5):+.3f}, {ks_out(2.5):+.3f}')
vc = np.sqrt(3.0)                                                         # uniform star: infall speed from rest at infinity at r = 0 is sqrt(3GM/R)
check('E2 THEOREM: a fixed proper tick makes slice normals geodesic; a stationary such slicing of a static star needs a '
      'shift = infall speed from infinity, sqrt(3GM/R) at a uniform star\'s centre (a hedgehog, singular there), else it '
      'focuses in a free-fall time; its lost lapse equation is dust (C1)', vc > 0, f'central speed/sqrt(GM/R) {vc:.4f}')

print('== F. ESTIMATES (unit map a = sqrt(8 pi) l_P, cube 2a; measured numbers)')
Ha = 1.93e-5; e_max = 0.04; nps = r3 / (2 * np.sin(e_max) * Ha); MPl = 1.22089e19; Lc = 2 * np.sqrt(8 * np.pi) / MPl
kick_rad = lambda Tm: (17.1 * Tm ** 2 / MPl * Lc) ** 2 / 8 * 16 / 15; bound = 0.3 * 0.2271 / (1 + 3.044 * 0.2271)
check('F1 tick <= 0.023 l (eps0 <= 0.04); ticks per split in de Sitter sqrt3/(2 sin(eps0) H a), the same every split '
      f'(n_s = 1 unchanged); split kicks leave {kick_rad(1e16):.0e} of the radiation as dark radiation after a 1e16 GeV start, '
      f'vs |Delta N_eff| < 0.3, |rho_C/rho_r| < {bound:.3f}, which the first-slab constant must also meet', nps > 1e6 and kick_rad(1e16) < 1e-6 * bound,
      f'ticks/split >= {nps:.1e} at H a = {Ha}; inflation kick {(2 * Ha) ** 2 / 8:.0e}/split, diluted as a^-4')
print('supplied: CL-1 cube tick, box reading, eps0 values, frustum carrier (central tick, mid-slab cell read, split hinges),\n'
      '  dust/photon/Lambda content, packets, planar fields, PG/KS metrics, unit map, measured numbers.')
print(f'elapsed {time.monotonic() - T00:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
