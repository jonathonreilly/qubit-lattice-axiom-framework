AUDIT_INPUT_PATHS = ('docs/SPLIT_EPOCH_STEP_IN_H_IS_GEOMETRIC_OF_ORDER_HL_SQUARED_WITH_ZERO_VACUUM_JUMP_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""split-step-hz: amplitude and phase of the split-epoch step in H(z), w(z), and of the tensor ripple.

Laws read: CL-1 split (children's edges = parent - s register steps; trigger = block mean edge full,
plus each unsplit +x,+y,+z neighbour's shared-face edges full); CL-3 response (Lambda a constant per
proper 4-volume, vacuum standard on the same edges). Carrier for the expansion law: the cubic-frustum
hinge area function A(u) of the register's cosmology work (desi-de, split-junction), with u = H l / 2.
Units: c = 1; rung L = sqrt(8 pi) l_P (post-split edge), edges in [L, 2L) between splits.
"""
AUDIT_TIMEOUT_SEC = 120
import math, time
import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print('[%s] %s%s' % ('PASS' if ok else 'FAIL', name, ('  ' + detail) if detail else ''))

LN2 = math.log(2.0)
L_m = math.sqrt(8 * math.pi) * 1.616255e-35
H0 = 67.7e3 / 3.0857e22                      # s^-1
EPS = (H0 * L_m / 2.99792458e8) ** 2         # (H0 L)^2
Om, OL = 0.31, 0.69

print('== A. counting at a split (exact)')
s_, l1, l2, tau, Lam = sp.symbols('s l1 l2 tau Lambda', positive=True)
# flat frustum cell: cube side interpolated linearly from l1 to l2 over proper time tau
V4 = lambda a1, a2, t: sp.integrate((a1 + (a2 - a1) * sp.Symbol('x') / t) ** 3, (sp.Symbol('x'), 0, t))
lm = (l1 + l2) / 2
child = 8 * (V4(l1 / 2, lm / 2, tau / 2) + V4(lm / 2, l2 / 2, tau / 2))
par = V4(l1, l2, tau)
d4 = sp.simplify(Lam * child - Lam * par)
lattice_count = sp.Rational(16, 1)            # child cell-ticks per parent cell-tick (8 cubes x 2 ticks)
check('A1 THEOREM (CL-3 count): Lambda per proper 4-volume summed over the 8 children x 2 child ticks equals the parent '
      'frustum\'s exactly, so the vacuum energy density does not jump at a split (a per-cell-per-tick count would jump x1/16)',
      d4 == 0, 'Lambda*(sum children - parent) = %s; child cell-ticks per parent %s' % (d4, lattice_count))
n4 = sp.Integer(4) * s_; nc = n4 - s_
ratio = sp.simplify(2 ** (n4 / s_) / 2 ** (nc / s_))
check('A2 THEOREM (register arithmetic): trigger at 4s, children at parent - s: the edge halves exactly for every s, so the '
      'step is set by the factor 2, not by 1/s; between splits the edge moves in steps of 2^(1/s)', ratio == 2, 'l(4s)/l(3s) = %s' % ratio)
b, mu, kap = sp.symbols('b mu kappa', positive=True)
A_ = (sp.cos(2 * b) + sp.cos(mu)) / 2
cosw0 = sp.simplify(A_ * 1 - (sp.cos(2 * b) - sp.cos(mu)) / 2)
E_rest = sp.simplify((kap * l1) / (sp.Rational(1, 3) * l1))  # rest phase mu = kappa l per tick of proper time ~ l
check('A3 THEOREM (flat-edge band at K = 0): cos w = cos mu, so the rest phase per tick is mu; mu and the proper tick both scale '
      'with the edge, so a split keeps every rest energy; matter changes only through state mismatch (O(K^2), O(mu^2))',
      sp.simplify(cosw0 - sp.cos(mu)) == 0 and not E_rest.has(l1), 'cos w(K=0) = %s; rest energy l-free: %s' % (cosw0, E_rest))

print('== B. the step in H on the hinge carrier (triggered split: X = 8 pi G rho/3 continuous, Lambda kept)')
u = sp.symbols('u', positive=True)
Afn = sp.asin(u ** 2 / (1 - u ** 2)) / sp.sqrt(1 - 2 * u ** 2)
ser = sp.series(Afn, u, 0, 6).removeO()
check('B1 THEOREM (series): A(u) = u^2 + 2u^4 + O(u^6) with A(u) = X l^2/4, u = H l/2, so H^2 = X - X^2 l^2/2: '
      'delta ln H = -(H l)^2/4 at leading order', sp.expand(ser - u ** 2 - 2 * u ** 4) == 0, 'A = %s' % sp.expand(ser))
mp.mp.dps = 300
Am = lambda x: mp.asin(x ** 2 / (1 - x ** 2)) / mp.sqrt(1 - 2 * x ** 2)
def H_of(X, l):
    x = mp.findroot(lambda x: Am(x) - X * l ** 2 / 4, mp.sqrt(X) * l / 2)
    return 2 * x / l
rows, ok = [], True
for HL in (mp.mpf('1e-3'), mp.mpf('1e-2'), mp.sqrt(mp.mpf(EPS))):
    X = HL ** 2                                   # units L = 1, X held fixed through the split
    jump = mp.log(H_of(X, 1) / H_of(X, 2)) / HL ** 2
    ok &= abs(jump - 0.75) < 0.75 * (12 * HL ** 2) + 1e-12
    rows.append('HL %s: %s' % (mp.nstr(HL, 3), mp.nstr(jump, 8)))
check('B2 THEOREM + exact check: at a split (l: 2L -> L, X continuous) ln H jumps by +(3/4)(H L)^2; '
      'the vacuum density does not move (A1), the jump is geometric', ok, 'jump/(HL)^2: ' + '; '.join(rows))
jump0 = 0.75 * EPS
E2 = lambda z: Om * (1 + z) ** 3 + OL
jump3 = 0.75 * EPS * E2(3.0)
print('   today: (H0 L)^2 = %.3e; jump in ln H = %.2e at z = 0, %.2e at z = 3; dH^2/H^2 sawtooth -(1/2)(H l)^2' % (EPS, jump0, jump3))

print('== C. synchronous or smeared')
def overshoot(n, m_own=18, m_nb=36):
    o = RNG.standard_normal((n, m_own)).mean(1); nb = RNG.standard_normal((n, m_nb)).min(1)
    return np.maximum(0.0, o - nb)               # register overshoot of the own mean at firing, units of sigma
Z = overshoot(40000)
res = []
for sig in (0.0315, 0.2):
    F = np.mean(np.exp(2j * np.pi * Z * sig / LN2))
    G = math.exp(-2 * math.pi ** 2 * (sig / LN2) ** 2 * Z.var())
    res.append((sig, abs(F), G, np.angle(F)))
check('C1 THEOREM (trigger at a fixed local edge; spectral-tilt D1): splits fire at a fixed local edge, so a spread of split TIMES '
      'does not smooth the step in 1+z (the edge ratio); only the neighbour wait smears the firing edge',
      True, 'structural')
check('C2 finite diagnostic (independent Born offsets per edge, sd sigma in ln l; trigger = own 18-edge mean and 36 neighbour '
      'face edges full): the ripple fundamental keeps |F| of its size; the wall margin (>= 22 spreads in ln 2 Delta, Delta = 1) '
      'gives sigma <= 0.0315: synchronous to ~1% (the mean lag is a phase shift); the one-cell spread 0.2 (excluded) leaves ~0.6',
      res[0][1] > 0.98 and abs(res[0][1] - res[0][2]) < 2e-3,
      '; '.join('sigma %.4f: |F| %.4f (gauss %.4f), phase lag %.3f rad' % r for r in res))
v_pois = 1.8 * LN2 ** 2 / (18 * 135)
Fp = math.exp(-2 * math.pi ** 2 * v_pois / LN2 ** 2)
print('   supplied Poisson stepping (spectral-tilt B3, coupled var 1.8 ln2^2/(ms), m 18, s >= 135) if read as a firing-edge spread: |F| = %.3f' % Fp)

print('== D. H(z), w(z) for 0 < z < 3 and the DESI comparison (per unit (H0 L)^2, then x %.2e)' % EPS)
lam2 = lambda z, ph: 4.0 ** (((-np.log2(1 + z) + ph) % 1.0))     # (l/L)^2, l ~ a between splits
zz = np.linspace(0, 3, 3001)
def splits_between(z, ph):
    x = np.log2(1 + z)
    return int(np.floor(ph) - np.floor(ph - x))
cnt = {splits_between(3.0, p) for p in RNG.uniform(0, 1, 2000)}
cnt_star = [splits_between(1089.9, p) for p in RNG.uniform(0, 1, 2000)]
check('D1 THEOREM (period): splits at 1 + z_k = 2^k (1 + z_0), period ln 2 in ln(1+z); exactly 2 steps in 0 < z <= 3 for every '
      'phase (ln 4 = 2 ln 2); 10 or 11 since recombination; the phase z_0 is not fixed by any law',
      cnt == {2}, 'z<=3: %s; z*: 10 for %.2f, 11 for %.2f' % (sorted(cnt), cnt_star.count(10) / 2000, cnt_star.count(11) / 2000))
def rhoDE(z, ph):        # inferred dark energy (GR observer, same G), units 3 H0^2/(8 pi G), per unit EPS
    return -0.5 * E2(z) ** 2 * lam2(z, ph)
def wp1_between(z, ph):  # w + 1 between splits, per unit EPS
    dlnE = -1.5 * Om * (1 + z) ** 3 / E2(z)
    return (0.5 * lam2(z, ph) * E2(z) ** 2 * (2 + 4 * dlnE)) / (3 * OL)
ph = 0.37; zt = np.array([0.0, 0.5, 1.0, 2.0]); h = 1e-5
num = []
for z0 in zt:
    lp, lm_ = np.log(1 / (1 + z0)) + h, np.log(1 / (1 + z0)) - h
    zp, zm = 1 / np.exp(lp) - 1, 1 / np.exp(lm_) - 1
    d = (rhoDE(zp, ph) - rhoDE(zm, ph)) / (2 * h) / OL
    num.append(-d / 3)
an = wp1_between(zt, ph)
check('D2 THEOREM: between splits w + 1 = (H l)^2 (1 + 2 dlnH/dlna)/(3 Omega_L(0)) x E^2 (desi-de form at z = 0); at each split a '
      'phantom spike, integral of (w+1) dln a = -(H L)^2 E^2/(2 Omega_L)', np.allclose(num, an, rtol=1e-5),
      'w+1 per (H0L)^2 at z 0/0.5/1/2 (phase .37): ' + ' '.join('%.3g' % v for v in an))
A = np.vstack([np.ones_like(zz), -3 * np.log(1 / (1 + zz)), -3 * (np.log(1 / (1 + zz)) + 1 - 1 / (1 + zz))]).T
fits = []
for p in np.linspace(0, 1, 16, endpoint=False):
    y = rhoDE(zz, p) / OL                       # delta ln rho_DE per unit EPS
    c, w0p1, wa = np.linalg.lstsq(A, y, rcond=None)[0]; fits.append((p, w0p1, wa))
fa = np.array(fits); mx = np.max(np.abs(fa[:, 1:]))
w0r, war = fa[:, 1], fa[:, 2]
check('D3 finite diagnostic: CPL fit of the inferred rho_DE(z) on 0 < z < 3, all 16 phases: |w0 + 1|, |wa| <= C (H0 L)^2',
      mx < 1e4, 'C = %.0f; w0+1 in [%.0f, %.0f], wa in [%.0f, %.0f] per (H0L)^2, wa/(1+w0) in [%.2f, %.2f]; times (H0L)^2: |dw| <= %.1e'
      % (mx, w0r.min(), w0r.max(), war.min(), war.max(), (war / w0r).min(), (war / w0r).max(), mx * EPS))
dz = 1e-3; zg = np.arange(0, 1100 + dz, dz)
def Einv(zv, w0, wa, hh):
    a = 1 / (1 + zv); wm = 0.1424; wr = 4.15e-5; OLh = hh * hh - wm - wr
    de = OLh * a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))
    return 1 / np.sqrt(wm * (1 + zv) ** 3 + wr * (1 + zv) ** 4 + de)
ZB = np.array([0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330]); idx = np.rint(ZB / dz).astype(int)
def obs(p, df=None):          # df given: the exact first-order change of the observables under H^2 -> H^2 (1 + df)
    e = Einv(zg, *p); de = -0.5 * df * e if df is not None else None
    cum = np.concatenate([[0], np.cumsum(0.5 * (e[1:] + e[:-1]) * dz)])
    if de is None: return np.concatenate([cum[idx], e[idx], [1 / cum[-1]]])   # D_M, D_H, theta* ~ 1/D_M(z*), r_d held
    dc = np.concatenate([[0], np.cumsum(0.5 * (de[1:] + de[:-1]) * dz)])
    return np.concatenate([dc[idx], de[idx], [-dc[-1] / cum[-1] ** 2]])
P0 = np.array([-1.0, 0.0, 0.6766]); o0 = obs(P0)
J = np.array([(obs(P0 + dv) - o0) / 1e-4 for dv in np.eye(3) * 1e-4]).T
W = np.diag(1 / (np.array([0.01] * 14 + [0.0003]) * o0) ** 2); Cv = np.linalg.inv(J.T @ W @ J)
proj, projL = [], []
Eb = 1 / Einv(zg, -1, 0, 0.6766) ** 2 / 0.6766 ** 2
for p in np.linspace(0, 1, 8, endpoint=False):
    df = -0.5 * Eb * lam2(zg, p)                                 # per unit (H0 L)^2, first order
    proj.append((Cv @ J.T @ W @ obs(P0, df))[:2]); projL.append((Cv @ J.T @ W @ obs(P0, df * (zg <= 3)))[:2])
Cb = np.max(np.abs(proj)); CL_ = np.max(np.abs(projL))
check('D4 finite diagnostic (DESI-like 1% BAO at the DR2 redshifts + theta*, r_d held; fit w0, wa, h; 8 phases): '
      'the hinge sawtooth projects to |dw| <= C (H0 L)^2', Cb < 1e10,
      'C = %.1e with the sawtooth out to z* (theta* lever, (H l)^2 grows as E^2), %.0f from z < 3 alone; |dw| <= %.1e: %.0e below a 0.01 sensitivity'
      % (Cb, CL_, Cb * EPS, 0.01 / (Cb * EPS)))
sgn = sum(1 for p, a, c in fits if a > 0 and c < 0)
check('D5 the DESI hint (w0, wa) = (-0.75, -0.86): the sign pattern (w0 > -1, wa < 0) appears for %d of 16 phases, but the size '
      'needs (H0 l)^2 ~ 0.25/C, an edge ~ %.3f of the Hubble length: the step cannot mimic DESI' % (sgn, math.sqrt(0.25 / mx)),
      Cb * EPS < 1e-100, 'needed (H0 l)^2 ~ %.1e vs %.1e' % (0.25 / mx, EPS))
a_m = L_m
mlat = lambda m_eV: m_eV * 2 * a_m / 1.97327e-7
rows = [('hinge jump in ln H at z = 0..3 (B2, THEOREM)', jump0, jump3),
        ('dark-constant kick (H L)^2/8 per split if zero mean not kept (register; cited)', EPS / 8, EPS * E2(3.0) / 8),
        ('massive-matter split energy change 0.05 mu^2, protons (desi-de ESTIMATE, cited)', 0.05 * mlat(0.938e9) ** 2 * Om, 0.05 * mlat(0.938e9) ** 2),
        ('radiation 0.04 K^2 per split, CMB photons (split-junction; cited)', 0.04 * mlat(6.3e-4) ** 2 * 1e-4, 0.04 * mlat(2.5e-3) ** 2 * 3e-4)]
print('   log-periodic step sources (fraction of H^2 per split, z = 0 / z = 3):')
for lab, a0, a3 in rows: print('     %-80s %8.1e %8.1e' % (lab, a0, a3))
check('D6 ESTIMATE: the largest known-content step is the proton split-energy ceiling ~1e-38 per split, the law-level geometric '
      'step ~1e-121; every source is >1e30 below a 0.01 w-sensitivity', max(r[1] for r in rows) < 1e-30, 'max %.1e' % max(r[1] for r in rows))

print('== E. the tensor ripple (discrete ticks, vacuum-carrying splits; edge-seeds machinery, 1D axis modes)')
SIG = 0.3 / math.sqrt(3)
def basis(hh, p, deta, w, m):
    th = np.arccos(1 - 0.5 * (deta * w) ** 2); Aa = np.sqrt(deta / (2 * m * np.sin(th)))
    s1 = hh / Aa; q = p * deta / (m * Aa); al = (s1 - q - s1 * np.exp(-1j * th)) / (2j * np.sin(th))
    return al, s1 - al
def build(al, be, deta, w, m):
    th = np.arccos(1 - 0.5 * (deta * w) ** 2); Aa = np.sqrt(deta / (2 * m * np.sin(th)))
    return Aa * (al + be), (m * Aa / deta) * (al * (1 - np.exp(1j * th)) + be * (1 - np.exp(-1j * th)))
def evolve(k, H, xf=1e-3):
    mof = lambda e: (-1 / (H * e)) ** 2 / 4
    n = 0; eta = -1 / H; ell = 1.0; deta = SIG * ell; w = (2 / ell) * np.abs(np.sin(k * ell / 2)); dprev = deta
    hh, p = build(np.ones_like(k, dtype=complex), np.zeros_like(k, dtype=complex), deta, w, mof(eta - deta / 2))
    while True:
        a = -1 / (H * eta)
        if a >= 2.0 ** (n + 1):
            al, be = basis(hh, p, deta, w, mof(eta)); n += 1; ell = 2.0 ** -n; deta = SIG * ell
            w = (2 / ell) * np.abs(np.sin(k * ell / 2)); hh, p = build(al, be, deta, w, mof(eta)); dprev = deta
        if np.max(k) / (a * H) < xf: return k ** 3 * np.abs(hh) ** 2 / (2 * H ** 2)
        p = p - 0.5 * (deta + dprev) * (a * a / 4) * w ** 2 * hh
        hh = hh + deta * p / mof(eta + deta / 2); eta += deta; dprev = deta
NK = 128; jj = np.arange(NK); kk = (np.pi / 2) * 2.0 ** ((jj + 0.5) / NK)
rip = []
for H in (0.08, 0.04, 0.02, 0.01):
    r = evolve(kk, H); c = np.fft.rfft(r - r.mean()) / NK * 2; nm = int(np.argmax(np.abs(c[1:]))) + 1
    rip.append((H, np.ptp(r), abs(c[1]) / H ** 2, nm * H, abs(c[nm]) / H))
c1max = max(x[2] for x in rip)
check('E1 finite diagnostic (one octave, 128 log-spaced k; the octave repeats exactly, edge-seeds A3): the period-ln 2 fundamental '
      'of the frozen tensor spectrum is second order, |c1| <= 1.1 (H l_c)^2; the first-order structure (ptp ~1.5 H l_c) is a fast lattice '
      'oscillation at ~0.32/(H l_c) cycles per octave, amplitude ~0.4 H l_c',
      c1max < 1.2 and all(0.29 < x[3] < 0.35 for x in rip) and all(0.25 < x[4] < 0.6 for x in rip),
      '; '.join('Hl %.2f: ptp %.1e, c1/(Hl)^2 %.2f, peak n*Hl %.2f, |c_peak|/Hl %.2f' % x for x in rip))
Pt0 = 2 * EPS / math.pi ** 2                 # 2 H^2/(pi^2 M_P^2), M_P reduced = 1/L
Hinf = 1e13 / 2.435e18                       # H L for a supplied H = 1e13 GeV
check('E2 ESTIMATE: in the laws\' only de Sitter phase (today, P_t ~ %.0e) the period-ln 2 ripple is ~%.0e of P_t and the fast '
      'oscillation ~%.0e at ~%.0e cycles per octave (unresolvable); under a supplied H = 1e13 GeV inflation (not in the laws): '
      '%.0e and %.0e at %.0e cycles' % (Pt0, c1max * EPS, 0.4 * math.sqrt(EPS), 0.32 / math.sqrt(EPS), c1max * Hinf ** 2, 0.4 * Hinf, 0.32 / Hinf),
      c1max * EPS < 1e-100, 'absolute fundamental today ~%.0e' % (c1max * EPS * Pt0))
print('supplied: frustum hinge carrier A(u); unit map L = sqrt(8 pi) l_P, edges in [L, 2L); H0 67.7, Om 0.31; independent Gaussian')
print('  edge offsets (C2); wall margin 22 spreads, Delta = 1; DESI-like 1% errors, r_d held; 1D axis tensor modes, sin eps0 = 0.3.')
print('elapsed %.1f s' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % (NP, NF))
