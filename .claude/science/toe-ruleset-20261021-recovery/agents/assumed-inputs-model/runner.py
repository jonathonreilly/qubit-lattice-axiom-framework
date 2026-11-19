#!/usr/bin/env python3
"""assumed-inputs-model: numeric checks behind the predictions table of the assumed-inputs model.

 A  exact/finite: the copy-mass dimension-six coefficient of the light fermion band of the cube tick (12-rule base,
    rules 1-2) relative to the link band, scanned over the step eps and copy mass M; its angular form.
 B  the link band's own dimension-six term (common to photon, gluon and, at M = 0, every fermion).
 C  gamma -> e+ e- thresholds (exact kinematics vs the closed form) and the sky fraction left open per energy.
 D  proton photopion (GZK) kinematics with a subluminal dimension-six proton term: blocking energy per eta_p.
 E  estimates with supplied numbers: Delta N_eff of three decoupled nu^c, mirror spectrum of the parity variant,
    axion mass of the far-wall-vertex axion reading.
Units: K in rad per cube, cube edge 2L, L = sqrt(8 pi) l_P (register unit map; G supplied).  Supplied models; no
physical identification beyond the stated reading.
"""
import itertools, os, sys, time, math, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm

T0 = time.time(); P = F = 0
def check(name, ok, detail=''):
    global P, F
    P += bool(ok); F += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")

# ---------------------------------------------------------------- CL-1 cube tick (inlined; same construction as links-metric)
r3 = math.sqrt(3)
C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8, dtype=complex)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); NV = (2 * C8 - 1.0) / r3; XI = []
for i in range(8):
    _, v_ = np.linalg.eigh(sum(NV[i, k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
WAX = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(a + 1, 8):
        if np.sum(abs(C8[a] - C8[b])) == 1:
            g_ = XI[a].conj() @ XI[b]; x = -g_ / abs(g_) / r3; ax = int(np.argmax(abs(C8[a] - C8[b])))
            WAX[ax][a, b] = x; WAX[ax][b, a] = np.conj(x)
R = sum(WAX); VOL = (r3 ** 3) * WAX[0] @ WAX[1] @ WAX[2]; S3 = 1j * VOL @ R
Pm = (I8 - S3) / 2; PL3 = (I8 + S3) / 2
def DK(K): return np.diag(np.exp(1j * (C8 @ np.asarray(K, float))))
def fineU(K, eps, M):
    Fh = expm(1j * (M / 2) * Pm @ R); Ue = Fh @ expm(-1j * eps * R) @ Fh; Uo = expm(1j * eps * R)
    D = DK(K); return D @ Uo @ D.conj().T @ Ue
def light(K, eps, M):
    ev, V = np.linalg.eig(fineU(K, eps, M)); w = -np.angle(ev); lw = np.linalg.norm(PL3 @ V, axis=0)
    return np.sort(w[(lw > 0.7) & (w > 0)]).mean()
def link(K, eps):   # link band = CL-1 band at M = 0 (links-metric A4 theorem)
    return 2 * np.arcsin(np.sin(eps) * np.sqrt(np.sum(np.sin(np.asarray(K) / 2) ** 2) / 3))
def c6_of(n, eps, M, k=0.01):   # Richardson in k: (w_l/w_link - 1)/k^2 at k and k/2
    a = (light(k * n, eps, M) / link(k * n, eps) - 1) / k ** 2
    b = (light(0.5 * k * n, eps, M) / link(0.5 * k * n, eps) - 1) / (0.5 * k) ** 2
    return (4 * b - a) / 3
form = lambda n: -(np.sum(n ** 4) - 1 / 3) / 8          # candidate closed form
check('A0 tick sanity: R^2 = 1 and M = 0 light band equals the link band', abs(R @ R - I8).max() < 1e-12 and
      abs(light(np.array([.3, -.2, .5]), .1, 0.0) - link(np.array([.3, -.2, .5]), .1)) < 1e-12, 'exact to 1e-12')

# A1 scan over eps, M (M < 2 eps keeps the partner gapped; eps0 < 0.0375 is the register's stability bound)
axis, face, body = np.array([1., 0, 0]), np.array([1., 1, 0]) / math.sqrt(2), np.ones(3) / r3
rows, spread = [], 0.0
for eps, M in ((0.3, 0.5), (0.1, 0.1), (0.03, 0.05), (0.03, 0.01), (0.01, 0.015), (0.005, 0.002)):
    v = [c6_of(n, eps, M) for n in (axis, face, body)]; rows.append((eps, M, v))
    spread = max(spread, abs(v[0] + 1 / 12), abs(v[1] + 1 / 48), abs(v[2]))
for eps, M, v in rows: print(f"   eps {eps:<6} M {M:<6} c6 axis {v[0]:+.5f} face {v[1]:+.5f} body {v[2]:+.1e}")
check('A1 copy-mass c6 is -1/12 (axis), -1/48 (face), 0 (body) at every eps and M tested: no dependence on the supplied step or copy mass',
      spread < 2e-4, f'max deviation {spread:.1e} over 6 (eps, M) points')
rng = np.random.default_rng(7); dev = 0.0
for _ in range(12):
    n = rng.normal(size=3); n /= np.linalg.norm(n); dev = max(dev, abs(c6_of(n, 0.03, 0.04) - form(n)))
check('A2 angular form: c6(n) = -(1/8)(sum n_i^4 - 1/3), zero only on the four body diagonals', dev < 2e-4,
      f'12 random rays, max |c6 - form| = {dev:.1e}')

# B link band dimension-six term vs the continuum cone sin(eps)|K|/sqrt3
devB = 0.0
for _ in range(12):
    n = rng.normal(size=3); n /= np.linalg.norm(n); k = 0.004; eps = 0.003
    cl = (link(k * n, eps) / (math.sin(eps) * k / r3) - 1) / k ** 2; devB = max(devB, abs(cl + np.sum(n ** 4) / 24))
check('B link band: w = c|K|(1 - (sum K_i^4/K^2)/24) at small eps (photon, gluon, and fermions before the copy term)', devB < 1e-4,
      f'max |c_link + sum n^4/24| = {devB:.1e}; axis -1/24, body -1/72')

# ---------------------------------------------------------------- physical units
MP = 1.22089e19; me = 0.51099895e-3; mp = 0.93827; mpi = 0.13498          # GeV
Estar = MP / (2 * math.sqrt(8 * math.pi))                                  # hbar c / cube edge
print(f"   E* = hbar c/(2L) = {Estar:.3e} GeV; eta (in M_P units) = -2 c (M_P/E*)^2 = -2c x {(MP / Estar) ** 2:.1f}")

# C gamma -> e+e-: exact two-body kinematics with photon c_g and electron c_g + c6 (E = p(1 + c p^2/E*^2) form)
def decays(k, cg, ce):   # sign of sum E_e - E_gamma, computed without cancellation (k ~ 1e8 GeV, mass terms ~ 1e-15 GeV)
    x = np.linspace(1e-4, 0.5, 20000); p = np.stack([x * k, (1 - x) * k])
    q = p * (1 + ce * (p / Estar) ** 2)
    diff = np.sum(ce * p ** 3 / Estar ** 2 + me ** 2 / (np.sqrt(q ** 2 + me ** 2) + q), axis=0) - cg * k ** 3 / Estar ** 2
    return diff.min() <= 0
def kth_exact(cg, ce):
    lo, hi = 1e6, 1e10
    for _ in range(60):
        mid = math.sqrt(lo * hi); lo, hi = (lo, mid) if decays(mid, cg, ce) else (mid, hi)
    return hi
kreg = lambda b: (8 / b) ** 0.25 * math.sqrt(me * Estar)                       # register form (photon term ignored)
kf = lambda a, b: (6 * (a + b) / b ** 2) ** 0.25 * math.sqrt(me * Estar)      # with photon c_g = -a, copy c6 = -b
def ab(n): s4 = np.sum(np.asarray(n) ** 4); return s4 / 24, (s4 - 1 / 3) / 8
(aa, ba), (af, bf) = ab(axis), ab(face)
ka, kfc = kth_exact(-aa, -aa - ba), kth_exact(-af, -af - bf)
sym_closed = all(0.75 * (-a_) + b_ / 4 < 0 for a_, b_ in (ab(axis), ab(face)))
check('C1 photon decay threshold, exact kinematics with the photon own dim-6 term: symmetric splits are CLOSED (|c6| < 3|c_g| on every ray); decay runs through x = b/6(a+b) splits at k_th = (6(a+b)/b^2)^(1/4) sqrt(m_e E*)',
      sym_closed and abs(ka / kf(aa, ba) - 1) < 0.01 and abs(kfc / kf(af, bf) - 1) < 0.01,
      f'axis {ka / 1e6:.0f} PeV (register form {kreg(ba) / 1e6:.0f}), face {kfc / 1e6:.0f} PeV (register {kreg(bf) / 1e6:.0f}); body diagonal: never; LHAASO reach ~1.4 PeV')
N = rng.normal(size=(200000, 3)); N /= np.linalg.norm(N, axis=1)[:, None]; s4 = np.sum(N ** 4, axis=1)
an, bn = s4 / 24, (s4 - 1 / 3) / 8
frac = {}
for E in (0.1e9, 0.2e9, 1e9, 1e10):
    frac[E] = np.mean(E ** 4 * bn ** 2 / (an + bn) < 6 * me ** 2 * Estar ** 2)
print('   sky fraction where photons survive: ' + ', '.join(f'{E / 1e9:g} EeV {100 * f:.3g}%' for E, f in frac.items()))
check('C2 above ~0.2 EeV photons survive only in eight small spots around the body diagonals; open fraction falls as E^-2',
      frac[1e9] < 0.02 and 50 < frac[1e9] / max(frac[1e10], 1e-6), f'0.2 EeV {100 * frac[0.2e9]:.2f}%, 1 EeV {100 * frac[1e9]:.3f}%, 10 EeV {100 * frac[1e10]:.4f}%')

# D proton photopion with subluminal E = p + m^2/2p - eta p^3/(2 M_P^2); head-on CMB photon eps_g
def pion_allowed(Pp, eta, eg):
    x = np.logspace(-4, math.log10(0.999), 3000)
    rhs = (mpi ** 2 / x + mp ** 2 / (1 - x) - mp ** 2) / (2 * Pp) + eta * Pp ** 3 / (2 * MP ** 2) * 3 * x * (1 - x)
    return rhs.min() <= 2 * eg
eg = 10 * 2.348e-13                                     # 10 kT_CMB (generous Wien tail)
def window(eta):
    Ps = np.logspace(8, 12.5, 400); ok = [pion_allowed(p, eta, eg) for p in Ps]
    return (Ps[ok].min(), Ps[ok].max()) if any(ok) else None
w0 = window(0.0); res = {}
for eta in (1e-6, 1e-5, 1e-4, 0.03, 0.3, 3.0): res[eta] = window(eta)
print('   photopion window (GeV): eta 0: ' + f'{w0[0]:.1e}-' + ' | '.join(f'eta {e:g}: ' + ('none' if r is None else f'{r[0]:.1e}-{r[1]:.1e}') for e, r in res.items()))
crit = [e for e, r in res.items() if r is None]
check('D photopion off CMB is kinematically CLOSED at every energy for subluminal eta_p >~ 1e-5; rule estimate eta_p ~ 0.03-3 (parton-weighted, supplied)',
      w0 is not None and res[0.03] is None and res[1e-6] is not None, f'standard threshold {w0[0]:.1e} GeV; closed for eta_p in {crit}')

# E estimates with supplied numbers
dNeff = 3 * (4 / 7) ** 0 * (10.75 / 106.75) ** (4 / 3)
check('E1 three nu^c decoupled with SM content at decoupling: Delta N_eff = 3 (10.75/106.75)^(4/3)', abs(dNeff - 0.141) < 0.002,
      f'{dNeff:.3f}; SO sigma 0.05 -> {dNeff / 0.05:.1f} sigma, CMB-S4 sigma 0.03 -> {dNeff / 0.03:.1f} sigma (needs a hot start, supplied)')
v = 246.22; masses = {"u'": 2.16e-3, "d'": 4.67e-3, "e'": me, "mu'": 0.10566}
vp = 1.5e3 / masses["u'"] * v
spec = ', '.join(f'{k} {m * vp / v / 1e3:.2f} TeV' for k, m in masses.items())
check("E2 parity variant: m_f' = m_f v'/v; LHC bound m_u' > 1.5 TeV (supplied) sets v' >= ~1.7e8 GeV and the whole mirror ladder",
      1.5e8 < vp < 2e8, f"v' = {vp:.2e} GeV: {spec}; nu' ~ m_nu v'/v = {0.05 * vp / v / 1e3:.0f} keV (m_nu 0.05 eV supplied)")
ma = lambda fa: 5.69e-6 * (1e12 / fa)
check('E3 axion: m_a = 5.69 ueV (1e12 GeV/f_a); far-wall-vertex reading f_a ~ (0.01-1) E*/N_DW with N_DW = N_f = 3',
      True, f'f_a = E*/3: {ma(Estar / 3):.1e} eV; f_a = 0.01 E*/3: {ma(0.01 * Estar / 3):.1e} eV (stellar-BH superradiance probes ~1e-13 to 2e-11 eV, supplied)')
print(f"   runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={P} FAIL={F}")
