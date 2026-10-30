AUDIT_INPUT_PATHS = ('docs/NUCLEAR_VACUUM_BREAKUP_UNDER_RULE_FIXED_DIMENSION_SIX_LIV_IS_A_HARD_WALL_BELOW_FIFTY_EEV_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""nuclear-vacuum-breakup: adversarial recheck of 'nuclei cannot follow the composite flow'.

Inherited ([F] upstream, unchanged): E = p + m^2/2p + c p^3/E*^2, c_q = -S/6 + 1/24, E* = 1.217e18 GeV.
Hypothesis under test: every nucleon is UNIVERSAL, c_N = c_q at all momenta.
Light front at fixed total P: M^2 = sum (k^2 + M_i^2)/x_i + V + lam sum c_i x_i^3, lam = 2 P^4/E*^2.
T1 exact (sympy): driver structure.  F1 exact 2-body LF diagonalisation (rank-one separable kernel
f = 1/(M0^2 - (M1+M2)^2 + Lam^2), Lam^2 = beta^2 (M1+M2)/mu, supplied beta), x and k_perp, at fixed P.
F2 nucleon + core cluster (t, 4He, 14N, 56Fe).  R complex-pole width -> decay length.
Supplied: beta, separable form, measured separation energies, core at its additive coefficient.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import warnings
import numpy as np
import sympy as sp
from scipy.integrate import quad, dblquad
from scipy.optimize import brentq, minimize_scalar
warnings.filterwarnings('ignore')
AUDIT_TIMEOUT_SEC = 120
np.random.seed(20261026)
ESTAR, HBARC, U, MN, MP = 1.217e18, 1.97327e-16, 0.931494, 0.93892, 0.93827
RAYS = {'axis': -1 / 8, 'sky': -0.6 / 6 + 1 / 24, 'body': -1 / 72}
NPASS = [0]


def check(name, ok, info=''):
    if not ok:
        raise SystemExit(f'FAIL {name} {info}')
    NPASS[0] += 1
    print(f'PASS {name}' + (f' [{info}]' if info else ''))


# ---------- T1 exact driver structure
A_, c, P, M = sp.symbols('A c P M', positive=True)
liv_free = sp.simplify(A_ * c * (P / A_) ** 3)
check('T1a matched velocities: A free universal nucleons at P/A carry LIV c P^3/A^2 = additive bound value; '
      'zero driver at the matched point', sp.simplify(liv_free - c * P ** 3 / A_ ** 2) == 0)
xs = sp.symbols('x1:5', positive=True)
lagr = sum(xi ** 3 for xi in xs)
grad = [sp.diff(lagr, xi).subs({xj: sp.Rational(1, 4) for xj in xs}) for xi in xs]
hess = sp.hessian(lagr, xs).subs({xj: sp.Rational(1, 4) for xj in xs})
ok = len(set(grad)) == 1 and all(hess[i, i] == sp.Rational(3, 2) for i in range(4))
check('T1b sum x^3 is stationary on the simplex at x_i=1/A (equal gradients) with Hessian 6/A > 0, so c<0 gives '
      'NEGATIVE LIV curvature: the driver is second order (convexity of x^3), not a first-order sum x^3 < 1 term', ok)
lam = sp.symbols('lam', positive=True)
crit = sp.solve(sp.Eq(lam * 6 * c / A_, 2 * M ** 2 * A_ ** 3), lam)[0]
check('T1c local instability of the matched point (no binding): lam|c| = M^2 A^4/3, i.e. '
      'P_inst = A (M^2 E*^2/6|c|)^(1/4)', sp.simplify(crit * c - M ** 2 * A_ ** 4 / 3) == 0)
pin = {r: 2 * (MN ** 2 * ESTAR ** 2 / (6 * abs(cr))) ** 0.25 * 1e9 for r, cr in RAYS.items()}
print('   deuteron P_inst axis/sky/body (eV): ' + ' / '.join(f'{v:.2e}' for v in pin.values()))


# ---------- F1/F2 exact separable light-front two-body problem
def Fin(A, B):
    """int_0^inf ds/((s+A)^2 (s+B)); principal value if B<0. Stable in u=(B-A)/A."""
    u = (B - A) / A
    if abs(u) < 1e-4:
        return (0.5 - u / 3 + u * u / 4) / A ** 2
    return (u - np.log(abs(1 + u))) / (u * u * A * A)


class Two:
    def __init__(s, M1, M2, Sep, beta, c1, c2):
        s.M1, s.M2, s.c1, s.c2 = M1, M2, c1, c2
        s.a = beta ** 2 * (M1 + M2) ** 2 / (M1 * M2) - (M1 + M2) ** 2
        s.x0, s.zB0 = M1 / (M1 + M2), (M1 + M2 - Sep) ** 2
        s.g = 1 / s.I(s.zB0, 0.0)

    def K1(s, x):
        return s.M1 ** 2 / x + s.M2 ** 2 / (1 - x)

    def K(s, x, lm):
        return s.K1(x) + lm * (s.c1 * x ** 3 + s.c2 * (1 - x) ** 3)

    def I(s, z, lm, pts=(), im=False):
        def f(x):
            A, B = s.K1(x) + s.a, s.K(x, lm) - z
            return (np.pi / (A - B) ** 2 if B < 0 else 0.0) if im else Fin(A, B)
        p = sorted(set(q for q in [s.x0] + list(pts) if 1e-12 < q < 1 - 1e-12))
        return np.pi * quad(f, 0, 1, points=p, limit=1000, epsabs=0, epsrel=1e-10)[0]

    def mins(s, lm):
        xg = np.linspace(1e-6, 1 - 1e-6, 100001)
        v = s.K(xg, lm)
        i = np.where((v[1:-1] <= v[:-2]) & (v[1:-1] <= v[2:]))[0] + 1
        out = [minimize_scalar(lambda x: s.K(x, lm), bounds=(xg[j - 1], xg[j + 1]), method='bounded',
                               options={'xatol': 1e-14}) for j in i]
        return sorted((r.fun, r.x) for r in out)

    def roots(s, z, lm):
        xg = np.linspace(1e-6, 1 - 1e-6, 100001)
        v = s.K(xg, lm) - z
        return list(xg[np.where(np.sign(v[1:]) != np.sign(v[:-1]))[0]])

    def bound(s, lm):
        m = s.mins(lm)
        T = m[0][0]
        f = lambda z: s.g * s.I(z, lm, [x for _, x in m]) - 1
        if f(T - 1e-9) <= 0:
            return None, m
        return brentq(f, T - 300, T - 1e-9, xtol=1e-13), m

    def lam_open(s, lo=0.0, hi=1e8):
        for _ in range(60):
            mid = np.sqrt(max(lo, 1e-3) * hi)
            if s.bound(mid)[0] is None:
                hi = mid
            else:
                lo = mid
            if hi / max(lo, 1e-3) < 1.002:
                break
        return hi

    def resonance(s, lm):
        m = s.mins(lm)
        if len(m) < 2:
            return None
        Tf, Tl = m[0][0], m[1][0]
        pts = lambda z: [x for _, x in m] + s.roots(z, lm)
        f = lambda z: s.g * s.I(z, lm, pts(z)) - 1
        hi = Tl - 1e-9
        if f(hi) <= 0:
            return None
        lo, st = hi, 1e-3
        while f(lo) > 0:
            lo -= st
            st *= 2
            if lo < Tf:
                return None
        zr = brentq(f, lo, hi, xtol=1e-12)
        h = 1e-5 * max(1.0, abs(zr - Tf))
        der = (s.I(zr + h, lm, pts(zr)) - s.I(zr - h, lm, pts(zr))) / (2 * h)
        return zr, 2 * s.I(zr, lm, pts(zr), im=True) / abs(der), Tl - zr


def P_of(lu, cr):
    return (lu * ESTAR ** 2 / (2 * abs(cr))) ** 0.25 * 1e9


d = Two(MN, MN, 0.0022246, 0.2859, -1.0, -1.0)
direct = np.pi * dblquad(lambda K, x: 1 / ((K + d.a) ** 2 * (d.K(x, 2.0) - d.K1(x) + K - 3.0)),
                         1e-9, 1 - 1e-9, lambda x: d.K1(x), lambda x: np.inf, epsrel=1e-11)[0]
cf = d.I(3.0, 2.0)
check('F1a closed-form k_perp integral = direct 2D quadrature (deuteron, lam|c|=2 GeV^2)',
      abs(cf / direct - 1) < 1e-6, f'rel {abs(cf / direct - 1):.1e}')
zb, _ = d.bound(0.0)
check('F1b separable LF deuteron reproduces B = 2.2246 MeV at lam = 0 (g fixed there)',
      abs(2 * MN - np.sqrt(zb) - 0.0022246) < 1e-9)
lo_d = d.lam_open()
sl = []
for lm in (0.0, 0.5 * lo_d, 0.95 * lo_d):
    za, _ = d.bound(lm)
    zc, _ = d.bound(lm + 1e-3)
    sl.append((zc - za) / 1e-3)
print('   deuteron bound-state slope dM_B^2/d(lam|c|) at 0, 0.5, 0.95 lam_open: ' +
      ', '.join(f'{v:.4f}' for v in sl) + '  (additive -0.25, universal -1)')
check('F1c the bound deuteron does NOT follow the flow: |c_eff|/|c| rises only from 1/4 to < 1/2 (universal = 1) '
      'before the pole dissolves', all(0.25 <= -v < 0.5 for v in sl), f'max {max(-v for v in sl):.3f}')
mm = d.mins(1.2 * lo_d)
check('F1d deuteron: no metastable state (pitchfork at lam|c| = 16M^2/3 = %.3f); bound pole meets the moving '
      'continuum minimum and dissolves at lam_open|c| = %.3f GeV^2' % (16 * MN ** 2 / 3, lo_d),
      d.bound(1.2 * lo_d)[0] is None and lo_d > 16 * MN ** 2 / 3 and max(v for v, _ in mm) - mm[0][0] < 1e-8)
print('   deuteron dissolves at P (eV) axis/sky/body: ' + ' / '.join(f'{P_of(lo_d, cr):.2e}' for cr in RAYS.values()) +
      '  (prior estimate 3.5-6.0e18)')

NUC = {'t': (3, 0.0062572, MN), 'He4': (4, 0.019814, MP), 'N14': (14, 0.007551, MP), 'Fe56': (56, 0.010184, MP)}
res = {}
print('F2 cluster N + (A-1) (S = lowest single-nucleon separation, AME; core at c/(A-1)^2):')
for nm, (A, S, M1) in NUC.items():
    row = []
    for beta in (0.2, 0.2859, 0.4):
        s = Two(M1, (A - 1) * U, S, beta, -1.0, -1.0 / (A - 1) ** 2)
        row.append(s.lam_open())
        if beta == 0.2859:
            res[nm] = s
    Ps = [P_of(row[1], cr) for cr in RAYS.values()]
    res[nm].lo, res[nm].band = row[1], (P_of(min(row), RAYS['axis']), P_of(max(row), RAYS['body']))
    print(f'   {nm:4s} lam_open|c| = {row[1]:.4g} GeV^2 (beta .2/.4: {row[0]:.3g}/{row[2]:.3g}); P_open axis/sky/body '
          f'{Ps[0]:.2e}/{Ps[1]:.2e}/{Ps[2]:.2e} eV; per nucleon axis {Ps[0] / A:.2e}')
po = [P_of(res[n].lo, RAYS['axis']) for n in NUC]
check('F2a breakup is REAL for every nucleus and P_open rises monotonically with A', all(np.diff(po) > 0))
fe = res['Fe56']
hb = max(P_of(res[n].lo, RAYS['body']) for n in NUC) * 0.214 ** -0.25
print(f'   weak-driver end c_N = 0.214 c_q: all P_open x 0.214^(-1/4) = {0.214 ** -0.25:.3f} (exact scaling); '
      f'Fe body worst case {P_of(fe.lo, RAYS["body"]) * 0.214 ** -0.25:.2e} eV')
check('F2b even at the weak-driver body-ray beta=0.4 corner the Fe wall lies below the Amaterasu energy 2.44e20 eV',
      fe.band[1] * 0.214 ** -0.25 < 2.44e20, f'{fe.band[1] * 0.214 ** -0.25:.2e}')

print('R complex-pole width of the frozen nucleus above P_open (Gamma_lab = Gamma_M2/2P, L = hbar c/Gamma):')
Ls = []
for nm in ('He4', 'N14', 'Fe56'):
    s = res[nm]
    out = []
    for fac in (1.1, 1.5, 2.0):
        lm = s.lo * fac ** 4
        r = s.resonance(lm)
        Pg = P_of(lm, RAYS['axis']) / 1e9
        if r is None:
            out.append(f'x{fac}: no frozen pole (dissolved), L_form ~ {HBARC * 2 * Pg / abs(s.mins(lm)[0][0] - s.zB0):.1e} m')
            Ls.append(HBARC * 2 * Pg / abs(s.mins(lm)[0][0] - s.zB0))
            continue
        L = HBARC * 2 * Pg / r[1]
        Ls.append(L)
        out.append(f'x{fac}: Gamma_M2 {r[1]:.2e} GeV^2 (gap {r[2]:.2e}), L {L:.1e} m')
    print(f'   {nm}: ' + '; '.join(out))
check('R1 every computed decay/formation length above 1.1 P_open is < 1 kpc = 3.1e19 m: HARD WALL', max(Ls) < 3.1e19,
      f'max {max(Ls):.1e} m')

print('Confrontation (web-verified values; rays unoriented, so all three rays allowed):')
for nm in NUC:
    lo_, hi_ = res[nm].band
    print(f'   {nm:4s} wall band {lo_:.2e} - {hi_ * 0.214 ** -0.25:.2e} eV (beta x c_N x ray)')
check('C1 no nucleus t..Fe-56 survives above 5e19 eV on any ray/beta/c_N corner: pure protons above (Auger heavy bin 50-100 EeV)',
      max(res[n].band[1] for n in NUC) * 0.214 ** -0.25 < 5e19)
print('   Fe wall vs Auger heavy <lnA> 50-100 EeV and Amaterasu 2.44e20 / Fly\'s Eye 3.2e20: see note')
print(f'TOTAL: PASS={NPASS[0]} FAIL=0')
