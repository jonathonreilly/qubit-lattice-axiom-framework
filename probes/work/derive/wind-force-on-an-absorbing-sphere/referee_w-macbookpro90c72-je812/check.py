#!/usr/bin/env python3
"""Referee for J:derive:wind-force-on-an-absorbing-sphere:a4.

The circle geometry and the Legendre moments are recomputed. The author's
script is not called, and the flow past the sphere is not claimed.
"""
import sys

import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


# ---------- K1. the class is a circle, and the two arguments of P_l coincide ----------
s1, s2 = sp.symbols("s1:4"), sp.symbols("t1:4")
# Use scalar t = s1·s2 with |s1|=|s2|=1
t = sp.symbols("t", real=True)
P2 = 2 + 2 * t
half = sp.simplify(sp.sqrt(P2) / 2)
uhat = sp.simplify((1 + t) / sp.sqrt(P2))
u = sp.sqrt((1 + t) / 2)
ok("K1", sp.simplify(half - u) == 0 and sp.simplify(uhat - u) == 0,
   "|P|/2 = P-hat · s1 = sqrt((1+t)/2); P-s is the opposite point of the same circle")

# change of variables: 2 E_t[P_l(u)^2] = 4 int_0^1 u P_l(u)^2 du
uvar = sp.symbols("u", positive=True)
# E_t[f(u(t))] = (1/2) int_{-1}^1 f dt, t=2u^2-1, dt=4u du
# so E = (1/2) int_0^1 f * 4 u du = 2 int u f du, and mu = 2 E = 4 int u f du


def c_k(k):
    if k == 0:
        return sp.Integer(1)
    num = sp.prod(range(1, 2 * k, 2))  # 1*3*...*(2k-1)
    den = sp.prod(range(2, 2 * k + 1, 2))  # 2*4*...*2k
    return sp.Rational(num, den)


def mu_closed(l):
    return 2 * c_k(l // 2) * c_k((l + 1) // 2)


def mu_int(l):
    x = sp.symbols("x")
    Pl = sp.legendre(l, x)
    return sp.simplify(4 * sp.integrate(x * Pl ** 2, (x, 0, 1)))


want = {
    1: 1,
    2: sp.Rational(1, 2),
    3: sp.Rational(3, 8),
    4: sp.Rational(9, 32),
    5: sp.Rational(15, 64),
    6: sp.Rational(25, 128),
    7: sp.Rational(175, 1024),
    8: sp.Rational(1225, 8192),
}
spec = True
for l, val in want.items():
    got_i = mu_int(l)
    got_c = sp.simplify(mu_closed(l))
    spec &= got_i == val and got_c == val
# the closed form through l=12, which is as far as the attempt checked
for l in range(9, 13):
    spec &= mu_int(l) == sp.simplify(mu_closed(l))
ok("K2", spec, "mu_l = 4 int_0^1 u P_l(u)^2 du equals 2 c_floor(l/2) c_ceil(l/2) for l=1..12, with the eight printed values")

# rates in the product closure: 6 gamma rho (1-mu)
g, rho = sp.symbols("gamma rho", positive=True)
rates = {
    2: 3 * g * rho,
    3: sp.Rational(15, 4) * g * rho,
    4: sp.Rational(69, 16) * g * rho,
}
rate_ok = all(sp.simplify(6 * g * rho * (1 - want[l]) - rates[l]) == 0 for l in rates)
ok("K3", rate_ok and want[1] == 1 and want[2] == sp.Rational(1, 2),
   "momentum is conserved, the stress is halved, and it relaxes at 3 gamma rho; l=3,4 at 15 gamma rho/4 and 69 gamma rho/16")

# independent quadrupole contractions
a, b = sp.symbols("a b")
eq1 = sp.Eq(9 * a + 6 * b, 2)
eq2 = sp.Eq(3 * a + 12 * b, 1)
sol = sp.solve([eq1, eq2], [a, b])
# E_t[(1+t)^2/2 + (1-t)^2/4] = 1
tt = sp.symbols("tt")
expect = sp.simplify(sp.integrate(((1 + tt) ** 2 / 2 + (1 - tt) ** 2 / 4), (tt, -1, 1)) / 2)
# incoming 4/15 versus outgoing 4b: ratio 15 b
ratio = sp.simplify(sp.Rational(15) * sol[b])
ok("K4", sol[a] == sp.Rational(1, 5) and sol[b] == sp.Rational(1, 30) and expect == 1 and ratio == sp.Rational(1, 2),
   "the isotropic contractions give a=1/5, b=1/30, and a traceless quadrupole is halved")

# large-l approach to 4/(pi l), by Gauss quadrature of the exact integral
import numpy as np

def mu_num(l):
    # int_0^1 4 u P^2 du via Legendre-Gauss on [0,1]
    n = max(2 * l + 4, 32)
    xs, ws = np.polynomial.legendre.leggauss(n)
    # map [-1,1] -> [0,1]
    us = 0.5 * (xs + 1)
    wus = 0.5 * ws
    Pl = np.polynomial.legendre.legval(us, [0] * l + [1])
    return float(np.sum(wus * 4 * us * Pl ** 2))

asym = True
for l in (40, 80, 160):
    got = l * mu_num(l)
    asym &= abs(got - 4 / np.pi) < 0.02 and abs(got - 4 / np.pi) < abs((l // 2) * mu_num(l // 2) - 4 / np.pi)
ok("K5", asym, "l mu_l approaches 4/pi: " + ", ".join(f"{l}:{l * mu_num(l):.4f}" for l in (40, 80, 160)))

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - clause (C) multiplies a degree-l harmonic by mu_l = 4 int_0^1 u P_l^2 du, with mu_1=1 and mu_2=1/2, so the stress relaxes at 3 gamma rho.")
print("HIT: confirmed - the re-draw is uniform on the circle |s|=1, s·P=|P|^2/2; mu_l = 2 c_floor(l/2) c_ceil(l/2) equals 1, 1/2, 3/8, 9/32, 15/64, 25/128, 175/1024, 1225/8192 for l=1..8 and ~4/(pi l); in the product closure the stress rate is 3 gamma rho. The flow past the sphere is not part of this result.")
