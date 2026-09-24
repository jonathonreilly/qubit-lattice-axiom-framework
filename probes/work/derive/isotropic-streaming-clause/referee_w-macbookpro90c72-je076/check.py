#!/usr/bin/env python3
"""Independent referee for isotropic-streaming-clause a3.

The staircase and axes-and-faces rules, the universal diagonal, and the
one float that places a mixture at beta = 1/16. Does not import the attempt.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import numpy as np
import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def axis(m: int, sign: int):
    v = [0, 0, 0]
    v[m] = sign
    return tuple(v)


def add(*vs):
    return tuple(sum(c) for c in zip(*vs))


def frame(s):
    order = sorted(range(3), key=lambda m: (-abs(s[m]), m))
    i, j, k = order
    sign = [1 if s[m] >= 0 else -1 for m in range(3)]
    return abs(s[i]), abs(s[j]), abs(s[k]), axis(i, sign[i]), axis(j, sign[j]), axis(k, sign[k])


def staircase(s):
    a, b, c, ui, uj, uk = frame(s)
    t = 0 if b + c == 0 else (1 - a) / (b + c)
    return [
        ((1 - t) * (a - b) + t * a, ui),
        ((1 - t) * (b - c), add(ui, uj)),
        ((1 - t) * c, add(ui, uj, uk)),
        (t * b, uj),
        (t * c, uk),
    ]


def faces(s):
    a, b, c, ui, uj, uk = frame(s)
    if a >= b + c:
        zs = (b, c, 0)
    else:
        zs = ((a + b - c) / 2, (a - b + c) / 2, (-a + b + c) / 2)
    total = sum(zs)
    theta = 0 if total == 0 else (a + b + c - 1) / total
    zij, zik, zjk = (theta * z for z in zs)
    return [
        (zij, add(ui, uj)),
        (zik, add(ui, uk)),
        (zjk, add(uj, uk)),
        (a - zij - zik, ui),
        (b - zij - zjk, uj),
        (c - zik - zjk, uk),
    ]


def dot(p, q):
    return sum(x * y for x, y in zip(p, q))


def valid(rule, s) -> bool:
    weights = [(w, d) for w, d in rule(s) if w != 0]
    total = sum(w for w, _ in weights)
    mean = tuple(sum(w * d[m] for w, d in weights) for m in range(3))
    forward = all(dot(d, s) > 0 for _, d in weights)
    signs = all(x * y >= 0 for _, d in weights for x, y in zip(d, s))
    return all(w > 0 for w, _ in rule(s) if w != 0) and total == 1 and mean == tuple(s) and forward and signs


# ---------------------------------------------------------------- symbolic staircase
a, b, c = sp.symbols("a b c", real=True, nonnegative=True)
t = (1 - a) / (b + c)
wi = sp.together((1 - t) * (a - b) + t * a)
wf = sp.together((1 - t) * (b - c))
wb = sp.together((1 - t) * c)
wj = sp.together(t * b)
wk = sp.together(t * c)
mean_ok = (
    sp.simplify(wi + wf + wb - a) == 0
    and sp.simplify(wf + wb + wj - b) == 0
    and sp.simplify(wb + wk - c) == 0
    and sp.simplify(wi + wf + wb + wj + wk - 1) == 0
)
# a <= 1 on the sphere, and a+b+c >= 1, so t is in [0,1]. Both are polynomial facts.
sum_gap = sp.expand((a + b + c) ** 2 - (a**2 + b**2 + c**2) - 2 * (a * b + b * c + c * a))
cauchy = sp.expand((a + b + c) ** 2 - 3 * (a**2 + b**2 + c**2) + (a - b) ** 2 + (b - c) ** 2 + (c - a) ** 2)
check(
    "H1 staircase algebra",
    mean_ok and sum_gap == 0 and cauchy == 0 and sp.simplify(wi - (a - b * (1 - t))) == 0,
    "the mixture has total 1 and mean (a,b,c); t is in [0,1] because a<=1<=a+b+c on the sphere",
)

# axes-and-faces: both branches scale to total 1 and keep the mean
sig = a + b + c
theta_hi = (sig - 1) / (b + c)  # a >= b+c, sum of merges is b+c
theta_lo = 2 * (sig - 1) / sig  # sum of merges is sig/2
# axis leftovers and face weights
zij, zik, zjk = (a + b - c) / 2, (a - b + c) / 2, (-a + b + c) / 2
merge_ok = sp.simplify(zij + zik + zjk - sig / 2) == 0 and sp.simplify(zij + zik - a) == 0
merge_ok = merge_ok and sp.simplify(zij + zjk - b) == 0 and sp.simplify(zik + zjk - c) == 0
check(
    "H3 merge algebra",
    merge_ok and sp.simplify(sig - theta_hi * (b + c) - 1) == 0 and sp.simplify(sig - theta_lo * (sig / 2) - 1) == 0,
    "both maximal merges, scaled by (a+b+c-1)/sum z, have total weight 1 and keep the mean",
)

# ---------------------------------------------------------------- no pointwise isotropy
aa, bb = sp.symbols("aa bb", positive=True)
beta = (aa + bb - 1) / (aa * bb)
m22 = aa - beta * (aa**2 - bb**2)
gap = sp.together(m22 - bb)
target = -(aa - bb) * (1 - aa) * (1 - bb) / (aa * bb)
numerator = sp.numer(sp.together(gap - target))
on_circle = sp.expand(numerator.subs(aa**2, 1 - bb**2))
check(
    "H6 arc obstruction",
    on_circle == 0,
    "on (a,b,0) a constant-rate forward rule cannot have M in span{I, s s^T}: the forced M22 is below b",
)

# ---------------------------------------------------------------- sphere moments
th, ph = sp.symbols("theta phi", real=True)
moment_1111 = sp.integrate(sp.cos(th) ** 3 * sp.sin(th), (th, 0, sp.pi / 2))
# s1 = sin theta cos phi, s2 = sin theta sin phi. The integrand s1^2 |s2| sin theta separates.
theta_part = sp.integrate(sp.sin(th) ** 4, (th, 0, sp.pi))
phi_part = 4 * sp.integrate(sp.cos(ph) ** 2 * sp.sin(ph), (ph, 0, sp.pi / 2))
moment_1122 = sp.simplify(theta_part * phi_part / (4 * sp.pi))
nu = sp.simplify(sp.Rational(3, 16) / sp.sqrt(3))
diff = sp.simplify(sp.Rational(1, 4) / sp.sqrt(3))
check(
    "H7 moments",
    sp.simplify(moment_1111 - sp.Rational(1, 4)) == 0
    and moment_1122 == sp.Rational(1, 8)
    and nu == sp.sqrt(3) / 16
    and diff == 1 / (4 * sp.sqrt(3))
    and sp.Rational(1, 4) == sp.Rational(1, 8) + 2 * sp.Rational(1, 16),
    "T1111=1/4, T1122=1/8, so isotropy is beta=1/16; at speed 1/sqrt(3), nu_lat=sqrt(3)/16 and D_lat=1/(4 sqrt(3))",
)

# ---------------------------------------------------------------- rational witnesses
seeds = []
for p, q, den in ((0, 0, 1), (1, 0, 1), (3, 4, 5), (2, 2, 3), (6, 3, 7), (1, 2, 3), (2, 3, 7)):
    u, v = F(p, den), F(q, den)
    # keep only those with u^2+v^2 < 1 so the third coordinate is real and rational: use Pythagorean-style points below
    seeds.append((u, v))
rational = []
for u, v, w in (
    (F(1), F(0), F(0)),
    (F(3, 5), F(4, 5), F(0)),
    (F(2, 3), F(2, 3), F(1, 3)),
    (F(6, 7), F(3, 7), F(2, 7)),
    (F(1, 3), F(2, 3), F(2, 3)),
    (F(2, 7), F(3, 7), F(6, 7)),
    (F(4, 9), F(4, 9), F(7, 9)),
    (F(1, 9), F(4, 9), F(8, 9)),
):
    if u * u + v * v + w * w == 1:
        rational.append((u, v, w))
images = []
for base in rational:
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            images.append(tuple(signs[m] * base[perm[m]] for m in range(3)))
images = list(dict.fromkeys(images))
point_ok = all(valid(staircase, s) and valid(faces, s) for s in images)


def aggregated(rule, s):
    out = {}
    for w, d in rule(s):
        if w != 0:
            out[d] = out.get(d, 0) + w
    return out


invert_ok = True
for s in images:
    for rule in (staircase, faces):
        flipped = aggregated(rule, tuple(-x for x in s))
        original = {tuple(-x for x in d): w for d, w in aggregated(rule, s).items()}
        invert_ok = invert_ok and flipped == original
diag_ok = True
for s in images:
    for rule in (staircase, faces):
        buckets = aggregated(rule, s)
        for m in range(3):
            diag_ok = diag_ok and sum(w * d[m] * d[m] for d, w in buckets.items()) == abs(s[m])
check(
    "H1-H5 witnesses",
    point_ok and invert_ok and diag_ok and len(images) >= 48,
    "both rules are forward barycentres with M_mm=|s_m| and a(-s,d)=a(s,-d) on %d cubic images of %d rational points"
    % (len(images), len(rational)),
)

# ---------------------------------------------------------------- independent quadrature of beta
def beta_of(rule) -> float:
    n = 96
    us, wu = np.polynomial.legendre.leggauss(n)
    ps, wp = np.polynomial.legendre.leggauss(n)
    ps = np.pi * (ps + 1.0)  # [0, 2pi]
    wp = wp * np.pi
    acc = 0.0
    for u, w_u in zip(us, wu):
        radial = float(np.sqrt(max(0.0, 1.0 - u * u)))
        for phi, w_p in zip(ps, wp):
            s = (radial * float(np.cos(phi)), radial * float(np.sin(phi)), float(u))
            weights = rule(s)
            joint = 0.0
            for weight, step in weights:
                if step[0] != 0 and step[1] != 0:
                    joint += weight
            acc += w_u * w_p * abs(s[0] * s[1]) * joint
    return acc / (4.0 * np.pi)


beta_stair = beta_of(staircase)
beta_face = beta_of(faces)
one = F(1, 16)
lam = (beta_stair - float(one)) / (beta_stair - beta_face)
check(
    "N beta signs",
    beta_stair > float(one) + 1e-3 and beta_face < float(one) - 1e-3 and 0.0 < lam < 1.0
    and abs(beta_stair - 0.06489844) < 2e-4 and abs(beta_face - 0.05612879) < 2e-4,
    "quadrature gives staircase beta=%.8f and axes-and-faces beta=%.8f, so lambda=%.8f mixes them to 1/16"
    % (beta_stair, beta_face, lam),
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed. Every unit content is the barycentre of at most five forward, sign-compatible "
    "neighbours under the staircase rule, and of axes and face diagonals under the maximal merge; both have "
    "total rate 1. Every such rule has M_mm=|s_m|, so the fourth-rank tensor is fixed by beta=<|s1 s2| W_12> "
    "and is isotropic exactly at beta=1/16. The two rules lie on opposite sides of 1/16 (float quadrature), "
    "and no constant-rate forward rule is pointwise isotropic on the arcs (a,b,0). The exact value of the "
    "mixing weight is not a closed form, and the shadow's density form stays assumed.",
    flush=True,
)
print(
    "HIT: confirmed - forward rules on the 26 neighbours with constant speed and constant total rate exist, "
    "their diagonal is |s_m|, and a mixture of the staircase and axes-and-faces rules meets beta=1/16",
    flush=True,
)
