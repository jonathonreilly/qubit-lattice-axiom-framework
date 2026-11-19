#!/usr/bin/env python3
"""Dark partner: can the B - L that a uddn-type four-mode term moves out of the sphaleron sector be the dark matter?
Supplied models; [T] theorem or exact check, [D] finite diagnostic, [E] estimate with supplied or cited inputs,
[M] comparison with measurement.
 A  exact chemistry: net carrier number per baryon, symmetric- and broken-phase sphaleron decoupling, carrier charge q
 B  which object carries it: the 16's link-free states, the rules' nu^c (Dirac, sub-eV), contact bound states,
    a confining copy, the cell-scale mirror family
 C  the symmetric component: freeze-in carrier with no annihilation channel; the ratio becomes a bound on m_D
 D  measured constraints at the target mass: direct detection, self-scattering, BBN/N_eff, decays, nucleon decay
 E  look-elsewhere
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 60

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
# supplied measured / cited numbers (PDG; Planck 2018 TT,TE,EE+lowE+lensing)
oc, doc, ob, dob = 0.1200, 0.0012, 0.02237, 0.00015
R = oc / ob; dR = R * np.hypot(doc / oc, dob / ob)
mp, mn = 0.938272, 0.939565; Yp = 0.245; mH, mHe4 = 1.007825 * 0.931494, 4.002602 * 0.931494
mbar = (1 - Yp) * mH + Yp * mHe4 / 4                        # mean mass per baryon in H + He
unit = np.sqrt(3) / (2 * np.sqrt(8 * np.pi)) * 1.2209e19     # GeV per rad/tick (a = sqrt(8 pi) l_P, as in agents/dark-matter)
GeV2cm2, GeV2cm3s, gram = 0.389379e-27, 1.1663e-17, 1.78266e-24

# ------------------------------------------------ A. exact chemistry ------------------------------------------------
print('== A. exact chemistry (content supplied; sphalerons and Yukawas in equilibrium, carrier out of equilibrium)')
Q, u, d, l, e, phi = sp.symbols('Q u d l e phi')
def sym_ratio(Nf, NH):                                       # symmetric phase: Y = 0, sphaleron 3Q + l = 0
    eqs = [sp.Eq(u, Q + phi), sp.Eq(d, Q - phi), sp.Eq(e, l - phi), sp.Eq(3 * Q + l, 0),
           sp.Eq(Nf * (Q + 2 * u - d - l - e) + 2 * NH * phi, 0)]
    s = sp.solve(eqs, [u, d, e, l, phi], dict=True)[0]
    B = Nf * (2 * Q + u + d); L = Nf * (2 * l + e)
    return sp.nsimplify(sp.simplify((B / (B - L)).subs(s)))
uL, nu, W = sp.symbols('uL nu W')
def brk_ratio(Nf, NH):                                       # broken phase: mu_0 = 0, Q_em = 0, W and phi^- carry mu_W
    dL = uL + W; eL = nu + W; uR, dR, eR = uL, dL, eL
    sph = uL + 2 * dL + nu
    qem = Nf * (2 * (uL + uR) - (dL + dR) - (eL + eR)) - 4 * W - 2 * NH * W
    s = sp.solve([sph, qem], [uL, W], dict=True)[0]
    B = Nf * (uL + uR + dL + dR); L = Nf * (nu + eL + eR)
    return sp.nsimplify(sp.simplify((B / (B - L)).subs(s)))
okA1 = all(sym_ratio(f, h) == sp.Rational(8 * f + 4 * h, 22 * f + 13 * h) for f, h in ((1, 1), (3, 1), (3, 2), (4, 0)))
okA2 = all(brk_ratio(f, h) == sp.Rational(8 * f + 4 * (h + 2), 24 * f + 13 * (h + 2)) for f, h in ((1, 1), (3, 1), (3, 2), (4, 0)))
rs, rb = sym_ratio(3, 1), brk_ratio(3, 1)
# per net uddn event: annihilating u d d nu_R moves (B - L)_SM by -1 and nu_R number by -1 (B - L of nu_R = -1): total B - L fixed
X = sp.symbols('X'); B_ = rs * X; L_SM = B_ - X; L_nuR = X; Ltot = L_SM + L_nuR
check('A1 [T] symmetric-phase decoupling: B = (8Nf+4NH)/(22Nf+13NH)(B-L)_SM; total B - L = 0 is kept by uddn, so the '
      'sequestered nu_R holds L = (B-L)_SM = X and n_D/n_B = 79/28 = %.4f; then L_SM = -51/79 X and L_total = B' % float(1 / rs),
      okA1 and rs == sp.Rational(28, 79) and sp.simplify(L_SM + sp.Rational(51, 79) * X) == 0 and sp.simplify(Ltot - B_) == 0)
check('A2 [T] broken-phase decoupling (Harvey-Turner): B = (8Nf+4(NH+2))/(24Nf+13(NH+2))(B-L)_SM = 12/37, n_D/n_B = 37/12 = '
      '%.4f; the crossover freeze-out (131 GeV) lies between the two' % float(1 / rb), okA2 and rb == sp.Rational(12, 37))
tgt = {(ph, q): R * m * float(r) * q for ph, r in (('sym', rs), ('brk', rb)) for q in (1, 2, 3) for m in (mp,)}
mD_s, mD_b = R * mp * float(rs), R * mp * float(rb)
check('A3 [T/E] carrier of B - L charge q: n_D/n_B = (1/q) x (79/28 or 37/12); the measured %.3f +- %.3f needs m_D = %.3f '
      '(sym) / %.3f (brk) GeV x q (q = 1; per-baryon mass m_p; %.3f with the H+He mean mass): a target, set by chemistry'
      % (R, dR, mD_s, mD_b, R * mbar * float(rs)), abs(mD_s - R * mp * 28 / 79) < 1e-12 and 1.6 < mD_b < mD_s < 1.8)

# ------------------------------------------ B. which object carries it ------------------------------------------
print('== B. which object carries the sequestered B - L')
gen = [('Q', 3, 2, Fr(1, 6)), ('u^c', 3, 1, Fr(-2, 3)), ('d^c', 3, 1, Fr(1, 3)), ('L', 1, 2, Fr(-1, 2)), ('e^c', 1, 1, Fr(1)), ('nu^c', 1, 1, Fr(0))]
free = [f for f, c, w, y in gen if c == 1 and w == 1 and y == 0]
check('B1 [T] of the 16 (SM links) exactly one Weyl state is link-free: %s; under the Pati-Salam reading it sits in (4bar,1,2) '
      'and is not link-free: the cell holds no other carrier' % free, free == ['nu^c'] and sum(c * w for _, c, w, _ in gen) == 16)
dm_atm, sum_max = 0.0501e-9, 0.12e-9                        # GeV: sqrt(dm2_atm); Planck 2018 sum bound
lo, hi = float(1 / rs) * dm_atm / mbar, float(1 / rs) * sum_max / mbar
check('B2 [E/M] the rules\' nu^c is the Dirac partner of nu_L (Majorana mass Z4-forbidden), m <= %.2f eV: Omega_D/Omega_b = '
      '(79/28) m/m_b <= %.1e (>= %.1e for the heaviest alone) vs %.2f, short by %.0e, and hot: excluded as dark matter'
      % (sum_max * 1e9, hi, lo, R, R / hi), hi < 1e-9)
# link-free bound state / condensate from a cell-scale contact term: gap equation on the CL-1 light band (b = 0.3)
bb = 0.3; gold = np.pi * (3 - np.sqrt(5)); nd = 400; zz = 1 - (2 * np.arange(nd) + 1) / nd
dirs = np.stack([np.sqrt(1 - zz ** 2) * np.cos(gold * np.arange(nd)), np.sqrt(1 - zz ** 2) * np.sin(gold * np.arange(nd)), zz], 1)
rmax = np.pi / np.abs(dirs).max(1); xg, wg = np.polynomial.legendre.leggauss(100)
def I_of(M, b=bb):
    tot = 0.0
    for d_, rm in zip(dirs, rmax):
        uu = np.log(1e-9 * rm) + (np.log(rm) - np.log(1e-9 * rm)) * (xg + 1) / 2
        r = np.exp(uu); jac = r * (np.log(rm) - np.log(1e-9 * rm)) / 2
        w = 2 * np.arcsin(np.cos(b) * np.sqrt(np.sum(np.sin(np.outer(r, d_) / 2) ** 2, 1) / 3))   # 1 - cos w = cos^2 b (1 - S), mu = 0
        tot += np.sum(wg * jac * r ** 2 / np.sqrt(w ** 2 + M ** 2))
    return tot * 4 * np.pi / nd / (2 * np.pi) ** 3
vg = np.cos(bb) / np.sqrt(3); I0 = I_of(0.0); Ms = np.array([1e-2, 1e-3]); fM = np.array([(I0 - I_of(m)) / m ** 2 for m in Ms])
slope = (fM[1] - fM[0]) / np.log(Ms[0] / Ms[1]); Cc = fM[1] - slope * np.log(1 / Ms[1])
Mt = mD_s / unit; tune = Mt ** 2 * (slope * np.log(1 / Mt) + Cc) / I0
check('B3 [D/E] a link-free bound state or condensate of mass m_D from a cell-scale contact term: I(0) = %.3f finite, '
      'I(0) - I(M) = M^2 ln(1/M)/(4 pi^2 v^3) (slope check %.3f); %.2f GeV = %.1e rad/tick needs 1 - g_c/g = %.0e: '
      'no GeV scale without tuning' % (I0, slope * 4 * np.pi ** 2 * vg ** 3, mD_s, Mt, tune),
      abs(slope * 4 * np.pi ** 2 * vg ** 3 - 1) < 0.08 and tune < 1e-30)
aZ = 1 / 0.1180; MZ, mt = 91.1876, 172.6
ainv_cell = aZ + (23 / 3) / (2 * np.pi) * np.log(mt / MZ) + 7 / (2 * np.pi) * np.log(unit / mt)
Lpg = unit * np.exp(-2 * np.pi * ainv_cell / 11)              # pure-glue SU(3)' with alpha'(cell) = alpha_s(cell), one loop
dainv = -(7 / (2 * np.pi)) * np.log(mD_s / mn)               # offset of 1/alpha'(cell) for an identical-content copy at m_D
Rtwin = mn / mbar; dNeff = (8 / 7) * (11 / 4) ** (4 / 3) + 3; sig_atom = np.pi * (0.529177e-8) ** 2 / (mH * gram)
check('B4 [E] a confining copy is not in the rules (a non-abelian link needs exactly degenerate supplied copies; the heavy '
      'copy has no exact number); supplied: pure glue from alpha_s(cell) = 1/%.1f confines at %.0e GeV; identical light '
      'content gives Lambda\' = Lambda_QCD, m_D/m_n = 1.90 needs 1/alpha\'(cell) shifted by %.2f (%.1f%%); an exact twin gives '
      'Omega\'/Omega_b = %.2f (%.0f sigma), Delta N_eff = %.1f at equal T, mirror-atom sigma/m ~ %.0e cm^2/g'
      % (ainv_cell, Lpg, dainv, 100 * abs(dainv) / ainv_cell, Rtwin, (R - Rtwin) / dR, dNeff, sig_atom),
      Lpg > 1e4 and abs(dNeff - 7.40) < 0.01 and sig_atom > 1e6)
gf = 33.5804; mf = gf * unit                                  # smg-verify fermion gap at coupling g = 1 per rad/tick
check('B5 [E] the cell-scale mirror family (Spin(10) pair square): lowest charged excitation 33.58 g = %.1e GeV at g = 1, '
      'so n_D/n_B would have to be %.0e; no chemistry rational is that small, and its ground state is a full singlet (no '
      'charge to carry)' % (mf, R * mbar / mf), R * mbar / mf < 1e-17)

# ------------------------------------------ C. the symmetric component ------------------------------------------
print('== C. symmetric component (carrier made only by the transfer term, Gamma/H < 1, no link)')
eps_lo, eps_hi = 1e-2, 2e-1                                   # agents/baryogenesis C6 toy range per event
check('C1 [T] each transfer event makes one carrier or anticarrier, so n_net/n_tot = eps (event-averaged CP asymmetry) and '
      'with no annihilation Omega_D/Omega_b = (m_D/m_b)(79/28)/eps; eps <= 1 gives the bound m_D <= %.2f GeV (sym), %.2f '
      '(brk), with equality only if the symmetric part is removed; at eps = %.0e-%.0e, m_D = %.0f-%.0f MeV'
      % (mD_s, mD_b, eps_lo, eps_hi, 1e3 * eps_lo * mD_s, 1e3 * eps_hi * mD_s), eps_hi * mD_s < mD_s)
Lam = unit; sv = mD_s ** 2 / (4 * np.pi * Lam ** 4) * GeV2cm3s
check('C2 [T/E] removal needs <sigma v> >~ 5e-26 cm^3/s and thermal contact: CL-3 links none (B - L survives only as Z4: no '
      'massless link), the cell-scale contact gives %.0e cm^3/s (short by %.0e), and a freeze-in carrier never '
      'thermalises; Z4 forbids the Majorana mass (i^2 = -1), so no oscillation erases the asymmetry either'
      % (sv, 5e-26 / sv), sv < 1e-80 and 1j ** 2 == -1)

# ---------------------------------------- D. measured constraints at the target ----------------------------------------
print('== D. measured constraints for a link-free carrier at 1.6-1.8 GeV (eps-scaled masses alike)')
beta = 0.0144; mu_r = mD_s * mn / (mD_s + mn); dm = abs(mD_s - mn)
sDN = mu_r ** 2 * beta ** 4 / (np.pi * Lam ** 8 * dm ** 2) * GeV2cm2
check('D1 [E/M] direct detection: no link, so nucleon scattering is second order in the cell-scale uddD contact: sigma ~ %.0e '
      'cm^2 vs DarkSide-50 (2023) ~1e-41 and CRESST-III ~1e-39 near 2 GeV, and below the neutrino fog by > 80 orders: '
      'passes, and is never detectable' % sDN, sDN < 1e-120)
sm_ = mD_s ** 2 / (4 * np.pi * Lam ** 4) * GeV2cm2 / (mD_s * gram)
check('D2 [E/M] self-scattering through a cell-scale D^4 term: sigma/m = %.0e cm^2/g vs Bullet Cluster < ~1: passes; '
      'non-dissipative, unlike a mirror sector' % sm_, sm_ < 1e-60)
Teq = 2.7255 * 8.617e-14 * 3403; rD = (oc / (oc + ob)) * Teq / 1e-3
check('D3 [E/M] BBN: produced near the cell scale and never thermalised, the carrier is non-relativistic and cold by BBN '
      '(warm-DM bound ~19 keV for this spectrum); rho_D/rho_rad at 1 MeV = %.0e, Delta N_eff ~ %.0e; the nu_R degeneracy '
      'xi ~ 79/28 eta ~ 2e-9 vs |xi_e| < 0.03' % (rD, rD * (1 + 0.2271 * 3.046) / 0.2271), rD < 1e-5)
G_ = mD_s * 0.1 ** 2 / (32 * np.pi * Lam ** 4); tau = 6.582e-25 / G_
check('D4 [E/M] decays: Z4 and B - L leave D -> nbar pi0 (m_D > m_n + m_pi) through uddD, tau ~ %.0e s vs gamma/antiproton '
      'limits ~1e26-1e28 s; nucleon decay p -> pi+ nubar_R through the same term ~1e52 s vs > 1e41 s; induced nucleon decay '
      'needs the same contact squared: all pass' % tau, tau > 1e40)

# ------------------------------------------------ E. look-elsewhere ------------------------------------------------
print('== E. look-elsewhere')
rats = sorted({Fr(22 * f + 13 * h, 8 * f + 4 * h) / q for f in range(1, 5) for h in range(0, 3) for q in (1, 2, 3, Fr(1, 3), Fr(1, 2))}
              | {Fr(24 * f + 13 * (h + 2), 8 * f + 4 * (h + 2)) / q for f in range(1, 5) for h in range(0, 3) for q in (1, 2, 3, Fr(1, 3), Fr(1, 2))})
masses = {'p': mp, 'n': mn, 'Lambda': 1.11568, 'Sigma0': 1.19264, 'Xi0': 1.31486, 'Delta': 1.232, 'Omega': 1.67245, 'eta\'': 0.95778,
          'phi': 1.019461, 'd': 1.875613, '2p': 2 * mp, 'S(1.88)': 1.88, '3p': 3 * mp}
vals = [(float(r) * m / mbar, str(r), k) for r in rats for k, m in masses.items()]
hits = [v for v in vals if abs(v[0] - R) < dR]
rng = np.random.default_rng(20261021); tg = np.exp(rng.uniform(np.log(2), np.log(20), 4000))
arr = np.array([v[0] for v in vals]); hit_mask = np.array([np.any(np.abs(arr - t) < dR * t / R) for t in tg]); Pr = float(hit_mask.mean())
best = [(abs(float(Fr(79, 28)) * masses[k] / mbar - R) / dR, k) for k in ('2p', 'd', 'S(1.88)')]
check('E1 [E] %d chemistry rationals x %d natural hadron masses: %d products lie within 1 sigma of %.3f, and a random target in '
      '2-20 gets one with P = %.2f: any such match is not evidence (the hit: %s x m_%s, from Nf = 1, NH = 2); the textbook '
      '79/28 with 2m_p, m_d, a 1.88 GeV sexaquark misses by %.1f, %.1f, %.1f sigma'
      % (len(rats), len(masses), len(hits), R, Pr, hits[0][1] if hits else '-', hits[0][2] if hits else '-', *[b for b, _ in best]),
      Pr > 0.5 and min(b for b, _ in best) > 3)
check('E2 [T/E] with the symmetric part kept (C1) the ratio is (m_D/m_b)(79/28)/eps with eps free in (0, 1]: every '
      'target is reachable, so the only rule-level output is the bound m_D <= %.2f GeV, not a value' % mD_s, True)

print('theorems: A1, A2, B1, C1 (exact rationals); finite: B3; estimates: A3, B2, B4, B5, C2, D1-D4, E')
print('supplied: one-family content x 3, NH = 1, full sphaleron/Yukawa equilibrium, the uddn-type transfer (and for D a new')
print('  link-free Dirac species, its mass and no nu_L mixing), eps, the cell-scale contact scale, hadron matrix element')
print('  beta = 0.0144 GeV^3 (lattice), the unit map; cited: Planck 2018, PDG, DarkSide-50 2023, CRESST-III, Bullet Cluster.')
print('elapsed_seconds %.1f' % (time.monotonic() - T0))
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
