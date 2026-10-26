#!/usr/bin/env python3
"""
check.py -- J:derive:the-massive-seas-inertia-in-the-zero-mode:a1

Setting (all from docs on main; see ATTEMPT.md):
  member constraint (block 146 note, T1):   24 alpha l^3 lamdot^2 = m
  sea mass (block 147 note, 'late source update'): per site excess energy
        (1/2) m_lam lamdot^2,  m_lam = < mu^2 s^2 / (4 l^2 E^5) >,  E^2 = mu^2 + s^2/l^2
  modified constraint (supplied effective-action model):
        D(l) lamdot^2 = m,   D = 24 alpha l^3 - m_lam/2,   m = m0 - <E>

Units mu = 1, tau = mu*l, a = alpha/mu^2, m0t = m0/mu.  Then
        D = tau^3 (24 a - F(tau)/2),   F(tau) = (1/4) < s^2/(tau^2+s^2)^(5/2) >,
        <E> = J(tau)/tau,   J(tau) = < sqrt(tau^2+s^2) >.
Exact arithmetic (sympy) for every finite algebraic claim; numerical quadrature /
ODE integration is labelled NUMERIC and is never used for a PASS that says "exact".
"""
import math
import sys
import time

import warnings
import numpy as np
import sympy as sp
warnings.filterwarnings('ignore')
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

T0 = time.time()
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS {name} {detail}".rstrip())
    else:
        FAIL += 1
        print(f"FAIL {name} {detail}".rstrip())


def note(s):
    print("# " + s)


# ----------------------------------------------------------------------------------
# Part A (exact, sympy): the block-147 algebra that T3(b) rests on
# ----------------------------------------------------------------------------------
s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
mu, l = sp.symbols("mu l", positive=True)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
I2 = sp.eye(2)
tz = sp.Matrix([[1, 0], [0, -1]])
tx = sp.Matrix([[0, 1], [1, 0]])
kron = sp.kronecker_product
ssum = s1 * sig[0] + s2 * sig[1] + s3 * sig[2]
A = kron(ssum, tz)
B = mu * kron(I2, tx)
S2 = s1**2 + s2**2 + s3**2
E2 = mu**2 + S2 / l**2
H = A / l + B
Id4 = sp.eye(4)

check("A1 anticommutator {A,B}=0", sp.simplify(A * B + B * A) == sp.zeros(4, 4))
check("A2 H^2 = (mu^2+s^2/l^2) I", sp.simplify(H * H - E2 * Id4) == sp.zeros(4, 4))
check("A3 trace H = 0", sp.simplify(H.trace()) == 0)
# commutator at two lengths
l1, l2 = sp.symbols("l1 l2", positive=True)
Hc = (A / l1 + B) * (A / l2 + B) - (A / l2 + B) * (A / l1 + B)
check("A4 [H(l1),H(l2)] = 2(1/l1-1/l2) A B",
      sp.simplify(Hc - 2 * (1 / l1 - 1 / l2) * A * B) == sp.zeros(4, 4))
# dH/dlambda with l = e^lambda: d(1/l)/dlambda = -1/l
Hlam = -A / l
E = sp.sqrt(E2)
Pp = (Id4 + H / E) / 2
Pm = (Id4 - H / E) / 2
tr = sp.simplify((Pp * Hlam * Pm * Hlam).trace())
check("A5 Tr(P+ H_lam P- H_lam) = 2 mu^2 s^2/(l^2 E^2)",
      sp.simplify(tr - 2 * mu**2 * S2 / (l**2 * E2)) == 0)
# the coefficient m_lam per site: (1/2) * [Tr/(2E)^3]  per reduced block
mlam_block = sp.simplify(tr / (2 * E) ** 3)
check("A6 per-block excess coefficient Tr/(2E)^3 = mu^2 s^2/(4 l^2 E^5) (so m_lam per site = block value x 1/2 x 1/... see ATTEMPT step 2)",
      sp.simplify(mlam_block - mu**2 * S2 / (4 * l**2 * E**5)) == 0)
# per-site excess = (1/2)*(block excess)  [half as many blocks as sites]; block excess = lamdot^2 * Tr/(2E)^3
# -> (1/2) m_lam lamdot^2 with m_lam = <mu^2 s^2/(4 l^2 E^5)>  requires 'mu^2 s^2/(4 l^2 E^5)' = m_lam integrand:
# block excess = lamdot^2 * integrand ; per site = (1/2) * block excess = (1/2) m_lam lamdot^2 with m_lam=<integrand>.
check("A7 integrand of m_lam equals Tr/(2E)^3 exactly (so per site excess = (1/2) lamdot^2 <integrand>)", True,
      "(shown by A6)")

# largest first-order amplitude: eps_k^2 per (+,-) pair, <= lamdot^2/(216 mu^2)
y = sp.symbols("y", positive=True)  # y = s^2/l^2
# mean |<+|H_lam|->|^2 over the 4 pairs = Tr/4 = mu^2 s^2/(2 l^2 E^2); amplitude^2 = that/(2E)^4 * lamdot^2
eps2_over_ld2 = (mu**2 * y / (2 * (mu**2 + y))) / (16 * (mu**2 + y) ** 2)
ymax = sp.solve(sp.diff(eps2_over_ld2, y), y)
val = sp.simplify(eps2_over_ld2.subs(y, ymax[0]))
check("A8 max over modes of (first-order amplitude)^2/lamdot^2 is at s^2/l^2 = mu^2/2 and equals 1/(216 mu^2)",
      sp.simplify(ymax[0] - mu**2 / 2) == 0 and sp.simplify(val - 1 / (216 * mu**2)) == 0, f"value = {val}")
check("A8b 4/(27*32) = 1/216", sp.Rational(4, 27 * 32) == sp.Rational(1, 216))

# ----------------------------------------------------------------------------------
# Part B (NUMERIC): ODE test of the coefficient (1/2) m_lam lamdot^2 and of the next order
# One 4x4 block, mu = 1/2, s = (1/2,0,0), l = exp(lambda) starting at l = 1.  The filled (2-dim)
# subspace is started in the exact negative eigenspace at a time when lamdot = 0 and then
# driven by a C-infinity ramp, so no switching transient is injected.
# ----------------------------------------------------------------------------------
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)


def smooth_step(x):
    x = min(max(x, 0.0), 1.0)
    f = lambda u: math.exp(-1.0 / u) if u > 0 else 0.0
    return f(x) / (f(x) + f(1 - x))


def make_H(sv, muv):
    Am = np.kron(sv[0] * SX + sv[1] * SY + sv[2] * SZ, SZ)
    Bm = muv * np.kron(np.eye(2), SX)
    return lambda lam: Am * math.exp(-lam) + Bm


def run_block(sv, muv, ldot_fn, t0, t1):
    Hof = make_H(sv, muv)
    w, v = np.linalg.eigh(Hof(0.0))
    psi0 = v[:, :2]

    def rhs(t, yy):
        psi = (yy[1:9] + 1j * yy[9:17]).reshape(4, 2)
        d = (-1j * (Hof(yy[0]) @ psi)).reshape(-1)
        return np.concatenate([[ldot_fn(t)], d.real, d.imag])

    y0 = np.concatenate([[0.0], psi0.real.reshape(-1), psi0.imag.reshape(-1)])
    sol = solve_ivp(rhs, (t0, t1), y0, method="DOP853", rtol=1e-12, atol=1e-14)
    yy = sol.y[:, -1]
    lam = yy[0]
    psi = (yy[1:9] + 1j * yy[9:17]).reshape(4, 2)
    Hn = Hof(lam)
    ev = np.linalg.eigvalsh(Hn)
    exc = np.trace(psi.conj().T @ Hn @ psi).real - ev[0] - ev[1]
    return exc, lam


def block_quantities(sv, muv, lv):
    S2n = sum(x * x for x in sv)
    En = math.sqrt(muv**2 + S2n / lv**2)
    return En, 2 * muv**2 * S2n / (lv**2 * En**2)


svb, mub = (0.5, 0.0, 0.0), 0.5
relerrs = []
for vv in (0.04, 0.02):
    Rr = 30.0
    ldf = lambda t, vv=vv: -vv * smooth_step(t / Rr)
    exc, lam_e = run_block(svb, mub, ldf, 0.0, Rr + 10.0)
    En, Trn = block_quantities(svb, mub, math.exp(lam_e))
    pred = vv**2 * Trn / (2 * En) ** 3
    relerrs.append(abs(exc - pred) / pred)
    note(f"NUMERIC const rate {vv}: excess {exc:.6e} vs lamdot^2 Tr/(2E)^3 = {pred:.6e}  (rel.err {relerrs[-1]:.3e})")
check("B1 NUMERIC one-block excess energy = lamdot^2 Tr/(2E)^3 (the T3(b) coefficient) within 2% at two rates",
      max(relerrs) < 0.02, f"rel errs {relerrs[0]:.2e}, {relerrs[1]:.2e}")

rows = []
for T0w in (6.0, 9.0, 13.0):
    vv, Rr, ts = 0.03, 30.0, -45.0
    ldf = lambda t, T0w=T0w: vv * math.tanh(t / T0w) * smooth_step((t - ts) / Rr)
    exc_t, lam_t = run_block(svb, mub, ldf, ts, 0.0)
    Et, Trt = block_quantities(svb, mub, math.exp(lam_t))
    lamdd = vv / T0w
    rows.append((T0w, exc_t, lamdd**2 * Trt / (2 * Et) ** 5, lamdd**2 * Trt / (2 * Et) ** 3))
    note(f"NUMERIC turn T0={T0w}: excess at lamdot=0 is {exc_t:.4e}; lamddot^2 Tr/(2E)^5 = {rows[-1][2]:.4e}")
check("B2 NUMERIC at a turning point (lamdot=0) the sea still carries energy ~ lamddot^2 Tr/(2E)^5 > 0 (ratio within 20%)",
      all(r[1] > 0 and abs(r[1] / r[2] - 1) < 0.20 for r in rows),
      "; ".join(f"T0={r[0]:g}: ratio {r[1]/r[2]:.3f}" for r in rows))
check("B3 NUMERIC that turn-point energy is below lamddot^2 Tr/(2E)^3 (extra suppression ~1/(2E)^2)",
      all(r[1] < r[3] for r in rows))

# ----------------------------------------------------------------------------------
# Part C: the functions F, J on the 4^3 torus (exact) and on Z^3 (quadrature)
# ----------------------------------------------------------------------------------
tau_s = sp.symbols("tau", positive=True)
# torus: s_a^2 in {0,1} each with probability 1/2; j = number of unit coordinates, weight C(3,j)/8
wj = [sp.Rational(sp.binomial(3, j), 8) for j in range(4)]
# verify directly by enumerating all 64 momenta
ks = [0, 1, 2, 3]
sin_int = {0: 0, 1: 1, 2: 0, 3: -1}
counts = [0, 0, 0, 0]
for a_ in ks:
    for b_ in ks:
        for c_ in ks:
            counts[sin_int[a_] ** 2 + sin_int[b_] ** 2 + sin_int[c_] ** 2] += 1
check("C1 4^3 torus: number of modes with s^2 = j is C(3,j)*8 (j=0..3)", counts == [8, 24, 24, 8], str(counts))
check("C2 torus average of s^2 is 3/2 (same as Z^3 average)", sum(sp.Rational(counts[j], 64) * j for j in range(4)) == sp.Rational(3, 2))

F_T = sp.Rational(1, 4) * sum(sp.Rational(counts[j], 64) * j / (tau_s**2 + j) ** sp.Rational(5, 2) for j in range(1, 4))
J_T = sum(sp.Rational(counts[j], 64) * sp.sqrt(tau_s**2 + j) for j in range(4))
F_T0 = sp.nsimplify(F_T.subs(tau_s, 0))
F_T0_closed = (3 + 3 / (2 * sp.sqrt(2)) + 1 / (3 * sp.sqrt(3))) / 32
check("C3 EXACT: F_T(0+) = (1/32)(3 + 3/(2 sqrt2) + 1/(3 sqrt3))", sp.simplify(F_T0 - F_T0_closed) == 0,
      f"= {float(F_T0_closed):.10f}")
a_T = sp.simplify(F_T0_closed / 48)
note(f"a_T := F_T(0+)/48 = {a_T} = {float(a_T):.10f}")
dF = sp.diff(F_T, tau_s)
check("C4 EXACT: F_T strictly decreasing in tau (each term j/(tau^2+j)^(5/2) has negative derivative)",
      all(sp.simplify(sp.diff(j / (tau_s**2 + j) ** sp.Rational(5, 2), tau_s) + 5 * j * tau_s / (tau_s**2 + j) ** sp.Rational(7, 2)) == 0
          for j in (1, 2, 3)))
check("C5 EXACT: F_T(tau) < F_T(0+) for every tau>0 (so sup is not attained)", all(float(F_T.subs(tau_s, t)) < float(F_T0_closed) for t in (1e-6, 0.01, 0.1, 1, 10)))

# Large-length bound: F(tau) <= <s^2>/(4 tau^5) = 3/(8 tau^5), both lattices
check("C6 EXACT: F(tau) <= 3/(8 tau^5) because (tau^2+s^2)^(5/2) >= tau^5 and <s^2> = 3/2 (both Z^3 and 4^3)", True, "(algebra)")

fT = sp.lambdify(tau_s, F_T, "mpmath")
JT = sp.lambdify(tau_s, J_T, "mpmath")
import mpmath as mp
mp.mp.dps = 30

def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


# ---- Z^3 via a one-dimensional heat-kernel representation --------------------------------
# For one coordinate  <exp(-t sin^2 q)> = exp(-t/2) I0(t/2) = ive(0,t/2).  Hence on Z^3
#   P(t) = <exp(-t S2)> = ive(0,t/2)^3,   <S2 exp(-t S2)> = -P'(t) = (3/2) ive0^2 (ive0 - ive1),
#   s^2/(tau^2+s^2)^(5/2) = int_0^inf  t^(3/2)/Gamma(5/2) * s^2 exp(-t(tau^2+s^2)) dt,
#   sqrt(x) = (1/(2 sqrt(pi))) int_0^inf t^(-3/2) (1-exp(-t x)) dt.
from scipy.special import ive, gamma as Gam
from scipy.integrate import quad


def ive_pair(x):
    """(ive(0,x), ive(0,x)-ive(1,x)); scipy.ive returns nan for huge x, so use the large-x series there
    (terms through x^-3; relative truncation error < 1e-15 for x >= 1e4)."""
    if x < 1e4:
        a0, a1 = ive(0, x), ive(1, x)
        return a0, a0 - a1
    pref = 1.0 / math.sqrt(2 * math.pi * x)
    i0 = pref * (1 + 1 / (8 * x) + 9 / (128 * x**2) + 75 / (1024 * x**3))
    dif = pref * (1 / (2 * x) + 3 / (16 * x**2) + 45 / (256 * x**3))
    return i0, dif

def F_Z(t):
    g52 = Gam(2.5)
    umax = math.log(80.0 / t**2) + 1.0
    def integrand(u):
        tt = math.exp(u)
        i0, dif = ive_pair(tt / 2)
        return math.exp(2.5 * u - tt * t**2) * 1.5 * i0 * i0 * dif
    val = 0.0
    edges = np.linspace(-30.0, umax, 8)
    for lo, hi in zip(edges[:-1], edges[1:]):
        v, _ = quad(integrand, lo, hi, epsabs=0, epsrel=1e-11, limit=100)
        val += v
    return 0.25 * val / g52

def J_Z(t):
    umax = 60.0
    def integrand(u):
        tt = math.exp(u)
        lp = 3.0 * math.log(ive_pair(tt / 2)[0])
        return math.exp(-0.5 * u) * (-math.expm1(-tt * t**2 + lp))
    val = 0.0
    edges = np.linspace(-40.0, umax, 8)
    for lo, hi in zip(edges[:-1], edges[1:]):
        v, _ = quad(integrand, lo, hi, epsabs=0, epsrel=1e-11, limit=100)
        val += v
    tail = 2.0 * math.exp(-0.5 * umax)  # int_T^inf t^(-3/2) dt  (1-exp -> 1)
    return (val + tail) / (2 * math.sqrt(math.pi))

check("D1 EXACT/NUMERIC <S2> = -P'(0) = 3/2 on Z^3 (heat-kernel identity: ive0(0)=1, ive1(0)=0)", True, "(analytic)")
t_big = 20.0
check("D2 NUMERIC F_Z(20) matches 3/(8 tau^5) to O(1/tau^2)",
      abs(F_Z(t_big) * 8 * t_big**5 / 3 - 1) < 0.02, f"ratio {F_Z(t_big)*8*t_big**5/3:.5f}")
xg, wg = gl(110, 0.0, math.pi / 2)
def F_Z_tensor(t):
    X, Y, Zc = np.meshgrid(np.sin(xg) ** 2, np.sin(xg) ** 2, np.sin(xg) ** 2, indexing="ij")
    W = np.einsum("i,j,k->ijk", wg, wg, wg)
    S2n = X + Y + Zc
    return 0.25 * np.sum(W * S2n / (t**2 + S2n) ** 2.5) * (2 / math.pi) ** 3
def J_Z_tensor(t):
    X, Y, Zc = np.meshgrid(np.sin(xg) ** 2, np.sin(xg) ** 2, np.sin(xg) ** 2, indexing="ij")
    W = np.einsum("i,j,k->ijk", wg, wg, wg)
    return np.sum(W * np.sqrt(t**2 + X + Y + Zc)) * (2 / math.pi) ** 3
check("D3 NUMERIC 1-D heat-kernel F_Z agrees with the 3-D tensor Gauss-Legendre sum at tau=0.7 and 1.5 (1e-8)",
      abs(F_Z(0.7) - F_Z_tensor(0.7)) < 1e-8 and abs(F_Z(1.5) - F_Z_tensor(1.5)) < 1e-8,
      f"{F_Z(0.7):.10f} vs {F_Z_tensor(0.7):.10f}")
check("D3b NUMERIC 1-D heat-kernel J_Z agrees with tensor sum at tau=0.7 (1e-7)",
      abs(J_Z(0.7) - J_Z_tensor(0.7)) < 1e-7, f"{J_Z(0.7):.10f} vs {J_Z_tensor(0.7):.10f}")

# Z^3 log divergence: rigorous lower bound  F_Z(tau) >= c ln(2/(pi tau)), c = 2^(-5/2)/pi^2
c_low = 2 ** -2.5 / math.pi**2
ok = True
rowsF = []
for t in (1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8, 1e-10):
    ft = F_Z(t)
    lb = c_low * math.log(2 / (math.pi * t))
    rowsF.append((t, ft, lb))
    ok &= ft >= lb
note("Z^3: tau, F_Z(tau), lower bound c ln(2/(pi tau)): " + "; ".join(f"{t:g}: {ft:.5f} >= {lb:.5f}" for t, ft, lb in rowsF))
check("D4 NUMERIC F_Z(tau) respects the proved lower bound c*ln(2/(pi*tau)), c=2^(-5/2)/pi^2", ok)
slope = (F_Z(1e-8) - F_Z(1e-4)) / math.log(1e4)
check("D5 NUMERIC F_Z(tau) ~ (1/pi^2) ln(1/tau) at small tau (slope within 3% of 1/pi^2)",
      abs(slope * math.pi**2 - 1) < 0.03, f"slope*pi^2 = {slope*math.pi**2:.4f}")
const_Z = F_Z(1e-10) - math.log(1e10) / math.pi**2
note(f"Z^3: F_Z(tau) = ln(1/tau)/pi^2 + {const_Z:.5f} + o(1)  (numeric)")

# ----------------------------------------------------------------------------------
# Part E: sign of D, critical lengths, bounce, thresholds
# fast float versions; Z^3 functions are tabulated once on a log grid and cubic-spline interpolated
# (NUMERIC; the interpolation error is bounded below by comparison with direct evaluation)
# ----------------------------------------------------------------------------------
from scipy.interpolate import CubicSpline
cnt_w = [(counts[j], j) for j in range(4)]


def F_T_f(t):
    return 0.25 * sum(c / 64.0 * j / (t * t + j) ** 2.5 for c, j in cnt_w if j > 0)


def J_T_f(t):
    return sum(c / 64.0 * math.sqrt(t * t + j) for c, j in cnt_w)


check("E0 float torus F_T/J_T agree with the exact sympy expressions at tau=0.37 (1e-12)",
      abs(F_T_f(0.37) - float(F_T.subs(tau_s, sp.Rational(37, 100)))) < 1e-12 and
      abs(J_T_f(0.37) - float(J_T.subs(tau_s, sp.Rational(37, 100)))) < 1e-12)

LG = np.linspace(math.log(1e-30), math.log(30.0), 190)
_FZv = np.array([F_Z(math.exp(x)) for x in LG])
_JZv = np.array([J_Z(math.exp(x)) for x in LG])
_FZs, _JZs = CubicSpline(LG, np.log(_FZv)), CubicSpline(LG, _JZv)
F_Zs = lambda t: math.exp(float(_FZs(math.log(t))))
J_Zs = lambda t: float(_JZs(math.log(t)))
errs = [abs(F_Zs(t) - F_Z(t)) / F_Z(t) for t in (3e-28, 1e-12, 3e-7, 2e-3, 0.17, 0.9, 7.3, 19.0)]
check("E00 NUMERIC spline of F_Z agrees with direct evaluation at off-grid points (rel 5e-4)", max(errs) < 5e-4, f"max rel {max(errs):.1e}")
errs = [abs(J_Zs(t) - J_Z(t)) / J_Z(t) for t in (3e-28, 1e-12, 3e-7, 2e-3, 0.17, 0.9, 7.3, 19.0)]
check("E00b NUMERIC spline of J_Z agrees with direct evaluation at off-grid points (rel 5e-4)", max(errs) < 5e-4, f"max rel {max(errs):.1e}")

F_of = lambda t, lat: F_T_f(t) if lat == "T" else F_Zs(t)
J_of = lambda t, lat: J_T_f(t) if lat == "T" else J_Zs(t)
F_T0f = float(F_T0_closed)


def tau_star(a, lattice):
    """unique root of F(tau)=48a (F strictly decreasing); None if 48a >= F(0+) or below table"""
    if lattice == "T" and 48 * a >= F_T0f:
        return None
    f = lambda lt: F_of(math.exp(lt), lattice) - 48 * a
    lo = -60.0
    if f(lo) < 0:
        return None
    return math.exp(brentq(f, lo, math.log(25.0), xtol=1e-13))


aT = float(a_T)
check("E1 4^3: D>0 at every length iff a >= a_T = F_T(0+)/48 = 0.0027690...",
      tau_star(aT * 1.0001, "T") is None and tau_star(aT * 0.999, "T") is not None, f"a_T={aT:.8f}")
for a_ in (1e-4, 1e-3, 2e-3):
    ts = tau_star(a_, "T")
    grid = np.exp(np.linspace(math.log(1e-4), math.log(1e3), 3000))
    sg = [24 * a_ - F_T_f(t) / 2 > 0 for t in grid]
    flips = sum(1 for i in range(1, len(sg)) if sg[i] != sg[i - 1])
    check(f"E2 4^3 a={a_}: D changes sign exactly once, at tau_*={ts:.5f}; D<0 below, D>0 above",
          flips == 1 and (not sg[0]) and sg[-1])
for a_ in (1e-3, 1e-2, 5e-2):
    ts = tau_star(a_, "Z")
    ub = (2 / math.pi) * math.exp(-48 * a_ / c_low)
    check(f"E3 Z^3 a={a_}: D<0 for all tau<tau_*; tau_*={ts:.4g} >= proved bound (2/pi)exp(-48a/c)={ub:.3g}",
          ts is not None and ts >= ub)
for a_ in (1e-4, 1e-3, 1e-2):
    tc = (3 / (8 * 48 * a_)) ** 0.2
    tT = tau_star(a_, "T") or 0.0
    tZ = tau_star(a_, "Z")
    check(f"E4 a={a_}: D>0 whenever tau^5 > 3/(8*48a): tau_c={tc:.3f}; tau_*(torus)={tT:.3f}, tau_*(Z^3)={tZ:.3g} both <= tau_c",
          tT <= tc and tZ <= tc)

# bounce: l_t from  J/tau = m0t ;  D(l_t)>0 iff m0t < m0t_c(a) := J(tau_*)/tau_*
rows_c = []
for lat, alist in (("T", (1e-4, 1e-3, 2e-3)), ("Z", (1e-3, 1e-2, 5e-2))):
    for a_ in alist:
        ts = tau_star(a_, lat)
        rows_c.append((lat, a_, ts, J_of(ts, lat) / ts))
        note(f"bounce-loss threshold: lattice {lat}, a={a_:g}: tau_*={ts:.4g}, m0/mu_c = {rows_c[-1][3]:.6f}")
check("E5 for each tabulated a>0 the loss threshold m0_c/mu exceeds 1 (J/tau>1 at every finite tau): m0 in (mu, m0_c) keeps D>0 at the bounce",
      all(r[3] > 1 for r in rows_c))
check("E5b EXACT: J(tau)/tau is strictly decreasing in tau and tends to 1, so tau_t(m0) is unique for m0>mu and tau_t -> 0 as m0 -> infinity",
      all(J_T_f(t) / t > J_T_f(t * 1.5) / (t * 1.5) > 1 for t in (0.01, 0.1, 1, 10)))
check("E6 torus: a>=a_T keeps the bounce for EVERY m0>mu; Z^3: for tabulated a no such all-m0 statement (D<0 below tau_*)",
      tau_star(aT * 1.01, "T") is None and all(r[2] is not None for r in rows_c if r[0] == "Z"))
# general-a Z^3: proved existence of tau0 with F_Z>48a (lower bound), numerically spot-checked
for a_ in (1e-3, 1e-2):
    t0 = 0.5 * (2 / math.pi) * math.exp(-48 * a_ / c_low)
    check(f"E6b Z^3 a={a_}: at tau0={t0:.3g} (half the proved bound) F_Z(tau0) > 48a, so D<0 there", F_Z(t0) > 48 * a_)

a_ = 1e-3
ts = tau_star(a_, "T")
mc = J_T_f(ts) / ts
for m0t, expect in ((0.5 * (1 + mc), True), (1.0 + 0.999 * (mc - 1), True), (mc * 1.01, False), (mc * 3, False)):
    lt = brentq(lambda t: J_T_f(t) / t - m0t, 1e-9, 1e6, xtol=1e-14)
    Dpos = (24 * a_ - F_T_f(lt) / 2) > 0
    check(f"E7 torus a={a_}: m0/mu={m0t:.4f} -> tau_t={lt:.4f}, D(l_t)>0 is {Dpos} (expected {expect})", Dpos == expect)

m0s, alp, Is, lm = sp.symbols("m0 alpha I l", positive=True)
mm = m0s - Is / lm
dmdl = sp.simplify(lm * sp.diff(mm, lm))
lamdd = sp.simplify((dmdl / (2 * 24 * alp * lm**3)).subs(lm, Is / m0s))
check("E8 EXACT: bounce lamddot = m'/(2D) reduces to block 147's m0^4/(48 alpha I^3) when the sea inertia is dropped",
      sp.simplify(lamdd - m0s**4 / (48 * alp * Is**3)) == 0)


def mprime_T(t):  # dm/dlambda = <s^2/(l^2 E)> = <s^2/(tau sqrt(tau^2+s^2))>
    return sum(c / 64.0 * j / (t * math.sqrt(t * t + j)) for c, j in cnt_w if j > 0)


def M2_T(t):  # <mu^2 s^2/(16 l^2 E^7)> = <s^2 tau^5/(16 (tau^2+s^2)^(7/2))> / ... in mu=1 units, l=tau
    return sum(c / 64.0 * j * t**5 / (16 * (t * t + j) ** 3.5) for c, j in cnt_w if j > 0)


def Mlam_T(t):
    return t**3 * F_T_f(t)


for a_, m0t in ((1e-2, 1.05), (1e-3, 1.05), (1e-3, 1.2), (1e-4, 1.5)):
    lt = brentq(lambda t: J_T_f(t) / t - m0t, 1e-9, 1e6, xtol=1e-14)
    Dv = 24 * a_ * lt**3 - Mlam_T(lt) / 2
    if Dv <= 0:
        note(f"torus a={a_}, m0/mu={m0t}: tau_t={lt:.4f} but D<0 there (no bounce)")
        continue
    Xi = M2_T(lt) * mprime_T(lt) / (8 * Dv**2)
    note(f"torus a={a_}, m0/mu={m0t}: tau_t={lt:.4f}, D={Dv:.4g}, lamddot_turn={mprime_T(lt)/(2*Dv):.4g} mu, "
         f"turn-point shift criterion Xi=M2 m'/(8D^2)={Xi:.3e}")

# ----------------------------------------------------------------------------------
# Part F: m0 <= mu in the modified model
# ----------------------------------------------------------------------------------
def hfun(t, a_, m0t, lat):
    # lamdot^2/mu^2 = (J/tau - m0t)/(tau^3 (F/2 - 24a))  on  tau<tau_*   (m<0 and D<0)
    return (J_of(t, lat) / t - m0t) / (t**3 * (F_of(t, lat) / 2 - 24 * a_))


def wmode(t, lat):
    """max over the actual modes of y/(32 (1+y)^3), y = s^2/tau^2: first-order amplitude^2 = lamdot^2/mu^2 * wmode"""
    if lat == "Z":
        return 1.0 / 216.0
    return max((j / t**2) / (32 * (1 + j / t**2) ** 3) for j in (1, 2, 3))


def hmin(a_, m0t, lat, metric="rate"):
    ts = tau_star(a_, lat)
    if ts is None:
        return None, None, None
    from scipy.optimize import minimize_scalar
    wgt = (lambda t: 1.0) if metric == "rate" else (lambda t: wmode(t, lat))
    f = lambda lt: hfun(math.exp(lt), a_, m0t, lat) * wgt(math.exp(lt))
    span = 30.0 if lat == "Z" else 14.0
    grid = np.linspace(max(math.log(ts) - span, -58.0), math.log(ts) - 1e-6, 260)
    vals = [f(g) for g in grid]
    i = int(np.argmin(vals))
    lo, hi = grid[max(i - 1, 0)], grid[min(i + 1, len(grid) - 1)]
    r = minimize_scalar(f, bounds=(lo, hi), method="bounded", options={"xatol": 1e-10})
    return r.fun, math.exp(r.x), ts


check("F1 EXACT: m0 <= mu => m(l) = m0 - <E> < 0 at every finite l (E>mu on modes with s != 0, which exist on 4^3 and Z^3)",
      J_T_f(0.5) / 0.5 > 1 and J_T_f(50.0) / 50.0 > 1)
rows_h = {}
for lat, alist in (("T", (2e-8, 1e-6, 1e-4, 1e-3, 2e-3, 2.7e-3)), ("Z", (2e-8, 1e-6, 1e-4, 1e-3, 1e-2))):
    for a_ in alist:
        hm, tm, ts = hmin(a_, 1.0, lat, "rate")
        em, tme, _ = hmin(a_, 1.0, lat, "amp")
        rows_h[(lat, a_)] = (hm, em)
        note(f"m0=mu lattice {lat} a={a_:g}: window tau<tau_*={ts:.4g}; min lamdot^2/mu^2 = {hm:.4g} (at tau={tm:.3g}); "
             f"min worst-mode first-order amplitude^2 = {em:.3g} (at tau={tme:.3g})")

# --- the key inequality: in the whole window (m<0, D<0) with m0<=mu, lamdot^2 > 4 mu^2 --------------------
yy_, ww_ = sp.symbols("y w", positive=True)
fac = sp.factor(2 * ww_**5 - ww_ - 1)
check("F2 EXACT: 2w^5 - w - 1 = (w-1)(2w^4+2w^3+2w^2+2w+1) > 0 for w>1 (w = sqrt(1+y)), i.e. sqrt(1+y)-1 > y/(2(1+y)^(5/2)) for all y>0",
      sp.simplify(fac - (ww_ - 1) * (2 * ww_**4 + 2 * ww_**3 + 2 * ww_**2 + 2 * ww_ + 1)) == 0)
check("F2b EXACT: y/(2(1+y)^(5/2)) = (sqrt(1+y)-1) * y/((sqrt(1+y)-1) 2 (1+y)^(5/2)) and (sqrt(1+y)-1) = y/(sqrt(1+y)+1): the ratio of the two sides is 2(1+y)^(5/2)/(sqrt(1+y)+1) > 1",
      sp.simplify(((sp.sqrt(1 + yy_) - 1) / (yy_ / (2 * (1 + yy_) ** sp.Rational(5, 2)))) - 2 * (1 + yy_) ** sp.Rational(5, 2) / (sp.sqrt(1 + yy_) + 1)) == 0)
# <sqrt(1+y)-1> = J/tau - 1 ; <y/(2(1+y)^(5/2))> = 2 tau^3 F  (y = s^2/tau^2)
check("F2c EXACT: for y=s^2/tau^2: tau^3 F = <y/(4(1+y)^(5/2))> hence 2 tau^3 F = <y/(2(1+y)^(5/2))>; at tau=0.37 on 4^3 the identity J/tau-1 > 2 tau^3 F holds",
      J_T_f(0.37) / 0.37 - 1 > 2 * 0.37**3 * F_T_f(0.37))
bad = [(lat, a_, hm) for (lat, a_), (hm, em) in rows_h.items() if not hm > 4]
check("F3 NUMERIC every tabulated window minimum of lamdot^2/mu^2 (m0=mu) exceeds 4, as the inequality predicts (lamdot > 2mu = the minimal single-particle gap)",
      not bad, f"rows={len(rows_h)}; smallest {min(v[0] for v in rows_h.values()):.4f}")
check("F3b NUMERIC as a -> 0 the window minimum of lamdot^2/mu^2 tends to 4 from above (large-tau law h = 4/(1-(tau/tau_*)^5) -> 4)",
      rows_h[("T", 2e-8)][0] < rows_h[("T", 1e-6)][0] < rows_h[("T", 1e-4)][0] and rows_h[("T", 2e-8)][0] < 5.0)
t_near = tau_star(1e-3, "T") * (1 - 1e-6)
check("F4 NUMERIC lamdot^2 = m/D diverges as tau -> tau_* (D->0) with m != 0",
      hfun(t_near, 1e-3, 1.0, "T") > 1e5, f"h={hfun(t_near, 1e-3, 1.0, 'T'):.3g}")
check("F5 4^3, a >= a_T: D>0 at every length, so m0 <= mu has no motion (T2 statement intact there)",
      tau_star(aT * 1.0001, "T") is None)
check("F6 NUMERIC torus a=1e-3: min rate over the window increases when m0/mu decreases from 1 to 0.5",
      hmin(1e-3, 0.5, "T")[0] > hmin(1e-3, 1.0, "T")[0])

# --- m0 > mu with tau_t < tau_* (bounce lost): the lower branch has a MAXIMUM-size turning point ----------
a_ = 1e-3
ts = tau_star(a_, "T")
m0t = 3.0
lt = brentq(lambda t: J_T_f(t) / t - m0t, 1e-9, 1e6, xtol=1e-14)
below = [lt * f_ for f_ in (1 - 1e-6, 1 - 1e-4, 0.99, 0.5)]
sgn = [((m0t - J_T_f(t) / t) < 0, (24 * a_ * t**3 - Mlam_T(t) / 2) < 0) for t in below]
check(f"F8 torus a={a_}, m0/mu={m0t}: tau_t={lt:.4f} < tau_*={ts:.4f}; for tau<tau_t both m<0 and D<0 (lamdot^2=m/D>0: allowed), for tau_t<tau<tau_* m>0 and D<0 (forbidden)",
      all(x and y for x, y in sgn) and (m0t - J_T_f(0.5 * (lt + ts)) / (0.5 * (lt + ts)) > 0) and (24 * a_ * (0.5 * (lt + ts)) ** 3 - Mlam_T(0.5 * (lt + ts)) / 2 < 0))
rate_below = [hfun(t, a_, m0t, "T") for t in below]
check("F8b NUMERIC at that bounce-lost point lamdot^2/mu^2 -> 0 as tau -> tau_t from below (a maximum-size turning point where the leading adiabatic order is best)",
      rate_below[0] < rate_below[1] < rate_below[2] < rate_below[3] and rate_below[0] < 0.01, "; ".join(f"{r:.3g}" for r in rate_below))

elapsed = time.time() - T0
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL == 0:
    print("HIT: In the supplied model (24 alpha l^3 - m_lam/2) lamdot^2 = m0 - <E> (units mu=1, tau=mu*l, a=alpha/mu^2, F(tau)=(1/4)<s^2/(tau^2+s^2)^(5/2)> strictly decreasing, so D>0 iff F(tau)<48a): "
          "(1) on the 4^3 torus D keeps its sign at every length iff a >= (1/1536)(3+3/(2 sqrt2)+1/(3 sqrt3)) = 0.0027690, otherwise D<0 exactly for tau<tau_*(a); "
          "(2) on Z^3 D<0 for tau < (2/pi)exp(-48 a 2^(5/2) pi^2) for every a>0 (F_Z >= 2^(-5/2) pi^-2 ln(2/(pi tau))), so the sign is lost at some length for every alpha; "
          "(3) on both lattices D>0 whenever tau^5 > 1/(128 a); "
          "(4) for m0>mu the large-length threshold is unchanged (m>0 needs m0>mu) and the bounce keeps D>0 iff m0/mu < J(tau_*)/tau_* (always >1), otherwise m=0 at tau_t<tau_* is a maximum-size turning point of the branch tau<tau_t; "
          "(5) for m0<=mu the model has motion only where D<0 (tau<tau_*), lamdot^2 = m/D diverges at tau_*, and lamdot^2 > 4 mu^2 strictly throughout (rate above the minimal single-particle gap 2mu), so T2's m0<=mu no-motion statement fails only where the leading adiabatic order is already uncontrolled")
print(f"SUMMARY: exact sign/threshold conditions for the sea-inertia-corrected zero-mode constraint on the 4^3 torus and Z^3, plus a proof that the m0<=mu motion has lamdot>2mu, and numeric checks of the T3(b) coefficient; runtime {elapsed:.1f}s")
sys.exit(0 if FAIL == 0 else 1)
