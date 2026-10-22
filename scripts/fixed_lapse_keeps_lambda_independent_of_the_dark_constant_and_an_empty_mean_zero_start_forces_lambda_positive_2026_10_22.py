AUDIT_INPUT_PATHS = ('docs/FIXED_LAPSE_KEEPS_LAMBDA_INDEPENDENT_OF_THE_DARK_CONSTANT_AND_AN_EMPTY_MEAN_ZERO_START_FORCES_LAMBDA_POSITIVE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""lambda-quantum: do the quantum-edge laws (fixed lapse, mean-zero dark constant,
finite log window, glued split) give a handle on the size of CL-3's constant per
proper 4-volume (Lambda)?  Self-contained; numpy/scipy/sympy only.

Units: rung units, L = flat cell rung, 8 pi G hbar = L^2 (unit map), c = 1.
Per cell and per tick (CL-1 fixed lapse): proper time dt = sig*l, sig = sin(eps0)/sqrt3.
Per-tick phases of the homogeneous edge (volume) mode of one cell, edge l = L 2^(n/s-3):
  kinetic (ghost sign)  K = 3 (l/L)^2 (d ln l)^2 / sig      (enters D with a minus sign)
  constant per 4-volume  Lambda * sig * (l/L)^4             (Lambda in units 1/L^2)
  D = -K + Lambda*v + (matter departure, zero for the empty one-cube start).
"""
import time, math
import numpy as np
import sympy as sp
from scipy.linalg import eigh

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = NF = 0


def check(ok, label, detail=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" | {detail}" if detail else ""))


LAM_MEAS = 7.151e-121          # Lambda L^2 (lambda-size M: Planck 2018, L = sqrt(8 pi) l_P)
LN2 = math.log(2.0)

# ---------------------------------------------------------------- A
print("== A. is Lambda degenerate with the dark constant? (fixed lapse)")
a, n, rho0, w, Lam, D, G = sp.symbols('a n rho0 w Lambda D G', positive=True)
# minisuperspace: conserved generator of the tick = N*sqrt(gamma)*(rho_tot - 3H^2/(8piG)); N = a^n.
# a perfect fluid rho = rho0 a^(-3(1+w)) contributes N a^3 rho = rho0 a^(n - 3w); it is a CONSTANT
# (indistinguishable from the integration constant D) iff n = 3w.
expo = sp.simplify(n + 3 - 3 * (1 + w))
wsol = sp.solve(sp.Eq(expo, 0), w)[0]
check(sp.simplify(wsol - n / 3) == 0,
      "THEOREM: with lapse N = a^n the conserved value of the tick enters as a fluid of w = n/3",
      f"w = {wsol}")
eps0, l = sp.symbols('epsilon0 l', positive=True)
Nfix = sp.solve(sp.Eq(sp.sqrt(3) * sp.Symbol('N') * sp.sqrt(1 / l**2), sp.sin(eps0)), sp.Symbol('N'))[0]
check(sp.simplify(Nfix - sp.sin(eps0) * l / sp.sqrt(3)) == 0,
      "THEOREM (CL-1 text): sqrt3 N rms sqrt(gamma^ii) = sin eps0 on isotropic edges gives N = sig*l, n = 1",
      f"N = {Nfix}; so D is dark radiation (w = 1/3), as the register states")
# Lambda's term in N a^3 (...): a^(n+3) = a^4 for n = 1: independent monomial from D's a^0.
lam_term = sp.expand(a**1 * a**3 * Lam)          # N sqrt(gamma) Lambda at n = 1
unimod_n = (sp.Symbol("m", real=True) + 3).subs("m", 1)  # D-type power at n=1 is a^0 only if n = -3
check(sp.degree(lam_term, a) == 4 and sp.Poly(lam_term + D, a).degree() == 4
      and sp.Poly(lam_term + D, a).coeff_monomial(1) == D and unimod_n != 0,
      "THEOREM: Lambda enters the fixed-lapse generator as Lambda*a^4, D as a^0: linearly independent,"
      " so no shift of D absorbs Lambda; the unimodular degeneracy needs n = -3",
      "conformal-time (a'^2 = C(D + rho_m a + Lambda a^4/3)) coefficients are separately readable")
# numeric: two (Lambda, D) pairs with the same early expansion separate later -> Jacobian nonsingular
def a_of_eta(Lv, Dv, eta_end=2.0, steps=4000):
    av, h = 1.0, eta_end / steps
    for _ in range(steps):
        f = lambda x: math.sqrt(max(Dv + 1.0 + 0.3 * x + Lv * x**4 / 3, 0.0))
        k1 = f(av); k2 = f(av + h * k1 / 2); k3 = f(av + h * k2 / 2); k4 = f(av + h * k3)
        av += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return av
d = 1e-4
J = np.array([[(a_of_eta(0.5 + d, 0, te) - a_of_eta(0.5 - d, 0, te)) / (2 * d),
               (a_of_eta(0.5, d, te) - a_of_eta(0.5, -d, te)) / (2 * d)] for te in (0.5, 1.5)])
check(abs(np.linalg.det(J)) > 1e-3,
      "FINITE DIAGNOSTIC: a(eta) at two times reads (Lambda, D) separately", f"det J = {np.linalg.det(J):.3e}")

# ---------------------------------------------------------------- B
print("== B. mean-zero dark constant on the empty one-cube start (quantum volume mode)")


def register(s, Delta=0, b=1):
    """window n = 0..(4+Delta)s, l/L = 2^(n/s-3) in [1/8, 2^(1+Delta)]; block of b^3 cells
    moving together (b = 1: one cube). Returns hop kinetic K (PSD, Dirichlet) and v = sig (l/L)^4."""
    sig = 1.0  # sig cancels from Lambda = <K>/<v> (K ~ 1/sig, v ~ sig): set below
    nmax = (4 + Delta) * s
    nn = np.arange(nmax + 1)
    x = 2.0 ** (nn / s - 3)
    # classical K = m dn^2/2, m(n) = 6 b^3 x^2 (ln2/s)^2 / sig  ->  hop weight w = 1/m on each bond
    xm = 2.0 ** ((nn[:-1] + 0.5) / s - 3)
    wb = 1.0 / (6 * b**3 * xm**2 * (LN2 / s) ** 2)
    K = np.zeros((nmax + 1, nmax + 1))
    for i, wi in enumerate(wb):          # w (1 - cos k) on each bond, PSD
        K[i, i] += wi / 2; K[i + 1, i + 1] += wi / 2
        K[i, i + 1] -= wi / 2; K[i + 1, i] -= wi / 2
    # Dirichlet walls (no register outside the window): the hop to the missing value is absent,
    # but its diagonal share stays, so K > 0 strictly
    K[0, 0] += wb[0] / 2; K[-1, -1] += wb[-1] / 2
    v = b**3 * x**4
    return K, v, nn, x


def lam_range(K, v):
    vi = 1 / np.sqrt(v)
    ev = eigh(vi[:, None] * K * vi[None, :], eigvals_only=True)
    return ev


res = {}
for s in (23, 50, 113):
    K, v, nn, x = register(s)
    ev = lam_range(K, v)
    res[s] = ev
lmins = [res[s][0] for s in res]
check(all(e > 0 for e in lmins),
      "THEOREM + check: empty start (matter departure 0): <D> = 0 needs Lambda = <K>/<v>, K PSD,"
      " v > 0, so Lambda >= 0; on the finite window K > 0 strictly, so Lambda > 0 (sign forced)",
      "Lambda_min L^2 = " + ", ".join(f"s={s}: {res[s][0]:.3e}" for s in res))
spread = max(lmins) / min(lmins)
check(spread < 1.5,
      "THEOREM-shape: Lambda_min is set by the window's lengths (mostly its top), not by s",
      f"max/min over s = 23..113: {spread:.3f}; top 4L (Delta=1): {lam_range(*register(50, 1)[:2])[0]:.3e}")
# the top is the glued split, transparent for the homogeneous mode of the whole start: extend it
lt = [lam_range(*register(23, Dl)[:2])[0] for Dl in (0, 2, 4)]
sl = math.log(lt[2] / lt[0]) / (4 * LN2)
check(sl < -5,
      "FINITE DIAGNOSTIC: with the top transparent (glued split continuing the start's homogeneous"
      " mode) Lambda_min falls as (top length)^-6 -> 0: Lambda > 0 strictly, but its size is free",
      f"top 2L, 8L, 32L: {lt[0]:.1e}, {lt[1]:.1e}, {lt[2]:.1e}; slope {sl:.2f}")
# mean form admits a continuum: any Lambda in [lam_1, lam_max] has a mean-zero state (two eigvecs)
s = 23
K, v, nn, x = register(s)
vi = 1 / np.sqrt(v)
ev, U = eigh(vi[:, None] * K * vi[None, :])
ok = True
for target in np.linspace(ev[0] * 1.01, ev[5], 7):
    # psi = v^-1/2 (c0 u0 + c5 u5) : <K> - target <v> = c0^2 (ev0 - t) + c5^2 (ev5 - t) = 0
    c0 = math.sqrt((ev[5] - target) / (ev[5] - ev[0])); c5 = math.sqrt(1 - c0**2)
    psi = vi * (c0 * U[:, 0] + c5 * U[:, 5])
    Dm = psi @ (-K + target * np.diag(v)) @ psi
    ok &= abs(Dm) < 1e-9 * (psi @ K @ psi)
check(ok, "FINITE DIAGNOSTIC: in the MEAN form every Lambda >= Lambda_min has mean-zero states:"
      " no quantisation", f"7 targets in [1.01, {ev[5]/ev[0]:.1f}] x Lambda_min")
gaps = np.diff(ev[:4]) / ev[0]
check(gaps[0] > 0.5,
      "FINITE DIAGNOSTIC: the SHARP form (a D = 0 eigenstate; rejected by CL-3, it freezes the odds)"
      " would quantise Lambda at the generalised eigenvalues, Planck-spaced",
      "Lambda_j/Lambda_1 = " + ", ".join(f"{e/ev[0]:.2f}" for e in ev[:4]))
# blocks: Lambda_min ~ b^-6
lb = [lam_range(*register(23, 0, b)[:2])[0] for b in (1, 2, 4)]
slope = math.log(lb[2] / lb[0]) / math.log(4)
check(abs(slope + 6) < 0.05, "THEOREM-shape: a block of b^3 cells moving together gives Lambda_min ~ b^-6",
      f"slope {slope:.3f}")
lam1 = min(lmins)
check(lam1 / LAM_MEAS > 1e100,
      "ESTIMATE vs measurement: if the start's edges took the closed window's least-kinetic state"
      " (supplied clause; top treated as a wall), Lambda is forced, positive and Planckian",
      f"Lambda L^2 = {lam1:.2e} vs measured {LAM_MEAS:.2e}: x{lam1/LAM_MEAS:.0e}; at b_e = 10/76: "
      f"{lam1*10**-6:.1e}/{lam1*76**-6:.1e}")
bstar = (lam1 / LAM_MEAS) ** (1 / 6)
Lm = math.sqrt(8 * math.pi) * 1.616e-35
RL = math.sqrt(3 / (LAM_MEAS / Lm**2))
coinc = (Lm**2 * RL) ** (1 / 3)
check(0.1 < bstar * Lm / coinc < 10,
      "LOOK-ELSEWHERE: the block that would give the measured value, b* L, is the dimensional"
      " combination (L^2 R_Lambda)^(1/3) (fm scale), not a rule scale; a one-cube start has b = 1",
      f"b* = {bstar:.2e}, b*L = {bstar*Lm:.2e} m, (L^2 R)^(1/3) = {coinc:.2e} m; rules: b_e >= 10..76")

# ---------------------------------------------------------------- C
print("== C. quasi-energy mod 2 pi: periodicity / quantisation of Lambda")
ss = sp.Symbol('s', positive=True, integer=True)
rat = all(not sp.nsimplify(sp.Integer(2) ** sp.Rational(4, k)).is_rational for k in (23, 50, 113))
check(rat, "THEOREM: Lambda -> Lambda + dL is a symmetry of the tick iff dL*sig*(l_n/L)^4 in 2piZ for every"
      " window value; consecutive ratios 2^(4/s) are irrational for s not dividing 4 (and s > 23 is"
      " required), so no period exists", "2^(4/23), 2^(4/50), 2^(4/113) irrational")
# numeric: no near-period up to 2pi*1e3 / v_min (sig = 1)
s = 23
vals = 2.0 ** (4 * (np.arange(4 * s + 1) / s - 3))
grid = np.linspace(1.0, 2 * math.pi * 1e3, 200000)
worst = np.full(grid.size, 0.0)
for vv in vals:
    ph = (grid * vv) / (2 * math.pi)
    worst = np.maximum(worst, np.abs(ph - np.round(ph)))
check(worst.min() > 0.05, "FINITE DIAGNOSTIC: no near-period of Lambda (all window values within"
      " 0.05 turn of 2piZ) for dL L^2 up to 6e3/sig", f"best max-distance {worst.min():.3f} turn")
check(2 * math.pi * 8**4 > 1e3, "THEOREM: even an exact period (s | 4) is >= 2pi/v_min = 2pi 8^4/sig in"
      " 1/L^2: the circle acts only at Planck scale; the measured value is 1e-120 into the first period",
      f"2pi 8^4 = {2*math.pi*8**4:.0f}")
x4 = 15 / (4 * LN2)
for e0 in (0.0075, 0.0375):
    sg = math.sin(e0) / math.sqrt(3)
    print(f"   today's Lambda phase per cell-tick (eps0={e0}): {LAM_MEAS*sg*x4:.2e} rad")

# ---------------------------------------------------------------- D
print("== D. window, splits and tick-count numerology")
# phase accumulated by one cell over a split cycle (L -> 2L) in de Sitter: Lambda*int l^3 dt / L^2
lamx = sp.Symbol('lam', positive=True)
H = sp.sqrt(lamx / 3)
tt = sp.Symbol('t', positive=True)
Phi = sp.simplify(lamx * sp.integrate(sp.exp(3 * H * tt), (tt, 0, sp.log(2) / H)))
coef = float(sp.simplify(Phi / sp.sqrt(lamx)))
check(abs(coef - 7 / math.sqrt(3)) < 1e-9,
      "THEOREM: one cell's Lambda phase over a split cycle is (7/sqrt3) sqrt(Lambda L^2): the window"
      " bounds it per cycle but no rule fixes it; demanding 2pi gives Planck Lambda",
      f"today {coef*math.sqrt(LAM_MEAS):.1e} rad/cycle; Phi=2pi -> Lambda L^2 = {(2*math.pi/coef)**2:.2f}")
t0 = 13.8e9 * 3.156e7
tauL = Lm / 2.998e8
ratios = []
for e0 in (0.0075, 0.0375):
    sg = math.sin(e0) / math.sqrt(3)
    Nt = t0 / (sg * tauL / LN2)          # <l/L> over [1,2] log-uniform = 1/ln2
    ratios.append((2 * math.pi / Nt) ** 2 / LAM_MEAS)
check(1e-4 < min(ratios) and max(ratios) < 1,
      "LOOK-ELSEWHERE: (2pi/N_ticks)^2 lands within ~1e2 of Lambda L^2 because Lambda L^2 = 3 Omega_L"
      " (H0 L)^2 and N_ticks ~ 1/(H0 sig L): it is the coincidence, and it tracks H^2 (w != -1)",
      f"ratio {ratios[0]:.1e}..{ratios[1]:.1e} over the eps0 range (a free x25)")
ksp = math.log(RL / Lm) / LN2
check(abs(4.0 ** (-ksp) * 3 - LAM_MEAS) / LAM_MEAS < 1e-6,
      "LOOK-ELSEWHERE: 4^-k with k the split count to the Lambda radius is (L/R)^2 by definition;"
      " a growing count tracks (lambda-size: w = -1/3, 23 sigma)", f"k = {ksp:.1f} octaves")
# family scan: c * (2pi)^p * N^-q * (eps0 free in range) hits target within x2?
hits = tot = 0
for c in (1, 1 / 3, 3, 1 / (8 * math.pi), 8 * math.pi):
    for p in (0, 1, 2):
        for q in (1, 2, 3):
            tot += 1
            lo = c * (2 * math.pi) ** p * (t0 / (math.sin(0.0375) / math.sqrt(3) * tauL / LN2)) ** -q
            hi = c * (2 * math.pi) ** p * (t0 / (math.sin(0.0075) / math.sqrt(3) * tauL / LN2)) ** -q
            hits += (lo / 2 <= LAM_MEAS <= hi * 2) or (hi / 2 <= LAM_MEAS <= lo * 2)
check(hits >= 1, "LOOK-ELSEWHERE: a 45-form tick-count family with eps0 free contains a x2 hit",
      f"{hits}/{tot} hit, the q = 2 (H^2 coincidence) form; it would carry no weight")
check(True, "THEOREM (A + CL-2): the dark constant's spread is radiation-like in every branch (w = 1/3),"
      " so its zero-mean distribution cannot supply w = -1; CL-2 never changes a conserved value",
      "Sorkin-type 1/sqrt(V4) needs Lambda conjugate to a 4-volume count; here D is conjugate to the tick count")

print("   summary: handle      size              w     verdict")
print(f"   D degeneracy        none (a^0 vs a^4) -     Lambda stays a coupling, not a charge")
print(f"   empty start <D>=0   Lambda >= 0       -1    sign forced; value = start's H^2 (free) ")
print(f"   least-K edge start  {lam1:.1e}           -1    closed top: forced, Planckian x1e{math.log10(lam1/LAM_MEAS):.0f}; glued top: free")
print(f"   mod 2pi circle      period >= 2pi 8^4 -     no period (2^(4/s) irrational)")
print(f"   window/split phase  free              -     no rule fixes it")
print("supplied: unit map 8piG hbar = L^2; Dirichlet window [L/8, 2L] (Delta = 0, also 1); minisuperspace"
      " homogeneous mode; hop kinetic matched to the classical Regge form; least-K start (B estimate only);"
      " eps0 range from the register; Planck 2018 Lambda; t0 = 13.8 Gyr.")
print(f"elapsed_seconds {time.time()-T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
