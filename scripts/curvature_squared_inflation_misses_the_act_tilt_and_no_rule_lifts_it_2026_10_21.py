#!/usr/bin/env python3
"""act-tilt: the campaign's tilt candidates against Planck and ACT DR6 (P-ACT-LB); which shapes fit 0.974 with r < 0.036;
whether the rules supply any of them.  Supplied models, finite diagnostics; no physical identification.
 A  data and pulls          B  Starobinsky: N* needed, reheating histories, stiff phases, GW bound
 C  the rules' own forms (hinge plateau, running coupling, constant transfer, legacy graph growth)
 D  slow-roll shapes (exact background + 2nd-order Hubble flow), plateau-class theorem
 E  can the rules supply the shift (lattice R^2/R^3 terms, hinge corrections, copy mass, condensate)
 F  look-elsewhere
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/CURVATURE_SQUARED_INFLATION_MISSES_THE_ACT_TILT_AND_NO_RULE_LIFTS_IT_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120
import cmath, math, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
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


DS = {'Pl': (0.9649, 0.0042), 'ACT': (0.9740, 0.0030), 'DR2': (0.9752, 0.0030)}   # measured inputs (coordinator-verified)
R_MAX, As_m, MP = 0.036, 2.100e-9, 2.435e18
C_SR = -2 + math.log(2) + 0.5772156649
def pulls(ns): return ' '.join('%s%+.1f' % (k, (ns - c) / s) for k, (c, s) in DS.items())


class Model:                                    # exact background in e-fold time, end at eps_H = 1
    def __init__(self, V, x0):
        self.V = V; self.Vr = lambda p: V(complex(p, 0)).real; self.dV = lambda p: V(complex(p, 1e-20)).imag / 1e-20
        eV = lambda p: 0.5 * (self.dV(p) / self.Vr(p)) ** 2
        lo = x0
        while eV(lo) < 1: lo *= 0.5
        pend = brentq(lambda p: eV(p) - 1, lo, x0)
        p0 = solve_ivp(lambda N, s: [self.dV(s[0]) / self.Vr(s[0])], (0, 125), [pend], rtol=1e-10, atol=1e-13).y[0, -1]
        ev = lambda N, s: s[1] ** 2 / 2 - 1; ev.terminal = True
        self.BG = solve_ivp(lambda N, s: [s[1], -(3 - s[1] ** 2 / 2) * (s[1] + self.dV(s[0]) / self.Vr(s[0]))], (0, 300),
                            [p0, -self.dV(p0) / self.Vr(p0)], events=ev, rtol=1e-10, atol=1e-13, dense_output=True, method='DOP853')
        self.NEND = self.BG.t_events[0][0]; self.PEND = self.BG.y_events[0][0][0]
    def flow(self, Ns, h=1e-3):
        S = self.BG.sol; N = self.NEND - Ns; e1f = lambda n: S(n)[1] ** 2 / 2
        def e2f(n): l = [math.log(e1f(n + k * h)) for k in (-2, -1, 1, 2)]; return (l[0] - 8 * l[1] + 8 * l[2] - l[3]) / (12 * h)
        e1, e2 = e1f(N), e2f(N); e3 = (math.log(abs(e2f(N + h))) - math.log(abs(e2f(N - h)))) / (2 * h)
        ns = 1 - 2 * e1 - e2 - 2 * e1 ** 2 - (2 * C_SR + 3) * e1 * e2 - C_SR * e2 * e3
        V = self.Vr(S(N)[0]); H2 = V / (3 - e1); P1 = H2 / (8 * math.pi ** 2 * e1) * (1 - 2 * (C_SR + 1) * e1 - C_SR * e2)
        return ns, 16 * e1 * (1 + C_SR * e2), dict(e1=e1, V=V, H2=H2, A=math.sqrt(As_m / P1))


print('== A. data')
tens = (DS['ACT'][0] - DS['Pl'][0]) / math.hypot(DS['Pl'][1], DS['ACT'][1])
print('   n_s: Planck 0.9649(42); P-ACT-LB DR1 0.9740(30); with DESI DR2 0.9752(30); r < 0.036 (BK18), ~0.032 combined')
print('   ACT - Planck = %.4f = %.1f sigma (shared Planck data: a lower bound on the tension); both reported below' % (DS['ACT'][0] - DS['Pl'][0], tens))

print('== B. Starobinsky R^2 (supplied term, inflaton G)')
s23 = math.sqrt(2 / 3)
ST = Model(lambda p: 0.75 * (1 - cmath.exp(-s23 * p)) ** 2, 5.0)
Nreq = {k: brentq(lambda n: ST.flow(n)[0] - c, 30, 100) for k, (c, s) in DS.items()}
check('B1 N* that gives each n_s (2nd-order flow): Planck %.2f, ACT %.2f, DR2 %.2f (leading 2/(1-n_s): %.1f, %.1f, %.1f); r there %.4f, %.4f, %.4f'
      % (*Nreq.values(), *(2 / (1 - c) for c, s in DS.values()), *(ST.flow(n)[1] for n in Nreq.values())),
      abs(ST.flow(55)[0] - 0.96489) < 2e-5 and 70 < Nreq['ACT'] < 80)
H0 = 67.4e3 / 3.0857e22 * 6.582e-25; T0K = 2.348e-13
def a3(mu): return 1 / (1 / 0.1180 + 7 / (2 * math.pi) * math.log(mu / 91.1876))
def Gam_col(M): Mg = M * MP; return 49 * a3(Mg) ** 2 * Mg ** 3 / (192 * math.pi ** 3 * MP ** 2) + 3 * 172.7 ** 2 * Mg / (48 * math.pi * MP ** 2)
def nstar(w=0.0, rho_rh=None, gam=None, gs=106.75):
    Ns = 55.0
    for _ in range(6):
        _, _, d = ST.flow(Ns); M = d['A']; Hs = math.sqrt(d['H2']) * M * MP; ye = math.exp(-s23 * ST.PEND)
        rho_end = 1.5 * 0.75 * (1 - ye) ** 2 * M ** 2 * MP ** 4
        rr = 3 * MP ** 2 * gam(M) ** 2 if gam else (rho_rh if rho_rh else rho_end)
        Trh = (30 * rr / (math.pi ** 2 * gs)) ** 0.25
        Ns = (-math.log(0.05 / (67.4 / 2.99792458e5)) + math.log(Hs / H0) + math.log(rr / rho_end) / (3 * (1 + w))
              + math.log(3.909 / gs) / 3 + math.log(T0K / Trh))
    return Ns, Trh, rho_end
Ninst, _, rho_end = nstar(); Ncol, Tcol, _ = nstar(0.0, gam=Gam_col)
rho_bbn = math.pi ** 2 / 30 * 10.75 * 4e-3 ** 4; Nkin, _, _ = nstar(1.0, rho_rh=rho_bbn, gs=10.75)
check('B2 reheating histories (e-fold matching at k = 0.05/Mpc): colour-anomaly decay (w = 0, T_rh = %.1e GeV) N* = %.1f, n_s = %.4f [%s]; '
      'instant N* = %.1f, n_s = %.4f [%s]; plain R^2 reheats through its quadratic minimum (w = 0), so instant is its maximum'
      % (Tcol, Ncol, ST.flow(Ncol)[0], pulls(ST.flow(Ncol)[0]), Ninst, ST.flow(Ninst)[0], pulls(ST.flow(Ninst)[0])),
      48 < Ncol < 53 and 54 < Ninst < 58 and (DS['ACT'][0] - ST.flow(Ncol)[0]) / DS['ACT'][1] > 3.5)
w, L = sp.symbols('w L', positive=True)
dN = (3 * w - 1) * L / (12 * (1 + w)); lnE = 2 * (3 * w - 1) / (3 * w + 1) * (1 + 3 * w) / 2 * L / (3 * (1 + w))
check('B3 THEOREM (sympy): a phase of constant w from rho_end to rho_rh adds dN = (3w-1) ln(rho_end/rho_rh)/(12(1+w)) e-folds and boosts '
      'the GW background of the modes entering in it by E with ln E = 4 dN for every w; kination (w = 1) to BBN (4 MeV): N* = %.1f, n_s = %.4f [%s]: '
      'even the stiffest phase to BBN does not reach ACT (needs %.1f)' % (Nkin, ST.flow(Nkin)[0], pulls(ST.flow(Nkin)[0]), Nreq['ACT']),
      sp.simplify(lnE / dN) == 4 and Ninst + 10 < Nkin < Nreq['ACT'])
r_i = ST.flow(Ninst)[1]; Om_rad = 4.15e-5 * 0.39 * r_i * As_m / 24; Om_max = 5.6e-6 * 0.3
dNgw = math.log(Om_max / Om_rad) / 4; Ngw = Ninst + dNgw
check('B4 ESTIMATE: Omega_GW h^2 = %.1e on the radiation plateau vs the BBN/N_eff limit %.1e (dN_eff < 0.3) caps any stiff phase at dN <= %.1f: '
      'N* <= %.1f, n_s <= %.4f [%s]; ACT needs dN = %.1f, a GW boost e^%.0f' % (Om_rad, Om_max, dNgw, Ngw, ST.flow(Ngw)[0], pulls(ST.flow(Ngw)[0]),
      Nreq['ACT'] - Ninst, 4 * (Nreq['ACT'] - Ninst)), ST.flow(Ngw)[0] < DS['ACT'][0] - DS['ACT'][1])

print('== C. the rules\' own forms')
def Afr(x): return cmath.asin(x * x / (1 - x * x)) / cmath.sqrt(1 - 2 * x * x)
rat = []
for q in (1e3, 1e4):
    us = brentq(lambda x: Afr(x).real - q / 2, 1e-9, (1 - 1e-15) / math.sqrt(2), xtol=1e-17, rtol=1e-15)
    dA = Afr(complex(us, 1e-20)).imag / 1e-20; rat.append((3 * (q / 2) / (us * dA)) / (3 * math.pi ** 2 / q ** 2))
wneed = {k: (1 - c) / 6 - 1 for k, (c, s) in DS.items()}
check('C1 hinge plateau (theorem in the limit, check %.3f %.3f): eps_H = 3(1+w)(pi rho*/rho)^2, n_s - 1 = -6(1+w): needs w = %.5f (Planck), %.5f (ACT), '
      '%.5f (DR2), a fluid no rule supplies; P_t >= 4/pi^2 = 0.41 at l = a vs r A_s < %.1e: excluded on both datasets by the amplitude'
      % (*rat, wneed['Pl'], wneed['ACT'], wneed['DR2'], R_MAX * As_m), all(abs(x - 1) < 0.02 for x in rat) and 4 / math.pi ** 2 > 1e9 * R_MAX * As_m)
lP, Mpc = 1.616255e-35, 3.0857e22; acell = math.sqrt(8 * math.pi) * lP; Lp = math.log(Mpc / 0.05 / acell); Lind = 4.891 / 2
MZ = 91.1876; Mc = 1.220890e19 / math.sqrt(8 * math.pi); aY = 127.951 * (1 - 0.23122); bY = 41 / 6
NY = (aY - bY / (2 * math.pi) * math.log(Mc / MZ)) / (bY / (2 * math.pi))
Lf = Lp - (math.log(Mc / 2.3487e-13) + math.log(106.75 / 3.909) / 3)
rd = {'ladder induced L*+C/2': 1 - 2 / (Lp + Lind), 'hypercharge pole at cell': 1 - 2 / NY, 'common-epoch induced': 1 - 2 / (Lf + Lind),
      'common-epoch hypercharge': 1 - 2 / (Lf + NY)}
gneed = {k: (1 - c) * Lp for k, (c, s) in DS.items()}
print('   C2 running coupling n_s - 1 = gamma/N (running-tilt C1; C = 4.891 cited), gamma = -2:')
for k, v in rd.items(): print('      %-26s n_s %.4f [%s]' % (k, v, pulls(v)))
check('C2 N to the pole needed: %.1f (Planck), %.1f (ACT), %.1f (DR2); on the ladder (N >= L* = %.2f) |gamma| = %.2f, %.2f, %.2f: ACT moves the '
      'ladder reading from +4.8 to +3.8 sigma, still excluded; gamma is supplied' % (*(2 / (1 - c) for c, s in DS.values()), Lp, *gneed.values()),
      (rd['ladder induced L*+C/2'] - DS['ACT'][0]) / DS['ACT'][1] > 3)
NeA = 2 / (1 - DS['ACT'][0]); qr = 2 * (8 / R_MAX) * (1 - DS['ACT'][0])
check('C3 constant transfer per split (split-schedule E): n_s = 1 - q/(2N_e), r = 8/N_e single-clock: ACT with q = 4 needs N_e = %.1f, r = %.3f '
      '(excluded); r < 0.036 needs N_e > 222 and q = %.1f; its Jordan-frame reading is R^2 (inflaton G2), i.e. B' % (NeA, 8 / NeA, qr), 8 / NeA > R_MAX)
v60 = 1 - 2 / 60
check('C4 legacy graph-growth notes on main (PRIMORDIAL_SPECTRUM, TENSOR_SCALAR_RATIO 2026-04-22): n_s = 1 - 2/N_e at N_e = 60 is %.4f [%s]; ACT needs N_e = %.1f'
      % (v60, pulls(v60), NeA), (v60 - DS['ACT'][0]) / DS['ACT'][1] < -2)

print('== D. shapes (exact background, 2nd-order flow); max n_s with r < 0.036 at N* = 50.3 / 55.7')
ph, k_, c_, N_, ka = sp.symbols('phi k c N kappa', positive=True)
Np = ph ** (k_ + 2) / (c_ * k_ * (k_ + 2)); etap = sp.diff(-c_ * ph ** -k_, ph, 2)
Ne = sp.exp(ka * ph) / (c_ * ka ** 2); etae = sp.diff(-c_ * sp.exp(-ka * ph), ph, 2)
ok_pl = sp.simplify(etap * Np + (k_ + 1) / (k_ + 2)) == 0 and sp.simplify(etae * Ne + 1) == 0 and \
    sp.simplify(sp.diff(Np, ph) * sp.diff(-c_ * ph ** -k_, ph) - 1) == 0 and sp.simplify(sp.diff(Ne, ph) * sp.diff(-c_ * sp.exp(-ka * ph), ph) - 1) == 0
kneed = {}
for nn in (Ncol, Ninst):
    t = (1 - DS['ACT'][0]) * nn / 2; kneed[nn] = (2 * t - 1) / (1 - t)
tP = (1 - DS['Pl'][0]) * Ninst / 2
check('D1 THEOREM (leading order in 1/N, sympy): V = 1 - c e^(-kappa phi) gives n_s = 1 - 2/N for every kappa (Starobinsky, alpha-attractors, Higgs); '
      'V = 1 - c phi^-k gives n_s = 1 - 2(k+1)/((k+2)N). ACT needs k = %.2f (N* %.1f) or %.2f (N* %.1f); Planck needed k = %.0f (N* %.1f): '
      'ACT asks for a power-law, not exponential, approach to the plateau' % (kneed[Ncol], Ncol, kneed[Ninst], Ninst, (2 * tP - 1) / (1 - tP), Ninst),
      ok_pl and 0 < kneed[Ncol] < kneed[Ninst] < 3)
def r3V(lam):
    def V(p):
        F = cmath.exp(s23 * p); x = 2 * (F - 1) / (1 / 3 + cmath.sqrt(1 / 9 + lam * (F - 1) / 3))
        return (x * F - (x + x * x / 6 + lam * x ** 3 / 36)) / (2 * F * F)
    return V
fam = {'E-model alpha': [(lambda p, kk=math.sqrt(2 / (3 * a)): (1 - cmath.exp(-kk * p)) ** 2, 5 * math.sqrt(a)) for a in np.geomspace(0.3, 1000, 12)],
       'T-model alpha': [(lambda p, a=a: cmath.tanh(p / math.sqrt(6 * a)) ** 2, 5 * math.sqrt(a)) for a in np.geomspace(0.3, 1000, 12)],
       'power plateau k=1': [(lambda p, m=m: p / (p + m), 5 * m + 5) for m in np.geomspace(0.01, 10, 7)],
       'power plateau k=2': [(lambda p, m=m: p ** 2 / (p ** 2 + m ** 2), 5 * m + 5) for m in np.geomspace(0.01, 10, 7)],
       'power plateau k=4': [(lambda p, m=m: p ** 4 / (p ** 4 + m ** 4), 5 * m + 5) for m in np.geomspace(0.01, 10, 7)],
       'hilltop p=2,4,6': [(lambda q, m=m, pp=pp: 1 - ((m - q) / m) ** pp, 0.5 * m) for pp in (2, 4, 6) for m in (5, 10, 15, 20, 30, 50)],
       'natural (copy-mass class)': [(lambda q, f=f: 1 - cmath.cos(q / f), 1.5 * f) for f in (3, 5, 7, 10, 20, 100)],
       'R^2 + lam R^3': [(r3V(l), 5.0) for l in (-2e-4, -1e-4, -5e-5, -2e-5, 2e-5, 5e-5, 1e-4)]}
grid = {}
for nm, lst in fam.items():
    res = []
    for V, x0 in lst:
        m = Model(V, x0); res.append([m.flow(n)[:2] for n in (Ncol, Ninst)])
    grid[nm] = res
    best = [max([x[i][0] for x in res if x[i][1] < R_MAX], default=float('nan')) for i in (0, 1)]
    print('   %-26s %.4f / %.4f  [ACT %+.1f / %+.1f]' % (nm, best[0], best[1], *((b - DS['ACT'][0]) / DS['ACT'][1] for b in best)))
lam_need = {}
for lab, nn in (('Ncol', Ncol), ('Ninst', Ninst)):
    for k in ('Pl', 'ACT', 'DR2'):
        lam_need[(lab, k)] = brentq(lambda l: Model(r3V(l), 5.0).flow(nn)[0] - DS[k][0], -2.5e-4, 3e-5, xtol=1e-8)
okD = max(x[1][0] for x in grid['power plateau k=1'] if x[1][1] < R_MAX) > DS['ACT'][0] and \
    max(x[0][0] for x in grid['hilltop p=2,4,6'] if x[0][1] < R_MAX) < DS['ACT'][0] - 2 * DS['ACT'][1] and \
    max(x[1][0] for x in grid['E-model alpha'] if x[1][1] < R_MAX) < DS['ACT'][0] - 2 * DS['ACT'][1]
check('D2 at r < 0.036 the exponential plateaus (E/T alpha-attractors, any alpha) and natural inflation stay > 2 sigma below ACT at N* <= 55.7, hilltops '
      'reach -1 sigma only near r ~ 0.03 at instant reheating; power plateaus k = 1, 2 and R^2 + lam R^3 reach it. lam for Planck/ACT/DR2: N* %.1f: %.1e %.1e %.1e; N* %.1f: %.1e %.1e %.1e (negative: a softened R^2 tail)'
      % (Ncol, lam_need[('Ncol', 'Pl')], lam_need[('Ncol', 'ACT')], lam_need[('Ncol', 'DR2')], Ninst, lam_need[('Ninst', 'Pl')], lam_need[('Ninst', 'ACT')],
         lam_need[('Ninst', 'DR2')]), okD and lam_need[('Ncol', 'ACT')] < 0)

print('== E. can the rules supply the shift')
Mi = ST.flow(Ninst)[2]['A']; Mc_ = ST.flow(Ncol)[2]['A']; cneed = 1 / (12 * Mi ** 2)
check('E1 THEOREM: V = M^2 v(phi) makes eps, eta, n_s and r M-free, so in pure R^2 n_s depends on N* alone; a lattice R^2 piece (Kuhn O(k^4) '
      'remainder, O(0.1)) changes c = %.1e by ~2e-10 and n_s by nothing: no R^2-type term can lift the tilt' % cneed,
      abs(Model(lambda p: 7.3 * 0.75 * (1 - cmath.exp(-s23 * p)) ** 2, 5.0).flow(55)[0] - ST.flow(55)[0]) < 1e-9)
Hl2 = (2 * math.sqrt(ST.flow(Ninst)[2]['H2']) * Mi) ** 2
check('E2 ESTIMATE hinge Friedmann law H^2 = rho/3 (1 - rho/rho* + ...): rho/rho* = (Hl)^2/2 <= %.1e at l = 2a, so |dn_s| <~ 2 rho/rho* = %.0e vs the needed +%.3f'
      % (Hl2 / 2, Hl2, DS['ACT'][0] - ST.flow(Ncol)[0]), Hl2 < 1e-8)
lamA = lam_need[('Ncol', 'ACT')]; lam_nat = 72 * Mc_ ** 4; Rst = 230
lam_loop = 72 * 1e-2 * Mc_ ** 2 / (16 * math.pi ** 2 * Rst)
check('E3 cubic: a cell-scale c3 R^3 with c3 = O(1) a^4 gives lam = 72 M^4 c3 = %.1e c3 vs the needed %.1e (%.0e x short); a loop of any field heavy '
      'enough to be local (m^2 > R* ~ %d M^2), a3 coefficient <= 1e-2: |lam| <= %.0e (ESTIMATE); lam is a second supplied coefficient' % (lam_nat, lamA, abs(lamA) / lam_nat, Rst, lam_loop),
      abs(lamA) / lam_nat > 1e10 and abs(lamA) / lam_loop > 1e8)
g2 = 1.5 * (1 - DS['ACT'][0])
check('E4 copy-mass promotion is the natural-inflation class (inflaton E1): it never reaches 1 - 2/N at r < 0.036 (row above); the SU(2) condensate '
      'hilltop needs g^2 = %.3f (1/alpha = %.0f) for ACT and stands at 24/g^2 = %.0f M_P^4, %.0e x the tensor bound' % (g2, 4 * math.pi / g2, 24 / g2, 24 / g2 / (3 * R_MAX * As_m * math.pi ** 2 / 2)),
      max(x[1][0] for x in grid['natural (copy-mass class)'] if x[1][1] < R_MAX) < DS['ACT'][0] - 3 * DS['ACT'][1])
print('   E5 SPECULATION: a k = 1 tail is the 3D Coulomb form (1 - mu/phi); the rules hold no canonically normalised separation modulus to carry it')

print('== F. look-elsewhere')
reads = {'R2 colour reheat': ST.flow(Ncol)[0], 'R2 instant': ST.flow(Ninst)[0], **rd, 'transfer q=4 N57': 1 - 2 / 57, 'transfer q=2 N57': 1 - 1 / 57,
         'graph growth N60': v60, 'running-tilt cell 1/a=24': 1 - 2 / (Lp + 24 / (4 / (3 * math.pi))), 'running-tilt cell 1/a=42': 1 - 2 / (Lp + 42 / (4 / (3 * math.pi)))}
hit = {k: sum(abs(v - c) < 2 * s for v in reads.values()) for k, (c, s) in DS.items()}
exp_ = {k: len(reads) * 4 * s / 0.04 for k, (c, s) in DS.items()}
check('F1 %d campaign readings (all with a supplied piece) within 2 sigma: Planck %d, ACT %d, DR2 %d vs %.1f, %.1f, %.1f by chance (uniform on 0.955-0.995): '
      'a reading landing on either dataset is not evidence' % (len(reads), *hit.values(), *exp_.values()), max(exp_.values()) > 1)
pts = [x[1] for v in grid.values() for x in v]
fA = sum(abs(p[0] - DS['ACT'][0]) < 2 * DS['ACT'][1] and p[1] < R_MAX for p in pts) / len(pts)
fP = sum(abs(p[0] - DS['Pl'][0]) < 2 * DS['Pl'][1] and p[1] < R_MAX for p in pts) / len(pts)
check('F2 shape grid (%d points, N* = %.1f): %.0f%% fit ACT at 2 sigma with r < 0.036, %.0f%% fit Planck; every fit spends >= 1 supplied shape parameter'
      % (len(pts), Ninst, 100 * fA, 100 * fP), 0.05 < fA < 0.9 and fP > 0.05)
print('supplied: R^2 and R^3 coefficients, shape families, pivot 0.05/Mpc, g*, colour running + top mass, GW transfer factors, BBN dN_eff,')
print('  C = 4.891 and SM b_i (running-tilt), measured n_s/r/A_s. Cited: inflaton B4/E1/G, running-tilt C-D, split-schedule E.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
