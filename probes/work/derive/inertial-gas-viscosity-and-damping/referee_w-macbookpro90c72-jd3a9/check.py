#!/usr/bin/env python3
"""Independent referee of inertial-gas viscosity, attempt a2.

Author w-macbookpro90c72-jd030 (claude-opus-5-5). Referee w-macbookpro90c72-jd3a9 (grok-4.6).
Own class matrix and own moments. The Galerkin truncation and the tick simulations were not rebuilt.
"""
import itertools
from fractions import Fraction as F

import numpy as np
import sympy as sp

FAILS = []


def require(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


D6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def pair_index(a, b):
    return 6 * a + b


# redraw uniformly inside the total-momentum class
classes = {}
for a, b in itertools.product(range(6), repeat=2):
    mom = tuple(x + y for x, y in zip(D6[a], D6[b]))
    classes.setdefault(mom, []).append(pair_index(a, b))

T = [[F(0) for _ in range(36)] for _ in range(36)]
for members in classes.values():
    w = F(1, len(members))
    for i in members:
        for j in members:
            T[i][j] = w

sizes = sorted(len(v) for v in classes.values())
symmetric = all(T[i][j] == T[j][i] for i in range(36) for j in range(36))
stochastic = all(sum(row) == 1 for row in T)
# T^2 = T because each class is already uniform
square = True
for i in range(36):
    for j in range(36):
        s = sum(T[i][k] * T[k][j] for k in range(36))
        if s != T[i][j]:
            square = False
            break
# rank: one indicator per class, and they are independent
rank = len(classes)
require(symmetric and stochastic and square and rank == 19 and sizes.count(1) == 6 and sizes.count(2) == 12 and sizes.count(6) == 1,
        f"redraw T is the projector on 19 momentum classes (sizes {sizes.count(1)} singletons, {sizes.count(2)} pairs, one class of 6)")
# generator gamma(T-I) squares to -gamma times itself on the complement, so the isolated-pair
# semigroup is exactly I + (1 - e^{-gamma t})(T - I) and saturates at T
nil = True
for i in range(36):
    for j in range(36):
        # (T-I)^2 = T^2 - 2T + I = I - T = -(T - I)
        s = sum((T[i][k] - (1 if i == k else 0)) * (T[k][j] - (1 if k == j else 0)) for k in range(36))
        if s != -(T[i][j] - (1 if i == j else 0)):
            nil = False
require(nil, " (T-I)^2 = -(T-I), so a second redraw of an isolated pair does nothing beyond the first")

# marginals: U[c,a] sums the site's post content, V the partner's
U = [[F(0) for _ in range(6)] for _ in range(6)]
V = [[F(0) for _ in range(6)] for _ in range(6)]
for a, b, c, d in itertools.product(range(6), repeat=4):
    w = T[pair_index(a, b)][pair_index(c, d)]
    U[c][a] += w
    V[c][b] += w
require(U == V, "the site and the partner have the same one-site marginal")

Us = sp.Matrix([[sp.Rational(U[i][j].numerator, U[i][j].denominator) for j in range(6)] for i in range(6)])
gam, rho = sp.symbols("gamma rho", positive=True)
C0 = gam * rho * (Us + Us - 6 * sp.eye(6) - sp.ones(6))
ev = C0.eigenvals()
require(ev.get(0) == 4 and ev.get(-2 * gam * rho) == 2, f"k=0 collision eigenvalues {ev}")
ones = sp.ones(6, 1)
mom_ok = C0 * ones == sp.zeros(6, 1)
for axis in range(3):
    vec = sp.Matrix([D6[d][axis] for d in range(6)])
    mom_ok = mom_ok and sp.simplify(C0 * vec) == sp.zeros(6, 1)
quad = sp.Matrix([2, 2, -1, -1, -1, -1])
mom_ok = mom_ok and sp.simplify(C0 * quad + 2 * gam * rho * quad) == sp.zeros(6, 1)
# retention: average over a uniform partner is U/6
px = sp.Matrix([D6[d][0] for d in range(6)])
retain_p = sp.simplify((Us * px)[0] / 6)
retain_q = sp.simplify((Us * quad)[0] / quad[0] / 6)
require(mom_ok and retain_p == sp.Rational(1, 2) and retain_q == sp.Rational(1, 3),
        "density and three momenta are conserved; the axis quadrupole decays at 2 gamma rho; one collision retains 1/2 of the momentum and 1/3 of the quadrupole")

# Gamma and its minimum
g = sp.symbols("g", positive=True)
Gamma = sp.Rational(2, 3) + rho / 6 + g * rho / 2 + 1 / (3 * g * rho)
dG = sp.diff(Gamma, g)
crit = sp.solve(sp.numer(sp.together(dG)), g)
require(len(crit) == 1 and sp.simplify(crit[0] * rho - sp.sqrt(sp.Rational(2, 3))) == 0,
        "six-axis Gamma is minimized at gamma rho = sqrt(2/3)")
require(sp.diff(Gamma, g, 2).subs(g, crit[0]) > 0, "that critical point is a minimum")

# shear eigenvalue from the displayed closure, k along x, transverse (y up minus y down)
k = sp.symbols("k", real=True)
cosk = sp.cos(k)
ph = [sp.exp(-sp.I * k * D6[d][0]) for d in range(6)]
S = sp.zeros(6)
for c in range(6):
    for c2 in range(6):
        S[c, c2] = (rho / 6) * (1 - ph[c2])
    S[c, c] += (ph[c] - 1) + (rho / 6) * (2 * cosk + 4 - 6)
two = 2 * cosk + 4
C = g * (rho / 6) * (6 * Us + two * Us - 36 * sp.eye(6) - two * sp.ones(6))
ty = sp.Matrix([0, 0, 1, -1, 0, 0])
shear = sp.simplify((S + C) * ty)
expect = -(1 - cosk) * rho * (sp.Rational(1, 3) + g) * ty
require(sp.simplify(shear - expect) == sp.zeros(6, 1),
        "transverse shear eigenvalue is exactly -(1-cos k) rho (1/3 + gamma), so nu_T = rho/6 + gamma rho/2")

# sphere moments
u = sp.symbols("u", real=True)
avg = lambda f: sp.integrate(f, (u, -1, 1)) / 2
moms = [sp.simplify(avg(f)) for f in (u**2, u**4, sp.Abs(u), sp.Abs(u) ** 3, sp.Abs(u) * (1 - u**2) / 2, u**2 * (1 - u**2) / 2)]
require(moms[:5] == [sp.Rational(1, 3), sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 8)],
        f"sphere moments <sx^2>, <sx^4>, <|sx|>, <|sx|^3>, <|sx| sy^2> = {moms[:5]}")
require(sp.simplify(moms[5] / (sp.Rational(1, 3)) - sp.Rational(1, 5)) == 0 or moms[5] == sp.Rational(1, 15),
        f"<sx^2 sy^2>/<sy^2> = {moms[5]} / (1/3)")

# the chains quoted in the attempt
chain = sp.simplify((1 / sp.sqrt(3)) * (sp.Rational(4, 15) / sp.sqrt(3)) / (3 * g * rho))
require(chain == sp.Rational(4, 135) / (g * rho), "longitudinal kinetic viscosity 4/(135 gamma rho)")
require(sp.simplify(sp.Rational(1, 4) * 3 / (2 * sp.sqrt(3)) - 3 / (8 * sp.sqrt(3))) == 0, "hop-noise piece 3/(8 sqrt 3)")
require(sp.simplify(sp.Rational(1, 2) / (2 * sp.sqrt(3)) - 1 / (4 * sp.sqrt(3))) == 0, "density diffusion 1/(4 sqrt 3)")
require(sp.simplify(sp.Rational(1, 8) * 3 / (2 * sp.sqrt(3)) - sp.sqrt(3) / 16) == 0, "shear streaming piece sqrt(3)/16")
require(sp.Rational(1, 5) / (9 * g * rho) == 1 / (45 * g * rho), "projecting the l=2 return gives 1/(45 gamma rho)")

# closure dampings at rho=0.3, gamma=1, from (Gamma/2) k^2
rho0 = F(3, 10)
G6 = F(2, 3) + rho0 / 6 + rho0 / 2 + 1 / (3 * rho0)
Gs = (F(5, 8) + rho0 / 4) / sp.sqrt(3) + rho0 / 2 + F(4, 135) / rho0
pi2 = np.pi ** 2
d64 = float(G6) / 2 * pi2 / 1024
d32 = 4 * d64
ds64 = complex(Gs).real / 2 * pi2 / 1024
require(abs(d64 - 0.00965) < 2e-4 and abs(d32 - 0.0386) < 1e-3, f"six-axis (Gamma/2)k^2 is {d64:.4f} and {d32:.4f}")
require(abs(ds64 - 0.00315) < 2e-4, f"sphere (Gamma_s/2)k^2 at wavelength 64 is {ds64:.4f}")

# tick replacement gamma -> 1-e^{-gamma}, and 1/lambda -> 1/lambda - 1/2
gp = 1 - np.exp(-1)
Gtick = F(2, 3) + rho0 / 6 + F(gp).limit_denominator(10**8) * rho0 / 2 + 1 / (3 * F(gp).limit_denominator(10**8) * rho0) - F(1, 3)
# use floats for the exp
Gtick_f = 2 / 3 + 0.3 / 6 + gp * 0.3 / 2 + 1 / (3 * gp * 0.3) - 1 / 3
dt64 = Gtick_f / 2 * pi2 / 1024
require(abs(dt64 - 0.0109) < 2e-4 and abs(4 * dt64 - 0.0436) < 2e-3,
        f"tick-map six-axis damping from the k^2 formula is {dt64:.4f}, {4*dt64:.4f}")

print(f"TOTAL FAIL={len(FAILS)}", flush=True)
if FAILS:
    print("SUMMARY: fails at the first broken finite claim - " + FAILS[0], flush=True)
else:
    print("HIT: confirmed - the product closure gives Gamma = 2/3 + rho/6 + gamma rho/2 + 1/(3 gamma rho) on six axes, and an isolated pair saturates after one redraw", flush=True)
    print("SUMMARY: confirmed - T is the class projector, the quadrupole rate is 2 gamma rho, shear has no 1/(gamma rho) piece, and Gamma is minimized at gamma rho = sqrt(2/3). Simulations were not rebuilt.", flush=True)
