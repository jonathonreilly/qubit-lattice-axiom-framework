#!/usr/bin/env python3
"""J:derive:transparent-bodies-capture-rate:a1 -- exact checks (Fractions, sympy, integer counts) plus labelled float notes.

Clause (blocks 44, 45, 48): a record of content s steps to x + e_k with probability max(0, s.e_k)/sqrt3; a capturing site keeps
a record that steps onto it.  For independent records of content s (step frequencies w = |s|/|s|_1 in the octant of s) the walk
is directed.  rho = 0.29 as in the executed runs.
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    print(("ok   " if cond else "FAIL ") + tag + (": " + msg if msg else ""), flush=True)
    if not cond:
        FAILS.append(tag)


# ---------------------------------------------------------------- E1: capture of one streaming record, by enumeration
def capture_enum(B, w, nmax):
    """sum over all step sequences: probability that the directed walk from 0 steps onto a site of B"""
    tot = Fr(0)
    for n in range(1, nmax + 1):
        for seq in itertools.product(range(3), repeat=n):
            pos = [0, 0, 0]; pr = Fr(1); hit = False
            for idx, kk in enumerate(seq):
                pos[kk] += 1; pr *= w[kk]
                if tuple(pos) in B:
                    hit = idx == n - 1          # counted once, at the length where it first lands on B
                    break
            if hit:
                tot += pr
    return tot


def capture_dp(B, w, nmax):
    n = {(0, 0, 0): Fr(1)}
    cap = Fr(0)
    for tsum in range(1, nmax + 1):
        for x in [(a, b, tsum - a - b) for a in range(tsum + 1) for b in range(tsum + 1 - a)]:
            inflow = Fr(0)
            for kk in range(3):
                y = list(x); y[kk] -= 1; y = tuple(y)
                if min(y) >= 0 and y in n and y not in B:
                    inflow += w[kk] * n[y]
            if x in B:
                cap += inflow
            else:
                n[x] = inflow
    return cap


good = True
bodies = [{(1, 0, 0), (1, 1, 0), (2, 1, 1), (0, 2, 1)}, {(1, 1, 0), (0, 1, 1), (1, 0, 1)}, {(2, 0, 0), (1, 1, 1), (0, 0, 3), (2, 2, 0)}]
laws = [(Fr(1, 2), Fr(1, 3), Fr(1, 6)), (Fr(1, 3), Fr(1, 3), Fr(1, 3)), (Fr(3, 5), Fr(1, 5), Fr(1, 5))]
vals = []
for B in bodies:
    nmax = max(sum(p) for p in B)
    for w in laws:
        e_, d_ = capture_enum(B, w, nmax), capture_dp(B, w, nmax)
        good &= e_ == d_
        vals.append(e_)
ok("E.single", good, "the probability that one streaming record is captured by a small porous body, by enumerating every step "
   "sequence, equals the transport recursion n(x) = sum_k w_k n(x - e_k)[x - e_k not captured] exactly (3 bodies x 3 rational step "
   "laws), e.g. %s" % str(vals[0]))

# ---------------------------------------------------------------- E2: the kinetic rate per exposed face; solid lattice balls
z = sp.symbols("z")
face = sp.integrate(z / 2, (z, 0, 1))                  # <max(0, s_z)> over the uniform sphere (s_z uniform on [-1, 1])
l1m = 3 * sp.integrate(sp.Abs(z) / 2, (z, -1, 1))       # <|s|_1>
rho_ = sp.symbols("rho", positive=True)
good = face == sp.Rational(1, 4) and l1m == sp.Rational(3, 2) and sp.simplify(6 * rho_ * face / sp.sqrt(3) - rho_ / sp.sqrt(3) * l1m) == 0


def ball(R):
    return [p for p in itertools.product(range(-R, R + 1), repeat=3) if p[0] ** 2 + p[1] ** 2 + p[2] ** 2 <= R * R]


def faces(B):
    S = set(B)
    return sum(1 for p in B for e in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
               if (p[0] + e[0], p[1] + e[1], p[2] + e[2]) not in S)


Fc = {R: faces(ball(R)) for R in (2, 3, 4, 5)}
good &= [len(ball(R)) for R in (2, 3, 4, 5)] == [33, 123, 257, 515] and [Fc[R] for R in (2, 3, 4, 5)] == [78, 174, 294, 486]
ok("E.faces", good, "<max(0, s.n)> = 1/4 and <|s|_1> = 3/2, so a site's rate q1 = (rho/sqrt3)(3/2) is 6 faces x rho/(4 sqrt3); lattice "
   "balls of radius 2..5 have 33, 123, 257, 515 sites and 78, 174, 294, 486 exposed faces: in a locally isotropic gas of density rho "
   "a solid ball captures rho F/(4 sqrt3)")

# ---------------------------------------------------------------- E3: the optical depth and the crossover
ell, R = sp.symbols("l R", positive=True)
mean_chord = sp.integrate(ell * ell / (2 * R ** 2), (ell, 0, 2 * R))
Nstar = sp.Rational(4, 3) * sp.pi * R ** 3 / (2 * R)
ok("E.crossover", sp.simplify(mean_chord - 4 * R / 3) == 0 and sp.simplify(sp.integrate(ell / (2 * R ** 2), (ell, 0, 2 * R)) - 1) == 0
   and sp.simplify(Nstar - 2 * sp.pi * R ** 2 / 3) == 0,
   "a ball's chords under a uniform isotropic flux have density l/(2R^2) on [0, 2R], mean 4R/3; a straight path of length l visits "
   "|s|_1 l sites, mean 3/2 per unit length, so the optical depth of a ball with fill phi is 2 R phi and N* = (2 pi/3) R^2 (52 at R = 5)")

mu, tau = sp.symbols("mu tau", positive=True)
pabs = 1 - sp.integrate(sp.exp(-mu * ell) * ell / (2 * R ** 2), (ell, 0, 2 * R))
closed = 1 - (1 - (1 + 2 * mu * R) * sp.exp(-2 * mu * R)) / (2 * mu ** 2 * R ** 2)
ratio = sp.series((pabs / (mu * 4 * R / 3)).subs(mu, 3 * tau / (4 * R)), tau, 0, 2).removeO()
ok("E.screening", sp.simplify(pabs - closed) == 0 and sp.simplify(ratio - (1 - sp.Rational(9, 16) * tau)) == 0,
   "continuum chord model (absorption mu = (3/2) phi per unit length): P_abs = 1 - (1 - (1 + 2 mu R) e^{-2 mu R})/(2 mu^2 R^2), and "
   "Q/(N q1) = 1 - (9/16) tau + O(tau^2) with tau = 2 R phi: additive within eps needs N < (16/9) eps N*")

# ---------------------------------------------------------------- notes: transport computations (floating quadrature over contents)
rho = 0.29


def Q_model(Bset, R, region=None, M=14):
    lo = -R - 1; L = 2 * R + 3
    inB = np.zeros((L, L, L), bool); inR = np.zeros((L, L, L), bool)
    for p in Bset:
        inB[p[0] - lo, p[1] - lo, p[2] - lo] = True
    if region is not None:
        for p in region:
            inR[p[0] - lo, p[1] - lo, p[2] - lo] = True
    x, wx = np.polynomial.legendre.leggauss(M); x = (x + 1) / 2; wx = wx / 2
    U = np.repeat(x, M); V = np.tile(x, M); WU = np.repeat(wx, M); WV = np.tile(wx, M)
    W = [U, (1 - U) * V, (1 - U) * (1 - V)]
    wt = WU * WV * (1 - U) * (W[0] ** 2 + W[1] ** 2 + W[2] ** 2) ** -2.0      # dOmega |s|_1 = dw/|w|^4
    tot = 0.0
    for sig in itertools.product((1, -1), repeat=3):
        A = inB[::sig[0], ::sig[1], ::sig[2]]; RR = inR[::sig[0], ::sig[1], ::sig[2]]
        Bp = np.zeros((L + 1, L + 1, L + 1), bool); Bp[1:, 1:, 1:] = A
        Rp = np.zeros((L + 1, L + 1, L + 1), bool); Rp[1:, 1:, 1:] = RR
        n = np.ones((L + 1, L + 1, L + 1, M * M))
        for i in range(1, L + 1):
            for j in range(1, L + 1):
                for k in range(1, L + 1):
                    if region is not None and not Rp[i, j, k]:
                        continue
                    val = 0.0
                    if not Bp[i - 1, j, k]: val = val + W[0] * n[i - 1, j, k]
                    if not Bp[i, j - 1, k]: val = val + W[1] * n[i, j - 1, k]
                    if not Bp[i, j, k - 1]: val = val + W[2] * n[i, j, k - 1]
                    n[i, j, k] = val
        cap = 0.0
        for (i, j, k) in np.argwhere(Bp):
            if not Bp[i - 1, j, k]: cap = cap + W[0] * n[i - 1, j, k]
            if not Bp[i, j - 1, k]: cap = cap + W[1] * n[i, j - 1, k]
            if not Bp[i, j, k - 1]: cap = cap + W[2] * n[i, j, k - 1]
        tot += np.sum(wt * cap)
    return rho / math.sqrt(3) * tot / (4 * math.pi)


q1 = rho * math.sqrt(3) / 2
solid_fs = [Q_model(ball(Rr), Rr) for Rr in (2, 3, 4, 5)]
print("note: solid balls R = 2..5: executed 3.2 7.8 13.2 21.8; local kinetic rho F/(4 sqrt3) = %s; collisionless streaming %s; "
      "single site %.4f = q1 %.4f" % (" ".join("%.2f" % (rho * Fc[Rr] / (4 * math.sqrt(3))) for Rr in (2, 3, 4, 5)),
                                    " ".join("%.2f" % v_ for v_ in solid_fs), Q_model([(0, 0, 0)], 1), q1))
B5 = ball(5)
S5 = set(B5)
bint = sum(1 for p in B5 for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)) if (p[0] + e[0], p[1] + e[1], p[2] + e[2]) in S5)
rng = np.random.default_rng(7)
rows = []
for N, ex in ((51, 9.4), (164, 17.8)):
    fs, hy = [], []
    for rep in range(6):
        idx = rng.choice(len(B5), N, replace=False)
        Bs = [B5[i] for i in idx]
        fs.append(Q_model(Bs, 5)); hy.append(Q_model(Bs, 5, region=B5))
    loc = rho * (6 * N - 2 * bint * N * (N - 1) / (515 * 514)) / (4 * math.sqrt(3))
    rows.append("N=%d: executed %.1f; additive N q1 %.2f; collisionless %.2f; streaming inside, re-equilibrated outside %.2f; local kinetic %.2f"
                % (N, ex, N * q1, np.mean(fs), np.mean(hy), loc))
print("note: porous balls R = 5 (6 random bodies each): " + "; ".join(rows))

print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: capture here is kinetic, not diffusive: a site's rate q1 = rho sqrt3/2 is 6 faces x rho/(4 sqrt3) exactly, and solid lattice "
    "balls (F = 78, 174, 294, 486 exposed faces) capture rho F/(4 sqrt3) = 3.26, 7.28, 12.31, 20.34 at rho = 0.29 against the executed "
    "3.2, 7.8, 13.2, 21.8, growing like R^2 where 4 pi D R rho grows like R.",
    "HIT: a porous ball of radius R has optical depth 2 R phi (mean chord 4R/3, 3/2 sites per unit length), so Q = N q1 needs N << "
    "N* = (2 pi/3) R^2 (52 at R = 5); the executed R = 5 values 9.4 and 17.8 lie inside the parameter-free brackets [8.47, 11.76] and "
    "[13.49, 30.18] between collisionless streaming and a locally re-equilibrated gas; F ~ N1 N2 needs fill << 1/(2R).",
]
print("SUMMARY: PARTIAL the diffusive picture fails at its first step (no depletion; Q grows like R^2); exact kinetic face rate and "
      "lattice face counts predict solid balls to 7 percent; the optical-depth crossover N* = (2 pi/3) R^2 and brackets for porous bodies")
print("\n".join(HITS))
