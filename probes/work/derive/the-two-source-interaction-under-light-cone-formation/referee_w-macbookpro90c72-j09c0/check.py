#!/usr/bin/env python3
"""Referee for J:derive:the-two-source-interaction-under-light-cone-formation:a2.

The doubled ring is enumerated again. Weights are t = e^beta on each new record
against the three records below it, and each held source sits on both levels.
The author's script is not called.
"""
import itertools
import sys

import sympy as sp

FAILS = []
t, v, u1, u2, w = sp.symbols("t v u1 u2 w", positive=True)


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


def configs(L):
    return list(itertools.product((1, -1), repeat=L))


def weight(s, sn, x1, x2):
    """Boltzmann weight of two consecutive levels. Sources act on both."""
    L = len(s)
    acc = 1
    for x in range(L):
        below = sum(s[(x + d) % L] for d in (-1, 0, 1))
        acc *= t ** (sn[x] * below)
    acc *= v ** (sum(s) + sum(sn))
    acc *= u1 ** (s[x1] + sn[x1]) * u2 ** (s[x2] + sn[x2])
    return acc


def kernel(s, x1, x2):
    """Unnormalized conditional weight of one new spin, as a function of the past."""
    L = len(s)
    out = []
    for x in range(L):
        below = sum(s[(x + d) % L] for d in (-1, 0, 1))
        eh = t ** below * v
        if x == x1:
            eh *= u1
        if x == x2:
            eh *= u2
        out.append(eh)
    return out


L = 4
conf = configs(L)
x1, x2 = 0, 1
# detailed balance: pi(s) P(sn|s) = pi(sn) P(s|sn), with pi the marginal
db = True
for s in conf:
    eh_s = kernel(s, x1, x2)
    den = sp.prod([eh + 1 / eh for eh in eh_s])
    pi_s = v ** sum(s) * u1 ** s[x1] * u2 ** s[x2] * den
    for sn in conf:
        num = sp.prod([(eh if bit == 1 else 1 / eh) for eh, bit in zip(eh_s, sn)])
        if sp.cancel(pi_s * (num / den) - weight(s, sn, x1, x2)) != 0:
            db = False
            break
    if not db:
        break
ok("R1", db, "on the ring of 4, pi(s) P(sn|s) equals the doubled weight for every pair of levels")

# marginal: sum_sn mu(s, sn) = pi(s)
marg = True
for s in conf:
    total = sum(weight(s, sn, x1, x2) for sn in conf)
    den = sp.prod([eh + 1 / eh for eh in kernel(s, x1, x2)])
    pi_s = v ** sum(s) * u1 ** s[x1] * u2 ** s[x2] * den
    if sp.cancel(total - pi_s) != 0:
        marg = False
        break
ok("R2", marg, "the level marginal of the doubled ferromagnet is the stationary weight, sources on both vertices")

at0 = {u1: 1, u2: 1, v: 1}
Z = sum(weight(s, sn, x1, x2) for s in conf for sn in conf)
Z0 = sp.expand(Z.subs(at0))


def sig(s, sn, x):
    return s[x] + sn[x]


corr = sp.cancel(sum(weight(s, sn, x1, x2).subs(at0) * sig(s, sn, x1) * sig(s, sn, x2) for s in conf for sn in conf) / Z0)
# d/dh = beta u d/du, so (1/beta^2) d^2 log Z / dh1 dh2 = u1 u2 d^2 log Z / du1 du2 at u=1, plus no first-derivative term if mean spin is 0
lZ = sp.log(Z)
cross = sp.cancel((u1 * sp.diff(u2 * sp.diff(lZ, u2), u1)).subs(at0))
# mean of sigma vanishes at zero field
mean1 = sp.cancel(sum(weight(s, sn, x1, x2).subs(at0) * sig(s, sn, x1) for s in conf for sn in conf) / Z0)
ok("R3", mean1 == 0 and sp.cancel(cross - corr) == 0,
   f"at zero field the cross derivative of log Z is beta^2 <sigma_1 sigma_2> = {sp.factor(corr)}")

# Fourier kernel: Rhat/beta = 2 N^{-1} <|S|^2>, S = sigma/2, and R(r)/beta = N^{-1} sum e^{ikr} Rhat/beta
Rhat = []
for n in range(L):
    phase = sp.exp(2 * sp.pi * sp.I * n / L)
    acc = 0
    for s in conf:
        for sn in conf:
            S = sum(phase ** (-x) * sig(s, sn, x) for x in range(L)) / 2
            acc += weight(s, sn, x1, x2).subs(at0) * sp.expand(S * sp.conjugate(S))
    Rhat.append(sp.simplify(2 * acc / (L * Z0)))
R = lambda r: sp.simplify(sum(sp.exp(2 * sp.pi * sp.I * n * r / L) * Rhat[n] for n in range(L)) / L)
modes = [sp.simplify(z.subs(t, 2)) for z in Rhat]
ok("R4", all(sp.re(m) >= 0 and sp.im(m) == 0 for m in modes) and sp.simplify(corr - 2 * R(x2 - x1)) == 0,
   "the cross term is 2 beta R(x2-x1); at t=2 every Fourier mode of Rhat is nonnegative")

# third order vanishes; alignment is symmetric
D = lambda f, var: var * sp.diff(f, var)
third = [sp.cancel(D(D(D(lZ, u1), u1), u2).subs(at0)), sp.cancel(D(D(D(lZ, u1), u2), u2).subs(at0))]
m1 = sum(weight(s, sn, x1, x2) * sig(s, sn, x1) for s in conf for sn in conf) / Z
m2 = sum(weight(s, sn, x1, x2) * sig(s, sn, x2) for s in conf for sn in conf) / Z
align1 = sp.cancel(D(m1, u2).subs(at0))
align2 = sp.cancel(D(m2, u1).subs(at0))
ok("R5", all(z == 0 for z in third) and sp.cancel(align1 - corr) == 0 and sp.cancel(align2 - corr) == 0,
   "third-order cross terms vanish, and d<sigma_1>/d h2 = d<sigma_2>/d h1 = beta <sigma_1 sigma_2>")


def one_sign(expr):
    num, den = sp.fraction(sp.together(expr.subs(t, 1 + w)))
    num, den = sp.expand(num), sp.expand(den)
    pn, pd = sp.Poly(num, w), sp.Poly(den, w)
    for a, b in ((pn, pd), (-pn, -pd)):
        if all(c >= 0 for c in a.coeffs()) and all(c >= 0 for c in b.coeffs()) and a.subs(w, 1) != 0:
            return True
    return False


ok("R6", one_sign(corr), f"on the ring of 4, sites one apart, <sigma_0 sigma_1> > 0 for every beta > 0 ({sp.factor(corr)})")

# ring of 6, mirror separations 1 and 3
conf6 = configs(6)
Z6 = sum(weight(s, sn, 0, 0).subs(at0) for s in conf6 for sn in conf6)
# weight with x1=x2=0 still has the interaction; correlation doesn't use the sources at zero field
c6 = {}
for r in (1, 2, 3):
    c6[r] = sp.cancel(sum(weight(s, sn, 0, 0).subs(at0) * (s[0] + sn[0]) * (s[r] + sn[r]) for s in conf6 for sn in conf6) / Z6)
ok("R7", one_sign(c6[1]) and one_sign(c6[3]) and c6[1].subs(t, 2) > c6[2].subs(t, 2) > c6[3].subs(t, 2) > 0,
   f"ring of 6: mirror separations stay positive, and at t=2 the values are {[sp.simplify(c6[r].subs(t, 2)) for r in (1, 2, 3)]}")

# finite-volume identity R(0)-R(r) = N^{-1} sum_{k!=0} (1-cos) Rhat
diff = sp.simplify(R(0) - R(1) - sum((1 - sp.cos(2 * sp.pi * n / L)) * Rhat[n] for n in range(1, L)) / L)
ok("R8", diff == 0, "R(0)-R(r) is the cosine transform of Rhat over k != 0")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - two held sources stay reversible on the doubled ring, and the cross term of log Z is 2 beta R(x1-x2) plus O(h^4), nonnegative for mirror separations.")
print("HIT: confirmed - on the doubled light-cone ring the stationary law is the level marginal with each source on both vertices; at zero field d^2 log Z / dh1 dh2 = beta^2 <sigma_1 sigma_2> = 2 beta R, with R the Fourier response kernel, third order vanishing; mirror separations have <sigma sigma> > 0 for every beta > 0.")
