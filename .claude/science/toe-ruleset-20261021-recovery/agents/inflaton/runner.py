#!/usr/bin/env python3
"""Is there a field in the register's rules that can roll? (supplied models; finite diagnostics; no physical identification)
 A  target: tensor bound and lattice decoupling; Starobinsky (Hubble-flow 2nd order + Mukhanov-Sasaki); classic shapes
 B  (a) curvature squared: Schlaefli locality of the hinge sum (second-order recursion, no scalaron datum) vs a discrete
    R^2 term; the lattice remainder is first-derivative, de Sitter is R^2-blind but not lattice-blind; one-loop R^2
    coefficients of the rules' content (heat kernel)
 C  (b) condensates: the isotropic colour-link condensate (quartic below the cell, compact hilltop at the cell)
 D  (c) the step: the sea's vacuum phase is its only would-be potential and CL-3 removes it; without the 4-volume clause
    the discrete carrier fixes the tick weakly (T l ~ const); H carries no eps
 E  (d) copy mass: no equation of motion; a periodic would-be potential is natural inflation
 F  what any inflaton needs from the rules: the empty vacuum cannot hold today's baryons; local splits heat the sea
 G  replacement (not adopted): curvature squared per proper 4-volume; lapse equation; Jordan frame; reheating; predictions
 H  look-elsewhere
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import cmath, math, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import warnings
warnings.filterwarnings('ignore')

T0 = time.monotonic(); PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


MP = 2.435e18                                   # GeV; reduced Planck mass = 1/a (unit map: G = a^2/(8 pi) per cell)
As_m, dAs = 2.100e-9, 0.030e-9; ns_m, dns = 0.9649, 0.0042; r_max = 0.036; als_m, dals = -0.0045, 0.0067
C_SR = -2 + math.log(2) + 0.5772156649

print('== A. target')
Hmax = math.sqrt(r_max * As_m * math.pi ** 2 / 2); Vmax = 3 * Hmax ** 2
check('A1 tensor bound: H a < %.2e, V < %.1e M_P^4 (V^1/4 < %.1e GeV); every cell-scale term enters at <= (Ha)^2 = %.1e'
      % (Hmax, Vmax, Vmax ** 0.25 * MP, Hmax ** 2), Hmax < 2e-5 and Vmax < 1.2e-9)
s23 = math.sqrt(2 / 3)
def Vs(p): return 0.75 * (1 - math.exp(-s23 * p)) ** 2          # Starobinsky, M = 1 (V scales as M^2)
def dVs(p): y = math.exp(-s23 * p); return 1.5 * (1 - y) * s23 * y
def bg(N, s): p, pn = s; e = pn * pn / 2; return [pn, -(3 - e) * (pn + dVs(p) / Vs(p))]
def endev(N, s): return s[1] ** 2 / 2 - 1
endev.terminal = True
BG = solve_ivp(bg, (0, 300), [6.0, -dVs(6.0) / Vs(6.0)], events=endev, rtol=1e-11, atol=1e-13, dense_output=True, method='DOP853')
NEND = BG.t_events[0][0]; PEND = BG.y_events[0][0][0]
def flow(Ns, h=1e-3):
    N = NEND - Ns; e1f = lambda n: BG.sol(n)[1] ** 2 / 2
    def e2f(n): l = [math.log(e1f(n + k * h)) for k in (-2, -1, 1, 2)]; return (l[0] - 8 * l[1] + 8 * l[2] - l[3]) / (12 * h)
    e1, e2 = e1f(N), e2f(N); e3 = (math.log(e2f(N + h)) - math.log(e2f(N - h))) / (2 * h)
    p = BG.sol(N)[0]; H2 = Vs(p) / (3 - e1)
    ns = 1 - 2 * e1 - e2 - 2 * e1 ** 2 - (2 * C_SR + 3) * e1 * e2 - C_SR * e2 * e3
    r = 16 * e1 * (1 + C_SR * e2); al = -2 * e1 * e2 - e2 * e3
    P1 = H2 / (8 * math.pi ** 2 * e1) * (1 - 2 * (C_SR + 1) * e1 - C_SR * e2)
    return dict(ns=ns, r=r, als=al, M=math.sqrt(As_m / P1), V=Vs(p), e1=e1)
def ms_spec(Ns):                                # Mukhanov-Sasaki, e-fold time, Bunch-Davies at k = 200 aH
    Nx = NEND - Ns; p, pn = BG.sol(Nx); k = math.exp(Nx) * math.sqrt(Vs(p) / (3 - pn * pn / 2))
    aH = lambda n: math.exp(n) * math.sqrt(Vs(BG.sol(n)[0]) / (3 - BG.sol(n)[1] ** 2 / 2))
    def rhs(n, s):
        pp, ppn = BG.sol(n); ee = ppn * ppn / 2; ppnn = -(3 - ee) * (ppn + dVs(pp) / Vs(pp)); q = (k / aH(n)) ** 2; fr = 3 - ee + 2 * ppnn / ppn
        return [s[2], s[3], -fr * s[2] - q * s[0], -fr * s[3] - q * s[1], s[6], s[7], -(3 - ee) * s[6] - q * s[4], -(3 - ee) * s[7] - q * s[5]]
    Ni = Nx - math.log(200.0); pp, ppn = BG.sol(Ni); ee = ppn * ppn / 2; ppnn = -(3 - ee) * (ppn + dVs(pp) / Vs(pp))
    a0 = math.exp(Ni); z0 = a0 * abs(ppn); v0 = 1 / math.sqrt(2 * k); vn0 = -1j * k * v0 / aH(Ni)
    R0 = v0 / z0; Rn0 = (vn0 - v0 * (1 + ppnn / ppn)) / z0; h0 = v0 / a0; hn0 = (vn0 - v0) / a0
    so = solve_ivp(rhs, (Ni, Nx + 8), [R0.real, R0.imag, Rn0.real, Rn0.imag, h0.real, h0.imag, hn0.real, hn0.imag], rtol=1e-9, atol=1e-30, method='DOP853')
    return k, k ** 3 * (so.y[0, -1] ** 2 + so.y[1, -1] ** 2) / (2 * math.pi ** 2), 4 * k ** 3 * (so.y[4, -1] ** 2 + so.y[5, -1] ** 2) / math.pi ** 2
F55 = flow(55); (ka, Pa, _), (kb, Pb, _), (_, P0, Pt0) = ms_spec(54.9), ms_spec(55.1), ms_spec(55.0)
ns_ms = 1 + math.log(Pb / Pa) / math.log(kb / ka); r_ms = Pt0 / P0
check('A2 Starobinsky, N* = 55: n_s %.5f, r %.5f (2nd-order Hubble flow) = Mukhanov-Sasaki %.5f, %.5f; M = %.3e M_P, R^2 '
      'coefficient c = M_P^2/(12 M^2) = %.2e (measured-input target)' % (F55['ns'], F55['r'], ns_ms, r_ms, F55['M'], 1 / (12 * F55['M'] ** 2)),
      abs(F55['ns'] - ns_ms) < 2e-4 and abs(F55['r'] / r_ms - 1) < 0.02 and 4e8 < 1 / (12 * F55['M'] ** 2) < 7e8)
fs = np.linspace(0.5, 200, 20000)[:, None]; NN = np.array([50.0, 55.0, 60.0])[None, :]
s2 = (2 * fs ** 2 / (1 + 2 * fs ** 2)) * np.exp(-NN / fs ** 2); t2 = s2 / (1 - s2); nsN = 1 - (1 + 2 * t2) / fs ** 2; rN = 8 * t2 / fs ** 2
okN = (abs(nsN - ns_m) < 2 * dns) & (rN < r_max); rmin = rN[nsN > ns_m - 2 * dns].min()
shapes = {'phi^2': (2, 8), 'phi': (1.5, 4), 'phi^2/3': (4 / 3, 8 / 3)}
pw = {k: [(1 - a / N, b / N) for N in (50, 55, 60)] for k, (a, b) in shapes.items()}
okp = [k for k, v in pw.items() if any(abs(n_ - ns_m) < 2 * dns and r_ < r_max for n_, r_ in v)]
check('A3 shapes at N 50-60 (n_s within 2 sigma and r < 0.036): phi^2, phi, phi^(2/3) fail on r (%.3f, %.3f, %.3f at 55); natural '
      'inflation fails for every f (least r at n_s >= -2 sigma: %.3f); Starobinsky passes: the data need a flattened potential'
      % (pw['phi^2'][1][1], pw['phi'][1][1], pw['phi^2/3'][1][1], rmin), not okp and not okN.any() and rmin > r_max)

print('== B. (a) curvature squared in the hinge sum')
def hinge_S(ls, Ts):                            # cubic frustum per cell, kappa = 1 (carrier of agents/cosmology)
    us = [(ls[n + 1] - ls[n]) / (2 * Ts[n]) for n in range(len(Ts))]
    S = sum(3 * ls[n] ** 2 * 2 * (cmath.atanh(us[n]) - cmath.atanh(us[n - 1])) for n in range(1, len(ls) - 1))
    return S + sum(1.5 * (ls[n] + ls[n + 1]) * Ts[n] * cmath.sqrt(1 - 2 * us[n] ** 2) * 4 * cmath.asin(us[n] ** 2 / (1 - us[n] ** 2)) for n in range(len(Ts)))
def R2_S(ls, Ts):                               # supplied discrete sum_n V_n R_n^2, R = 6(l''/l + l'^2/l^2)
    S = 0
    for n in range(1, len(ls) - 1):
        T = 0.5 * (Ts[n - 1] + Ts[n]); lp = (ls[n + 1] - ls[n - 1]) / (2 * T); lpp = (ls[n + 1] - 2 * ls[n] + ls[n - 1]) / T ** 2
        S += ls[n] ** 3 * T * (6 * (lpp / ls[n] + (lp / ls[n]) ** 2)) ** 2
    return S
def eom(Sf, ls, Ts, n):
    lc = [complex(x) for x in ls]; lc[n] += 1e-20j; return Sf(lc, Ts).imag / 1e-20
rng = np.random.default_rng(1); LS = list(1.0 + np.cumsum(0.02 + 0.01 * rng.random(9))); TS = list(0.2 + 0.02 * rng.random(8)); n0 = 4
dep = {}
for lab, Sf in (('hinge', hinge_S), ('R2', R2_S)):
    b0 = eom(Sf, LS, TS, n0); dl = {}
    for m in (n0 - 2, n0 - 1, n0 + 1, n0 + 2):
        l2 = list(LS); l2[m] += 1e-3; dl[m - n0] = abs(eom(Sf, l2, TS, n0) - b0) / 1e-3
    for m in (n0 - 2, n0 + 1):
        T2 = list(TS); T2[m] += 1e-3; dl['T%+d' % (m - n0)] = abs(eom(Sf, LS, T2, n0) - b0) / 1e-3
    dep[lab] = dl
check('B1 THEOREM (Schlaefli) + check: the hinge-sum edge equation at slice n involves only l_n-1..n+1 and T_n-1, T_n (second-order '
      'recursion: no extra datum, no scalaron); a curvature-squared term reaches l_n+-2 (fourth order: the scalaron datum)',
      max(dep['hinge'][2], dep['hinge'][-2], dep['hinge']['T-2'], dep['hinge']['T+1']) == 0 and min(dep['hinge'][1], dep['hinge'][-1]) > 1
      and min(dep['R2'][2], dep['R2'][-2]) > 1, 'hinge |d/dl_n+-2| = %.0e, %.0e vs %.1f; R^2: %.0f' % (dep['hinge'][2], dep['hinge'][-2], dep['hinge'][1], dep['R2'][2]))
u, H, al, rho = sp.symbols('u H alpha rho', positive=True)
fL = sp.series(-24 * u * sp.atanh(u) + 12 * sp.sqrt(1 - 2 * u ** 2) * sp.asin(u ** 2 / (1 - u ** 2)), u, 0, 9).removeO()
Aser = sp.series(sp.asin(u ** 2 / (1 - u ** 2)) / sp.sqrt(1 - 2 * u ** 2), u, 0, 7).removeO()
Rv = 12 * H ** 2; dS00 = sp.simplify(3 * (1 + 2 * al * Rv) * H ** 2 - ((1 + 2 * al * Rv) * Rv - Rv - al * Rv ** 2) / 2 - rho)
check('B2 THEOREM: the slab Lagrangian is l f(u), f = %s (u = ldot/2: first derivatives only), and the hinge Friedmann law '
      'A(u) = u^2 + 2u^4 + ... shifts de Sitter by dH^2/H^2 = -(Hl)^2/2 <= %.0e; f(R) = R + aR^2 leaves de Sitter unshifted '
      '(3H^2 = rho, a drops out): the lattice remainder is not R^2' % (str(fL).replace(' ', ''), 2 * Hmax ** 2),
      sp.expand(fL + 12 * u ** 2 + 8 * u ** 4 + sp.Rational(44, 5) * u ** 6 + sp.Rational(80, 7) * u ** 8) == 0 and sp.expand(Aser - u ** 2 - 2 * u ** 4) == sp.Rational(11, 3) * u ** 6 and sp.simplify(dS00 - (3 * H ** 2 - rho)) == 0)
Rm, Rc, R2s, xi = sp.symbols('Riem2 Ric2 R2 xi'); ca, cb, cg = sp.symbols('ca cb cg')
def r2coef(e):
    eqs = sp.Poly(sp.expand(e - (ca * (Rm - 2 * Rc + R2s / 3) + cb * (Rm - 4 * Rc + R2s) + cg * R2s)), Rm, Rc, R2s).coeffs()
    return sp.factor(sp.solve(eqs, [ca, cb, cg], dict=True)[0][cg])
base = 5 * R2s - 2 * Rc + 2 * Rm                 # Gilkey a2: (1/360) tr[60 R E + 180 E^2 + 5R^2 - 2Ric^2 + 2Riem^2 + 30 Om^2]
hk = {'scalar xi': r2coef((-60 * xi * R2s + 180 * xi ** 2 * R2s + base) / 360),
      'Dirac': r2coef((-60 * R2s + 45 * R2s + 4 * base - 15 * Rm) / 360),
      'Maxwell+ghosts': r2coef((-60 * R2s + 180 * Rc + 4 * base - 30 * Rm - 2 * base) / 360)}
per = (1 / 72) * 2 * math.log(1 / F55['M']) / (32 * math.pi ** 2); cneed = 1 / (12 * F55['M'] ** 2)
check('B3 THEOREM (heat kernel, sympy): one-loop R^2 coefficient in the (C^2, E4, R^2) basis: scalar %s, Dirac %s, Maxwell %s: the '
      'rules\' content (one fermion mode per site, links) runs no R^2; %.1e minimally coupled scalars would be needed, the rules have 0'
      % (hk['scalar xi'], hk['Dirac'], hk['Maxwell+ghosts'], cneed / per),
      hk['Dirac'] == 0 and hk['Maxwell+ghosts'] == 0 and sp.simplify(hk['scalar xi'] - (6 * xi - 1) ** 2 / 72) == 0)
print('   cited: Kuhn-complex O(k^4) remainder (landed note) is tensor-sector, -(1+sum n^4)/12 a^2: O(0.1) vs c = %.1e' % cneed)
def Afr(x): return cmath.asin(x * x / (1 - x * x)) / cmath.sqrt(1 - 2 * x * x)
sat = []
for q in (1e3, 1e4):                            # rho/rho*, dust; A(u) = rho/(2 rho*)
    us_ = brentq(lambda x: Afr(x).real - q / 2, 1e-9, (1 - 1e-15) / math.sqrt(2), xtol=1e-17, rtol=1e-15)
    dA = Afr(complex(us_, 1e-20)).imag / 1e-20; sat.append((3 * (q / 2) / (us_ * dA)) / (3 * math.pi ** 2 / q ** 2))
check('B4 the hinge law\'s own plateau: H -> sqrt2/l as rho -> infinity, so with splits any super-critical matter inflates, with '
      'eps_H = 3(1+w)(pi rho*/rho)^2 (ratio %.3f, %.3f): n_s - 1 = -6(1+w) and P_t = 2H^2/pi^2 >= 0.1, 1e9 x the bound: cell-scale only'
      % tuple(sat), all(abs(x - 1) < 0.02 for x in sat) and 2 * 0.5 / math.pi ** 2 > 1e9 * r_max * As_m)

print('== C. (b) condensates')
th = sp.symbols('theta', real=True); sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Ux = sp.cos(th / 2) * sp.eye(2) + sp.I * sp.sin(th / 2) * sx; Uy = sp.cos(th / 2) * sp.eye(2) + sp.I * sp.sin(th / 2) * sy
fpl = sp.simplify(1 - sp.re(sp.simplify((Ux * Uy * Ux.H * Uy.H).trace())) / 2)
ftar = (1 - sp.cos(th)) ** 2 / 2; hill = sp.simplify((sp.diff(ftar, th, 2) / ftar).subs(th, sp.pi))
g2n = 1.5 * (1 - ns_m)                          # hilltop: n_s - 1 = 2 eta, eta = -g^2/3
Vh = 24 / g2n                                   # 3 plaquettes x (4/g^2) x f(pi) = 2, in a^-4 = M_P^4
check('C1 isotropic SU(2) link condensate: 1 - ReTr U_p/2 = (1-cos theta)^2/2 (sympy): quartic below the cell (traceless stress, '
      'w = 1/3: no inflation); compact hilltop at theta = pi with V\'\'/V = %s, eta = -g^2/3, so n_s needs 1/alpha = %.0f, but its '
      'height 24/g^2 = %.0f M_P^4 is %.0e x the tensor bound' % (hill, 4 * math.pi / g2n, Vh, Vh / Vmax),
      sp.simplify(fpl - ftar) == 0 and sp.series(ftar, th, 0, 5).removeO() == th ** 4 / 8 and hill == -1 and Vh / Vmax > 1e9)
print('   cited (smg-verify): the candidate mirror pair square has a unique symmetric ground state, no order parameter to roll')

print('== D. (c) the step')
gK = (np.arange(40) + 0.5) / 40 * 2 * np.pi - np.pi; SK = np.cos(np.stack(np.meshgrid(gK, gK, gK, indexing='ij'), -1).reshape(-1, 3)).mean(1)
rv = {e: -4 * np.arccos(np.clip(math.cos(e) ** 2 + math.sin(e) ** 2 * SK, -1, 1)).mean() * math.sqrt(3) / math.sin(e) for e in (1e-3, 0.04, 0.3, 0.9, 1.5, math.pi / 2)}
vals = list(rv.values())
check('D1 the massless sea\'s vacuum energy at fixed edge l (T = l sin eps/sqrt3): %.3f/l^4 at eps -> 0 to %.3f/l^4 at pi/2, '
      'monotone, negative, Planck-scale, radiation-like at fixed eps: a would-be eps potential that cannot inflate and that CL-3 '
      'removes by counting from the vacuum on the same edges' % (vals[0], vals[-1]), all(np.diff(vals) < 0) and vals[0] < -9 and vals[-1] < vals[0])
LAMB = 0.03
def fvol(a, b): return (a + b) * (a * a + b * b) / 4
def dfa(a, b): return ((a * a + b * b) + (a + b) * 2 * a) / 4
def Afn(x): return cmath.asin(x * x / (1 - x * x)) / cmath.sqrt(1 - 2 * x * x)
def edgeq(lm, l, lp, Tm, Tp):                   # Schlaefli form of dS/dl_n with a constant per 4-volume (CL-3, no 4-volume clause)
    um, up = (l - lm) / (2 * Tm), (lp - l) / (2 * Tp); dm = 4 * cmath.asin(um * um / (1 - um * um)); dp = 4 * cmath.asin(up * up / (1 - up * up))
    o = 12 * l * (cmath.atanh(up) - cmath.atanh(um)) + (1.5 * Tm * cmath.sqrt(1 - 2 * um * um) - 1.5 * (lm + l) * um / cmath.sqrt(1 - 2 * um * um)) * dm
    o += (1.5 * Tp * cmath.sqrt(1 - 2 * up * up) + 1.5 * (l + lp) * up / cmath.sqrt(1 - 2 * up * up)) * dp
    return (o - LAMB * (Tm * dfa(l, lm) + Tp * dfa(l, lp))).real
def consq(a, b, T): return (6 * (a + b) * Afn((b - a) / (2 * T)) - LAMB * fvol(a, b)).real
def tick_step(lm, l, Tm):                       # l_n+1(T) from the constraint, then every root in T of the edge equation
    lp_of = lambda T: brentq(lambda b: consq(l, b, T), l * (1 + 1e-14), l + 1.41 * T, xtol=1e-16, rtol=1e-15)
    g = lambda T: edgeq(lm, l, lp_of(T), Tm, T); Tg = np.geomspace(Tm / 30, Tm * 30, 61); gs = [g(x) for x in Tg]
    return [brentq(g, Tg[i], Tg[i + 1], xtol=1e-18, rtol=1e-14) for i in range(60) if gs[i] * gs[i + 1] < 0], lp_of
LAMB = 0.03; ls = [1.0]; Ts = [0.01]; ls.append(1 + 2 * brentq(lambda x: consq(1.0, 1 + 2 * x * 0.01, 0.01), 1e-9, 0.7) * 0.01); nr = []
for n in range(1, 60):
    rts, lp_of = tick_step(ls[n - 1], ls[n], Ts[n - 1]); nr.append(len(rts))
    if not rts: break
    Ts.append(rts[0]); ls.append(lp_of(rts[0]))
n = len(Ts) - 1; lp2 = lp_of(2 * Ts[n]); um = (ls[n] - ls[n - 1]) / (2 * Ts[n - 1])
weak = abs(edgeq(ls[n - 1], ls[n], lp2, Ts[n - 1], 2 * Ts[n])) / abs(12 * ls[n] * math.atanh(um))
Hd = [(lp - ls[n]) / (T * 0.5 * (lp + ls[n])) / math.sqrt(LAMB / 3) - 1 for lp, T in ((ls[n + 1], Ts[n]), (lp2, 2 * Ts[n]))]
LA, TA = np.array(ls), np.array(Ts); TL = TA * 0.5 * (LA[1:] + LA[:-1])
check('D2 without the 4-volume clause the carrier fixes the tick: one root per step (%s), but weakly (doubling it moves the edge '
      'equation by %.0e of its terms); T l kept to %.0e as T falls %.1f%%: sin eps ~ l^-2 rolls, while H/sqrt(Lambda/3) - 1 = %.1e, %.1e '
      'at T and 2T: H carries no eps' % (sorted(set(nr)), weak, abs(TL[-1] / TL[0] - 1), -100 * (TA[-1] / TA[0] - 1), Hd[0], Hd[1]),
      set(nr) == {1} and weak < 1e-5 and abs(TL[-1] / TL[0] - 1) < 2e-3 and TA[-1] / TA[0] < 0.97 and max(map(abs, Hd)) < 5e-3 and abs(Hd[1] - Hd[0]) < 1e-3)
print('   cited (split-schedule B, cosmology E): the cycle repeats exactly, so a constant-driven phase gives n_s = 1 and never ends')

print('== E. (d) copy mass')
print('   rule text: CL-3 varies edges and links only; M is a constant in proper units in CL-1, so it has no equation of motion')
def Phi_mu(mu, e=0.3):                           # CL-1 flat bands: cos w = A S + (cos 2eps + cos mu)/2, A = (cos mu - cos 2eps)/2
    c2 = math.cos(2 * e); return -4 * np.arccos(np.clip((math.cos(mu) - c2) / 2 * SK + (c2 + math.cos(mu)) / 2, -1, 1)).mean()
mus = np.linspace(-math.pi, math.pi, 41); phm = np.array([Phi_mu(m) for m in mus]); Imu = (Phi_mu(0) - Phi_mu(0.01)) / 1e-4
check('E1 SPECULATIVE promotion: a mass enters CL-1 only as the angle mu = M N per tick; the sea\'s vacuum phase in mu is even, '
      '2pi-periodic and maximal at mu = 0 (Phi(0) - Phi(mu) = %.2f mu^2): a periodic hilltop, the natural-inflation class that no f '
      'passes (A3), with no kinetic term in the rules' % Imu, abs(mus[np.argmax(phm)]) < 1e-12 and np.allclose(phm, phm[::-1])
      and abs(Phi_mu(0.7 + 2 * math.pi) - Phi_mu(0.7)) < 1e-12 and Imu > 0 and not okN.any())

print('== F. what any inflaton needs from the rules')
print('   rule text: Lambda is one supplied constant per proper 4-volume, so it cannot fall; an inflating phase must be a field')
nb = 0.02237 * 1.8785e-26 / 1.67262e-27; Vobs = 4 * math.pi / 3 * (14.2e3 * 3.0857e22) ** 3; nf = nb * Vobs * (3 + 1 - 0.245 / 2)
Hs_a = math.sqrt(F55['V'] / 3) * F55['M']; sites = 8 * 4 * math.pi / 3 / Hs_a ** 3; Hcrit = (8 * 4 * math.pi / 3 / nf) ** (1 / 3) * MP
check('F1 the update conserves mode number, so the empty vacuum creates no fermion: today\'s baryons and electrons need %.1e modes, '
      'the Hubble patch at pivot exit has <= %.1e sites (Starobinsky H): excluded by %.0e for any H_inf > %.0e GeV; reheating needs the sea'
      % (nf, sites, nf / sites, Hcrit), nf / sites > 1e50 and Hcrit < 1e-6)
heat = 0.19 * abs(vals[0]) / 16
check('F2 ESTIMATE a local split heats ~19%% of the sea (split-junction), ~%.2f M_P^4 at l = 2a, %.0e x any allowed inflaton energy: '
      'inflation with the sea needs splits heat-free below the Hubble radius (super-Hubble residue ~H^4, (Ha)^2/3 = %.0e per split)'
      % (heat, heat / Vmax, Hs_a ** 2 / 3), heat / Vmax > 1e7)

print('== G. replacement (not adopted): c R^2 per proper 4-volume in CL-3')
t = sp.symbols('t'); cc, Lm = sp.symbols('c Lambda'); a = sp.Function('a')(t); Nl = sp.Function('N')(t)
Rf = 6 * (sp.diff(a, t, 2) / (a * Nl ** 2) + sp.diff(a, t) ** 2 / (a ** 2 * Nl ** 2) - sp.diff(a, t) * sp.diff(Nl, t) / (a * Nl ** 3))
Lg = Nl * a ** 3 * (sp.Rational(1, 2) * (Rf - 2 * Lm) + cc * Rf ** 2); sub = {sp.diff(Nl, t, 2): 0, sp.diff(Nl, t): 0}
ELN = (sp.diff(Lg, Nl) - sp.diff(sp.diff(Lg, sp.diff(Nl, t)), t)).subs(sub).subs(Nl, 1)
R1 = Rf.subs(sub).subs(Nl, 1); Hh = sp.diff(a, t) / a; Ff = 1 + 4 * cc * R1
C00 = 3 * Ff * Hh ** 2 - (Ff * R1 - (R1 - 2 * Lm + 2 * cc * R1 ** 2)) / 2 + 3 * Hh * sp.diff(Ff, t)
check('G1 THEOREM (sympy): the lapse equation of a^3[(R - 2Lambda)/2 + c R^2] is a^3 x the f(R) constraint 3FH^2 = (FR-f)/2 - 3H Fdot '
      '+ Lambda, third order in a: the scalaron datum appears and CL-3\'s constant stays a constant', sp.simplify(ELN / C00 - a ** 3) == 0)
def jord(NE):
    p, pn = BG.sol(NE); HE = math.sqrt(Vs(p) / (3 - pn * pn / 2)); return NE - p / math.sqrt(6), math.exp(p / math.sqrt(6)) * HE * (1 - pn / math.sqrt(6)), math.exp(s23 * p)
(j1, h1, _), (j2, h2, _), (_, hj, Fj) = jord(NEND - 55 - 1e-3), jord(NEND - 55 + 1e-3), jord(NEND - 55)
tr = (h2 ** 2 - h1 ** 2) / (j2 - j1)
check('G2 in the lattice (Jordan) frame H^2 falls by a constant M^2/3 per e-fold (%.4f), %.2f%% per split at N* = 55: the '
      'split-schedule\'s constant transfer law; the hinge coupling is multiplied by F = %.0f (~4N/3), turning r = 8/N into 12/N^2'
      % (tr, -100 * tr * math.log(2) / hj ** 2, Fj), abs(tr + 1 / 3) < 3e-3 and 60 < Fj < 90)
def nstar_of(Ns, Gam):
    f_ = flow(Ns); M = f_['M']; Hs = math.sqrt(f_['V'] / (3 - f_['e1'])) * M * MP; ye = math.exp(-s23 * PEND)
    rho_end = 1.5 * 0.75 * (1 - ye) ** 2 * M ** 2 * MP ** 4; rho_rh = 3 * MP ** 2 * Gam(M) ** 2 if Gam else rho_end
    Trh = (30 * rho_rh / (math.pi ** 2 * 106.75)) ** 0.25; H0 = 67.4e3 / 3.0857e22 * 6.582e-25
    return -math.log(0.05 / (67.4 / 2.99792458e5)) + math.log(Hs / H0) + math.log(rho_rh / rho_end) / 3 + math.log(3.909 / 106.75) / 3 + math.log(2.348e-13 / Trh), Trh
def a3(mu): return 1 / (1 / 0.1180 + 7 / (2 * math.pi) * math.log(mu / 91.1876))
def Gam_rules(M):                               # sea present; colour links via the trace anomaly + top mass (supplied measured)
    Mg = M * MP; return 49 * a3(Mg) ** 2 * Mg ** 3 / (192 * math.pi ** 3 * MP ** 2) + 3 * 172.7 ** 2 * Mg / (48 * math.pi * MP ** 2)
Ns_ = 55.0
for _ in range(4): Ns_, Trh = nstar_of(Ns_, Gam_rules)
Ni_, _ = nstar_of(55.0, None); Ni_, _ = nstar_of(Ni_, None)
G_lo, G_hi = flow(Ns_), flow(Ni_)
check('G3 ESTIMATE reheating with the sea, no fundamental scalar: the scalaron decays through the colour anomaly (top channel 1e-21 of it): '
      'Gamma = %.3f GeV, T_rh = %.1e GeV, N* = %.1f (instant: %.1f)' % (Gam_rules(G_lo['M']), Trh, Ns_, Ni_), 1e7 < Trh < 1e9 and 48 < Ns_ < 53)
check('G4 then n_s = %.4f (%+.1f sigma), r = %.4f, alpha_s = %.1e (%+.1f sigma) DERIVED given the term; c = %.2e FIT to A_s (to %.4f, %.4f, '
      '%.2e at instant reheating)' % (G_lo['ns'], (G_lo['ns'] - ns_m) / dns, G_lo['r'], G_lo['als'], (G_lo['als'] - als_m) / dals,
      1 / (12 * G_lo['M'] ** 2), G_hi['ns'], G_hi['r'], 1 / (12 * G_hi['M'] ** 2)),
      abs(G_lo['ns'] - ns_m) < 2 * dns and G_lo['r'] < r_max and abs(G_lo['als'] - als_m) < dals)

print('== H. look-elsewhere')
lo, hi = 1 / (12 * G_lo['M'] ** 2) * (1 - dAs / As_m), 1 / (12 * G_hi['M'] ** 2) * (1 + dAs / As_m); dex = math.log10(hi / lo)
fam = {'2^n': 2, '4^n': 4, '8^n': 8, '16^n': 16, 'e^n': math.e, '3x2^n': (3, 2), '(4pi)^n': 4 * math.pi, '6^n': 6}
hits, expct = [], 0.0
for k, b in fam.items():
    pref, bb = (b if isinstance(b, tuple) else (1, b)); expct += min(1.0, dex / math.log10(bb))
    for n in range(1, 120):
        v = pref * bb ** n
        if lo <= v <= hi: hits.append(f'{k}:{n}')
check('H1 c window %.2e..%.2e (%.2f dex: N* 50-56, A_s 1 sigma) vs 8 rule-number families: hits %s, %.1f expected by chance: a '
      'match of c to a rung count is cheap, and a local coefficient cannot count splits' % (lo, hi, dex, hits, expct), len(hits) >= 1 and expct > 0.5)
Mw = (G_hi['M'], G_lo['M']); hit2 = []
for Nc in range(2, 7):
    ia = 11 * Nc / 3 * (-math.log(Mw[0])) / (2 * math.pi), 11 * Nc / 3 * (-math.log(Mw[1])) / (2 * math.pi)
    if 24 <= min(ia) <= 42 or 24 <= max(ia) <= 42: hit2.append(f'SU({Nc})@1/a={0.5 * sum(ia):.1f}')
check('H2 M = M_P exp(-2 pi/(b0 alpha_cell)) with pure SU(N) b0 and the register\'s 1/alpha_cell = 24..42: %s: dimensional '
      'transmutation fits M with a free group, not a derivation' % ', '.join(hit2), len(hit2) >= 2)
print('supplied: frustum carrier, kappa = 1, discrete R^2 form, Wilson plaquette, free sea, unit map, measured colour running,')
print('  top mass, g*, Planck/BK18 numbers, number families; cited: Kuhn k^4 note, smg-verify, split-junction, split-schedule.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
