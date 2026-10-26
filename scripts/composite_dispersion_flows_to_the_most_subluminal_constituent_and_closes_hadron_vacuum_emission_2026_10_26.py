AUDIT_INPUT_PATHS = ('docs/COMPOSITE_DISPERSION_FLOWS_TO_THE_MOST_SUBLUMINAL_CONSTITUENT_AND_CLOSES_HADRON_VACUUM_EMISSION_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Dispersion of a bound state whose constituents obey the rule-fixed dimension-six lattice dispersion.

Upstream (assumed-inputs-model A1/B, [F]): E = p + m^2/2p + c p^3/E*^2 with
  link band c_g = -S/24, light fermion c_q = -S/6 + 1/24, S = sum n_i^4 in [1/3, 1], E* = 1.22e18 GeV.
Question: is a composite's coefficient parton-additive (sum c_i <x_i^3>) or universal (c)?
  A  lattice-frame exact two-body problems (cos band, on-site attraction U, supplied):
     A1 Z^1 closed form; A2 Z^3 exact Lippmann-Schwinger (Laplace/Bessel reduction).
  B  boost-covariant light-front two-body composite (supplied Li-Maris-Vary longitudinal confinement),
     LIV in the mass operator: M^2 = M0^2-operator + lambda(P) sum_i c_i x_i^3, lambda = 2 P^4/E*^2.
     B1 Hellmann-Feynman; B2 large-lambda limit; B3 crossover momentum; B4 p -> p gamma kinematics.
"""
import math
import os
import time

os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq
from scipy.special import ive

AUDIT_TIMEOUT_SEC = 120
np.random.seed(20261026)
T0 = time.time()
NP = NF = 0


def check(name, ok, detail=''):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" | {detail}" if detail else ''))


def quartic_ratio(Ef, h=0.01, n=6):
    """Fit E(p)-E(0) = a p^2 + b p^4 + d p^6 + e p^8 on p = h..n h; return b/a."""
    p = h * np.arange(1, n + 1)
    y = np.array([Ef(pp) for pp in p]) - Ef(0.0)
    A = np.vstack([p ** 2, p ** 4, p ** 6, p ** 8]).T
    co = np.linalg.lstsq(A, y, rcond=None)[0]
    return co[1] / co[0]


# ---------------- A1: Z^1 pair, eps(k) = -2t cos k, on-site -|U| ----------------
print('A  lattice frame: cos band eps = 2t(1 - cos k) per axis; constituent P^4/P^2 ratio = -S/12')
t = 1.0


def E1_closed(P, U):
    return -math.sqrt(U * U + 16 * t * t * math.cos(P / 2) ** 2)


def E1_LS(P, U):
    cP = 4 * t * math.cos(P / 2)
    G = lambda E: quad(lambda q: 1.0 / (-cP * math.cos(q) - E), -math.pi, math.pi, epsabs=1e-14, epsrel=1e-13)[0] / (2 * math.pi)
    return brentq(lambda E: abs(U) * G(E) - 1.0, -cP - abs(U) - 10, -cP - 1e-5, xtol=1e-15)


err = max(abs(E1_LS(P, U) - E1_closed(P, U)) for P in (0.0, 0.7, 2.1) for U in (0.3, 2.0, 9.0))
check('A1a Z^1 pair: Lippmann-Schwinger root = closed form -sqrt(U^2 + 16t^2 cos^2(P/2))', err < 1e-8, f'max err {err:.1e}')
rows = []
okA1 = True
for U in (0.05, 1.0, 4.0, 20.0, 200.0):
    r_num = quartic_ratio(lambda P: E1_closed(P, U), h=0.02)
    r_th = -1 / 12 + t * t / (U * U + 16 * t * t)
    okA1 &= abs(r_num - r_th) < 1e-6
    rows.append(f'U/t={U:g}: {r_num:.5f} ({r_num / (-1 / 12):.3f} x const)')
print('   pair ratio b/a [theory -1/12 + t^2/(U^2+16t^2)]: ' + '; '.join(rows))
check('A1b exact law: pair ratio = -1/12 + t^2/(U^2+16t^2): additive (-1/48 = x^2 const at x=1/2) for |U|<<t, '
      'universal (-1/12) for |U|>>t', okA1, 'interpolation set by binding/bandwidth')

# ---------------- A2: Z^3 pair, exact LS via G = int_0^inf e^{-t delta} prod ive(0, 4 c_i t) dt ----------------


def ive0(z):
    if z < 1e4:
        return float(ive(0, z))
    return (1 + 1 / (8 * z) + 9 / (128 * z * z) + 225 / (3072 * z ** 3)) / math.sqrt(2 * math.pi * z)


def G3(delta, cs):
    f = lambda s: math.exp(s - math.exp(s) * delta) * np.prod([ive0(4 * c * math.exp(s)) for c in cs])
    return quad(f, -30, max(math.log(60.0 / max(delta, 1e-30)), 0) + 3, limit=400, epsabs=1e-15, epsrel=1e-13)[0]


def E3(pvec, U):
    cs = [math.cos(pi / 2) for pi in pvec]
    base = sum(4 - 4 * c for c in cs)
    d = brentq(lambda dl: U * G3(dl, cs) - 1.0, 1e-10, 10 * U, xtol=1e-15, rtol=1e-14)
    return base - d


Uc = 1.0 / G3(0.0, [1.0, 1.0, 1.0])
print(f'   Z^3 critical on-site attraction U_c = {Uc:.4f} (2 x Watson integral^-1)')
dirs = {'axis': (np.array([1, 0, 0.]), 1.0), 'face': (np.array([1, 1, 0.]) / math.sqrt(2), 0.5),
        'body': (np.array([1, 1, 1.]) / math.sqrt(3), 1 / 3)}
okA2 = True
for name, (n, S) in dirs.items():
    out = []
    for fU in (1.5, 3.0, 30.0, 300.0):
        r = quartic_ratio(lambda p: E3(p * n, fU * Uc), h=0.03, n=6)
        out.append(r / (-S / 12))
    okA2 &= all(abs(v - 1) < 0.1 for v in out[1:]) and abs(out[-1] - 1) < 2e-3
    print(f'   {name:4s} (S={S:.3f}): ratio/(-S/12) at U/U_c = 1.5, 3, 30, 300: ' + ', '.join(f'{v:.3f}' for v in out))
check('A2 Z^3 on-site pair: U_c = 7.91 is of order the bandwidth 12, so every Z^3 contact bound state is lattice-sized '
      'and carries the constituent (universal) ratio -S/12 with the cubic S pattern on every ray', okA2,
      'additive limit needs an extended bound state (A1, binding << bandwidth)')

# ---------------- B: light-front boost-covariant composite ----------------
print('B  light-front 2-body: M^2 = m1^2/x + m2^2/(1-x) - kap^4/(m1+m2)^2 d(x(1-x)d) + lam [c1 x^3 + c2 (1-x)^3],'
      ' lam = 2P^4/E*^2')
Es = 1.22e18


def build(N):
    x = 0.5 * (1 - np.cos(np.pi * np.arange(0, N + 2) / (N + 1)))
    h = np.diff(x)
    return x[1:-1], h, 0.5 * (x[1:] + x[:-1]), 0.5 * (h[1:] + h[:-1])


GR = {N: build(N) for N in (1500, 3000)}


def ground(lam, c1, c2, m1=0.3, m2=0.3, kap=0.6, N=3000):
    xi, h, xm, w = GR[N]
    a = (kap ** 4 / (m1 + m2) ** 2) * xm * (1 - xm) / h
    L = c1 * xi ** 3 + c2 * (1 - xi) ** 3
    d = (a[:-1] + a[1:]) / w + m1 * m1 / xi + m2 * m2 / (1 - xi) + lam * L
    val, vec = eigh_tridiagonal(d, -a[1:-1] / np.sqrt(w[:-1] * w[1:]), select='i', select_range=(0, 0))
    p2 = vec[:, 0] ** 2
    return val[0], float(p2 @ L), float(p2 @ xi ** 3)


def cB(P, c1, c2, M0, **kw):
    """Effective composite coefficient (M^2(P) - M0^2)/lam; first order (HF) where lam is tiny."""
    lam = 2 * P ** 4 / Es ** 2
    Ms, L, _ = ground(lam, c1, c2, **kw)
    return L if lam * max(abs(c1), abs(c2)) < 1e-4 else (Ms - M0) / lam


RAYS = (('axis', -1 / 8, -1 / 24), ('sky', -7 / 120, -1 / 40), ('body', -1 / 72, -1 / 72))
# models: qq = two light quarks; q+s0 = quark + LI spectator (rest of the hadron, conservative); q+sg = gluonic spectator
MODELS = {'qq': dict(m1=0.3, m2=0.3, spec=None), 'q+s0': dict(m1=0.3, m2=0.7, spec=0.0), 'q+sg': dict(m1=0.3, m2=0.7, spec='g')}


def coeffs(model, cq, cg):
    sp_ = MODELS[model]['spec']
    return cq, (cq if sp_ is None else (0.0 if sp_ == 0.0 else cg))


for mod in MODELS:
    mm = MODELS[mod]
    M0, _, x3 = ground(0.0, -1, -1, mm['m1'], mm['m2'])
    M0c = ground(0.0, -1, -1, mm['m1'], mm['m2'], N=1500)[0]
    print(f'   {mod:5s}: M0 = {math.sqrt(M0):.4f} GeV (N 1500/3000 rel {abs(M0c / M0 - 1):.0e}), quark <x^3>_0 = {x3:.4f}')
# B1 Hellmann-Feynman
c1, c2 = -1 / 8, -1 / 24
dl = 1e-4
fd = (ground(dl, c1, c2, 0.3, 0.7)[0] - ground(-dl, c1, c2, 0.3, 0.7)[0]) / (2 * dl)
hf = ground(0.0, c1, c2, 0.3, 0.7)[1]
check('B1 Hellmann-Feynman: dM^2/dlam|0 = <c1 x^3 + c2 (1-x)^3>_0, i.e. at first order in the LIV the composite '
      'coefficient is exactly parton-additive with the rest-frame momentum fractions', abs(fd / hf - 1) < 1e-4,
      f'{fd:.7f} vs {hf:.7f}')
# B2 large lam
big = []
for mod in MODELS:
    mm = MODELS[mod]
    a, b = coeffs(mod, -1 / 8, -1 / 24)
    M0 = ground(0.0, a, b, mm['m1'], mm['m2'])[0]
    big.append((ground(1e7, a, b, mm['m1'], mm['m2'])[0] - M0) / 1e7 / a)
check('B2 lam >> M0^2: c_B -> min_i c_i = c_q (momentum flows to the most subluminal constituent) in every model',
      all(abs(v - 1) < 0.02 for v in big), 'c_B/c_q at lam=1e7 GeV^2 (axis): ' + ', '.join(f'{v:.4f}' for v in big))
# B3 interpolation law on the sky-average ray
Pg = np.logspace(6, 12, 61)
ok3 = True
for mod in MODELS:
    mm = MODELS[mod]
    a, b = coeffs(mod, -7 / 120, -1 / 40)
    M0, L0, _ = ground(0.0, a, b, mm['m1'], mm['m2'])
    r = np.array([cB(P, a, b, M0, m1=mm['m1'], m2=mm['m2']) / a for P in Pg])
    ok3 &= bool(np.all(np.diff(r) > -1e-4)) and abs(r[0] - L0 / a) < 1e-3 and abs(r[-1] - 1) < 0.02
    Px = Pg[np.argmin(abs(r - 0.5 * (L0 / a + 1)))]
    print(f'   sky {mod:5s}: c_B/c_q = {r[0]:.3f} (additive, P<1e8 GeV) -> {r[40]:.3f} (1e10) -> {r[-1]:.3f} (1e12);'
          f' half-way at {Px * 1e9:.1e} eV')
check('B3 c_B(P) interpolates monotonically from the additive value (P << P_x) to the most subluminal constituent '
      '(P >> P_x); P_x ~ (M0^2 E*^2/2|c|)^(1/4) is EeV-scale, the same scale as the additive emission threshold', ok3)


def emission(mod, cq, cg, frozen, m1=None, m2=None, kap=0.6):
    mm = MODELS[mod]
    m1 = mm['m1'] if m1 is None else m1
    m2 = mm['m2'] if m2 is None else m2
    a, b = coeffs(mod, cq, cg)
    M0, L0, _ = ground(0.0, a, b, m1, m2, kap)
    lg = np.linspace(5, 12.5, 151)
    cbt = np.array([L0 if frozen else cB(10 ** l, a, b, M0, m1=m1, m2=m2, kap=kap) for l in lg])
    Msq = lambda P: M0 + 2 * P ** 4 / Es ** 2 * np.interp(np.log10(P), lg, cbt)
    y = np.concatenate([np.logspace(-6, -1, 200), np.linspace(0.1, 1 - 1e-6, 900)])
    for P in np.logspace(8, 11, 241):
        k = y * P
        g = Msq(P - k) / (2 * (P - k)) + cg * k ** 3 / Es ** 2 - Msq(P) / (2 * P)
        if g.min() < 0:
            return P * 1e9
    return None


fmt = lambda v: 'closed' if v is None else f'{v:.1e}'
R = {}
for mod in MODELS:
    R[mod] = [(emission(mod, cq, cg, True), emission(mod, cq, cg, False)) for _, cq, cg in RAYS]
    print(f'   p->p gamma opens (eV) {mod:5s} axis/sky/body: frozen-additive ' + '/'.join(fmt(v[0]) for v in R[mod]) +
          '; full eigenstate ' + '/'.join(fmt(v[1]) for v in R[mod]))
check('B4a frozen-additive proton proxies (q+s0, q+sg; low quark <x^3>) open p -> p gamma on every ray below 1e20 eV '
      '(reproduces the parent tension)', all(v[0] is not None for mod in ('q+s0', 'q+sg') for v in R[mod]))
check('B4b full eigenstate: p -> p gamma CLOSED to 1e20 eV on axis and sky-average rays in every model',
      all(R[mod][i][1] is None for mod in MODELS for i in (0, 1)))
sc = []
for m1, m2, kap in ((0.1, 0.5, 0.4), (0.3, 0.9, 0.8), (0.4, 0.6, 0.5), (0.2, 0.7, 0.6)):
    sc.append([emission('q+s0', cq, cg, False, m1, m2, kap) for _, cq, cg in RAYS])
print('   scan q+s0 full, (m1,m2,kap) = (.1,.5,.4) (.3,.9,.8) (.4,.6,.5) (.2,.7,.6): ' +
      '; '.join('/'.join(fmt(v) for v in s) for s in sc))
check('B4c closure on axis + sky rays stable under the supplied-binding scan', all(s[0] is None and s[1] is None for s in sc))
print(f'runtime {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
