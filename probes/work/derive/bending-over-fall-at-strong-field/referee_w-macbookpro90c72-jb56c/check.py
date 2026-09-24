#!/usr/bin/env python3
"""Referee for J:derive:bending-over-fall-at-strong-field:a2.

The one-body ratio and the capture radius are re-derived in sympy.
A straight-line integral is a numerical weighted mean, not the author's script.
"""
import sys

import numpy as np
import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


Q, g, g0, u, u0, w0 = sp.symbols("Q g g0 u u0 w0", positive=True)
# chi = 1 + Q g, N = 1 - P g, P = Q w0, l = chi^2, w = N/chi, c = w/l = N/chi^3
chi = 1 + Q * g
N = 1 - Q * w0 * g
w = N / chi
l = chi ** 2
c = sp.simplify(w / l)
ok("B1", sp.simplify(c - N / chi ** 3) == 0,
   "with l = chi^2 and w = N/chi, the ray speed is c = w/l = N/chi^3")

# Hamilton: H = c |k|. At kx = 0, x-double-dot = -c d c / dx
# Slow body E = w sqrt(m^2 + k^2/l^2). At k=0, x-double-dot = -(w/l)^2 d ln w / dx
# ratio of the coefficients of the common gradient:
ln_lw = sp.log(l / w)
ln_w = sp.log(w)
# d(ln)/dg
ray_g = sp.diff(ln_lw, g)
fall_g = -sp.diff(ln_w, g)
ratio = sp.simplify(ray_g / fall_g)
claimed = (2 + 3 * Q * g0 - Q * g) / (1 + Q * g0)
# substitute w0 = 1/(1+2 Q g0) and compare as a function of g
w0_of = 1 / (1 + 2 * Q * g0)
ratio_s = sp.simplify(ratio.subs(w0, w0_of))
claimed_s = sp.simplify(claimed)
ok("B2", sp.simplify(ratio_s - claimed_s) == 0,
   "the local ratio is (2 + 3 Q g0 - Q g)/(1 + Q g0) for any Green function")

second = sp.simplify(1 + 2 / (1 + w0 / w))
second_s = sp.simplify(second.subs(w0, w0_of))
ok("B3", sp.simplify(second_s - claimed_s) == 0,
   "the same ratio is 1 + 2/(1 + w0/w)")

at_body = sp.simplify(claimed.subs(g, g0))
at_far = sp.simplify(claimed.subs(g, 0))
far_block = sp.simplify(1 + (1 + 2 * Q * g0) / (1 + Q * g0))
w_body = sp.simplify(w.subs({g: g0, w0: w0_of}))
ok("B4", at_body == 2 and sp.simplify(at_far - far_block) == 0 and sp.simplify(w_body - w0_of) == 0,
   "exactly 2 at the body, block 60's far value at g=0, and w(g0)=w0")

# decreases in g, and far value is in (2, 3)
d_ratio = sp.simplify(sp.diff(claimed, g))
gap = sp.simplify(3 - at_far)
ok("B5", d_ratio < 0 and sp.simplify(gap - 1 / (1 + Q * g0)) == 0,
   "the ratio falls in g, and 3 minus the far value is 1/(1+Q g0) > 0, so it lies in [2, 3)")

# capture: n = (1+a/r)^3 / (1 - w0 a/r), stationarity of r n
a, r = sp.symbols("a r", positive=True)
n = (1 + a / r) ** 3 / (1 - w0 * a / r)
f = sp.simplify(r * n)
df = sp.together(sp.diff(f, r))
# numerator of df should vanish on r^2 - 2(1+w0) a r + w0 a^2
num = sp.numer(sp.together(df))
quad = r ** 2 - 2 * (1 + w0) * a * r + w0 * a ** 2
# the derivative numerator, cleared of positive factors, should be proportional to -quad or similar
# check both roots of the quadratic are critical points
r_big = a * (1 + w0 + sp.sqrt(w0 ** 2 + w0 + 1))
r_small = a * (1 + w0 - sp.sqrt(w0 ** 2 + w0 + 1))
ok("B6", sp.simplify(df.subs(r, r_big)) == 0 and sp.simplify(df.subs(r, r_small)) == 0
   and sp.simplify(r_big / a - (1 + w0 + sp.sqrt(w0 ** 2 + w0 + 1))) == 0,
   "r n(r) is stationary at r* = a (1 + w0 + sqrt(w0^2 + w0 + 1)), outside the other root")

# straight-line weighted mean for g = 1/sqrt(b^2+s^2), several strengths
def straight_ratio(u0, b):
    # u = Q g, u0 = Q g0. Use g shape with g(0) not 1; scale so max on the line is not g0.
    # The local formula depends only on Qg and Qg0. Take g = g0 / sqrt(1 + (s/b_phys)^2) along a miss.
    # Parameterize s from -L to L, g = g0 * b / sqrt(b^2 + s^2) with b>0 so g <= g0.
    s = np.linspace(-80, 80, 40001)
    g_line = b / np.sqrt(b ** 2 + s ** 2)  # in units Q=1, this is u, and u0 is the body value
    # body value u0, field along the line is u0 * b/sqrt... if b here is the impact in units of the scale where g0 corresponds.
    # Use u(s) = u0 * b / sqrt(b^2+s^2) <= u0.
    u = u0 * b / np.sqrt(b * b + s * s)
    # coefficients of du (the common factor |du| cancels in the ratio of integrals of the two accelerations)
    # ray density prop to (3/(1+u) + w0/(1-w0 u)) |du|
    # fall density prop to (1/(1+u) + w0/(1-w0 u)) |du|
    ww = 1 / (1 + 2 * u0)
    ray = 3 / (1 + u) + ww / (1 - ww * u)
    fall = 1 / (1 + u) + ww / (1 - ww * u)
    # du along the line is not uniform; weight by |du/ds|
    du = np.abs(np.gradient(u, s))
    Rloc = ray / fall
    integ = np.sum(Rloc * fall * du) / np.sum(fall * du)
    far = (2 + 3 * u0) / (1 + u0)
    return integ, far

samples = []
inside = True
for u0 in (0.5, 2.0, 7.58):
    for b in (3.0, 6.0, 12.0):
        integ, far = straight_ratio(u0, b)
        samples.append((u0, b, integ, far))
        inside &= 2 <= integ <= far + 1e-6 and far < 3
ok("B7", inside, "straight-line ratios at Qg0 in {0.5, 2, 7.58} and b in {3, 6, 12} lie in [2, far) subset [2, 3): "
   + ", ".join(f"{v[2]:.3f}" for v in samples))

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - the pointwise bending-over-fall ratio is (2+3Qg0-Qg)/(1+Qg0) in [2, 3) for every Green function, and the continuum index captures at r* = a(1+w0+sqrt(w0^2+w0+1)).")
print("HIT: confirmed - in block 60's one-body field the ray acceleration over a slow body's fall is 1+2/(1+w0/w), exactly 2 at the body and block 60's far value at infinity, hence in [2, 3) at every point and along every straight line; the nonlinear index n=(1+a/r)^3/(1-w0 a/r) has capture radius r*=a(1+w0+sqrt(w0^2+w0+1)), so path-integrated deflection can exceed any bound while the local ratio stays in [2, 3).")
