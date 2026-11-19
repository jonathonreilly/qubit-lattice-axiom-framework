#!/usr/bin/env python3
"""ltb-crush: spherically symmetric (Lemaitre-Tolman-Bondi / Oppenheimer-Snyder) dust collapse on a radial chain of
box-frustum cells under CL-1's fixed-step tick per cube and CL-3 stationarity in the edges.
Supplied models; exact identities, finite diagnostics and estimates; no physical identification.
Carrier (comoving, shift-free, conforming): shells R_1..R_K; cell c between R_c and R_{c+1} (R_0 = 0) has radial edge
a_c = R_{c+1} - R_c and two transverse edges b_c = th_c (R_c + R_{c+1})/2 (th_c fixed: cubes at the start), weight
n_c = 1/th_c^2 angular copies, dust M_c at rest in the cell, Lorentzian box-frustum Regge slabs, tick per cell
T_c = sin(eps0)/sqrt(1/m_a^2 + 2/m_b^2) (CL-1; mid read).
 A  the carrier: kinetic identity, Schlaefli, homogeneous degeneracy of the edge equations, free-lapse control = LTB
 B  CL-1 fixed tick: homogeneous OK; inhomogeneous dark constants made at a rate independent of eps0; OS fold
 C  a free-radial-edge carrier with a supplied curvature potential: unstable in flat space (not used)
 D  estimates against measurement
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
from scipy.optimize import least_squares
np.seterr(all='ignore')
T00 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ''))

PAIRS = ((0, 1, 2), (1, 2, 0), (2, 0, 1))
def lapse(l, lp, sE): m = (l + lp) / 2; return sE / np.sqrt(np.sum(1 / m ** 2))
def slabT(l, lp, T, M=0.0):
    m = (l + lp) / 2; u = (lp - l) / (2 * T); S = -M * T
    for i, j, k in PAIRS:
        h = np.sqrt(1 - u[j] ** 2 - u[k] ** 2); w = u[j] * u[k] / np.sqrt((1 - u[j] ** 2) * (1 - u[k] ** 2))
        S = S + m[i] * T * h * 4 * np.arcsin(w)
    return S, u
def S_loc(l0, l1, l2, sE, M, T0=None, T1=None):
    T0 = lapse(l0, l1, sE) if T0 is None else T0; T1 = lapse(l1, l2, sE) if T1 is None else T1
    s0, u0 = slabT(l0, l1, T0, M); s1, u1 = slabT(l1, l2, T1, M)
    S = s0 + s1 + sum(2 * l1[j] * l1[k] * (np.arctanh(u1[i]) - np.arctanh(u0[i])) for i, j, k in PAIRS)
    return S + sum(2 * l0[j] * l0[k] * np.arctanh(u0[i]) - 2 * l2[j] * l2[k] * np.arctanh(u1[i]) for i, j, k in PAIRS)
def slab_full(l, lp, T, M=0.0):
    s, u = slabT(l, lp, T, M); return s + sum(2 * (l[j] * l[k] - lp[j] * lp[k]) * np.arctanh(u[i]) for i, j, k in PAIRS)
def energy_formula(l, lp, T, M):
    u = (lp - l) / (2 * T); m = (l + lp) / 2; E = -M
    for i, j, k in PAIRS:
        h = np.sqrt(1 - u[j] ** 2 - u[k] ** 2); w = u[j] * u[k] / np.sqrt((1 - u[j] ** 2) * (1 - u[k] ** 2)); E += 4 * m[i] * np.arcsin(w) / h
    return E
def cgrad(f, x, h=1e-30):
    g = np.zeros(len(x))
    for a in range(len(x)):
        d = np.zeros(len(x), complex); d[a] = 1j * h; g[a] = f(x + d).imag / h
    return g

class Chain:
    def __init__(s, R0, M, sE):
        s.R0 = np.asarray(R0, float); s.K = len(R0); s.M = np.asarray(M, float); s.sE = sE
        Rf = np.concatenate([[0.0], s.R0]); s.th = (Rf[1:] - Rf[:-1]) / ((Rf[1:] + Rf[:-1]) / 2); s.n = 1 / s.th ** 2
    def edges(s, R):
        Rf = np.concatenate([[0.0], R]); a = Rf[1:] - Rf[:-1]; b = s.th * (Rf[1:] + Rf[:-1]) / 2
        return [np.array([a[c], b[c], b[c]]) for c in range(s.K)]
    def resid(s, Rm, R, Rp, Tm=None, T=None):
        e0, e1, e2 = s.edges(Rm), s.edges(R), s.edges(Rp); F = np.zeros(s.K)
        for c in range(s.K):
            t0 = None if Tm is None else Tm[c]; t1 = None if T is None else T[c]
            g = cgrad(lambda x: S_loc(e0[c].astype(complex), x, e2[c].astype(complex), s.sE, s.M[c], t0, t1), e1[c].astype(complex)) * s.n[c]
            ga, gb = g[0], (g[1] + g[2]) * s.th[c] / 2; F[c] += ga + gb
            if c > 0: F[c - 1] += -ga + gb
        return F
    def lapses(s, Ra, Rb): return np.array([lapse(x, y, s.sE) for x, y in zip(s.edges(Ra), s.edges(Rb))])
    def energies(s, Ra, Rb, T=None):
        T = s.lapses(Ra, Rb) if T is None else T
        return np.array([energy_formula(x, y, t, m) for x, y, t, m in zip(s.edges(Ra), s.edges(Rb), T, s.M)])
    def valid(s, Ra, Rb, T=None):
        if np.any(np.diff(np.concatenate([[0.0], Rb])) <= 0): return False
        T = s.lapses(Ra, Rb) if T is None else T
        if np.any(T <= 0): return False
        for x, y, t in zip(s.edges(Ra), s.edges(Rb), T):
            u = (y - x) / (2 * t)
            if not (1 - 2 * u[1] ** 2 > 0 and 1 - u[0] ** 2 - u[1] ** 2 > 0): return False
        return True
    def scale(s, R, Rp):
        e1 = s.edges(R); T = s.lapses(R, Rp); v = s.n * np.array([e[1] ** 2 for e in e1]) / T
        return np.maximum(v, np.concatenate([v[1:], [0]]))
def newton(F, valid, x, tol=1e-11, it=60):
    e = np.inf
    for _ in range(it):
        F0 = F(x); e = np.max(np.abs(F0))
        if e < tol: return True, x, e
        J = np.zeros((len(F0), len(x)))
        for q in range(len(x)):
            xp = x.copy(); dx = 1e-8 * max(1.0, abs(x[q])); xp[q] += dx; J[:, q] = (F(xp) - F0) / dx
        dx = np.linalg.lstsq(J, -F0, rcond=None)[0]; t = 1.0
        while t > 1e-12:
            xn = x + t * dx
            if valid(xn):
                f = F(xn)
                if np.all(np.isfinite(f)) and np.max(np.abs(f)) < e: break
            t /= 2
        if t <= 1e-12: return e < 1e-8, x, e
        x = xn
    return e < 1e-8, x, e
def setup(prof, sE, M0=0.0075):
    K = len(prof); R0 = np.arange(1, K + 1, dtype=float); M = M0 * np.asarray(prof, float); ch = Chain(R0, M, sE)
    m2 = np.cumsum(M / ch.th ** 2); T0 = sE / np.sqrt(3)
    ok, R1, e = newton(lambda R1: ch.energies(R0, R1) / M0, lambda R1: ch.valid(R0, R1), R0 - np.sqrt(m2 / R0) * T0)
    return ch, [R0, R1], m2, ok
def evolve(ch, L, nt):
    for n in range(nt):
        Rm, R = L[-2], L[-1]; g = 2 * R - Rm; sc = ch.scale(R, g)
        ok, Rp, e = newton(lambda Rp: ch.resid(Rm, R, Rp) / sc, lambda Rp: ch.valid(R, Rp), g)
        if not ok: return ('fold', n, e)
        L.append(Rp)
    return ('ok', nt)

print('== A. the comoving shell chain (exact algebra; sub-Hubble small-u limit of the box slab is -T x Bianchi I kinetic)')
x, y, xd, yd, th = sp.symbols('x y xd yd theta', positive=True)
a_, b_, ad, bd = y - x, th * (x + y) / 2, yd - xd, th * (xd + yd) / 2
idn = sp.simplify((2 * ad * bd * b_ + bd ** 2 * a_) / th ** 2 - (y * yd ** 2 - x * xd ** 2 - a_ * ad ** 2 / 4))
check('A1 THEOREM: n_c (2 adot bdot b + bdot^2 a) = Delta(R Rdot^2) - a adot^2/4 exactly (a = Delta R, b = th Rbar, n = 1/th^2): '
      'each cell\'s kinetic term is the jump of the Misner-Sharp function R Rdot^2 = 2m across it, up to a lattice term; '
      'with a uniform lapse the chain kinetic term telescopes to the outer shell, so the bulk edge equations carry no LTB content',
      idn == 0, f'sympy residual {idn}')
rng = np.random.default_rng(20261022); dev = 0
for _ in range(5):
    l = rng.uniform(0.5, 2, 3); u = rng.uniform(-0.4, 0.4, 3); T = rng.uniform(0.01, 0.1); lp = l + 2 * u * T; Mx = rng.uniform(0, 1)
    cs = slab_full(l.astype(complex), lp.astype(complex), T + 1e-30j, Mx).imag / 1e-30; dev = max(dev, abs(cs - energy_formula(l, lp, T, Mx)) / abs(cs))
check('A2 THEOREM (Schlaefli): a cell\'s lapse equation is dS/dT = -M + sum_i 4 m_i asin(w_i)/h_i; with the CL-1 tick its value '
      'is the cell\'s dark constant (zero = the GR constraint of that cell)', dev < 1e-9, f'complex step vs formula {dev:.0e}')
ch = Chain(np.arange(1, 9, dtype=float), np.full(8, 0.0075), 0.1); R = ch.R0; inner = []; outer = []
for lam0, lam in ((0.998, 0.995), (1.003, 0.99), (0.99, 1.004)):
    F = ch.resid(lam0 * R, R, lam * R) / ch.scale(R, lam * R); inner.append(np.max(np.abs(F[:-1]))); outer.append(abs(F[-1]))
check('A3 THEOREM (A1, isotropic cells): F_i = (i^2 - 1/4)(g_{i-1} - g_i), so on any homogeneous slice every inner edge '
      'equation holds identically for any next slice R -> lam R; only the outer shell fixes lam (bulk degeneracy)',
      max(inner) < 1e-10 and min(outer) > 1e-4, f'inner |F| max {max(inner):.0e} for 3 non-stationary lam; outer |F| min {min(outer):.1e}')
# free-lapse control (per-cell lapse equations kept)
sE = 0.1; prof = [1.0] * 6 + [0.0] * 4; K = 10; ch = Chain(np.arange(1, K + 1, dtype=float), 0.0075 * np.array(prof), sE)
m2 = np.cumsum(ch.M / ch.th ** 2); R0 = ch.R0; T0 = np.full(K, sE / np.sqrt(3))
ok, R1, e = newton(lambda R1: ch.energies(R0, R1, T0) / 0.0075, lambda R1: ch.valid(R0, R1, T0), R0 - np.sqrt(m2 / R0) * T0)
L = [R0, R1]; TT = [T0]
for n in range(8):
    Rm_, Rc, Tm = L[-2], L[-1], TT[-1]
    def Fc(z):
        Rp, T = z[:K], z[K:]; return np.concatenate([ch.resid(Rm_, Rc, Rp, Tm, T) / ch.scale(Rc, Rp), ch.energies(Rc, Rp, T) / 0.0075])
    ok, z, e = newton(Fc, lambda z: ch.valid(Rc, z[:K], z[K:]), np.concatenate([2 * Rc - Rm_, Tm]), tol=1e-9)
    if not ok: break
    L.append(z[:K]); TT.append(z[K:])
tau = np.sum(TT, axis=0); Rl = np.maximum(R0 ** 1.5 - 1.5 * np.sqrt(m2) * tau, 0) ** (2 / 3); dev = np.max(np.abs(L[-1] / Rl - 1))
spread = np.max(np.abs(TT[-1] / TT[-1][0] - 1))
check('A4 DIAGNOSTIC (control: lapse varied per cell, as GR): the chain follows Oppenheimer-Snyder / LTB E = 0 inside and '
      'Lemaitre free fall outside, with the solved lapse uniform across cells (synchronous, as comoving dust needs)',
      ok and dev < 5e-3 and spread < 1e-3, f'{len(TT)} slabs; max |R/R_LTB - 1| {dev:.1e}; lapse spread {spread:.0e}; dR/R {1 - L[-1][0] / R0[0]:.3f}')

print('== B. CL-1 fixed tick per cube (lapse not varied)')
ch, L, m2, ok = setup([1.0] * 8, 0.1); info = evolve(ch, L, 100); E = ch.energies(L[-2], L[-1])
check('B1 DIAGNOSTIC: homogeneous dust (all cells alike) follows the cubic-frustum carrier: every cell\'s dark constant stays zero',
      info[0] == 'ok' and np.max(np.abs(E)) < 1e-9 * 0.0075 + 1e-12, f'{info}; max|E| {np.max(np.abs(E)):.0e}; R/R0 {L[-1][0] / L[0][0]:.4f}')
rates = {}
for con in (0.01, 0.1):
    for s in (0.1, 0.01):
        ch, L, m2, ok = setup([1.0] * 6 + [1 - con] * 4, s); evolve(ch, L, 3); E = ch.energies(L[-2], L[-1])
        rates[(con, s)] = E[0] / (0.0075 * np.sqrt(0.0075 / 3) * 3 * s / np.sqrt(3))
r = rates
check('B2 DIAGNOSTIC: a density step of contrast d makes per-cell dark constants at dE/dtau = c d M H with c ~ 85 independent of '
      'eps0 (a continuum effect, not a lattice-scale one): the lost lapse equations are not recovered, and dark constants flow '
      'between cells (core +, exterior -)', abs(r[(0.01, 0.1)] / r[(0.01, 0.01)] - 1) < 0.05 and abs(r[(0.1, 0.01)] / r[(0.01, 0.01)] / 10 - 1) < 0.05,
      'E/(M H tau): ' + ', '.join(f'd {k[0]} sinE {k[1]}: {v:.2f}' for k, v in r.items()))
ch, L, m2, ok = setup([1.0] * 6 + [0.0] * 4, 0.1); info = evolve(ch, L, 10); Ecore = ch.energies(L[-2], L[-1])[0] / 0.0075
Rm_, Rc = L[-2], L[-1]; sc = ch.scale(Rc, 2 * Rc - Rm_)
def Fr(xx):
    Rp = Rc * np.exp(xx)
    return ch.resid(Rm_, Rc, Rp) / sc if ch.valid(Rc, Rp) else np.full(ch.K, 1e3)
roots = []; nearmin = []
for t in range(30):
    x0 = np.log((2 * Rc - Rm_) / Rc) + rng.normal(0, 0.003 * (1 + t / 8), ch.K)
    if not ch.valid(Rc, Rc * np.exp(x0)): continue
    sol = least_squares(Fr, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=300); res_ = np.max(np.abs(sol.fun))
    (roots if res_ < 1e-9 else nearmin).append((res_, sol.x))
uniq = []
for rr in roots:
    if all(np.max(np.abs(rr[1] - q[1])) > 1e-6 for q in uniq): uniq.append(rr)
ext = np.log((2 * Rc - Rm_) / Rc)
def vol(Rp): return sum(ch.n[c] * e[0] * e[1] ** 2 for c, e in enumerate(ch.edges(Rp)))
def act(Rp): return sum(ch.n[c] * S_loc(e0, e1, e2, ch.sE, ch.M[c]) for c, (e0, e1, e2) in enumerate(zip(ch.edges(Rm_), ch.edges(Rc), ch.edges(Rp))))
rows = [(np.max(np.abs(q[1] - ext)), act(Rc * np.exp(q[1])), vol(Rc * np.exp(q[1])), q[1]) for q in uniq]
picks = (int(np.argmin([w[0] for w in rows])), int(np.argmin([abs(w[1]) for w in rows])), int(np.argmax([w[2] for w in rows]))) if rows else ()
check('B3 DIAGNOSTIC (Oppenheimer-Snyder step, sinE 0.1): the continued root meets a fold within a few ticks (core dark constant '
      'already O(M)); stationary points still exist elsewhere, so CL-1\'s clause does not act, but no root is near the extrapolated '
      'slice; the three selection rules (nearest / smallest |S| / largest volume) are tested on the roots found',
      info[0] == 'fold' and len(uniq) >= 1 and Ecore > 1,
      f'{info[:2]}; E_core/M {Ecore:.1f}; roots {len(uniq)}, root jumps max|dlnR - extrap| {min(w[0] for w in rows):.1e}..{max(w[0] for w in rows):.1e} (one tick moves dlnR {np.max(np.abs(ext)):.1e}); picks (near, |S|, vol) {picks}; near-misses {len(nearmin)}')

print('== C. a free-radial-edge carrier (a_c independent; supplied potential T(a - dR^2/a) - (T_j+T_j+1) R_j (rho_j+1 - rho_j))')
PAIR = PAIRS
def slab_cell(e, ep, T, M):
    s, u = slabT(e, ep, T, M); return s + sum(2 * (e[j] * e[k] - ep[j] * ep[k]) * np.arctanh(u[i]) for i, j, k in PAIR)
class Free:
    def __init__(s, K, sE, T=None):
        s.K = K; R0 = np.arange(1, K + 1, dtype=float); Rf = np.concatenate([[0.0], R0]); s.th = 1 / ((Rf[1:] + Rf[:-1]) / 2)
        s.n = 1 / s.th ** 2; s.sE = sE; s.Tfix = T; s.X0 = np.concatenate([R0, np.ones(K)])
    def S(s, X, Xp):
        K = s.K; R, a = X[:K], X[K:]; Rp, ap = Xp[:K], Xp[K:]
        f = lambda R_: np.concatenate([[0.0], R_]); dR, dRp = np.diff(f(R)), np.diff(f(Rp))
        b, bp = s.th * (f(R)[1:] + f(R)[:-1]) / 2, s.th * (f(Rp)[1:] + f(Rp)[:-1]) / 2
        T = s.sE / np.sqrt(1 / ((a + ap) / 2) ** 2 + 2 / ((b + bp) / 2) ** 2) if s.Tfix is None else s.Tfix + 0 * a
        am, dRm, Rm = (a + ap) / 2, (dR + dRp) / 2, (R + Rp) / 2; rho = dRm / am; out = 0
        for c in range(K):
            out = out + s.n[c] * slab_cell(np.array([a[c], b[c], b[c]]), np.array([ap[c], bp[c], bp[c]]), T[c], 0.0) + T[c] * (am[c] - dRm[c] ** 2 / am[c])
        for j in range(K - 1): out = out - (T[j + 1] + T[j]) * Rm[j] * (rho[j + 1] - rho[j])
        return out - 2 * T[K - 1] * Rm[K - 1] * (1.0 - rho[K - 1])
def free_run(fr, kick, nt):
    K = fr.K; fv = [q for q in range(2 * K) if q not in (K - 1, 2 * K - 1)]; X0 = fr.X0; X1 = X0.copy(); X1[3] += kick; L = [X0, X1]
    for n in range(nt):
        Xm, X = L[-2], L[-1]
        def F(yv):
            Xp = X.copy(); Xp[fv] = yv
            return np.array([(fr.S(Xm.astype(complex), X + 1e-30j * np.eye(2 * K)[q]) + fr.S(X + 1e-30j * np.eye(2 * K)[q], Xp.astype(complex))).imag / 1e-30 for q in fv])
        ok, yv, e = newton(F, lambda yv: True, (2 * X - Xm)[fv], tol=1e-12)
        if not ok: return L, ('fail', n)
        Xp = X.copy(); Xp[fv] = yv; L.append(Xp)
    return L, ('ok', nt)
fr = Free(8, 0.2); L0, i0 = free_run(fr, 0.0, 4); fr2 = Free(8, 0.2, T=0.2 / np.sqrt(3)); L1, i1 = free_run(fr2, 1e-4, 12)
gr = [np.max(np.abs(x - fr2.X0)) for x in L1]
check('C1 DIAGNOSTIC (negative, carrier not used): flat space is an exact static solution, but a 1e-4 kick of one shell grows '
      'by about x2 per tick even with a constant lapse, so the supplied potential discretisation (not CL-1) is unstable; a '
      'Regge spatial-curvature carrier (frustum cells, radial hinges) is still to be built', max(np.max(np.abs(x - fr.X0)) for x in L0) == 0 and gr[-1] > 1e2 * gr[2],
      f'static drift 0; kick growth |dX| at ticks 2/6/{len(gr) - 1}: {gr[2]:.1e}/{gr[6]:.1e}/{gr[-1]:.1e}; {i1}')

print('== D. ESTIMATES (measured inputs; cube 2 sqrt(8 pi) l_P)')
s4, vrel = np.sin(0.04), 0.1; ru = (1 - s4 * vrel / 2) / (1 + s4 * vrel / 2); n30 = np.log(1e30) / np.log(1 / ru)
check('D1 ESTIMATE shell crossing on one cell (kasner-crush C2 applied to the cell between crossing shells, NOT computed on a '
      'chain): the radial face speed is half the relative shell speed, the tick reads the shrinking radial edge, so the edge '
      'falls by (1 - s u)/(1 + s u) per tick, the crossing lies at no finite tick and the cell freezes in proper time (sticky '
      'shells, not crossing streams); valid only on a chain whose fixed-tick dynamics is LTB, which B2 says this one is not',
      0 < ru < 1, f'sin eps0 0.04, v_rel 0.1 c: ratio {ru:.6f}/tick, {n30:.1e} ticks to shrink the edge by 1e30')
Om_dm, Om_b, Om_bh = 0.264, 0.0493, 1.5e-4
check('D2 crushed cubes inside horizons add no separate dark population: a remnant\'s mass is part of its hole\'s; stellar-collapse '
      'holes hold Omega ~ 1e-4, below Omega_DM by > 1e3, so remnants of astrophysical collapse cannot be the dark matter; '
      'primordial collapse keeps the register\'s exp(-2.4e8) fraction', Om_dm / Om_bh > 1e3, f'Omega_DM/Omega_BH,stellar {Om_dm / Om_bh:.0e}; DM/baryon {Om_dm / Om_b:.2f}')
print('supplied: comoving shift-free conforming shell chain (a = Delta R), box-frustum cells with angular weights, dust at rest')
print('  in its cell, mid tick read, zero initial dark constants, kappa = 1; section C potential; measured Omega values.')
print(f'elapsed {time.monotonic() - T00:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
