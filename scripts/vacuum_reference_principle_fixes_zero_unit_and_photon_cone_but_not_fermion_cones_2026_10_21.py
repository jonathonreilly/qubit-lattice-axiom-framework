#!/usr/bin/env python3
"""one-principle: can one vacuum-reference rule replace CL-3's four adopted clauses?

Rule tested (VR): edges and links respond only to departures from the vacuum of the same edges, in the vacuum's own
units: the vacuum's phase (same edges, no field, same configuration) is the zero; its dressed response to a uniform field
is the unit of each link's coupling, one unit for electric and magnetic fields, the same in every cell.
Supplied models (as in induced-response, matter-sees-geometry, lambda-split, proper-couplings): the CL-1 cube tick and
its filled sea, site-phase links, static cells, free sea, second order; the cubic-frustum Regge FRW carrier; a 1D gapped
Dirac chain for the conditional source.  Finite diagnostics; no physical identification.
 A  the lattice sea's vacuum term is not proportional to 4-volume: fixed 4-volume per record removes almost none of it
 B  links: E and B uniform-field couplings of the sea; under VR the photon cone is the edge cone and the subtracted
    running is cell-blind and Lorentz invariant up to O((mL)^2)
 C  splits: rule U turns the junction residual into a Lambda kick; VR without rule U does not
 D  conditional source: literal reference keeps the frozen-sea noise; VR on local phases removes it exactly
 E  estimates with measured numbers
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/VACUUM_REFERENCE_PRINCIPLE_FIXES_ZERO_UNIT_AND_PHOTON_CONE_BUT_NOT_FERMION_CONES_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy import sparse
np.seterr(all='ignore')
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ CL-1 cube tick and second-order sea response
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C8[i] - 1.0) / r3; _, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
EDGES = [(a, b) for a in range(8) for b in range(8) if a < b and np.sum(abs(C8[a] - C8[b])) == 1]
W = np.zeros((8, 8), complex)
for a, b in EDGES:
    g_ = XI[a].conj() @ XI[b]; W[a, b] = -g_ / abs(g_) / r3; W[b, a] = np.conj(W[a, b])
def expmW(t): return np.cos(t) * I8 - 1j * np.sin(t) * W
def Dm(K): return np.exp(1j * (np.atleast_2d(K) @ C8.T))
def Uo(Ko, Ki, M):
    Do, Di = Dm(Ko), Dm(Ki); return Do[:, :, None] * M[None] * Di.conj()[:, None, :]
def tick(K, eps, mu):
    Ue = expmW(eps - mu / 2); Mo = expmW(-(eps + mu / 2)); return Uo(K, K, Mo) @ Ue, Ue, Mo
def w_an(K, eps, mu, f2=None):                    # band law; f2 = normalised axis weights f_i^2/sum f^2
    S = np.cos(np.atleast_2d(K)) @ (np.full(3, 1 / 3) if f2 is None else f2)
    A = (np.cos(mu) - np.cos(2 * eps)) / 2
    return np.arccos(np.clip(A * S + (np.cos(2 * eps) + np.cos(mu)) / 2, -1, 1))
def speed2(eps, mu):
    A = (np.cos(mu) - np.cos(2 * eps)) / 2; return A / 3 * (mu / np.sin(mu) if mu else 1.0)
def mu_of_m(eps, m):
    mu = np.sin(eps) / r3 * m
    for _ in range(60): mu = np.sqrt(speed2(eps, mu)) * m
    return mu
def dag(A): return np.conj(np.swapaxes(A, -1, -2))
def tr(A): return np.trace(A, axis1=-2, axis2=-1)
def proj(U):
    cw = np.real(tr(U)) / 8; w = np.arccos(np.clip(cw, -1, 1)); X = (U - dag(U)) / (2j * np.sin(w)[:, None, None])
    return (I8 + X) / 2, (I8 - X) / 2, w
def second_order(U0, U0p, U0m, d1p, d1m, d2):
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
def total(fn, Ks, *args, batch=2000):
    return sum(second_order(*fn(Ks[s:s + batch], *args)) for s in range(0, len(Ks), batch))
def kgrid(ns, shift=0.5):
    gs = [2 * np.pi * (np.arange(n) + shift) / n - np.pi for n in ns]
    return np.array(np.meshgrid(*gs, indexing='ij')).reshape(3, -1).T
D_R = C8 - 0.5
def link_h(kind, q, adir=(0, 0, 1)):
    s = np.sinc((D_R @ q) / 2 / np.pi)
    if kind == 'E': return -0.5 * s, -0.5 * s
    a = (q / np.linalg.norm(q)) if kind == 'L' else np.array(adir, float); h = (D_R @ a) * s; return h, -h
kap = 2 / (6 * np.pi ** 2)                          # log coefficient of one species (two Dirac copies)
def A_kind(kind, eps, mlat, Nx, js):
    """static uniform-field-normalised link coupling 1/e^2_kind(q) of the sea, q = 2 pi j/Nx along x."""
    mu = mu_of_m(eps, mlat); c = np.sqrt(speed2(eps, mu)); Ks = kgrid((Nx, Nx // 2, Nx // 2)); out = []
    for j in js:
        q = np.array([2 * np.pi * j / Nx, 0, 0]); r = total(gauge_blocks, Ks, eps, mu, q, *link_h(kind, q))
        v = (-4 if kind == 'E' else 4) * r / (q[0] ** 2 * len(Ks)); out.append(c * v if kind == 'E' else v / c)
    return np.array(out)
def fit0(a, Nx):
    qq = (2 * np.pi * np.arange(1, 4) / Nx) ** 2; return np.linalg.solve(np.stack([np.ones(3), qq, qq ** 2], 1), a[:3])[0]

# ------------------------------------------------------------------ A. vacuum term of the sea vs fixed 4-volume
print('== A. the sea\'s vacuum phase on the box-read cube tick (band law; per block per tick, c0 = tau/L)')
KU = kgrid((40, 40, 40))
def Phi(eps, mu=0.0, f2=None): return -4 * np.mean(w_an(KU, eps, mu, f2))
def Phi_tL(tau, L, m=0.0):                          # isotropic cell: sin eps = sqrt3 tau/L, mu = m tau
    return Phi(np.arcsin(r3 * tau / L), m * tau)
t0, L0, h = 0.04 / r3, 1.0, 1e-5
shape = (Phi_tL(t0 * np.exp(3 * h), L0 * np.exp(-h)) - Phi_tL(t0 * np.exp(-3 * h), L0 * np.exp(h))) / (2 * h) / t0
conf0 = (Phi_tL(t0 * np.exp(h), L0 * np.exp(h)) - Phi_tL(t0 * np.exp(-h), L0 * np.exp(-h))) / (2 * h) / t0
mm = 0.25 / t0 * 0.01                                # mu = m tau = 0.0025
shm = (Phi_tL(t0 * np.exp(3 * h), L0 * np.exp(-h), mm) - Phi_tL(t0 * np.exp(-3 * h), L0 * np.exp(h), mm)) / (2 * h) / t0
cfm = (Phi_tL(t0 * np.exp(h), L0 * np.exp(h), mm) - Phi_tL(t0 * np.exp(-h), L0 * np.exp(-h), mm)) / (2 * h) / t0
def Phi_shear(s, eps0=0.04):                         # L = (e^s, e^-s, 1), tau fixed: every 4-volume exactly fixed
    f = np.exp(np.array([-s, s, 0.0])); rms = np.sqrt(np.mean(f ** 2))
    return Phi(np.arcsin(np.sin(eps0) * rms), 0.0, f ** 2 / np.sum(f ** 2))
ks = [(Phi_shear(s) - Phi_shear(0.0)) / s ** 2 / (np.sin(0.04) / r3) for s in (0.02, 0.01)]
check('A1 massless sea: the phase depends on the cell only through tau/L (Weyl), so a shape change at fixed 4-volume '
      '(tau e^3x, L e^-x) moves it at first order and a conformal one not at all: fixed 4-volume per record removes none '
      'of it; a volume-preserving shear moves it at second order. VR removes both identically (vacuum minus itself)',
      abs(conf0) < 1e-9 and shape < -30 and all(k_ < -1 for k_ in ks) and abs(ks[0] / ks[1] - 1) < 0.01,
      f'dPhi/dx = {shape:.2f} c0, conformal {conf0:.0e}; shear d2Phi/ds2/2 = {ks[1]:.3f} c0')
check('A2 massive sea (mu = 0.0025): the conformal part, the only part fixed 4-volume removes, is a fraction '
      f'{abs(cfm / shm):.0e} of the fixed-volume part; the lattice vacuum stress is radiation-like, not w = -1',
      abs(cfm / shm) < 1e-3, f'shape {shm:.3f} c0, conformal {cfm:.2e} c0')

# ------------------------------------------------------------------ B. links
print('== B. sea link couplings A_E, A_B (units kappa = 2/(6 pi^2)); VR: bare E and B terms absorb A_E(0), A_B(0)')
js = np.arange(1, 5); cells = {}
for eps, Nx in ((0.05, 64), (0.05, 80), (0.05, 100), (0.3, 80)):
    m = 25.6 / Nx; aE = A_kind('E', eps, m, Nx, js); aB = A_kind('B', eps, m, Nx, js)
    cells[(eps, Nx)] = dict(m=m, E0=fit0(aE, Nx), B0=fit0(aB, Nx), RE=aE - fit0(aE, Nx), RB=aB - fit0(aB, Nx))
sz = [cells[(0.05, n)] for n in (64, 80, 100)]
dC = [(c_['E0'] - c_['B0']) / kap for c_ in sz]; sl = [(sz[i + 1]['E0'] - sz[i]['E0']) / kap / np.log(1.25) for i in range(2)]
check('B1 without VR: the uniform-field E and B couplings differ (photon off the edge cone) and A(0) follows the cell '
      'size with the QED log (alpha tracks the cell)', all(d > 0.1 for d in dC) and all(abs(s_ - 1) < 0.03 for s_ in sl),
      'dC = ' + ', '.join(f'{d:.4f}' for d in dC) + ' at mL .4,.32,.256; slope ' + ', '.join(f'{s_:.3f}' for s_ in sl))
lv = [np.abs((c_['RE'] - c_['RB']) / c_['RE']) for c_ in sz]; lv0 = [x[0] for x in lv]
pE = [np.log(lv0[i] / lv0[i + 1]) / np.log(1.25) for i in range(2)]
check('B2 VR: the dressed photon speed at q -> 0 is the edge cone exactly, and the subtracted E and B runnings agree up '
      'to a lattice term falling as (mL)^2, so the running is Lorentz invariant in the continuum limit',
      lv0[0] > lv0[1] > lv0[2] and all(1.6 < p < 2.5 for p in pE),
      '|R_E-R_B|/|R| = ' + ', '.join(f'{x:.4f}' for x in lv0) + f' at q/m .245; power {pE[0]:.2f}, {pE[1]:.2f}')
dR = [np.abs(sz[i + 1]['RE'] - sz[i]['RE']).max() / (kap * np.log(1.25)) for i in range(2)]; pL = np.log(dR[0] / dR[1]) / np.log(1.25)
shp = max(np.abs(cells[(0.3, 80)][k_] - cells[(0.05, 80)][k_]).max() / np.abs(cells[(0.05, 80)][k_]).max() for k_ in ('RE', 'RB'))
check('B3 VR: at the same proper q/m the subtracted running is cell-blind: cells 25% apart differ by ~1% of the unfixed '
      'shift, falling with mL; a shape change eps .05 -> .3 moves it by < 3e-3', dR[1] < dR[0] < 0.03 and shp < 3e-3,
      f'dR/(kappa ln1.25) = {dR[0]:.4f}, {dR[1]:.4f} (power {pL:.2f}); shape {shp:.1e}')
def cont(x): return -(1 / np.pi ** 2) * quad(lambda u: u * (1 - u) * np.log(1 + u * (1 - u) * x * x), 0, 1)[0]
Rc = np.array([cont(2 * np.pi * j / 25.6) for j in js])
rat = {k_: [np.mean(c_[k_] / Rc) for c_ in sz] for k_ in ('RE', 'RB')}
def extrap(r):
    p = np.log((r[0] - r[1]) / (r[1] - r[2])) / np.log(1.25); return r[2] - (r[1] - r[2]) / (1.25 ** p - 1)
xE, xB = extrap(rat['RE']), extrap(rat['RB'])
check('B4 both subtracted runnings extrapolate to one-loop QED as mL -> 0', abs(xE - 1) < 0.03 and abs(xB - 1) < 0.03,
      f'R_E/R_QED {rat["RE"][0]:.4f} -> {xE:.4f}; R_B/R_QED {rat["RB"][0]:.4f} -> {xB:.4f}')

# ------------------------------------------------------------------ C. splits on the frustum Regge carrier (lambda-split)
print('== C. a synchronous 2^3 split of dust on the cubic-frustum Regge FRW carrier (kappa = 1)')
def Af(u): return np.arcsin(u * u / (1 - u * u)) / np.sqrt(1 - 2 * u * u)
def fv(a, b): return (a + b) * (a * a + b * b) / 4
mean2 = lambda x: 0.5 * (x[1:] + x[:-1])
def split_run(Cd, Lv, step, unimod, nafter=40):
    ls, Ts, mesh = [1.0], [], []; u = np.sqrt((Cd + Lv) / 3) / 2; mc = 0; r = None
    while True:
        if mc == 0 and ls[-1] >= 2.0: r = len(ls) - 1; mc = 1; ls[-1] /= 2
        l = ls[-1]; T = step * l / (2 * u); Em = Cd / 8 ** mc
        uu = brentq(lambda x: Em + Lv * fv(l, l + 2 * x * T) - 6 * (2 * l + 2 * x * T) * Af(x), 1e-300, (1 - 1e-15) / np.sqrt(2), xtol=1e-300, rtol=1e-15)
        ls.append(l + 2 * uu * T); Ts.append(T); mesh.append(mc); u = uu
        if mc == 1 and len(ls) - r > nafter: break
    ls, Ts, mesh = np.array(ls), np.array(Ts), np.array(mesh); M = len(Ts)
    def edges(k, lv): return lv[k], (2 * lv[k + 1] if (mesh[k] == 0 and k + 1 == r) else lv[k + 1])
    Vv = np.array([Ts[k] * fv(*edges(k, ls)) for k in range(M)])
    def slabterm(k, lv, Tk, rv):
        la, lb = edges(k, lv); T = Tk(k, la, lb); uk = (lb - la) / (2 * T); w = 8 ** mesh[k]
        return w * (6 * (la + lb) * T * np.sqrt(1 - 2 * uk * uk) * np.arcsin(uk * uk / (1 - uk * uk)) - Cd / w * T - rv * T * fv(la, lb)), uk
    def hinge(k, ua, ub, lv):
        return (8 ** mesh[k] * 6 * lv[k] ** 2 * (np.arctanh(ub) - np.arctanh(ua)) if mesh[k - 1] == mesh[k] else 6 * (2 * lv[k]) ** 2 * (2 * np.arctanh(ub) - np.arctanh(ua)))
    if not unimod:
        def act(lv, rv):
            S = 0.0; us = []
            for k in range(M):
                s_, uk = slabterm(k, lv, lambda k, la, lb: Ts[k], rv); S += s_; us.append(uk)
            return S + sum(hinge(k, us[k - 1], us[k], lv) for k in range(1, M))
        hh = 1e-6 * ls[r]; lp_, lm_ = ls.copy(), ls.copy(); lp_[r] += hh; lm_[r] -= hh
        return (act(lp_, Lv) - act(lm_, Lv)) / (2 * hh) / (6 * (2 * ls[r]) ** 2 * np.arctanh((ls[r + 1] - ls[r]) / (2 * Ts[r]))), 2 * (ls[r + 1] - ls[r]) / (2 * Ts[r])
    TU = lambda k, la, lb: Vv[k] / fv(la, lb)
    def localS(k, lv):
        Sm, um = slabterm(k - 1, lv, TU, 0.0); S0, u0 = slabterm(k, lv, TU, 0.0); out = Sm + S0 + hinge(k, um, u0, lv)
        if k - 1 == 0: out += 6 * lv[0] ** 2 * np.arctanh(um)
        if k - 1 >= 1: out += (8 ** mesh[k - 1] * 6 * lv[k - 1] ** 2 * np.arctanh(um) if mesh[k - 2] == mesh[k - 1] else 6 * (2 * lv[k - 1]) ** 2 * 2 * np.arctanh(um))
        if k + 1 <= M - 1: out += (-8 ** mesh[k + 1] * 6 * lv[k + 1] ** 2 * np.arctanh(u0) if mesh[k] == mesh[k + 1] else -6 * (2 * lv[k + 1]) ** 2 * np.arctanh(u0))
        return out
    lu = ls.copy()
    for k in range(1, M - 1):
        def G(lp):
            lv = lu.copy(); lv[k + 1] = lp; hh = 1e-7 * lv[k]; p_, q_ = lv.copy(), lv.copy(); p_[k] += hh; q_[k] -= hh
            return (localS(k, p_) - localS(k, q_)) / (2 * hh)
        wd = 0.3 * step * ls[k + 1]
        for _ in range(30):
            if G(ls[k + 1] - wd) * G(ls[k + 1] + wd) < 0: break
            wd *= 1.5
        lu[k + 1] = brentq(G, ls[k + 1] - wd, ls[k + 1] + wd, xtol=1e-15, rtol=1e-14)
    Lam = []
    for k in range(M - 1):
        la, lb = edges(k, lu); T = Vv[k] / fv(la, lb); Lam.append((6 * (la + lb) * Af((lb - la) / (2 * T)) - Cd / 8 ** mesh[k]) / fv(la, lb))
    Lb = mean2(np.array(Lam)); return Lb[r + 4:r + 30].mean() - Lb[r - 12:r - 4].mean(), (Cd / 8 / lu[r] ** 3 + Lv) ** 2 * lu[r] ** 2 / 6
ku = [split_run(Cd, 0.005, 0.004, True) for Cd in (0.05, 0.0125)]
rs = [split_run(Cd, 0.005, 0.004, False) for Cd in (0.05, 0.0125)]
pr = np.log(rs[0][0] / rs[1][0]) / np.log(rs[0][1] / rs[1][1])
check('C1 rule U (fixed record 4-volume) turns each split\'s junction residual into a permanent kick rho^2/rho* of Lambda; '
      'with VR the vacuum is already removed, rule U can go, Lambda is a geometric constant and the residual stays a '
      'one-slab mismatch of order (H l)^2', all(abs(a_ / b_ - 1) < 0.01 for a_, b_ in ku) and 1.7 < pr < 2.4,
      'kick/(rho^2/rho*) ' + ', '.join(f'{a_ / b_:.4f}' for a_, b_ in ku) + '; residual ' + ', '.join(f'{x:+.2e} (Hl {y:.3f})' for x, y in rs)
      + f', power {pr:.2f}')

# ------------------------------------------------------------------ D. conditional source parts (1D gapped Dirac sea)
print('== D. conditional source: 12-site gapped Dirac ring, 6 fermions (924 configurations), parts = 2-site blocks')
N1, NF1 = 12, 6; confs = list(itertools.combinations(range(N1), NF1)); D1 = len(confs)
occ = np.zeros((D1, N1), int)
for i, c in enumerate(confs): occ[i, list(c)] = 1
bits = 1 << np.arange(N1); code = occ @ bits; pos = {int(c): i for i, c in enumerate(code)}
def hop(a, b):                                      # c_a^dag c_b with Jordan-Wigner signs (sparse)
    rr, cc, vv = [], [], []
    for i in range(D1):
        o = occ[i]
        if o[b] and not o[a]:
            s = (-1) ** int(o[:b].sum()); o2 = o.copy(); o2[b] = 0; s *= (-1) ** int(o2[:a].sum()); o2[a] = 1
            rr.append(pos[int(o2 @ bits)]); cc.append(i); vv.append(float(s))
    return sparse.csr_matrix((vv, (rr, cc)), shape=(D1, D1))
Hb = {}
for j in range(N1):
    a, b = j, (j + 1) % N1; Mb = -(hop(a, b) + hop(b, a)); Hb[(a, b)] = -Mb if j == N1 - 1 else Mb   # antiperiodic
blk = np.arange(N1) // 2; ms = (-1.0) ** np.arange(N1)
H = sum(Hb.values()) + sparse.diags(occ @ ms)
HP = [sparse.diags(occ[:, 2 * k:2 * k + 2] @ ms[2 * k:2 * k + 2]) + sum(0.5 * (int(blk[a] == k) + int(blk[b] == k)) * Mb
      for (a, b), Mb in Hb.items()) for k in range(N1 // 2)]
E, V = np.linalg.eigh(H.toarray()); Om = V[:, 0]; V = V[:, :3].copy()
grp = [np.unique(code & ~(3 << (2 * k)), return_inverse=True)[1] for k in range(N1 // 2)]
def cond(psi, k):                                    # part k's conditional energy given the rest's actual configuration
    num = np.real(np.conj(psi) * (HP[k] @ psi)); p = np.abs(psi) ** 2
    sn, sp_ = np.bincount(grp[k], num), np.bincount(grp[k], p)
    with np.errstate(all='ignore'): return np.where(sp_[grp[k]] > 1e-28, sn[grp[k]] / sp_[grp[k]], 0.0)
def loc(psi, k):
    with np.errstate(all='ignore'): return np.where(np.abs(psi) > 1e-14, np.real(HP[k] @ psi) / psi, 0.0)
def src(psi, mode):
    p = np.abs(psi) ** 2
    if mode == 'lit': per = [cond(psi, k) - Om @ (HP[k] @ Om) for k in range(6)]
    elif mode == 'cond': per = [cond(psi, k) - cond(Om, k) for k in range(6)]
    else: per = [loc(psi, k) - loc(Om, k) for k in range(6)]
    per = [np.where(p > 1e-28, e, 0.0) for e in per]; S = sum(per); mu_ = p @ S
    return mu_, np.sqrt(p @ (S - mu_) ** 2), np.array([p @ e for e in per]), np.array([np.sqrt(p @ (e - p @ e) ** 2) for e in per]), S
X = hop(1, 0) @ Om; Xl = X / np.linalg.norm(X); exc = {'eig1': V[:, 1], 'eig2': V[:, 2], 'local': Xl}
tgt = {k_: v_ @ (H @ v_) - E[0] for k_, v_ in exc.items()}
lit0, vr0 = src(Om, 'lit'), src(Om, 'loc')
check('D1 vacuum: with the literal reference (vacuum phase on the same edges, a constant) the frozen sea\'s actual '
      'configuration makes the source fluctuate; with VR (vacuum odds at the same configuration) it is 0 everywhere',
      lit0[1] > 0.1 and np.abs(vr0[4]).max() < 1e-12 and abs(src(Om, 'cond')[1]) < 1e-12,
      f'sd of total: literal {lit0[1]:.4f} (per part {lit0[3][0]:.4f}); VR {np.abs(vr0[4]).max():.0e}')
cm = {k_: src(v_, 'cond')[0] / tgt[k_] for k_, v_ in exc.items()}; lv_ = {k_: src(v_, 'loc') for k_, v_ in exc.items()}
lit = {k_: src(v_, 'lit') for k_, v_ in exc.items()}
eigok = max(np.abs(lv_[k_][4] - tgt[k_])[np.abs(exc[k_]) ** 2 > 1e-28].max() for k_ in ('eig1', 'eig2'))
check('D2 charge-neutral excitations: subtracting part-conditioned vacuum phases loses energy (mean/target below 0.9); subtracting '
      'local phases at the same configuration keeps the mean exactly, gives a noise-free total for every eigenstate, '
      'and puts a local excitation\'s source on its own block and neighbours',
      max(cm.values()) < 0.9 and all(abs(lv_[k_][0] - tgt[k_]) < 1e-10 for k_ in exc) and eigok < 1e-10
      and lv_['local'][2][3] < 0.01 < lv_['local'][2][0] and lv_['local'][3][3] < 0.5 * lit['local'][3][3],
      'cond mean/target ' + ', '.join(f'{v_:.3f}' for v_ in cm.values()) + f'; eigen total dev {eigok:.0e}; local block means '
      + ' '.join(f'{x:.3f}' for x in lv_['local'][2]) + f'; far sd {lv_["local"][3][3]:.3f} vs literal {lit["local"][3][3]:.3f}')

# ------------------------------------------------------------------ E. estimates
print('== E. ESTIMATES (supplied SM content and measured numbers; not theorems)')
ainv = 137.035999084; Am = ainv / (4 * np.pi); b8 = 8 / (6 * np.pi ** 2); k_no = b8 / (3 * Am)
mLe = 0.511e-3 * 2 * np.sqrt(8 * np.pi) / 1.220890e19
resid = k_no * (dR[1] * 3) * (mLe / sz[2]['m']) ** pL; lvE = lv0[2] * (mLe / sz[2]['m']) ** 2
print(f'   alpha in a potential: no VR |dln a/dPhi| = {k_no:.2e} (Yb+ bound 1.4e-8); VR residual ~{resid:.0e}; photon running LV at the electron ~{lvE:.0e}')
fVP = lambda Z, A_: 0.711 * Z * (Z - 1) / A_ ** (1 / 3) / (A_ * 931.494) * (2 / (3 * np.pi * ainv)) * (np.log(386.16 / (1.2 * A_ ** (1 / 3))) - 0.5772 - 5 / 6)
etaVP = fVP(78, 195.08) - fVP(22, 47.87)
print(f'   reference at the actual links instead of no field: no running (1/alpha(M_Z) {ainv:.2f} vs 128.94 measured), and the')
print(f'   vacuum-polarisation part of nuclear Coulomb energy stops weighing: eta(Pt,Ti) ~ {etaVP:.1e} vs MICROSCOPE 3e-15')
print('   G_TT/G_N: 1 under VR (sea removed) vs 0.81 without (induced-response, 24 Dirac) vs Hulse-Taylor 0.998(2); c_GW = edge cone')
print('   colour links: a bare plaquette gives Lambda_QCD ~ 1/L, baryons fall with 4/3 of the lapse (gamma_eff - 1 = -1/2 vs Cassini')
print('   2.3e-5, proper-couplings); VR\'s unit at one proper wavelength holds Lambda_QCD, so m_p, fixed in proper units')
print(f'   fermion cones: no response law changes a speed ratio; one-loop link dressing O(alpha/pi) = {1 / (np.pi * ainv):.1e} x f,')
print('   f unprotected, vs LEP 1e-11 and LHAASO 3e-19: an update gap of the additive-mass class (not computed here)')
print('   Lambda: VR gives zero vacuum Lambda; the measured 1.1e-123 rho_P needs a geometric term (w = -1 exactly); under rule U')
print('   eps also swings by 16 per 2^3 split cycle (tau L^3 fixed while L doubles)')
check('E1 arithmetic: VR residual and photon LV far below bounds; wrong reference fails MICROSCOPE by > 1e8',
      resid < 1e-25 and lvE < 1e-30 and etaVP > 1e8 * 3e-15 and abs(k_no - 4.13e-3) < 1e-5)
print('supplied: tick, sea branch, site-phase links, free sea, static cells, tori and fits; frustum carrier, kappa = 1; 1D toy,')
print('  2-site parts, shared bonds; QED comparator, SM charges, measured numbers; VR itself (adopted, not derived).')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
