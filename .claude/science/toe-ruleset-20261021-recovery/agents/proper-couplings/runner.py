#!/usr/bin/env python3
"""proper-couplings: does alpha track the gravitational potential under CL-1 + CL-3, and what rule holds it fixed?

Supplied model (as in induced-response): the CL-1 cube tick (spin-3/2 edge hop W, even then odd 2^3 cubes, half-ticks
exp(-i(eps - mu/2)W), exp(+i(eps + mu/2)W)), its filled negative-quasi-energy sea (one species = two light Dirac copies,
no copy mass), site-phase links, static backgrounds, free sea, second order.  CL-1 reading: a cell of proper tick tau and
proper edge L has sin eps = sqrt3 tau/L and mass phase mu = m tau, so its inverse Compton length in blocks is m L.
CL-3: each record's 4-volume is fixed, tau L^3 = v.  Finite diagnostics; no physical identification.
 A  exact: the cell in a static field; a plaquette counted in proper area; engine sanity
 B  the sea's link coupling 1/e^2 = A(m L, eps): size and shape slopes, and dA/dPhi on the CL-3 cell family
 C  candidate rule (dressed coupling of a uniform field the same in every cell): the subtracted running is cell-blind
 D  estimates with measured numbers
"""
from __future__ import annotations
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
from scipy.integrate import quad

T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ engine (inlined from induced-response)
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C8[i] - 1.0) / r3; _, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
EDGES = [(a, b) for a in range(8) for b in range(8) if a < b and np.sum(abs(C8[a] - C8[b])) == 1]
AXIS = {e: int(np.argmax(abs(C8[e[0]] - C8[e[1]]))) for e in EDGES}
W = np.zeros((8, 8), complex)
for a, b in EDGES:
    g_ = XI[a].conj() @ XI[b]; W[a, b] = -g_ / abs(g_) / r3; W[b, a] = np.conj(W[a, b])
BOND = {}
for e in EDGES:
    X = np.zeros((8, 8), complex); X[e] = W[e]; X[e[::-1]] = W[e[::-1]]; BOND[e] = X
PP, PMI = (I8 + W) / 2, (I8 - W) / 2
def expmW(t): return np.cos(t) * I8 - 1j * np.sin(t) * W
def Dm(K): return np.exp(1j * (np.atleast_2d(K) @ C8.T))
def Uo(Ko, Ki, M):
    Do, Di = Dm(Ko), Dm(Ki); return Do[:, :, None] * M[None] * Di.conj()[:, None, :]
def tick(K, eps, mu):
    Ue = expmW(eps - mu / 2); Mo = expmW(-(eps + mu / 2)); return Uo(K, K, Mo) @ Ue, Ue, Mo
def Sof(K): return np.cos(np.atleast_2d(K)).sum(1) / 3
def w_an(K, eps, mu):
    A = (np.cos(mu) - np.cos(2 * eps)) / 2
    return np.arccos(np.clip(A * Sof(K) + (np.cos(2 * eps) + np.cos(mu)) / 2, -1, 1))
def speed2(eps, mu):
    A = (np.cos(mu) - np.cos(2 * eps)) / 2; return A / 3 * (mu / np.sin(mu) if mu else 1.0)
def mu_of_m(eps, m):                       # mass angle with inverse Compton length m (blocks^-1)
    mu = np.sin(eps) / r3 * m
    for _ in range(60): mu = np.sqrt(speed2(eps, mu)) * m
    return mu
def dag(A): return np.conj(np.swapaxes(A, -1, -2))
def tr(A): return np.trace(A, axis1=-2, axis2=-1)
def proj(U):
    cw = np.real(tr(U)) / 8; w = np.arccos(np.clip(cw, -1, 1)); X = (U - dag(U)) / (2j * np.sin(w)[:, None, None])
    return (I8 + X) / 2, (I8 - X) / 2, w
def second_order(U0, U0p, U0m, d1p, d1m, d2):
    """coefficient of lambda^2 in the filled quasi-energy sum (batch total): Floquet second order."""
    PF, _, w = proj(U0); _, PEp, wp = proj(U0p); _, PEm, wm = proj(U0m)
    M1p, M1m = dag(U0p) @ d1p, dag(U0m) @ d1m
    A2 = 1j * (dag(U0) @ d2 + 0.5 * (dag(M1p) @ M1p + dag(M1m) @ M1m))
    t1 = tr(PF @ A2); A1p, A1m = 1j * M1p, 1j * M1m
    t2 = -0.5 * (np.real(tr(PEp @ A1p @ PF @ dag(A1p))) / np.tan((w + wp) / 2)
                 + np.real(tr(PEm @ A1m @ PF @ dag(A1m))) / np.tan((w + wm) / 2))
    return np.sum(np.real(t1) + t2)
def gauge_blocks(K, eps, mu, q, h1, h2):
    U0, Ue, Mo = tick(K, eps, mu); Kp, Km = K + q, K - q
    Op, Om, O0 = Uo(Kp, Kp, Mo), Uo(Km, Km, Mo), Uo(K, K, Mo)
    ph = np.exp(1j * (C8 @ q) / 2)
    T1p, T1m, T2p, T2m = (np.diag(h * p) / 2 for h, p in ((h1, ph), (h1, ph.conj()), (h2, ph), (h2, ph.conj())))
    d1p = 1j * T2p @ O0 @ Ue + Op @ (1j * T1p) @ Ue; d1m = 1j * T2m @ O0 @ Ue + Om @ (1j * T1m) @ Ue
    d2 = (-0.25 * np.diag(h2 ** 2) @ O0 @ Ue - 0.25 * O0 @ np.diag(h1 ** 2) @ Ue - T2m @ Op @ T1p @ Ue - T2p @ Om @ T1m @ Ue)
    return U0, Op @ Ue, Om @ Ue, d1p, d1m, d2
def dd1(x, y): return -1j * np.exp(-1j * x) if abs(x - y) < 1e-12 else (np.exp(-1j * x) - np.exp(-1j * y)) / (x - y)
def dd2(x, y, z):
    if abs(x - y) < 1e-12 and abs(y - z) < 1e-12: return -np.exp(-1j * x) / 2
    if abs(x - z) < 1e-12: x, y = y, x
    return (dd1(x, y) - dd1(y, z)) / (x - z)
def fr1(G, A):
    return sum(dd1(ga, gb) * (Pa @ A @ Pb) for ga, Pa in G for gb, Pb in G)
def fr2(G, A, B):
    return sum(dd2(ga, gc, gb) * (Pa @ A @ Pc @ B @ Pb + Pa @ B @ Pc @ A @ Pb) for ga, Pa in G for gc, Pc in G for gb, Pb in G)
def total(fn, Ks, *args, batch=2000):
    return sum(second_order(*fn(Ks[s:s + batch], *args)) for s in range(0, len(Ks), batch))
def kgrid(ns, shift=0.5):
    gs = [2 * np.pi * (np.arange(n) + shift) / n - np.pi for n in ns]
    return np.array(np.meshgrid(*gs, indexing='ij')).reshape(3, -1).T
D_R = C8 - 0.5                                  # even-centre -> odd-centre link through each site type (blocks)
def link_h(kind, q, adir=(0, 0, 1)):
    s = np.sinc((D_R @ q) / 2 / np.pi)
    if kind == 'E': return -0.5 * s, -0.5 * s
    a = (q / np.linalg.norm(q)) if kind == 'L' else np.array(adir, float); h = (D_R @ a) * s; return h, -h
kap = 2 / (6 * np.pi ** 2)                      # continuum log coefficient for two Dirac copies
def AEq(eps, mlat, Nx, js):
    """static Coulomb response 1/e^2_E(q) of the sea on a commensurate torus (Nx, Nx/2, Nx/2), q = 2 pi j/Nx along x."""
    mu = mu_of_m(eps, mlat); c = np.sqrt(speed2(eps, mu)); Ks = kgrid((Nx, Nx // 2, Nx // 2)); out = []
    for j in js:
        q = np.array([2 * np.pi * j / Nx, 0, 0]); r = total(gauge_blocks, Ks, eps, mu, q, *link_h('E', q))
        out.append(c * (-4) * r / (q[0] ** 2 * len(Ks)))
    return np.array(out)
def fit0(a, Nx):
    qq = (2 * np.pi * np.arange(1, 4) / Nx) ** 2; return np.linalg.solve(np.stack([np.ones(3), qq, qq ** 2], 1), a[:3])[0]
def A0(eps, mlat, Nx): return fit0(AEq(eps, mlat, Nx, (1, 2, 3)), Nx)

# ------------------------------------------------------------------ A. exact
print('== A. exact')
Ph, v, se = sp.symbols('Phi v s', positive=True); N = 1 + Ph; L = N ** sp.Rational(-1, 3); tau = N
dlnL = sp.diff(sp.log(L), Ph).subs(Ph, 0); dlns = sp.diff(sp.log(tau / L), Ph).subs(Ph, 0)
Lv = sp.symbols('Lv', positive=True); sol = sp.solve(sp.Eq((se / sp.sqrt(3) * Lv) * Lv ** 3, v), Lv)
okL = any(sp.simplify(s_ - v ** sp.Rational(1, 4) * (sp.sqrt(3) / se) ** sp.Rational(1, 4)) == 0 for s_ in sol)
check('A1 CL-1 cone + CL-3 fixed 4-volume, static field N = 1 + Phi: tau L^3 = v gives d ln L/dPhi = -1/3 and d ln sin eps/dPhi '
      '= +4/3; in general L = v^(1/4) (sqrt3/sin eps)^(1/4), so a cell\'s proper size is set by its step', dlnL == sp.Rational(-1, 3)
      and dlns == sp.Rational(4, 3) and okL, f'{dlnL}, {dlns}; isotropic gauge (L = 1 - Phi) would give -1')
t_, l_, e0, F, E, bs, bt = sp.symbols('tau L e0 F E beta_s beta_t', positive=True)
cB = sp.simplify((t_ / l_ / e0 ** 2) * (F * l_ ** 2) ** 2 / (t_ * l_ ** 3) / F ** 2)
cE = sp.simplify((l_ / t_ / e0 ** 2) * (E * l_ * t_) ** 2 / (t_ * l_ ** 3) / E ** 2)
iE, iB = sp.simplify(bt * (E * l_ * t_) ** 2 / (t_ * l_ ** 3) / E ** 2), sp.simplify(bs * (F * l_ ** 2) ** 2 / (t_ * l_ ** 3) / F ** 2)
check('A2 theorem: a plaquette phase counted in proper area (spatial weight tau/L, temporal L/tau, per 1/e0^2) gives 1/e^2_E = '
      '1/e^2_B = 1/e0^2 on every cell (4D Maxwell is scale and shape blind); fixed weights keep sqrt(1/e_E^2 e_B^2) but give '
      'photon speed^2 = (beta_s/beta_t)(L/tau)^2, which tracks Phi', cB == 1 / e0 ** 2 and cE == 1 / e0 ** 2
      and sp.simplify(iE * iB - bs * bt) == 0, f'proper: {cB}, {cE}; fixed: c^2 = {sp.simplify(iB / iE)}')
rng = np.random.default_rng(20261022); KR = rng.uniform(-np.pi, np.pi, (300, 3)); dv = 0
for eps, mu in ((0.05, 0.02), (0.3, 0.1)):
    U, _, _ = tick(KR, eps, mu); dv = max(dv, np.abs(np.sort(np.abs(np.angle(np.linalg.eigvals(U))), 1) - w_an(KR, eps, mu)[:, None]).max())
Ks = kgrid((16, 8, 8)); q = np.array([2 * np.pi / 16, 0, 0])
pg = abs(total(gauge_blocks, Ks, 0.3, 0.1, q, *link_h('L', q))); ref = abs(total(gauge_blocks, Ks, 0.3, 0.1, q, *link_h('B', q)))
check('A3 engine: all 8 bands obey the CL-1 band law; a pure-gauge link field gives zero response (exact gauge invariance)',
      dv < 1e-10 and pg < 1e-11 * ref, f'{dv:.1e}, {pg:.1e} vs {ref:.1e}')

# ------------------------------------------------------------------ B. the sea's coupling on the cell family
print('== B. the sea\'s link coupling A = 1/e^2 (one species = two copies, kappa = 2/(6 pi^2)) versus cell size and shape')
js = np.arange(1, 7); cells = {}
for eps in (0.05, 0.3):
    for Nx in ((64, 80, 100) if eps == 0.05 else (64, 100)):
        m = 25.6 / Nx; a = AEq(eps, m, Nx, js); cells[(eps, Nx)] = (m, fit0(a, Nx), a)
ms = [cells[(0.05, n)][0] for n in (64, 80, 100)]; As = [cells[(0.05, n)][1] for n in (64, 80, 100)]
sl = [(As[i + 1] - As[i]) / np.log(ms[i] / ms[i + 1]) / kap for i in range(2)]; mm = [np.sqrt(ms[i] * ms[i + 1]) for i in range(2)]
s0 = (sl[1] * mm[0] ** 2 - sl[0] * mm[1] ** 2) / (mm[0] ** 2 - mm[1] ** 2)
check('B1 size: -dA/d ln(mL) = kappa (1 - c m^2 L^2): the sea\'s cutoff is the proper cell, and the slope extrapolates to the '
      'QED beta coefficient', abs(s0 - 1) < 0.01 and sl[0] < sl[1] < 1, f'{sl[0]:.4f}, {sl[1]:.4f} at mL = {mm[0]:.3f}, {mm[1]:.3f}; mL -> 0: {s0:.4f}')
h = 0.01; de = {}
for eps in (0.05, 0.3):
    de[eps] = (A0(np.arcsin(np.sin(eps) * (1 + h)), 0.32, 80) - A0(np.arcsin(np.sin(eps) * (1 - h)), 0.32, 80)) / (2 * h) / kap
rs = {e: de[e] / np.sin(e) ** 2 for e in de}
check('B2 shape: dA/d ln sin eps at fixed mL is -r kappa sin^2 eps (r ~ 0.6), far from the -kappa/4 a 4-volume cutoff would '
      'give: the cutoff is the spatial cell, not the record 4-volume', all(-0.8 < x < -0.4 for x in rs.values()),
      f'{de[0.05]:+.5f}, {de[0.3]:+.5f} kappa at eps .05, .3 (r = {-rs[0.05]:.2f}, {-rs[0.3]:.2f})')
vals = []
for P in (-0.02, 0.02):
    n_ = 1 + P; vals.append(A0(np.arcsin(np.sin(0.05) * n_ ** (4 / 3)), 0.32 * n_ ** (-1 / 3), 80))
dm32 = (A0(0.05, 0.32 * (1 + h), 80) - A0(0.05, 0.32 * (1 - h), 80)) / (2 * h) / kap
dAdP = (vals[1] - vals[0]) / 0.04 / (kap / 3); rec = (-dm32 + 4 * de[0.05])
check('B3 the CL-3 cell family (fully proper CL-1 reading, bare plaquette in proper area): dA/dPhi = (kappa/3)(-dA/dlnmL '
      '+ 4 dA/dln sin eps)/kappa, nonzero; alpha tracks Phi', abs(dAdP - rec) < 2e-3 and dAdP > 0.9,
      f'direct {dAdP:.4f}, from slopes {rec:.4f} (units kappa/3)')

# ------------------------------------------------------------------ C. candidate rule
print('== C. rule: dressed coupling of a uniform field the same in every cell (bare term absorbs A(0)); running R = A(q) - A(0)')
def cont(x): return -(1 / np.pi ** 2) * quad(lambda u: u * (1 - u) * np.log(1 + u * (1 - u) * x * x), 0, 1)[0]
x6 = 2 * np.pi * js / 25.6; Rc = np.array([cont(x) for x in x6])
R = {k_: c_[2] - c_[1] for k_, c_ in cells.items()}
dA0 = [(As[i + 1] - As[i]) for i in range(2)]
dR = [np.abs(R[(0.05, n2)] - R[(0.05, n1)]).max() for n1, n2 in ((64, 80), (80, 100))]
sup = [dR[i] / dA0[i] for i in range(2)]
check('C1 unfixed, two cells 25% apart in size: A(0) differs by kappa ln 1.25; under the rule the running at the same proper '
      'q/m (0.25 to 1.5) differs by a few % of that, and the gap shrinks with mL', abs(dA0[1] / (kap * np.log(1.25)) - 1) < 0.02
      and sup[1] < sup[0] < 0.05, f'dA(0) = {dA0[0]:.5f}, {dA0[1]:.5f} (kappa ln1.25 = {kap * np.log(1.25):.5f}); max dR = {dR[0]:.1e}, {dR[1]:.1e}; ratio {sup[0]:.3f}, {sup[1]:.3f}')
ds = [np.abs(R[(0.3, n)] - R[(0.05, n)]).max() for n in (64, 100)]
check('C2 shape: changing eps from .05 to .3 at fixed mL moves the subtracted running by < 3e-3 of itself, falling with mL',
      ds[1] < ds[0] < 3e-3 * np.abs(R[(0.05, 64)]).max(), f'max dR = {ds[0]:.1e} (mL .4), {ds[1]:.1e} (mL .256)')
rat = [np.mean(R[(0.05, n)] / Rc) for n in (64, 80, 100)]; p = np.log((rat[0] - rat[1]) / (rat[1] - rat[2])) / np.log(1.25)
cinf = rat[2] - (rat[1] - rat[2]) / (1.25 ** p - 1)
check('C3 the running kept by the rule is one-loop QED: R/R_QED -> 1 as mL -> 0 (power-law extrapolation of three cells)',
      rat[0] > rat[1] > rat[2] > 1 and abs(cinf - 1) < 0.03, f'R/R_QED = {rat[0]:.4f}, {rat[1]:.4f}, {rat[2]:.4f} -> {cinf:.4f} (power {p:.2f})')

# ------------------------------------------------------------------ D. estimates
print('== D. ESTIMATES with measured numbers (supplied SM content; not theorems)')
ainv = 137.035999084; Am = ainv / (4 * np.pi); b8 = 8 / (6 * np.pi ** 2); r = -rs[0.05]
fac = lambda e: s0 - 4 * r * np.sin(e) ** 2
k = -b8 / (3 * Am)
print(f'   1/e^2 = {Am:.4f}; SM fermions, one light copy: b = 8/(6 pi^2) = {b8:.5f}; dln(alpha)/dPhi = -(b/3A)(1 - 4r sin^2 eps)'
      f' = {k:.4e} x {fac(0.04):.4f} (eps .04); isotropic gauge {3 * k:.3e}')
kW = -(b8 - 7 / (8 * np.pi ** 2)) / (3 * Am); print(f'   variants: with a W loop {kW:.2e}; copy mass a fixed phase M << eps adds 4b/3 -> {5 * k:.2e}')
GM, AU, c = 1.32712440018e20, 1.495978707e11, 2.99792458e8; U = GM / (AU * c ** 2); ecc = 0.0167086
amp = abs(k) * ecc * U
print(f'   Sun at Earth U/c^2 = {U:.3e}, annual amplitude {ecc * U:.3e}: dalpha/alpha amplitude {amp:.2e} (peak-to-peak {2 * amp:.2e})')
print(f'   Lange et al. 2021 (Yb+ E3/E2): k_alpha = 14(11)e-9 -> predicted |k| = {abs(k):.2e} is {abs(k) / 11e-9:.1e} sigma off')
def ec(Z, A_): return 0.711 * Z * (Z - 1) / A_ ** (1 / 3) / (A_ * 931.494)
eta = abs(k) * (ec(78, 195.08) - ec(22, 47.87))
print(f'   EP: Coulomb fraction Pt {ec(78, 195.08):.2e}, Ti {ec(22, 47.87):.2e} -> eta(Ti,Pt) = {eta:.1e} vs MICROSCOPE (-1.5 +- 2.7)e-15')
fe = 5.4858e-4 * (22 / 47.87 - 78 / 195.08)
print(f'   colour links with a fixed bare plaquette: Lambda_QCD ~ 1/L, dln m_p/dPhi = +1/3 -> baryons fall with 4/3 of the lapse:'
      f' gamma_eff - 1 = -1/2 (Cassini 2.3e-5), H-maser redshift x 2/3 (GP-A 1.4e-4), eta ~ {fe / 3:.1e}')
mL = 0.511e-3 * 2 * np.sqrt(8 * np.pi) / 1.220890e19; resid = sup[1] * (mL / mm[1]) ** p / 3 * kap / Am * 4
print(f'   under the rule: electron mL = {mL:.1e}; residual dln(alpha)/dPhi ~ {resid:.0e} (C1 gap scaled by (mL)^{p:.1f})')
check('D1 arithmetic: |k| = 4.13e-3; annual amplitude 6.8e-13; eta > 1e9 x MICROSCOPE; rule residual < 1e-25',
      abs(abs(k) - 4.129e-3) < 2e-6 and abs(amp - 6.8e-13) < 1e-14 and eta > 1e9 * 2.7e-15 and resid < 1e-25)
print('supplied: tick, sea branch, site-phase links, free sea, static cells, torus sizes and mL values (artifact extrapolation),')
print('  continuum one-loop QED as comparator, SM charges, measured alpha, solar and EP numbers, block = 2 sqrt(8 pi) l_P.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
