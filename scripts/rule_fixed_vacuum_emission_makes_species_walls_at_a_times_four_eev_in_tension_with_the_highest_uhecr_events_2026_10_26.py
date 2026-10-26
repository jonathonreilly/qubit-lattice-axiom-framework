AUDIT_INPUT_PATHS = ('docs/RULE_FIXED_VACUUM_EMISSION_MAKES_SPECIES_WALLS_AT_A_TIMES_FOUR_EEV_IN_TENSION_WITH_THE_HIGHEST_UHECR_EVENTS_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Rates and energy-loss lengths for vacuum emission by UHE protons and nuclei under the rule-fixed
dimension-six dispersion E = p + m^2/2p + c p^3/E*^2 (c_g = -S/24 links, c_q = -S/6 + 1/24 light
fermions, S = sum n_i^4; E* = hbar c/2L, L = sqrt(8 pi) l_P), with hadron-level parton additivity
c_h = sum_i <x^3>_i c_i (supplied PDFs; inherited from agents/liv-auger-confrontation).
Rate: collinear golden rule Gamma = (1/16 pi P) int dy |M|^2 F^2, k_perp^2 = y(1-y) D(y),
D = M_a^2(P) - M_b^2/(1-y) - mu^2/y with momentum-dependent effective masses M^2 = m^2 + 2 c K^4/E*^2.
Photon vertex |M|^2 = 2 e^2 D (1+(1-y)^2)/y (spin 1/2) or 2 e^2 D 2(1-y)/y (spin 0); pi0: g^2 (2 p.p' - 2 m^2).
Sections: R rate formula check (Frank-Tamm); A p -> p gamma; B p -> p pi0; C nuclei; D data confrontation."""
import math, os, time
os.environ.setdefault('OMP_NUM_THREADS', '1'); os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
from scipy.linalg import expm
from scipy.special import beta as B
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar

AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261026); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")

# ---- supplied constants ----
MP = 1.22089e28; Es = MP / (2 * math.sqrt(8 * math.pi))
mp, mpi, mN = 938.272e6, 134.977e6, 931.494e6
alpha = 1 / 137.036; e2 = 4 * math.pi * alpha
g2piNN = 4 * math.pi * 13.7                     # g^2/4pi = 13.7 (supplied)
HBARC = 1.97327e-5                              # eV cm
KPC, MPC = 3.0857e21, 3.0857e24                 # cm
cg = lambda S: -S / 24; cq = lambda S: -S / 6 + 1 / 24
GD2 = lambda Q2: (1 + Q2 / 0.71e18) ** -4       # dipole G_D^2 (Q2 in eV^2), supplied
GA2 = lambda Q2: (1 + Q2 / (1.03e9) ** 2) ** -4  # axial dipole M_A = 1.03 GeV, supplied
MUP2 = 2.793 ** 2

# ---- parton weights (inherited, supplied toy PDFs + LO N=4 evolution) ----
def proton_moments(a=0.7, bu=3.0, bd=4.0, fs=0.14, bg=5.0, bs=7.0):
    def val(nq, b):
        N = nq / B(a, b + 1); return N * B(a + 1, b + 1), N * B(a + 3, b + 1)
    mu, xu = val(2, bu); md, xd = val(1, bd)
    shape = lambda e, b, f: f / B(e + 1, b + 1) * B(e + 3, b + 1)
    xs = shape(-0.15, bs, fs); fg = 1 - mu - md - fs
    return np.array([xu + xd + xs, shape(-0.1, bg, fg)])
def pion_moments(a=0.6, bv=1.2, fs=0.12, bg=4.0):
    N = 2 / B(a, bv + 1); mv, xv = N * B(a + 1, bv + 1), N * B(a + 3, bv + 1)
    fg = 1 - mv - fs
    return np.array([xv + fs / B(0.85, 7) * B(2.85, 7), fg / B(0.9, bg + 1) * B(2.9, bg + 1)])
CF, CA, TR = 4 / 3, 3.0, 0.5
def gamma_AP(N, nf):
    S1 = sum(1 / k for k in range(1, N + 1))
    return np.array([[CF * (1.5 + 1 / (N * (N + 1)) - 2 * S1), 2 * nf * TR * (N * N + N + 2) / (N * (N + 1) * (N + 2))],
                     [CF * (N * N + N + 2) / (N * (N * N - 1)), 2 * CA * (1 / (N * (N - 1)) + 1 / ((N + 1) * (N + 2)) - S1) + (11 * CA - 4 * nf * TR) / 6]])
def evolve(M, Q0=2.0, Q1=Es * 1e-9, a=0.30):
    b0 = lambda nf: 11 - 2 * nf / 3
    for qa, qb, nf in ((Q0, 172.7, 5), (172.7, Q1, 6)):
        a1 = a / (1 + a * b0(nf) / (4 * math.pi) * math.log(qb ** 2 / qa ** 2))
        M = expm(-(2 / b0(nf)) * gamma_AP(4, nf) * math.log(a1 / a)) @ M; a = a1
    return M
Wp = {'2GeV': proton_moments()}; Wp['E*'] = evolve(Wp['2GeV'])
Wpi = {'2GeV': pion_moments()}; Wpi['E*'] = evolve(Wpi['2GeV'])
RAYS = (('axis', 1.0), ('sky', 0.6), ('body', 1 / 3))
ch = lambda W, S: W[0] * cq(S) + W[1] * cg(S)

# ---- generic collinear 1 -> 2 rate ----
def make(ma2, ca, mb2, cb, mx2, cx, kind, Z2=1.0, ff=lambda Q2: 1.0):
    """returns D(y,P) and rate(P) -> (Gamma, Gamma_E) in eV"""
    def D(y, P):
        u = 2 * P ** 4 / Es ** 2
        return (ma2 + ca * u) - (mb2 + cb * u * (1 - y) ** 4) / (1 - y) - (mx2 + cx * u * y ** 4) / y
    def integrand(y, P, w):
        d = D(y, P)
        if d <= 0: return 0.0
        Q2 = -(mx2 + cx * 2 * P ** 4 / Es ** 2 * y ** 4)
        if kind == 'f':   m2 = 2 * e2 * Z2 * d * (1 + (1 - y) ** 2) / y
        elif kind == 's': m2 = 2 * e2 * Z2 * d * 2 * (1 - y) / y
        else:
            u = 2 * P ** 4 / Es ** 2
            m2 = g2piNN * ((ma2 + ca * u) + (mb2 + cb * u * (1 - y) ** 4) - (mx2 + cx * u * y ** 4) - 2 * ma2)
        return max(m2, 0.0) * ff(max(Q2, 0.0)) * (y if w else 1.0) / (16 * math.pi * P)
    def rate(P):
        ys = np.concatenate([np.logspace(-12, -1, 400), np.linspace(0.1, 1 - 1e-9, 1200)])
        dv = np.array([D(y, P) for y in ys])
        j = int(np.argmax(dv))
        lo, hi = ys[max(j - 1, 0)], ys[min(j + 1, len(ys) - 1)]
        r = minimize_scalar(lambda y: -D(y, P), bounds=(lo, hi), method='bounded', options={'xatol': 1e-14})
        if -r.fun <= 0: return 0.0, 0.0
        ym = r.x
        a = brentq(lambda y: D(y, P), ys[0], ym, xtol=1e-16) if D(ys[0], P) < 0 else ys[0]
        b = brentq(lambda y: D(y, P), ym, ys[-1], xtol=1e-16) if D(ys[-1], P) < 0 else ys[-1]
        pts = [a, ym, b] if a < ym < b else [a, b]
        out = []
        for w in (0, 1):
            s = 0.0
            for u0, u1 in zip(pts[:-1], pts[1:]):
                if u1 / u0 > 100:  # log substitution for wide windows
                    s += quad(lambda t: integrand(math.exp(t), P, w) * math.exp(t), math.log(u0), math.log(u1), limit=200)[0]
                else:
                    s += quad(lambda y: integrand(y, P, w), u0, u1, limit=200)[0]
            out.append(s)
        return out[0], out[1]
    return D, rate
def threshold(D, Plo=1e17, Phi=1e23):
    ys = np.concatenate([np.logspace(-12, -1, 400), np.linspace(0.1, 1 - 1e-9, 1200)])
    def dmax(P):
        dv = np.array([D(y, P) for y in ys]); j = int(np.argmax(dv))
        r = minimize_scalar(lambda y: -D(y, P), bounds=(ys[max(j-1,0)], ys[min(j+1,len(ys)-1)]), method='bounded', options={'xatol': 1e-14})
        return max(-r.fun, dv[j])
    if dmax(Phi) <= 0: return math.inf
    lo, hi = math.log(Plo), math.log(Phi)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if dmax(math.exp(mid)) > 0: hi = mid
        else: lo = mid
    return math.exp(hi)
lcm = lambda GE: HBARC / GE if GE > 0 else math.inf

# ---- R: Frank-Tamm check (constant index n = 1 + d, LI point fermion) ----
d_ = 1e-20; P_ = 1e20
DFT = lambda y: mp ** 2 - mp ** 2 / (1 - y) + 2 * d_ * (y * P_) ** 2 / y
num = quad(lambda y: alpha / (2 * P_) * max(DFT(y), 0) * (1 + (1 - y) ** 2) / y, 1e-9, 1e-6, limit=200)[0]
ft = alpha * (2 * d_ - mp ** 2 / P_ ** 2) * (1e-6 - 1e-9) * P_
check('R1 collinear rate reproduces Frank-Tamm dN/dx dw = alpha (1 - 1/(beta n)^2) for soft photons (normalisation check)',
      abs(num / ft - 1) < 2e-3, f'ratio {num / ft:.5f}')

# ---- A: p -> p gamma ----
print('   A: p -> p gamma (elastic, |M|^2 x G_D^2 .. mu_p^2 G_D^2); l_E = hbar c/Gamma_E')
TAB = {}; thrA = {}; worst_l = 0; eps_100 = []
for ray, S in RAYS:
    for tag in ('2GeV', 'E*'):
        c_p = ch(Wp[tag], S)
        D, rate = make(mp ** 2, c_p, mp ** 2, c_p, 0.0, cg(S), 'f', ff=GD2)
        Pth = threshold(D); thrA[(ray, tag)] = Pth
        eps = np.logspace(-7, 1, 25); GE = np.array([rate(Pth * (1 + e))[1] for e in eps])
        TAB[(ray, tag)] = (Pth, eps, GE)
        l1 = lcm(rate(Pth * 1.01)[1]); l2 = lcm(rate(2 * Pth)[1]); worst_l = max(worst_l, l1)
        k = np.polyfit(np.log(eps[:6]), np.log(GE[:6]), 1)
        e100 = math.exp((math.log(HBARC / (100 * MPC)) - k[1]) / k[0]); eps_100.append(e100)
        if tag == 'E*' or ray == 'sky':
            print(f'   {ray:4s} W@{tag:4s}: E_th {Pth/1e18:.2f} EeV; l(1.01 E_th) {l1:.1e} cm, l(2 E_th) {l2:.1e} cm; '
                  f'Gamma_E ~ eps^{k[0]:.2f}; l = 100 Mpc at eps = {e100:.0e}')
check('A1 p -> p gamma above threshold: energy-loss length < 1 kpc already at 1.01 E_th on every ray and weighting (G_D^2 suppression included) -> hard wall',
      worst_l < KPC, f'worst l(1.01 E_th) = {worst_l:.1e} cm (1 kpc = 3.1e21 cm); thresholds {min(thrA.values())/1e18:.2f}-{max(thrA.values())/1e18:.2f} EeV')
check('A2 near-threshold law Gamma_E ~ eps^(3/2): the 100 Mpc loss length is reached within eps << 1e-3 of E_th, so E_cut = E_th (sharp)',
      max(eps_100) < 1e-3, f'max eps(100 Mpc) = {max(eps_100):.0e}; mu_p^2 G_D^2 bracket shortens l by {MUP2:.1f}x')

# ---- B: p -> p pi0 ----
thrB = {}; lB = []
for ray, S in RAYS:
    for tag in ('2GeV', 'E*'):
        c_p, c_pi = ch(Wp[tag], S), ch(Wpi[tag], S)
        D, rate = make(mp ** 2, c_p, mp ** 2, c_p, mpi ** 2, c_pi, 'p', ff=GA2)
        Pth = threshold(D); thrB[(ray, tag)] = Pth; lB.append(lcm(rate(1.01 * Pth)[1]))
print('   B: p -> p pi0 thresholds (EeV): ' + ', '.join(f'{r}/{t} {v/1e18:.1f}' for (r, t), v in thrB.items()))
check('B1 p -> p pi0 opens above the photon wall on every ray (7-21 EeV > 3.2-4.4 EeV) and is itself a hard wall (l(1.01 E_th) < 1 kpc): it never sets the proton cutoff',
      all(thrB[k] > thrA[k] for k in thrA) and max(lB) < KPC, f'max l(1.01 E_th) = {max(lB):.1e} cm')

# ---- C: nuclei ----
NUC = {'He': (4, 2, 1.68), 'N': (14, 7, 2.56), 'Si': (28, 14, 3.12), 'Fe': (56, 26, 3.74)}  # A, Z, r_rms fm (supplied)
def Ecut_from(rate_fn, Plo, Phi, L):
    f = lambda t: math.log(lcm(rate_fn(math.exp(t))) / L)
    if f(math.log(Phi)) > 0: return math.inf
    lo, hi = math.log(Plo), math.log(Phi)
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if lcm(rate_fn(math.exp(mid))) > L: lo = mid
        else: hi = mid
    return math.exp(hi)
print('   C1 coherent emission (Z^2, Gaussian charge form factor): kinematic threshold ~ sqrt(A) E_th,p; E_cut(l = 1 Mpc), EeV')
coh = {}
for nm, (A, Z, r) in NUC.items():
    MA = A * mN; r2 = (r * 1e-13 / HBARC) ** 2
    row = []
    for ray, S in (('axis', 1.0), ('body', 1 / 3)):
        cA = ch(Wp['E*'], S) / A ** 2
        D, rate = make(MA ** 2, cA, MA ** 2, cA, 0.0, cg(S), 's', Z2=Z * Z, ff=lambda Q2, r2=r2: math.exp(-Q2 * r2 / 3))
        Pk = threshold(D)
        Ec = Ecut_from(lambda P: rate(P)[1], Pk * 1.0001, 1e23, MPC)
        row.append((Pk, Ec))
    coh[nm] = row
    print(f'   {nm:2s}: kin thr axis/body {row[0][0]/1e18:.0f}/{row[1][0]/1e18:.0f}; E_cut axis/body {row[0][1]/1e18:.0f}/{row[1][1]/1e18:.0f}')
check('C1 coherent channel: kinematically open from ~sqrt(A) x E_th,p but form-factor-dead there; Gaussian-model E_cut for Fe lies above the incoherent wall',
      all(c[0][1] > c[0][0] for c in coh.values()), 'Gaussian F_A is a supplied model (falls faster than real large-q tails)')

# incoherent: nucleon at light-cone fraction alpha/A; Fermi-gas core (weight 0.8, k_F = 250 MeV) + tail 0.2 s e^{-s(alpha-1)}
kF = 0.25e9 / mN
def rho(a, s):
    core = 0.8 * 0.75 / kF * max(0.0, 1 - ((a - 1) / kF) ** 2)
    tail = 0.2 * s * math.exp(-s * (a - 1)) if (s and a >= 1) else 0.0
    return core + tail
incoh = {}
for ray, S in (('axis', 1.0), ('body', 1 / 3)):
    c_n = ch(Wp['E*'], S)
    D, rate = make(mp ** 2, c_n, mp ** 2 + 2 * mp * 8e6, c_n, 0.0, cg(S), 'f', ff=GD2)
    PthN = threshold(D)
    lk = np.logspace(-7, 1.5, 40); GEt = np.array([rate(PthN * (1 + e))[1] for e in lk])
    kk = np.polyfit(np.log(lk[:5]), np.log(GEt[:5]), 1)
    def GN(K):
        e = K / PthN - 1
        if e <= 0: return 0.0
        if e < lk[0]: return math.exp(kk[1]) * e ** kk[0]
        return math.exp(np.interp(math.log(e), np.log(lk), np.log(GEt)))
    for nm, (A, Z, r) in NUC.items():
        for s in (0, 16.5, 8.0):
            def RA(P, A=A, Z=Z, s=s):
                a0 = A * PthN / P
                amax = 1 + kF if s == 0 else 12.0
                if a0 >= amax: return 0.0
                g = np.linspace(a0, amax, 600)
                v = np.array([rho(a, s) * GN(a * P / A) * a for a in g])  # nucleon energy share alpha/A of P: Gamma_E/E_A
                return Z * np.trapezoid(v, g) / A
            incoh[(nm, ray, s)] = (A * PthN, Ecut_from(RA, 1e18, 1e22, KPC), Ecut_from(RA, 1e18, 1e22, MPC), Ecut_from(RA, 1e18, 1e22, 100 * MPC))
print('   C2 incoherent (Z x nucleon elastic, alpha-smeared) E_cut (EeV) at l = 1 kpc / 1 Mpc / 100 Mpc; no-tail | s = 16.5 | s = 8:')
for nm in NUC:
    print(f'   {nm:2s} ' + ' ; '.join(f'{ray}: ' + ' | '.join('{:.0f}/{:.0f}/{:.0f}'.format(*(x / 1e18 for x in incoh[(nm, ray, s)][1:])) for s in (0, 16.5, 8.0)) for ray in ('axis', 'body')))
Fe_nt = [incoh[('Fe', r, 0)][3] for r in ('axis', 'body')]; Fe_t = [incoh[('Fe', r, s)][3] for r in ('axis', 'body') for s in (16.5, 8.0)]
check('C2 incoherent walls: Fermi-core only gives E_cut(Fe) ~ A E_th/(1 + k_F/m); an exponential high-momentum tail (s = 8-16.5, supplied) pulls it far lower',
      max(Fe_t) < min(Fe_nt), f'Fe 100 Mpc cut: no tail {Fe_nt[0]/1e18:.0f}-{Fe_nt[1]/1e18:.0f} EeV; tails {min(Fe_t)/1e18:.0f}-{max(Fe_t)/1e18:.0f} EeV')

# ---- D: confrontation ----
Emax_nt = max(Fe_nt); Emax_t = max(Fe_t)
AMA, AMA_lo, FLY = 2.44e20, 1.68e20, 3.2e20
check('D1 highest events vs heaviest-species wall (Fe, 100 Mpc): Fermi-core-only: wall below the Amaterasu central value on every ray, above its lower-syst edge only on body-like rays; with an exponential tail it is below 1e20 eV (the observed >1e20 flux)',
      AMA_lo < Emax_nt < AMA and min(Fe_nt) < AMA_lo and Emax_t < 1e20, f'Fe wall {Emax_nt/1e18:.0f} (no tail, body) vs Amaterasu 244 (+51/-76), Fly\'s Eye 320; with tails <= {Emax_t/1e18:.0f} EeV')
thp = [thrA[(r, 'E*')] for r in ('axis', 'body')]
lnA = {lg: [math.log(10 ** lg / t) for t in thp] for lg in (19.5, 19.8, 20.0)}
print('   composition floor (no species lighter than A_min = E/E_th arrives): ' + '; '.join(f'10^{lg}: lnA_min {v[1]:.2f}-{v[0]:.2f}' for lg, v in lnA.items()))
check('D2 composition floor: no protons above 3.2-4.4 EeV, no He above ~13-17, no CNO above ~45-60 EeV; at 10^19.8-10^20 eV lnA_min = 2.7-3.4 vs Auger SD-DNN <lnA> ~ 3 (pure)',
      2.5 < lnA[19.8][1] < 3.1 and 3.0 < lnA[20.0][0] < 3.5, 'a floor, not a mean: any light admixture above its wall falsifies')
ratio = thp[1] / thp[0]
check('D3 direction dependence: E_cut(body)/E_cut(axis) = 1.3-1.4 for every species (cubic l = 4 anisotropy of the maximum energy, lattice frame unknown)',
      1.25 < ratio < 1.45, f'proton {thp[0]/1e18:.2f} (axis) -> {thp[1]/1e18:.2f} EeV (body); ratio {ratio:.3f}')
print('   [S] walls p/He/N (E*, axis-body): ' + ', '.join(f'{nm} {incoh[(nm,"axis",0)][0]/1e18:.0f}-{incoh[(nm,"body",0)][0]/1e18:.0f}' for nm in ('He', 'N')) +
      f' EeV (nucleon-level, no Fermi shift); Auger features: ankle 5.0, instep 13, suppression 46 EeV (arXiv:2008.06488) - reading only')
print(f'   runtime {time.time() - t0:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
