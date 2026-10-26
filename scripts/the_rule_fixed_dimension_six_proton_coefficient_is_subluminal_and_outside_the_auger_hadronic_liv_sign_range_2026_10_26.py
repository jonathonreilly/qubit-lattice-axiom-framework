AUDIT_INPUT_PATHS = ('docs/THE_RULE_FIXED_DIMENSION_SIX_PROTON_COEFFICIENT_IS_SUBLUMINAL_AND_OUTSIDE_THE_AUGER_HADRONIC_LIV_SIGN_RANGE_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Confront the rule-fixed dimension-six Lorentz-violating dispersion with UHECR LIV analyses.

Upstream (assumed-inputs-model runner A1/B, [F]): per K^2 (K = momentum per cube, cube edge 2L)
  link band (photon, gluon):  c_g(n) = -S/24,          S = sum n_i^4 in [1/3, 1]
  copy-mass shift:            c6(n)  = -(1/8)(S - 1/3)
  light fermion (quark, e):   c_q(n) = c_g + c6 = -S/6 + 1/24
so E = p + m^2/2p + c p^3/E*^2 with E* = hbar c/(2L), L = sqrt(8 pi kappa) l_P, kappa = 1 (register unit map).
Sections:
  A  convention map to Auger (E^2 - p^2 = m^2 + delta_{had,2} E^4) and Maccione et al. (eta p^4/M_P^2).
  B  direction statistics of S, c_g, c6, c_q (sky average exact; min/max).
  C  parton weighting W = sum_i <x^3>_i (supplied toy PDFs at 2 GeV; LO N = 4 evolution to E*).
  D  proton delta_{had,2}: sign, magnitude, ratio to the Auger 5 sigma number.
  E  pure-proton GZK analysis (Maccione-Taylor-Mattingly-Liberati 2009) in its own convention.
  F  photopion closure at the cell-scale weight (exact two-body kinematics).
  G  composite vacuum emission p -> p gamma, p -> p pi0 (new; parton-additive composite) and nuclei.
  H  rescue sizes: cell rung / kappa needed if the Auger magnitude were applied regardless of sign.
"""
import math
import os
import sys
import time

os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.special import beta as B

AUDIT_TIMEOUT_SEC = 120
t0 = time.time()
rng = np.random.default_rng(20261026)
NP = [0, 0]


def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")


# ---------------- constants (supplied) ----------------
MP = 1.22089e28            # eV, non-reduced Planck mass (both papers' M_Pl)
L_over_lP = math.sqrt(8 * math.pi)        # kappa = 1 cell rung (register one-G clause)
Es = MP / (2 * L_over_lP)  # E* = hbar c/(2L) in eV
mp, mpi, me = 938.272e6, 134.977e6, 0.511e6
BOUND_AUGER = 1e-57        # eV^-2, delta_had,2 upper limit, 5 sigma, only delta_had > 0 scanned
cg = lambda S: -S / 24
c6 = lambda S: -(S - 1 / 3) / 8
cq = lambda S: cg(S) + c6(S)

# ---------------- A: conventions ----------------
p, c, E0 = sp.symbols('p c E0', positive=True)
Edisp = p + c * p ** 3 / E0 ** 2
lhs = sp.series(sp.expand(Edisp ** 2 - p ** 2), p, 0, 7).removeO()
delta2 = sp.simplify(sp.expand(lhs).coeff(p, 4))
check('A1 E = p + c p^3/E*^2 gives E^2 - p^2 = delta E^4 + O(p^6) with delta_{had,2} = 2c/E*^2 (Auger Eq. 2.2 form); eta_MTML = 2c (M_P/E*)^2',
      sp.simplify(delta2 - 2 * c / E0 ** 2) == 0, f'E* = {Es:.4e} eV (L = sqrt(8 pi) l_P); 2/E*^2 = {2 / Es**2:.3e} eV^-2; (M_P/E*)^2 = {(MP / Es)**2:.2f}')
print('   sign: c < 0 (rules) => delta_{had,2} < 0 => group velocity 1 - 3|c|p^2/E*^2 < 1: SUBLUMINAL')

# ---------------- B: directions ----------------
th, ph = sp.symbols('theta phi')
nx, ny, nz = sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)
Savg = sp.simplify(sp.integrate(sp.integrate((nx**4 + ny**4 + nz**4) * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi))
v = rng.normal(size=(200000, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
Smc = np.sum(v ** 4, axis=1)
check('B1 sky average <sum n^4> = 3/5 exactly (MC 2e5 rays agrees); range [1/3 body, 1 axis]',
      Savg == sp.Rational(3, 5) and abs(Smc.mean() - 0.6) < 2e-3, f'MC {Smc.mean():.5f}, min {Smc.min():.4f}, max {Smc.max():.4f}')
Sa = sp.Rational(3, 5)
print(f'   sky avg: c_g = {-Sa/24}, c6 = {-(Sa - sp.Rational(1,3))/8}, c_q = {-Sa/6 + sp.Rational(1,24)};'
      f' axis c_q = -1/8, c_g = -1/24; body c_q = c_g = -1/72')
check('B2 c_q = c_g + c6 = -S/6 + 1/24 is <= c_g on every ray (fermions never less subluminal than links); equal only on body diagonals',
      np.all(cq(Smc) <= cg(Smc) + 1e-15), f'sky-avg c_q = -7/120 = {-7/120:.5f}, c_g = -1/40')

# ---------------- C: parton weights ----------------
# supplied toy PDFs at Q0 = 2 GeV (number/momentum sum rules imposed): x u_v ~ x^a (1-x)^3, x d_v ~ x^a (1-x)^4,
# x sea ~ x^-0.15 (1-x)^7 (momentum fs), x g ~ x^-0.1 (1-x)^bg, gluon momentum = 1 - valence - sea.
def proton_moments(a=0.7, bu=3.0, bd=4.0, fs=0.14, bg=5.0, bs=7.0):
    def val(nq, b):            # number nq: q(x) = N x^(a-1)(1-x)^b
        N = nq / B(a, b + 1)
        return N * B(a + 1, b + 1), N * B(a + 3, b + 1)   # momentum, <x^3>
    mu, xu = val(2, bu); md, xd = val(1, bd)
    def shape(e, b, fmom):     # x f = N x^e (1-x)^b with momentum fmom; <x^3> = int x^2 (x f)
        N = fmom / B(e + 1, b + 1)
        return N * B(e + 3, b + 1)
    xs = shape(-0.15, bs, fs)
    fg = 1 - mu - md - fs
    xg = shape(-0.1, bg, fg)
    return np.array([xu + xd + xs, xg]), mu + md, fg


def pion_moments(a=0.6, bv=1.2, fs=0.12, bg=4.0):
    N = 2 / B(a, bv + 1)
    mv, xv = N * B(a + 1, bv + 1), N * B(a + 3, bv + 1)
    xs = fs / B(0.85, 7) * B(2.85, 7)
    fg = 1 - mv - fs
    xg = fg / B(0.9, bg + 1) * B(2.9, bg + 1)
    return np.array([xv + xs, xg])


CF, CA, TR = 4 / 3, 3.0, 0.5
def gamma_AP(N, nf):
    S1 = sum(1 / k for k in range(1, N + 1))
    qq = CF * (1.5 + 1 / (N * (N + 1)) - 2 * S1)
    qg = 2 * nf * TR * (N * N + N + 2) / (N * (N + 1) * (N + 2))
    gq = CF * (N * N + N + 2) / (N * (N * N - 1))
    gg = 2 * CA * (1 / (N * (N - 1)) + 1 / ((N + 1) * (N + 2)) - S1) + (11 * CA - 4 * nf * TR) / 6
    return np.array([[qq, qg], [gq, gg]])


g2 = gamma_AP(2, 5)
check('C1 LO singlet anomalous dimensions conserve momentum at N = 2 (column sums 0)',
      np.max(np.abs(g2.sum(axis=0))) < 1e-12, f'N = 4 eigenvalues (nf=6): {np.round(np.linalg.eigvals(gamma_AP(4, 6)), 3)}')


def evolve(M, Q0=2.0, Q1=Es * 1e-9, a0=0.30):
    b0 = lambda nf: 11 - 2 * nf / 3
    segs = [(Q0, 172.7, 5), (172.7, Q1, 6)]
    a = a0
    for qa, qb, nf in segs:
        a1 = a / (1 + a * b0(nf) / (4 * math.pi) * math.log(qb ** 2 / qa ** 2))
        M = expm(-(2 / b0(nf)) * gamma_AP(4, nf) * math.log(a1 / a)) @ M
        a = a1
    return M, a


Wp0, mval, fg = proton_moments()
WpE, aE = evolve(Wp0)
Wpi0 = pion_moments(); WpiE, _ = evolve(Wpi0)
var = [proton_moments(a=a, bu=bu, bg=bg) for a in (0.55, 0.85) for bu in (2.5, 3.5) for bg in (4.0, 6.0)]
Wtot0 = [w[0].sum() for w in var]; WtotE = [evolve(w[0])[0].sum() for w in var]
print(f'   proton @2 GeV: momentum val {mval:.3f}, gluon {fg:.3f}; <x^3>_q = {Wp0[0]:.4f}, <x^3>_g = {Wp0[1]:.4f} (sum {Wp0.sum():.4f}; shape scan {min(Wtot0):.3f}-{max(Wtot0):.3f})')
print(f'   proton @E*: alpha_s = {aE:.4f}; <x^3>_q = {WpE[0]:.5f}, <x^3>_g = {WpE[1]:.5f} (sum {WpE.sum():.5f}; scan {min(WtotE):.4f}-{max(WtotE):.4f}); pion @2 GeV sum {Wpi0.sum():.4f}, @E* {WpiE.sum():.5f}')
check('C2 parton weight W = sum <x^3> is ~0.03 at 2 GeV and falls ~5-10x by the cell scale (LO N = 4 evolution; supplied PDFs and alpha_s(2 GeV) = 0.30)',
      0.01 < Wp0.sum() < 0.1 and WpE.sum() < Wp0.sum() / 3, f'ratio E*/2GeV = {WpE.sum() / Wp0.sum():.3f}')

# ---------------- D: proton delta_had,2 ----------------
cp = lambda S, W: W[0] * cq(S) + W[1] * cg(S)
rows = {}
for tag, W in (('2GeV', Wp0), ('E*', WpE)):
    d = {k: 2 * cp(S, W) / Es ** 2 for k, S in (('axis', 1.0), ('sky', 0.6), ('body', 1 / 3))}
    rows[tag] = d
    print(f'   W@{tag}: delta_had,2 (eV^-2) axis {d["axis"]:.2e}, sky-avg {d["sky"]:.2e}, body {d["body"]:.2e};'
          f' |.|/1e-57 = {abs(d["axis"])/BOUND_AUGER:.2f}, {abs(d["sky"])/BOUND_AUGER:.2f}, {abs(d["body"])/BOUND_AUGER:.3f}')
allneg = all(v < 0 for r in rows.values() for v in r.values())
check('D1 predicted delta_had,2 < 0 on every ray: outside the delta_had > 0 range Auger 2022 scanned, so its 5 sigma number does not apply as a bound',
      allneg, 'Auger: "only positive LIV coefficients (delta_had > 0)"; n=2 value is the Eq. 6.4 rescaling of the n=0 fit')
Rsky = [abs(rows[t]['sky']) / BOUND_AUGER for t in rows]; Rbody = [abs(rows[t]['body']) / BOUND_AUGER for t in rows]
check('D2 magnitude-only comparison (sign ignored): sky-average |delta|/1e-57 is 0.3-4.3 and the axis value 0.7-9.1 (below the pre-registered factor 10); least-constrained (body) ray 0.08-1.2',
      max(Rbody) < 1.5 and 0.1 < min(Rsky) and max(Rsky) < 10, f'sky {min(Rsky):.2f}-{max(Rsky):.2f}; body {min(Rbody):.3f}-{max(Rbody):.3f}')

# ---------------- E: Maccione et al. 2009 (pure protons) ----------------
eta = {t: {k: v * MP ** 2 for k, v in r.items()} for t, r in rows.items()}
print('   eta_p (MTML convention, E^2 = p^2 + m^2 + eta p^4/M_P^2): ' +
      '; '.join(f'W@{t}: axis {e["axis"]:.2e}, sky {e["sky"]:.2e}, body {e["body"]:.2e}' for t, e in eta.items()))
etamin = min(abs(v) for e in eta.values() for v in e.values())
check('E1 pure-proton analysis (MTML 2009, 99% CL: -1e-3 <~ eta_p <~ 1e-6; grid edge at -1e-3): every predicted eta_p lies below -1e-3, i.e. outside the allowed region IF the flux is pure protons',
      etamin > 1e-3, f'smallest |eta_p| = {etamin:.2e} = {etamin / 1e-3:.0f} x the grid edge')

# ---------------- F: photopion closure ----------------
def pion_allowed(P, cP, cPi, eg, xmax=0.999):
    x = np.linspace(1e-3, xmax, 4000)
    need = (mpi ** 2 / x + mp ** 2 / (1 - x) - mp ** 2) / (2 * P) + (cP * ((1 - x) ** 3 - 1) + cPi * x ** 3) * P ** 3 / Es ** 2
    return np.any(need <= 2 * eg)


eg = 10 * 8.617e-5 * 2.7255 * 2.82   # 10 kT_CMB x mean photon energy factor (generous)
open_any, first_hard = {}, {}
Pgrid = np.logspace(18, 22.5, 300)
for tag in ('2GeV', 'E*'):
    W, Wpi = (Wp0, Wpi0) if tag == '2GeV' else (WpE, WpiE)
    S = 1 / 3
    cpi_b = Wpi[0] * cq(S) + Wpi[1] * cg(S)
    open_any[tag] = any(pion_allowed(P, cp(S, W), cpi_b, eg, xmax=0.5) for P in Pgrid)
    first_hard[tag] = next((P for P in Pgrid if pion_allowed(P, cp(S, W), cpi_b, eg)), math.inf)
LIopen = pion_allowed(1e20, 0.0, 0.0, eg)
check('F1 GZK branch (pion fraction x <= 1/2) of p + gamma_CMB -> p + pi (photon up to 10 kT x 2.82) is closed at every energy even on the least-subluminal (body) ray at both weighting scales; the hard-pion branch opens only where p -> p pi0 opens by itself (G1)',
      LIopen and not open_any['2GeV'] and not open_any['E*'], f'|c_p| body: {abs(cp(1/3, Wp0)):.1e} (2 GeV), {abs(cp(1/3, WpE)):.1e} (E*); hard branch from {first_hard["2GeV"]/1e18:.0f} / {first_hard["E*"]/1e18:.0f} EeV (body)')

# ---------------- G: composite vacuum emission ----------------
def emit_threshold(c_i, m_i, c_f, m_f, c_X, m_X, extra=0.0):
    y = np.linspace(1e-3, 0.999, 20000)
    gain = c_i - c_f * (1 - y) ** 3 - c_X * y ** 3            # coefficient of P^3/E*^2 in E_i - E_f
    cost = (m_f ** 2 / (1 - y) + (m_X ** 2 / y if m_X > 0 else 0) - m_i ** 2 + extra) / 2   # coefficient of 1/P
    ok = gain > 0
    if not np.any(ok):
        return math.inf, None
    P4 = cost[ok] * Es ** 2 / gain[ok]
    j = np.argmin(P4)
    return P4[j] ** 0.25, y[ok][j]


thr = {}
for ray, S in (('axis', 1.0), ('sky', 0.6), ('body', 1 / 3)):
    for tag, W, Wpi in (('2GeV', Wp0, Wpi0), ('E*', WpE, WpiE)):
        c_p = cp(S, W); c_pi = Wpi[0] * cq(S) + Wpi[1] * cg(S)
        tg, yg = emit_threshold(c_p, mp, c_p, mp, cg(S), 0.0)
        tpi, ypi = emit_threshold(c_p, mp, c_p, mp, c_pi, mpi)
        thr[(ray, tag)] = (tg, yg, tpi)
print('   p -> p gamma threshold (EeV) [y*] / p -> p pi0 (EeV): ' + '; '.join(
    f'{r} W@{t}: {v[0]/1e18:.1f} [{v[1]:.2f}] / {v[2]/1e18:.1f}' for (r, t), v in thr.items()))
check('G1 parton-additive protons are less subluminal than photons on every ray (W < 1), so hard p -> p gamma is kinematically OPEN above a few EeV (soft emission stays closed)',
      all(math.isfinite(v[0]) and v[0] < 2e19 for v in thr.values()), f'range {min(v[0] for v in thr.values())/1e18:.1f}-{max(v[0] for v in thr.values())/1e18:.1f} EeV')
# nuclei: incoherent emission off one nucleon carrying P/A (separation energy S_n = 8 MeV in the mass cost)
Amax = {}
for A in (4, 14, 28, 56):
    tA = []
    for ray, S in (('axis', 1.0), ('body', 1 / 3)):
        c_n = cp(S, WpE)
        t, _ = emit_threshold(c_n, mp, c_n, mp, cg(S), 0.0, extra=2 * mp * 8e6)
        tA.append(A * t)
    Amax[A] = tA
print('   nuclei, nucleon-level p->p gamma threshold A x E_th (EeV, axis/body, W@E*): ' +
      '; '.join(f'A={A}: {v[0]/1e18:.0f}/{v[1]/1e18:.0f}' for A, v in Amax.items()))
check('G2 nucleus emission threshold scales ~A (rigidity-like): Fe reaches 1-3e20 eV, comparable to the highest events (TA 2.44e20, Fly\'s Eye 3.2e20 eV): a tension test, not yet a verdict',
      5e19 < Amax[56][0] < 1e21, f'Fe axis {Amax[56][0]:.2e} eV, body {Amax[56][1]:.2e} eV')

# ---------------- P: photon sector (Auger 2022 delta_gamma,2 > -1e-58 eV^-2, alternative scenario only) ----------------
dg = {r: 2 * cg(S) / Es ** 2 for r, S in (('axis', 1.0), ('sky', 0.6), ('body', 1 / 3))}
check('P1 photon delta_gamma,2 = 2 c_g/E*^2 is 190-560 x beyond -1e-58, but that bound assumes LI electrons (subluminal photons survive pair production); here gamma -> e+e- is open above 80-122 PeV, so its mechanism fails and it is not applied',
      all(v < -1e-58 for v in dg.values()), f'axis {dg["axis"]:.2e}, sky {dg["sky"]:.2e}, body {dg["body"]:.2e} eV^-2 (reference scenario: no Auger constraint)')

# ---------------- H: rescue sizes ----------------
Rmax = max(abs(rows[t]['sky']) for t in rows) / BOUND_AUGER
f_L = 1 / math.sqrt(Rmax)
check('H1 if the Auger magnitude were applied regardless of sign, the sky-average needs delta down by R; delta ~ L^2 so L -> L/sqrt(R), i.e. kappa -> kappa/R (one-G: L = sqrt(8 pi kappa) l_P with G fixed)',
      Rmax > 1, f'R_sky(max) = {Rmax:.2f}: L x {f_L:.2f}, kappa = {1 / Rmax:.2f} (the split window already allows cell factor <= 2)')
print(f'   runtime {time.time() - t0:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
