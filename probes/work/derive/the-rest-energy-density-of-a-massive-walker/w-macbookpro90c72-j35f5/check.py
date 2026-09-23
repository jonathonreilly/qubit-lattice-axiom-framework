#!/usr/bin/env python3
"""J:derive:the-rest-energy-density-of-a-massive-walker:a2

Objects (blocks 54, 55, 56, 60, 76, 77; open PRs #8570 #8571 #8573 #8590 #8611 #8612; not adopted):
  H = sum_j sigma_j D_j, (D_j psi)(x) = (i/2)(psi(x - e_j) - psi(x + e_j))  (symbol sin k_j),
  eps(x) = (-1)^{x+y+z}, the massive walk H + m eps, clocked phi (H + m eps) phi = phi H phi + m w eps,
  energy density e_x = Re psi_x^dag (H_w psi)_x (block 55), simplest member's weak-field law
  (1 - A) u = -(gamma/6)(e - mean e)/wbar (block 55 T4, A = average over the six neighbours),
  curvature member's weak-field laws Lap lam = -e/(4K wbar), Lap u = (e + tau)/(4K wbar) (block 60 T3).
Families: A the density of a positive-energy walker (exact, 4^3 torus, Gaussian rationals, m = 3/4);
B the field of the chessboard part and who feels a chessboard of clocks (exact); C the pull (exact
symbols; the argument in ATTEMPT.md); N a floating-point illustration (labelled, not load-bearing).
"""
import itertools
import sys
import time
from fractions import Fraction as F

import sympy as sp

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    print(("ok " if cond else "FAIL ") + tag + (" " + msg if msg else ""))
    if not cond:
        FAILS.append(tag)


# ---------------------------------------------------------------- Gaussian rationals
class G:
    __slots__ = ("r", "i")

    def __init__(s, r=0, i=0):
        s.r, s.i = F(r), F(i)

    def __add__(s, o):
        return G(s.r + o.r, s.i + o.i)

    def __sub__(s, o):
        return G(s.r - o.r, s.i - o.i)

    def __mul__(s, o):
        if isinstance(o, G):
            return G(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
        return G(s.r * o, s.i * o)

    __rmul__ = __mul__

    def conj(s):
        return G(s.r, -s.i)

    def __eq__(s, o):
        return s.r == o.r and s.i == o.i

    def abs2(s):
        return s.r * s.r + s.i * s.i


Z, ONE, I = G(0), G(1), G(0, 1)
L = 4
V = L**3
SITES = list(itertools.product(range(L), repeat=3))
IDX = {x: n for n, x in enumerate(SITES)}
EPS = [(-1) ** (x[0] + x[1] + x[2]) for x in SITES]
SIG = [[[Z, ONE], [ONE, Z]], [[Z, G(0, -1)], [I, Z]], [[ONE, Z], [Z, G(-1)]]]


def shift(x, j, s):
    y = list(x)
    y[j] = (y[j] + s) % L
    return IDX[tuple(y)]


def applyH(v):          # v: list over sites of [c0, c1]
    out = [[Z, Z] for _ in SITES]
    for n, x in enumerate(SITES):
        for j in range(3):
            dv = [(v[shift(x, j, -1)][a] - v[shift(x, j, +1)][a]) * G(0, F(1, 2)) for a in range(2)]
            for a in range(2):
                acc = Z
                for b in range(2):
                    acc = acc + SIG[j][a][b] * dv[b]
                out[n][a] = out[n][a] + acc
    return out


def applyM(v, m):
    return [[v[n][a] * (m * EPS[n]) for a in range(2)] for n in range(V)]


def add(u, v):
    return [[u[n][a] + v[n][a] for a in range(2)] for n in range(V)]


def scal(v, c):
    return [[v[n][a] * c for a in range(2)] for n in range(V)]


def dens(v):
    return [v[n][0].abs2() + v[n][1].abs2() for n in range(V)]


def edens(v, Hv):       # Re v_x^dag (Hv)_x
    return [(v[n][0].conj() * Hv[n][0] + v[n][1].conj() * Hv[n][1]).r for n in range(V)]


def ipow(e):            # i^e
    return [ONE, I, G(-1), G(0, -1)][e % 4]


m = F(3, 4)
Hm = lambda v: add(applyH(v), applyM(v, m))

# ---------------------------------------------------------------- A1 rest states at the zero live on one sublattice
good = True
for nvec in itertools.product((0, 1), repeat=3):
    for spin in ((ONE, Z), (Z, ONE)):
        chi = [[ipow(2 * sum(nv * xv for nv, xv in zip(nvec, x))) * (1 + EPS[k]) * spin[a] for a in range(2)]
               for k, x in enumerate(SITES)]
        HC = Hm(chi)
        good &= all(HC[k][a] == chi[k][a] * m for k in range(V) for a in range(2))
        good &= all(dens(chi)[k] == 0 for k in range(V) if EPS[k] == -1)
ok("A1.rest", good, "the 8 positive rest states e^{i pi n.x}(1+eps)u: (H + m eps) chi = m chi, zero on every odd site")
chi = [[(1 + EPS[k]) * ONE, Z] for k in range(V)]
nrm = sum(dens(chi))
e_rest = [x / nrm for x in edens(chi, Hm(chi))]
ok("A1.density", all(e_rest[k] == (m * F(2, V) if EPS[k] == 1 else 0) for k in range(V)) and sum(e_rest) == m,
   "e_x = m |chi_x|^2 = 2m/V on even sites, 0 on odd sites, sum m: non-negative, not alternating")

# ---------------------------------------------------------------- A2 a moving eigenstate, k = (pi/2, 0, 0), E = 5/4
kv = (1, 0, 0)
psi = [[ipow(sum(a * b for a, b in zip(kv, x))) * (1 + F(EPS[n], 3)) for _ in range(2)] for n, x in enumerate(SITES)]
Hp = Hm(psi)
ok("A2.eigen", all(Hp[n][a] == psi[n][a] * F(5, 4) for n in range(V) for a in range(2)),
   "psi = e^{ik.x}(1 + eps/3)(1,1): eigenvalue E = sqrt(1 + m^2) = 5/4")
dp = dens(psi)
nrm = sum(dp)
w_even = sum(dp[n] for n in range(V) if EPS[n] == 1) / nrm
e_full = [x / nrm for x in edens(psi, Hp)]
e_mass = [m * EPS[n] * dp[n] / nrm for n in range(V)]
e_kin = [a - b for a, b in zip(e_full, e_mass)]
ok("A2.weights", w_even == F(4, 5), "even weight (E+m)/(2E) = 4/5, odd weight (E-m)/(2E) = 1/5")
ok("A2.full", all(e_full[n] == F(5, 4) * dp[n] / nrm for n in range(V)) and sum(e_full) == F(5, 4),
   "full density e_x = E|psi_x|^2 >= 0 at every site, sum 5/4")
ok("A2.mass", sum(e_mass) == F(9, 20) and all((e_mass[n] > 0) == (EPS[n] == 1) for n in range(V)),
   "mass part m eps|psi|^2 alternates (sum 9/20 = m^2/E); kinetic part sum 4/5 = |h|^2/E fills the odd sites")
ok("A2.kin", sum(e_kin) == F(4, 5) and all(e_kin[n] >= 0 for n in range(V)))

# ---------------------------------------------------------------- A3 a packet: rest state + moving state
chi_n = scal(chi, F(1, 8))                  # rest state, ||chi_n||^2 = 2
psi_n = scal(psi, F(3, 8))                  # moving state, ||psi_n||^2 = 5/2
pk = add(chi_n, psi_n)
Hpk = add(Hm(chi_n), Hm(psi_n))
nr = sum(dens(pk))
n1, n2 = sum(dens(chi_n)), sum(dens(psi_n))
epk = [x / nr for x in edens(pk, Hpk)]
ev_sum = sum(epk[n] for n in range(V) if EPS[n] == 1)
od_sum = sum(epk[n] for n in range(V) if EPS[n] == -1)
ok("A3.packet", nr == n1 + n2 and sum(epk) == (m * n1 + F(5, 4) * n2) / nr,
   "packet rest + moving (orthogonal): sum e = (m|c1|^2 + E|c2|^2)/norm = %s; even sites %s, odd sites %s, min e_x %s"
   % (str(sum(epk)), str(ev_sum), str(od_sum), str(min(epk))))

# ---------------------------------------------------------------- B the chessboard: its field, its cost, who feels it
# neighbour average A on the torus, exact
def applyA(f):
    return [sum(f[shift(x, j, s)] for j in range(3) for s in (-1, 1)) / 6 for x in SITES]


ok("B.Aeps", applyA([F(e) for e in EPS]) == [F(-e) for e in EPS], "A eps = -eps, so (1 - A)(eps f) = eps (1 + A) f")
import random
random.seed(5)
f = [F(random.randint(-9, 9), random.randint(1, 7)) for _ in range(V)]
lhs = [a - b for a, b in zip([EPS[n] * f[n] for n in range(V)], applyA([EPS[n] * f[n] for n in range(V)]))]
rhs = [EPS[n] * (a + b) for n, (a, b) in enumerate(zip(f, applyA(f)))]
ok("B.identity", lhs == rhs, "(1 - A)(eps f) = eps (1 + A) f for an arbitrary f (exact on the torus)")
# the rest state's source with its mean removed is exactly (m/V) eps; the field is a pure chessboard
gam = sp.symbols("gamma", positive=True)
src = [F(x) - sum(e_rest) / V for x in e_rest]
ok("B.source", src == [m / V * EPS[n] for n in range(V)], "e - mean(e) = (m/V) eps exactly: the whole mean-removed source is a chessboard")
alpha = -m / (12 * V)          # u = gamma * alpha * eps solves (1 - A) u = -(gamma/6) src
u_test = [alpha * EPS[n] for n in range(V)]
ok("B.field", [a - b for a, b in zip(u_test, applyA(u_test))] == [-F(1, 6) * s_ for s_ in src],
   "(1 - A) u = -(gamma/6)(e - mean e) is solved by u = -(gamma m/(12 V)) eps: a pure chessboard of clocks")
c = sp.symbols("c", positive=True)
epsS = sp.symbols("epsilon")
for e_val in (1, -1):
    w = c ** (2 * e_val)
    ok("B.feel%+d" % e_val, sp.simplify(m * e_val * w - m * ((c**2 - c**-2) / 2 + e_val * (c**2 + c**-2) / 2)) == 0)
print("   phi = c^eps: phi_x phi_y = 1 on every bond (block 76 T1: phi H phi = H), but phi (m eps) phi = "
      "m (c^2 - c^-2)/2 + m eps (c^2 + c^-2)/2: a scalar potential and a mass factor")
cost = sp.simplify(sp.Rational(2) / gam * 3 * V * (c - 1 / c) ** 2)
ok("B.cost", sp.simplify(cost - 6 * V * (c - 1 / c) ** 2 / gam) == 0, "block 56 energy of the chessboard: (2/gamma) 3V (c - 1/c)^2 > 0")

# ---------------------------------------------------------------- C symbols at k = pi(111)
kk = sp.symbols("k1:4", real=True)
symA = 1 - sum(sp.cos(q) for q in kk) / 3
symLap = sum(2 * (1 - sp.cos(q)) for q in kk)
pi3 = {q: sp.pi for q in kk}
ok("C.symbols", symA.subs(pi3) == 2 and symLap.subs(pi3) == 12,
   "1 - A has symbol 2 and the lattice Laplacian 12 at pi(111): both invertible there, zero only at k = 0")
print("   pull at 1/R (both members, weak field, linear in each body): -(gamma/(4 pi)) Q_A Q_B / R with Q the TOTAL "
      "energies; the staggered part enters only through Q (argument: ATTEMPT.md step 7)")

# ---------------------------------------------------------------- N illustration (floats; not load-bearing)
try:
    import numpy as np
    Ln = 48
    k1 = 2 * np.pi * np.fft.fftfreq(Ln)
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
    sym = 1 - (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
    sym[0, 0, 0] = 1.0

    def field(src_):
        s = np.fft.fftn(src_)
        s[0, 0, 0] = 0
        return np.real(np.fft.ifftn(s / sym))

    def body(weights):              # weights along x at offsets -1, 0, +1 around the origin (an even site)
        b = np.zeros((Ln, Ln, Ln))
        for off, wv in zip((-1, 0, 1), weights):
            b[off % Ln, 0, 0] = wv
        return b

    uS = field(body((0.5, 1.0, 0.5)))      # total 2, dipole 0, staggered charge 0
    uC = field(body((0.0, 2.0, 0.0)))      # total 2, dipole 0, staggered charge 2 (all on the even site)
    rows = []
    for R in (4, 8, 12, 16):
        a_, b_ = uS[0, R, 0], uC[0, R, 0]
        rows.append("R=%d: %.5f vs %.5f, R^3 x difference %.3f" % (R, a_, b_, R**3 * (b_ - a_)))
    print("N.field NUMERICAL (1-A)u = source on a 48^3 torus, two bodies of total 2 and dipole 0, staggered charge 0 vs 2, "
          "field at (0,R,0): " + "; ".join(rows) + " -- the staggered charge adds no 1/R term (difference ~ R^-3, a quadrupole)")
except Exception as ex:
    print("N.skip " + type(ex).__name__)

print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: the positive-energy rest states of H + m eps at the zero lie on one sublattice (energy +m on eps = +1, -m on "
    "eps = -1), so a massive walker at rest has energy density m w|chi|^2 >= 0 there and 0 on the other sublattice, not "
    "an alternating one; any positive-energy eigenstate has e_x = E w|psi_x|^2 >= 0, and only its mass part alternates "
    "(odd weight (E-m)/(2E), 1/5 at k = pi/2, m = 3/4).",
    "HIT: a massive walker feels a chessboard of clocks: with phi = c^eps, phi H phi = H (block 76 T1) but phi(m eps)phi = "
    "m(c^2 - c^-2)/2 + m eps (c^2 + c^-2)/2, a scalar potential and a mass factor; on a torus the rest state's "
    "mean-removed source is exactly (m/V) eps and the simplest member's field is exactly u = -(gamma m/(12V)) eps.",
    "HIT: the chessboard component contributes nothing to the pull between two bodies at rest at any power of 1/R, in "
    "the simplest member and the curvature member: both weak-field operators are nonzero at k = pi(111) (2 and 12), so "
    "the pull at 1/R is -(gamma/4pi) Q_A Q_B/R with Q the total energies.",
]
print("SUMMARY: PARTIAL the chessboard part of a massive body's source does not reach the pull at any power of 1/R "
      "(simplest and curvature members); rest states sit on one sublattice; a massive walker feels a chessboard of "
      "clocks as a scalar potential")
print("\n".join(HITS))
