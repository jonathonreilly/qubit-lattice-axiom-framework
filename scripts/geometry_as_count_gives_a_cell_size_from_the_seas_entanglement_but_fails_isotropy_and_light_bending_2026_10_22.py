#!/usr/bin/env python3
"""Geometry as count: each cut bond one area quantum a^2, S = eta x N_bonds, Jacobson 1/(4G) = eta/a^2.
(supplied model; finite diagnostic; no physical identification)

 A  exact: Jacobson algebra and unit-map comparison; Gaussian first law; bond count per Euclidean
    area = |n|_1 and graph distance = L1 against the sea's isotropic cone; a split cascade with the
    tied block tick is conformally flat -> PPN gamma = -1 and no vacuum 1/r field; count curvature
    comes in O(1) quanta (2D quadtree Gauss-Bonnet; equilateral simplices never tile flat space).
 B  finite: eta_100 of the pi-flux sea and of a lattice scalar (chain decomposition); slab entropy
    per cut bond and per Euclidean area for (100), (110), (111) cuts on 12^3 and 16^3 antiperiodic
    tori; Bisognano-Wichmann locality per transverse mode; a/l_P = 2 sqrt(eta) for supplied contents.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/GEOMETRY_AS_COUNT_GIVES_A_CELL_SIZE_FROM_THE_SEAS_ENTANGLEMENT_BUT_FAILS_ISOTROPY_AND_LIGHT_BENDING_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120
import os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal, eigh, eigvalsh
from scipy.interpolate import CubicSpline

T0 = time.monotonic(); PASS = FAIL = 0
rng = np.random.default_rng(20261022)


def check(name, ok, detail=''):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))


def hb(x):
    x = np.clip(x, 1e-15, 1 - 1e-15)
    return float(-(x * np.log(x) + (1 - x) * np.log(1 - x)).sum())

# ---------------------------------------------------------------- A exact
print('A. exact')
eta, a, G, lP = sp.symbols('eta a G l_P', positive=True)
# Jacobson: S = eta_area A, dQ = T dS, T = kappa/2pi  ->  G = 1/(4 eta_area); count: eta_area = eta/a^2
Gc = sp.solve(sp.Eq(1 / (4 * G), eta / a**2), G)[0]
a_over_lP = sp.simplify(sp.solve(sp.Eq(Gc, lP**2), a)[0] / lP)
need_A = sp.solve(sp.Eq(a**2, 8 * sp.pi * Gc), eta)[0]          # hinge unit u = site
need_B = sp.solve(sp.Eq((2 * a)**2, 8 * sp.pi * Gc), eta)[0]    # hinge unit u = 2 sites
c_hinge = sp.simplify(a**2 / (8 * sp.pi * Gc))
check('A1 count Jacobson: G = a^2/(4 eta), a/l_P = 2 sqrt(eta); hinge-sum coefficient in site units = eta/(2 pi)',
      sp.simplify(a_over_lP - 2 * sp.sqrt(eta)) == 0 and sp.simplify(c_hinge - eta / (2 * sp.pi)) == 0
      and need_A == 2 * sp.pi and need_B == sp.pi / 2,
      f'unit map needs eta = {need_A} (site reading) or {need_B} (cell-rung reading)')

# Gaussian first law on a random 1D chain (identity, constrains nothing)
N1 = 40; Hc = np.diag(.5 * (-1.0)**np.arange(N1) + rng.normal(0, .1, N1)) + np.diag(np.ones(N1 - 1), 1) + np.diag(np.ones(N1 - 1), -1)
dH = np.diag(rng.normal(0, 1, N1 - 1), 1); dH = dH + dH.T
def CA(Hm):
    w, v = np.linalg.eigh(Hm); V = v[:20, w < 0]; return V @ V.T
C0 = CA(Hc); x, U = np.linalg.eigh(C0); x = np.clip(x, 1e-14, 1 - 1e-14); Kmod = (U * np.log((1 - x) / x)) @ U.T
res = []
for d in (1e-3, 1e-4):
    C1 = CA(Hc + d * dH); x1 = np.linalg.eigvalsh(C1); x0 = np.linalg.eigvalsh(C0)
    res.append((hb(x1) - hb(x0), np.trace(Kmod @ (C1 - C0))))
r2 = (res[0][1] - res[0][0]) / (res[1][1] - res[1][0])
check('A2 Gaussian first law dS = d<K>, remainder >= 0 and quadratic', res[1][1] - res[1][0] > 0 and 80 < r2 < 120 and abs(res[1][1] / res[1][0] - 1) < .05,
      f'd = 1e-4: dS = {res[1][0]:.4e}, d<K> = {res[1][1]:.4e}; remainder ratio (1e-3 : 1e-4) {r2:.1f}')

# bond count per Euclidean area and graph distance
L = 12; X, Y, Z = np.meshgrid(*(np.arange(L),) * 3, indexing='ij'); cnt = []
for lab, nrm in (((X), 1), (((X + Y) % L), np.sqrt(2)), (((X + Y + Z) % L), np.sqrt(3))):
    m = lab < L // 2; cut = sum(int((m != np.roll(m, -1, ax)).sum()) for ax in range(3))
    cnt.append(cut / (2 * L * L * nrm))       # torus slab: two planes, each of Euclidean area L^2 nrm
q = 1e-3; Ed = [2 * np.sqrt(sum(np.cos(np.pi / 2 + q * u)**2 for u in dirn)) / q
                for dirn in ((1, 0, 0), (1 / np.sqrt(2), 1 / np.sqrt(2), 0), (1 / np.sqrt(3),) * 3)]
check('A3 cut bonds per Euclidean area = |n|_1 and graph distance (L,L,L) = 3L, while the sea cone is isotropic',
      np.allclose(cnt, [1, np.sqrt(2), np.sqrt(3)]) and np.ptp(Ed) < 1e-5,
      f'bonds/area (100),(110),(111) = {cnt[0]:.4f}, {cnt[1]:.4f}, {cnt[2]:.4f}; cone speed {Ed[0]:.6f} all three: count length/matter length = sqrt(3) along (111)')

# conformally flat count geometry (tied block tick) -> gamma = -1; linearised vacuum Ricci kills 1/r
t, x1_, y1_, z1_, Mg = sp.symbols('t x y z M', real=True)
psi = sp.Function('psi')(x1_, y1_, z1_); co = [t, x1_, y1_, z1_]; etam = sp.diag(-1, 1, 1, 1)
Ric = sp.Matrix(4, 4, lambda i, j: -2 * sp.diff(psi, co[i], co[j]) - etam[i, j] * sum(etam[k, k] * sp.diff(psi, co[k], 2) for k in range(4)))
rr = sp.sqrt(x1_**2 + y1_**2 + z1_**2); sub = Ric.subs(psi, -Mg / rr).doit()
gam = sp.Symbol('gamma'); g00 = -(1 - 2 * Mg / rr); gii = (1 - 2 * Mg / rr)    # g = Omega^2 eta with Omega^2 = -g00
gamma_val = sp.solve(sp.Eq(sp.series(gii, Mg, 0, 2).removeO(), 1 + 2 * gam * Mg / rr), gam)[0]
check('A4 tied-tick splits give g = Omega^2 eta: PPN gamma = -1 (no light bending, no Shapiro delay), and R_ab = 0 forces psi linear',
      gamma_val == -1 and sp.simplify(sub[1, 2]) != 0,
      f'gamma = {gamma_val}; R_xy for psi = -M/r: {sp.simplify(sub[1, 2])}; Cassini gamma-1 = (2.1 +- 2.3)e-5 -> {2 / 2.3e-5:.1e} sigma')

# count curvature quanta: 2D quadtree with a refined 2x2 patch; faces regular polygons of unit edges
nq, lo, hi = 8, 3, 5; faces = []
for i in range(nq):
    for j in range(nq):
        if lo <= i < hi and lo <= j < hi: faces += [(i + u, j + w, .5) for u in (0, .5) for w in (0, .5)]
        else: faces.append((i, j, 1.))
vs = sorted({c for (x0, y0, s) in faces for c in ((x0, y0), (x0 + s, y0), (x0, y0 + s), (x0 + s, y0 + s))}); ang = dict.fromkeys(vs, 0.)
for x0, y0, s in faces:
    on = [v for v in vs if x0 - 1e-9 <= v[0] <= x0 + s + 1e-9 and y0 - 1e-9 <= v[1] <= y0 + s + 1e-9
          and min(abs(v[0] - x0), abs(v[0] - x0 - s), abs(v[1] - y0), abs(v[1] - y0 - s)) < 1e-9]
    for v in on: ang[v] += np.pi * (len(on) - 2) / len(on)
dq = np.array([2 * np.pi - ang[v] for v in vs if 0 < v[0] < nq and 0 < v[1] < nq])
th3, th4 = np.arccos(1 / 3), np.arccos(1 / 4)
check('A5 count curvature: quadtree deficits are O(1) quanta summing to 0; equilateral 3- and 4-simplices tile no flat space',
      abs(dq.sum()) < 1e-12 and abs(dq).max() > 1 and abs(2 * np.pi / th3 - round(2 * np.pi / th3)) > .1,
      f'deficits/pi = {[float(u) for u in sorted(set(np.round(dq / np.pi, 3)))]} at {int((abs(dq) > 1e-9).sum())} vertices; '
      f'2pi/arccos(1/3) = {2 * np.pi / th3:.4f}, 2pi/arccos(1/4) = {2 * np.pi / th4:.4f}; edge deficits n=5: {2 * np.pi - 5 * th3:+.4f}, n=6: {2 * np.pi - 6 * th3:+.4f} rad')

# ---------------------------------------------------------------- B finite
print('B. finite diagnostics (pi-flux sea = tick eps0 -> 0 limit; lattice scalar)')
Nc = 600; nA = Nc // 2
def s_f(M):
    w, v = eigh_tridiagonal(M * (-1.0)**np.arange(Nc), np.ones(Nc - 1)); V = v[:nA, w < 0]
    return hb(np.linalg.eigvalsh(V @ V.T))
def s_b(m):
    Km = np.diag(np.full(Nc, 2 + m * m)) - np.eye(Nc, k=1) - np.eye(Nc, k=-1); w, v = eigh(Km)
    Xm = (v / (2 * np.sqrt(w))) @ v.T; Pm = (v * (np.sqrt(w) / 2)) @ v.T
    nu = np.sqrt(np.clip(np.linalg.eigvals(Xm[:nA, :nA] @ Pm[:nA, :nA]).real, .25, None)); p_, m_ = nu + .5, nu - .5
    return float((p_ * np.log(p_) - np.where(m_ > 1e-14, m_ * np.log(np.maximum(m_, 1e-300)), 0)).sum())
uf = np.geomspace(.02, 2 * np.sqrt(2) + 1e-9, 40); tf = np.array([s_f(u) for u in uf])
ub = np.geomspace(.03, 2 * np.sqrt(2) + 1e-9, 30); tb = np.array([s_b(u) for u in ub])
def ev(u0, s0, spl, u):
    out = s0 - (1 / 6) * (np.log(u) - np.log(u0)); mk = u >= u0; out[mk] = spl(np.log(u[mk])); return out
Gk = 400; kk = -np.pi + 2 * np.pi * (np.arange(Gk) + .5) / Gk; KY, KZ = np.meshgrid(kk, kk)
Mk = 2 * np.sqrt(np.cos(KY)**2 + np.cos(KZ)**2); eF = ev(uf[0], tf[0], CubicSpline(np.log(uf), tf), Mk)
mk = np.sqrt(4 * np.sin(KY / 2)**2 + 4 * np.sin(KZ / 2)**2); eB = ev(ub[0], tb[0], CubicSpline(np.log(ub), tb), mk)
etaF, etaB = eF.mean(), eB.mean(); slf = np.polyfit(np.log(uf[:5]), tf[:5], 1)[0]; slb = np.polyfit(np.log(ub[:5]), tb[:5], 1)[0]
check('B1 eta_100 per cut bond: one-mode sea (2 Dirac = 4 Weyl) and one lattice scalar; c = 1 tails',
      abs(etaF - .19664) < 2e-4 and abs(etaB - .02426) < 2e-4 and abs(slf + 1 / 6) < 3e-3 and abs(slb + 1 / 6) < 3e-3,
      f'eta_F = {etaF:.5f} (per Weyl {etaF / 4:.5f}), eta_B = {etaB:.5f}; tail slopes {slf:.4f}, {slb:.4f}')

# slab entropies by orientation on antiperiodic tori
def ktab(Lt):
    k = 2 * np.pi * (np.arange(Lt) + .5) / Lt; A_, B_, C_ = np.meshgrid(k, k, k, indexing='ij')
    g = np.fft.ifftn(1 / np.sqrt(4 * (np.cos(A_)**2 + np.cos(B_)**2 + np.cos(C_)**2)))
    ph = np.exp(1j * np.pi * np.arange(Lt) / Lt); return (g * ph[:, None, None] * ph[None, :, None] * ph[None, None, :]).real.ravel()
def slabS(Lt, mask, T):
    c = np.array(np.nonzero(mask)).T.astype(np.int16); nAa = len(c); HG = np.zeros((nAa, nAa))
    for mu in range(3):
        et = np.ones(nAa) if mu == 0 else (-1.0)**(c[:, 0] % 2 if mu == 1 else (c[:, 0] + c[:, 1]) % 2)
        for sgn in (1, -1):
            idx = np.zeros((nAa, nAa), np.int32); par = np.zeros((nAa, nAa), np.int8)
            for ax in range(3):
                dd = c[:, None, ax].astype(np.int32) - c[None, :, ax] + (sgn if ax == mu else 0)
                qq = np.floor_divide(dd, Lt); dd -= qq * Lt; idx *= Lt; idx += dd; par += (qq & 1).astype(np.int8); del dd, qq
            tmp = T[idx]; del idx; tmp[(par & 1).astype(bool)] *= -1.0; del par
            tmp *= et[:, None]; HG += tmp; del tmp
    HG *= -.5; HG[np.diag_indices(nAa)] += .5
    return hb(eigvalsh(HG, overwrite_a=True, check_finite=False))
rows = {}
for Lt in (12, 16):
    T = ktab(Lt); X, Y, Z = np.meshgrid(*(np.arange(Lt),) * 3, indexing='ij')
    for nm, lab, nb in (('100', X, 1), ('110', (X + Y) % Lt, 2), ('111', (X + Y + Z) % Lt, 3)):
        S = slabS(Lt, lab < Lt // 2, T); rows[(Lt, nm)] = (S / (2 * nb * Lt * Lt), S / (2 * Lt * Lt * np.sqrt(nb)))
    if Lt == 16: wsc = [slabS(Lt, X < w, T) / (2 * Lt * Lt) for w in (4, 5)]
for Lt in (12, 16):
    print(f'   L={Lt}: per bond  ' + ', '.join(f'{nm} {rows[(Lt, nm)][0]:.5f}' for nm in ('100', '110', '111'))
          + ' | per Euclid area ' + ', '.join(f'{rows[(Lt, nm)][1]:.5f}' for nm in ('100', '110', '111')))
pb = [rows[(16, n)][0] for n in ('100', '110', '111')]; pa = [rows[(16, n)][1] for n in ('100', '110', '111')]
pexp = [1 + np.log(pb[i] / pb[0]) / np.log(np.sqrt(i + 1)) for i in (1, 2)]
drift = max(abs(rows[(16, n)][0] / rows[(12, n)][0] - 1) for n in ('100', '110', '111'))
check('B2 entropy per cut bond is orientation dependent (neither bond count nor Euclidean area)',
      pb[0] / pb[2] > 1.4 and pa[2] / pa[0] > 1.15 and drift < .01 and abs(wsc[1] / etaF - 1) < .01,
      f'(100)/(111) per bond {pb[0] / pb[2]:.3f}, per area {pa[2] / pa[0]:.3f}; S ~ A_E |n|_1^p with p = {pexp[0]:.3f}, {pexp[1]:.3f} '
      f'(count: 1, Euclidean: 0); L 12->16 drift {drift:.4f}; (100) width 4, 5 at L=16: {wsc[0]:.5f}, {wsc[1]:.5f} vs infinite {etaF:.5f}')

# Bisognano-Wichmann per transverse mode; share of eta from near-cone modes
bw = []
for Mv in (.1, 2.):
    w, v = eigh_tridiagonal(Mv * (-1.0)**np.arange(Nc), np.ones(Nc - 1)); V = v[:nA, w < 0]
    x, U = np.linalg.eigh(V @ V.T); x = np.clip(x, 1e-13, 1 - 1e-13); Kh = (U * np.log((1 - x) / x)) @ U.T
    bw.append(Kh[nA - 1, nA - 2] / np.pi)        # bond at distance 1 from the cut: (2 pi / v) x 1, v = 2
frac = eF[Mk < .3].sum() / eF.sum()
check('B3 modular Hamiltonian local (boost form) only near the cone; near-cone modes carry little of eta',
      bw[0] > .99 and bw[1] < .9 and frac < .05, f'bond ratio {bw[0]:.4f} at M = 0.1, {bw[1]:.4f} at M = 2; M < 0.3 carries {frac:.4f} of eta_F')

# content table: a / l_P = 2 sqrt(eta)
W = etaF / 4; Vg = 2 * etaB
cont = [('one-mode sea (axiom content)', etaF), ('sea + photon (2 scalars)', etaF + Vg),
        ('1 family 16 Weyl + 12 gauge + 4 Higgs, as fields', 16 * W + 12 * Vg + 4 * etaB),
        ('3 families + 12 gauge + 4 Higgs, as fields', 48 * W + 12 * Vg + 4 * etaB),
        ('1 family + Spin(10) 45 gauge, as fields', 16 * W + 45 * Vg)]
for nm, e in cont: print(f'   {nm:50s} eta = {e:.4f}  a/l_P = {2 * np.sqrt(e):.3f}  G_count/G_hinge(site) = {2 * np.pi / e:6.2f}')
cG = {'Wilson': .01032, 'staggered': .004966}
check('B4 a/l_P = 2 sqrt(eta) without fitting; unit map needs 2.507 (cell rung) or 5.013 (site); Sakharov per Dirac differs',
      abs(2 * np.sqrt(etaF) - .887) < .002 and 2 * np.sqrt(cont[-2][1]) < np.sqrt(8 * np.pi),
      f'one-mode sea a = {2 * np.sqrt(etaF):.3f} l_P; entanglement per Dirac {etaF / 2:.4f} vs induced 4 pi c_G = '
      f'{4 * np.pi * cG["staggered"]:.4f} (staggered), {4 * np.pi * cG["Wilson"]:.4f} (Wilson); hinge coefficient eta/2pi = {etaF / (2 * np.pi):.4f}')

print(f'elapsed {time.monotonic() - T0:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
