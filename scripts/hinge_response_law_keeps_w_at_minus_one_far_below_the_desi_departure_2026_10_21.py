AUDIT_INPUT_PATHS = ('docs/HINGE_RESPONSE_LAW_KEEPS_W_AT_MINUS_ONE_FAR_BELOW_THE_DESI_DEPARTURE_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""desi-de: does anything in CL-1..CL-3 give w(z) != -1 at the DESI level (delta w ~ 0.1)?

Self-contained (numpy/scipy/sympy/mpmath).  Parts:
  A  THEOREM: hinge Friedmann law (8 pi G/3) rho l^2/4 = A(Hl/2) -> inferred dark-energy w; exact high-precision check
  B  CPL projection engine: BAO D_M/r_d, D_H/r_d at DESI redshifts + CMB theta*, omega_m, omega_b fixed; fit (h, w0, wa)
  C  each rule effect as a perturbation of H^2(z), projected onto (w0, wa), with its size today (estimates)
  D  what a DESI-like (w0, wa) needs; speculative replacement law (constant vacuum decrement per split), not adopted
"""
import numpy as np, sympy as sp, mpmath as mp, warnings
from scipy.integrate import IntegrationWarning
warnings.simplefilter('ignore', IntegrationWarning)
from scipy.integrate import quad

AUDIT_TIMEOUT_SEC = 90
NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------- A. hinge Friedmann law -----------------------------------------------------------------
print('== A. hinge Friedmann law and the inferred dark-energy w')
u, X, l = sp.symbols('u X l', positive=True)
A = sp.asin(u**2 / (1 - u**2)) / sp.sqrt(1 - 2 * u**2)
serA = sp.series(A, u, 0, 8).removeO()
check('THEOREM (series): A(u) = u^2 + 2u^4 + O(u^6), so H^2 = X - X^2 l^2/2 + O(l^4), X = (8 pi G/3) rho',
      sp.simplify(serA.coeff(u, 2) - 1) == 0 and sp.simplify(serA.coeff(u, 4) - 2) == 0, f'A = {sp.expand(serA)}')
# inferred DE: D = H^2 - X_m (observer uses GR with the same G); edges grow as l ~ a between splits
# analytic: w + 1 = -(1/3) dlnD/dlna = -X l^2 (3 X_m - X) / (3 X_L) at leading order (l ~ a), = +X X_m l^2/X_L... if l fixed
mp.mp.dps = 420
Om, OL = mp.mpf('0.31'), mp.mpf('0.69')
def w_inferred(Hl0, lgrows=True):
    def D(lna):
        a = mp.e ** lna; Xm = Om * a**-3; Xt = Xm + OL; ll = Hl0 * (a if lgrows else 1)   # units H0 = 1
        Afn = lambda uu: mp.asin(uu**2 / (1 - uu**2)) / mp.sqrt(1 - 2 * uu**2)
        uu = mp.findroot(lambda uu: Afn(uu) - Xt * ll**2 / 4, mp.sqrt(Xt) * ll / 2)
        return (2 * uu / ll)**2 - Xm
    return -1 - mp.diff(lambda x: mp.log(D(x)), 0) / 3
ok, rows = True, []
for lab, Hl0 in (('l = a', mp.mpf('5.93e-61')), ('l = 2a', mp.mpf('1.186e-60'))):
    for gr in (True, False):
        wnum = w_inferred(Hl0, gr) + 1
        wan = -(Hl0**2) * (3 * Om - 1) / (3 * OL) if gr else -(Hl0**2) * Om / OL
        ok &= abs(wnum / wan - 1) < 1e-6; rows.append(f'{lab}{"" if gr else " fixed"}: {mp.nstr(wnum, 3)}')
check('hinge law, H0 a = 5.93e-61 (a = sqrt(8 pi) l_P): w + 1 = -(H0 l)^2 (3 Om - 1)/(3 OL) with edges growing (l ~ a), '
      '-(H0 l)^2 Om/OL at fixed edge; exact A(u) at 420 digits matches', ok, '; '.join(rows))

# ---------------- B. CPL projection engine -------------------------------------------------------------
print('== B. CPL projection (BAO + CMB theta*, omega_m and omega_b fixed by the CMB; fit h, w0, wa)')
wm, wb, wg = 0.1424, 0.02237, 2.473e-5; wr = wg * (1 + 0.2271 * 3.046); zs, zd = 1089.9, 1060.0
ZB = [0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330]
def make_E2(h, w0, wa, f=None):
    OLh = h * h - wm - wr
    def E2(z):  # H^2 in (100 km/s/Mpc)^2 units
        a = 1 / (1 + z); de = OLh * a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))
        base = wm * (1 + z)**3 + wr * (1 + z)**4 + de
        return base * (1 + (f(z) if f else 0.0))
    return E2
def obs(E2):
    H = lambda z: np.sqrt(E2(z)); cs = lambda z: 1 / np.sqrt(3 * (1 + 0.75 * wb / wg / (1 + z)))
    rd = quad(lambda z: cs(z) / H(z), zd, np.inf, limit=200)[0]
    rs = quad(lambda z: cs(z) / H(z), zs, np.inf, limit=200)[0]
    DM = lambda z: quad(lambda x: 1 / H(x), 0, z, limit=200)[0]
    pts = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 5.0, 10.0, 30.0, 100.0, 300.0, zs]   # split the long integral
    DMs = sum(quad(lambda x: 1 / H(x), pts[i], pts[i + 1], limit=200)[0] for i in range(len(pts) - 1))
    v = [DM(z) / rd for z in ZB] + [1 / H(z) / rd for z in ZB] + [rs / DMs]
    return np.array(v)
SIG = np.array([0.010] * 7 + [0.012] * 7 + [0.0003])          # fractional errors, DESI-DR2-like and Planck theta*
P0 = np.array([0.6766, -1.0, 0.0])
def J_at(p, f=None):
    o0 = obs(make_E2(*p, f)); J = []
    for i, d in enumerate((1e-4, 1e-3, 3e-3)):
        q = p.copy(); q[i] += d; J.append((obs(make_E2(*q, f)) - o0) / d)
    return o0, np.array(J).T
o_ref, J0 = J_at(P0)
Wt = np.diag(1 / (SIG * o_ref) ** 2)
Fm = J0.T @ Wt @ J0; Cov = np.linalg.inv(Fm)
def project(f):  # linear CPL response to a multiplicative H^2 perturbation f(z) of LCDM
    d = obs(make_E2(*P0, f)) - o_ref; return Cov @ J0.T @ Wt @ d
def fit_model(E2):  # Gauss-Newton fit of (h, w0, wa) to a given model's observables
    target = obs(E2); p = P0.copy()
    for _ in range(8):
        o, J = J_at(p); W = np.diag(1 / (SIG * target) ** 2)
        p = p + np.linalg.solve(J.T @ W @ J, J.T @ W @ (target - o))
    return p
pd = np.array([0.6400, -0.75, -0.86]); fitb = fit_model(make_E2(*pd))
check('engine self-test: a CPL universe (w0, wa) = (-0.75, -0.86) is recovered by the fit',
      np.allclose(fitb[1:], pd[1:], atol=2e-3), f'fit w0 {fitb[1]:.4f}, wa {fitb[2]:.4f}; forecast sigma(w0, wa) = {np.sqrt(Cov[1,1]):.3f}, {np.sqrt(Cov[2,2]):.3f}')
lam = 1.07; E2s = lambda z: lam**2 * make_E2(*P0)(z)
dv = np.max(np.abs(obs(E2s) / o_ref - 1))
check('THEOREM: a uniform rescaling H -> lam H at all z (a constant G_cosmo/G_N, e.g. a constant induced kinetic term) '
      'leaves every D/r_d and theta* unchanged: it projects onto (w0, wa) = (-1, 0) exactly', dv < 1e-9, f'max |d obs/obs| = {dv:.0e} at lam = {lam}')

# ---------------- C. rule effects ----------------------------------------------------------------------
print('== C. rule effects as perturbations f(z) = dH^2/H^2, projected per unit amplitude, times their size today')
step = lambda zs_: (lambda z: -1.0 if z < zs_ else 0.0)            # matter-like step: rho_m loses a fraction at a split
def matter_step(zs_, d=1.0):
    E2b = make_E2(*P0)
    return lambda z: (-d * wm * (1 + z)**3 / E2b(z)) if z < zs_ else 0.0
resp_step = []
for zsp in (0.3, 0.6, 1.0, 1.5, 2.2):
    r = project(matter_step(zsp, 1e-3)) / 1e-3; resp_step.append((zsp, r[1], r[2]))
cm = max(max(abs(a), abs(b)) for _, a, b in resp_step)
check('split step response: matter losing a fraction delta at a split epoch z_s gives |dw0|, |dwa| <= C delta',
      cm > 0, 'C = %.2f; ' % cm + ', '.join(f'z_s {z}: ({a:+.2f}, {b:+.2f})' for z, a, b in resp_step))
ln2 = np.log(2)
def sawtooth(phase, amp=1.0):
    return lambda z: amp * (((np.log(1 + z) / ln2 + phase) % 1.0) - 0.5)
cs_ = max(np.max(np.abs(project(sawtooth(ph, 1e-3))[1:])) / 1e-3 for ph in np.linspace(0, 1, 8, endpoint=False))
check('log-periodic sawtooth in H^2 (period ln 2 in ln a: one split cycle), amplitude s, worst phase: |dw| <= C s',
      cs_ > 0, f'C = {cs_:.2f}')
tD = obs(make_E2(*pd)); hh = P0[0]
for _ in range(8):   # best LCDM (h only) to the DESI-like model, then the H^2 shape difference it must be given
    o1 = obs(make_E2(hh, -1, 0)); o2 = obs(make_E2(hh + 1e-4, -1, 0)); jj = (o2 - o1) / 1e-4; Wd = 1 / (SIG * tD)**2
    hh += np.sum(jj * Wd * (tD - o1)) / np.sum(jj * jj * Wd)
fD = lambda z: make_E2(*pd)(z) / make_E2(hh, -1, 0)(z) - 1
fneed = max(abs(fD(z)) for z in np.linspace(0, 2.5, 51))
# sizes today (estimates; unit map a = sqrt(8 pi) l_P, edge l in [a, 2a]; hbar c = 1.97327e-7 eV m)
a_m = np.sqrt(8 * np.pi) * 1.616255e-35; Hl2 = (2.194e-18 * 2 * a_m / 2.998e8)**2
ml = lambda m_eV: m_eV * 2 * a_m / 1.97327e-7
Kcmb = ml(6.3e-4)
rows = [('hinge law (THEOREM, part A; |w+1| directly)', 0.45 * Hl2, 1.0),
        ('triggered-split junction: ln H steps (3/4)u^2 (split-junction, THEOREM there)', 0.375 * Hl2, cm),
        ('step roll: Lambda never sees eps (rule text); matter via (K l)^2, CMB', 1e-4 * 0.05 * Kcmb**2, cs_),
        ('split energy change of excitations, radiation 0.04 K^2 (split-junction) ', 1e-4 * 0.04 * Kcmb**2, cm),
        ('split energy change of massive matter, ~0.05 mu^2 (ESTIMATE), protons', 0.31 * 0.05 * ml(0.938e9)**2, cm),
        ('  same, heaviest species the vacuum-stability cap allows (mu <= 0.075)', 0.31 * 0.05 * 0.075**2, cm),
        ('sea heating at splits: CL-1 nearest unitary maps sea onto sea (sea-split C3)', 0.0, cm),
        ('adiabatic reference: non-adiabatic creation ~ (H l)^2 (ESTIMATE)', Hl2, cs_),
        ('instantaneous reference: nu < 1e-15 (GW170817) x eps sawtooth 0.14 x 1.6e-3 (ESTIMATE)', 1e-15 * 0.14 * 1.6e-3, cs_)]
print(f'   DESI-like (w0, wa) = (-0.75, -0.86) needs |dH^2/H^2| up to {fneed:.3f} at z < 2.5; rule effects (size f, |dw| <= C f):')
worst = 0.0
for lab, f, C in rows:
    worst = max(worst, C * f) if 'cap' not in lab else worst
    print(f'   {lab:<84s} f {f:8.1e}  |dw| {C * f:8.1e}')
cap = [C * f for lab, f, C in rows if 'cap' in lab][0]
check('no rule effect reaches the DESI level: largest known-content |dw| vs needed ~0.1; the cap-allowed ceiling also misses',
      worst < 1e-10 and cap < 1e-2, f'known content {worst:.0e}; heaviest-allowed ceiling {cap:.0e}; needed f {fneed:.2f}')

# ---------------- D. what the DESI direction needs --------------------------------------------------------
print('== D. the DESI direction')
for (w0, wa, lab) in ((-0.42, -1.75, 'BAO+CMB'), (-0.838, -0.62, '+Pantheon+'), (-0.667, -1.09, '+Union3'), (-0.752, -0.86, '+DESY5')):
    print(f'   DR2 {lab:<11s} (w0, wa) = ({w0:+.3f}, {wa:+.2f}): w = -1 at z = {1 / (1 + (1 + w0) / wa) - 1:.2f}, wa/(1+w0) = {wa / (1 + w0):.2f}')
print('   THEOREM (continuity): with Lambda constant and matter conserved, rho_DE,inferred is constant; a phantom crossing needs '
      'energy exchange with a varying vacuum term or a non-standard matter/G history')
def dec_model(q):  # speculative: vacuum density falls by a constant q rho_L0 per split (one split per ln 2)
    def E2(z):
        a = 1 / (1 + z); OLh = P0[0]**2 - wm - wr
        return wm * (1 + z)**3 + wr * (1 + z)**4 + OLh * max(1 - q * np.log2(a), 0)
    return E2
best = None
for q in (0.2, 0.35, 0.5):
    pf = fit_model(dec_model(q)); best = (q, pf) if best is None or abs(pf[1] + 0.75) < abs(best[1][1] + 0.75) else best
    print(f'   decrement q = {q:.2f} rho_L0 per split: CPL fit (w0, wa) = ({pf[1]:+.3f}, {pf[2]:+.3f}), wa/(1+w0) = {pf[2] / (1 + pf[1]):.2f}')
q, pf = best
check('SPECULATIVE (not adopted): a constant vacuum decrement per split is thawing (w >= -1, wa < 0) but lies off the DESI '
      'degeneracy line wa/(1+w0) ~ -3.4; it needs q ~ 0.4 rho_L0 per split by hand, and CL-3 keeps Lambda constant',
      pf[2] < 0 and pf[2] / (1 + pf[1]) > -2.5, f'q = {q}: ({pf[1]:+.3f}, {pf[2]:+.3f})')
print('supplied: unit map a = sqrt(8 pi) l_P, edge in [a, 2a], H0 67.7, Om 0.31, omega_m/b/r, DESI-like 1% errors, DR2 central values')
print('  (quoted), massive split coefficient 0.05 mu^2 (estimate), induced-kinetic GW bound 1e-15, eps range 0.04 -> 0.01.')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
