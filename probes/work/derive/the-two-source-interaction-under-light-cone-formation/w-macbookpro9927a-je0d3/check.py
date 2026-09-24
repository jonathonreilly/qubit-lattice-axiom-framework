#!/usr/bin/env python3
"""the-two-source-interaction-under-light-cone-formation, attempt a1 (worker w-macbookpro9927a-je0d3, claude-opus-5-5).

Two held sources under block 90's light-cone formation (block 91's held sources).  Exact arithmetic throughout
(Fractions, integer polynomials, sympy); the doubled ring is the one-dimensional light-cone clause (past {0, +-1}).
"""
import sys
import time
from fractions import Fraction as Fr
from itertools import product
from math import factorial

import sympy as sp

T0 = time.time()
FAILS = []


def check(tag, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + tag + (": " + msg if msg else ""))
    if not ok:
        FAILS.append(tag)


PAST = (0, 1, -1)


def local_field(s, x, L):
    return sum(s[(x + d) % L] for d in PAST)


# ================================================================= Q: two held sources, the two-valued menu, exactly
def kernel(sp_, s, L, t, v, u):   # K(s'|s) for contents +-1, weights t = e^beta, v = e^{beta eps}, u[x] = e^{beta h_x}
    w = Fr(1)
    for x in range(L):
        a = t ** local_field(s, x, L) * v * u[x]            # e^{beta (h_x(s) + eps + h(x))}
        w *= (a if sp_[x] == 1 else 1 / a) / (a + 1 / a)
    return w


def pi_tilde(s, L, t, v, u):      # the stationary weight of block 91 T1 with the sources on the sites
    w = Fr(1)
    for x in range(L):
        a = t ** local_field(s, x, L) * v * u[x]
        w *= (v * u[x]) ** s[x] * (a + 1 / a)
    return w


okQ1 = okQ2 = okQ3 = True
L = 4
t, v = Fr(3, 2), Fr(5, 4)
x1, x2 = 0, 2
for u1, u2 in ((Fr(7, 3), Fr(2, 5)), (Fr(3), Fr(3))):
    u = [Fr(1)] * L
    u[x1], u[x2] = u1, u2
    states = list(product((1, -1), repeat=L))
    for s in states:
        for s2 in states:                                   # detailed balance, every pair of levels
            okQ1 &= pi_tilde(s, L, t, v, u) * kernel(s2, s, L, t, v, u) == pi_tilde(s2, L, t, v, u) * kernel(s, s2, L, t, v, u)
    u0 = [Fr(1)] * L
    ua = list(u0); ua[x1] = u1
    ub = list(u0); ub[x2] = u2
    for s in states:                                        # the unnormalised weight factorises
        okQ2 &= pi_tilde(s, L, t, v, u) * pi_tilde(s, L, t, v, u0) == pi_tilde(s, L, t, v, ua) * pi_tilde(s, L, t, v, ub)
    # the pair law with sources is the source-free pair law tilted by u1^{sigma(x1)} u2^{sigma(x2)}
    for s in states:
        for s2 in states:
            lhs = pi_tilde(s, L, t, v, u) * kernel(s2, s, L, t, v, u)
            rhs = pi_tilde(s, L, t, v, u0) * kernel(s2, s, L, t, v, u0) * u1 ** (s[x1] + s2[x1]) * u2 ** (s[x2] + s2[x2])
            okQ3 &= lhs == rhs
check("Q1 two sources, reversible", okQ1, "doubled ring of 4, contents +-1: pi_h(s)K(s'|s) symmetric for every pair of levels")
check("Q2 no pair term", okQ2, "the unnormalised stationary weight factorises: w(h1,h2) w(0,0) = w(h1,0) w(0,h2) at every state")
check("Q3 tilt", okQ3, "the two-level law with sources equals the source-free two-level law times u1^sigma(x1) u2^sigma(x2), "
      "sigma = sum of the two records at a site")

# Q4: the cross terms are the mixed cumulants of the source-free records (second order: beta^2 Cov)
L = 6
t0 = Fr(3, 2)
states = list(product((1, -1), repeat=L))
u0 = [Fr(1)] * L
Pjoint = {}
Ztot = Fr(0)
for s in states:
    for s2 in states:
        w = pi_tilde(s, L, t0, Fr(1), u0) * kernel(s2, s, L, t0, Fr(1), u0)
        key = (s[0] + s2[0], s[2] + s2[2])
        Pjoint[key] = Pjoint.get(key, 0) + w
        Ztot += w
Pjoint = {k: w / Ztot for k, w in Pjoint.items()}
a, b = sp.symbols("a b")
cgf = sp.log(sum(sp.Rational(p.numerator, p.denominator) * sp.exp(a * k[0] + b * k[1]) for k, p in Pjoint.items()))
ser = sp.series(sp.series(cgf, a, 0, 3).removeO(), b, 0, 3).removeO()
cov = sum(Fr(k[0] * k[1]) * p for k, p in Pjoint.items()) - sum(Fr(k[0]) * p for k, p in Pjoint.items()) * sum(Fr(k[1]) * p for k, p in Pjoint.items())
c_ab = sp.nsimplify(sp.expand(ser).coeff(a, 1).coeff(b, 1))
c_a2b = sp.expand(sp.series(sp.series(cgf, a, 0, 4).removeO(), b, 0, 3).removeO()).coeff(a, 2).coeff(b, 1)
check("Q4 cross terms are cumulants", c_ab == sp.Rational(cov.numerator, cov.denominator) and sp.simplify(c_a2b) == 0 and cov > 0,
      "ring of 6, sources two sites apart: log Z(h1,h2)/Z(0) = log E_0 exp(beta h1 sigma1 + beta h2 sigma2); the h1 h2 "
      "coefficient is beta^2 Cov_0(sigma1, sigma2) = beta^2 * %s, the h1^2 h2 one is 0 (flip)" % cov)


# ================================================================= G: the sign at every separation (Griffiths' first inequality)
# G1: two-valued menu: each correlation of the doubled graph is a polynomial in w = tanh(beta) with non-negative coefficients
def poly_mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        if x:
            for j, y in enumerate(q):
                if y:
                    r[i + j] += x * y
    return r


L = 6
edges = [((x, 0), ((x + d) % L, 1)) for x in range(L) for d in PAST]
num = {r: [0] for r in (1, 2, 3)}
den = [0]


def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]


for conf in product((1, -1), repeat=2 * L):
    spin = {(x, lv): conf[2 * x + lv] for x in range(L) for lv in (0, 1)}
    w = [1]
    for (p, q) in edges:
        w = poly_mul(w, [1, spin[p] * spin[q]])            # e^{beta s s'} = cosh(beta)(1 + w s s')
    den = padd(den, w)
    for r in (1, 2, 3):
        sig = (spin[(0, 0)] + spin[(0, 1)]) * (spin[(r, 0)] + spin[(r, 1)])
        num[r] = padd(num[r], [sig * c for c in w])
okG1 = all(c >= 0 for c in den) and all(all(c >= 0 for c in num[r]) and any(num[r]) for r in (1, 2, 3))
lead = {r: next(i for i, c in enumerate(num[r]) if c) for r in (1, 2, 3)}
check("G1 two-valued menu", okG1, "doubled ring of 6: <sigma(0) sigma(r)> = P_r(w)/Q(w), w = tanh(beta), with non-negative integer "
      "coefficients for r = 1, 2, 3 (2 is not a mirror pair); lowest orders w^%d, w^%d, w^%d" % (lead[1], lead[2], lead[3]))


# G2: sphere menu: every monomial moment of the uniform measure on S^2 is non-negative (odd -> 0)
def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r


def sph(e):   # E[x^e0 y^e1 z^e2] on the unit sphere
    if any(k % 2 for k in e):
        return Fr(0)
    K = sum(e) // 2
    return Fr(dfact(e[0] - 1) * dfact(e[1] - 1) * dfact(e[2] - 1), dfact(2 * K + 1))


th, ph = sp.symbols("theta phi")
okm = True
for e in product(range(5), repeat=3):
    if sum(e) <= 4:
        f = (sp.sin(th) * sp.cos(ph)) ** e[0] * (sp.sin(th) * sp.sin(ph)) ** e[1] * sp.cos(th) ** e[2] * sp.sin(th)
        val = sp.integrate(sp.integrate(f, (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)) / (4 * sp.pi)
        okm &= sp.nsimplify(val) == sp.Rational(sph(e).numerator, sph(e).denominator) and sph(e) >= 0
check("G2 sphere moments", okm, "E[x^a y^b z^c] = (a-1)!!(b-1)!!(c-1)!!/(a+b+c+1)!! for even a, b, c and 0 otherwise, "
      "against direct integration for a + b + c <= 4: never negative")


# G3: the sphere menu on the doubled ring of 4: the beta-series of the unnormalised <s^1_a s^1_b> has non-negative coefficients
def series_coeffs(L, a_site, b_site, order, eps):
    """coefficients c_n of E_0[s^1_a s^1_b exp(beta(sum_edges s.s' + eps sum s^3))] = sum c_n beta^n (product sphere measure)."""
    verts = [(x, lv) for x in range(L) for lv in (0, 1)]
    vid = {v_: i for i, v_ in enumerate(verts)}
    E = [((x, 0), ((x + d) % L, 1)) for x in range(L) for d in PAST]
    lin = {}                                                 # the linear form sum_edges s.s' + eps sum s^3 as monomials
    for (p, q) in E:
        for comp in range(3):
            key = [0] * (3 * len(verts))
            key[3 * vid[p] + comp] += 1
            key[3 * vid[q] + comp] += 1
            lin[tuple(key)] = lin.get(tuple(key), 0) + 1
    if eps:
        for v_ in verts:
            key = [0] * (3 * len(verts))
            key[3 * vid[v_] + 2] += 1
            lin[tuple(key)] = lin.get(tuple(key), 0) + eps
    start = [0] * (3 * len(verts))
    start[3 * vid[a_site] + 0] += 1
    start[3 * vid[b_site] + 0] += 1
    cur = {tuple(start): Fr(1)}
    out = []
    for n in range(order + 1):
        out.append(sum(c * prod_moment(k) for k, c in cur.items()) / factorial(n))
        nxt = {}
        for k, c in cur.items():
            for k2, c2 in lin.items():
                kk = tuple(i + j for i, j in zip(k, k2))
                nxt[kk] = nxt.get(kk, 0) + c * c2
        cur = nxt
    return out


def prod_moment(k):
    r = Fr(1)
    for i in range(0, len(k), 3):
        m = sph(k[i:i + 3])
        if m == 0:
            return Fr(0)
        r *= m
    return r


cz = series_coeffs(4, (0, 0), (2, 0), 4, 0)          # non-mirror separation 2, same level
cf = series_coeffs(4, (0, 0), (2, 1), 4, Fr(1, 2))   # separation 2 across levels, transverse component, field eps = 1/2
okG3 = all(c >= 0 for c in cz) and all(c >= 0 for c in cf) and cz[2] > 0
check("G3 sphere series", okG3, "doubled ring of 4, sphere menu: beta-series coefficients of the unnormalised <s^1(0) s^1(2)> "
      "through beta^4: %s; with a field 1/2 e_z, transverse, across levels: %s" %
      ([str(c) for c in cz], [str(c) for c in cf]))

print("time %.0f s" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PARTIAL (new and exact on a2's open items). (c) The sign at every separation: on the doubled graph of "
      "light-cone formation the pair law exp(beta sum s.s' + beta eps sum s_z) expands with non-negative coefficients in "
      "the components, and every monomial moment of the sphere (or of any menu invariant under each coordinate sign flip) "
      "is >= 0, so <s^a(x,l) s^a(y,l')> >= 0, strictly for beta > 0 (a path term); hence R(r) = (beta/2)<sigma^a(0) "
      "sigma^a(r)> > 0 at every r at zero field, and R_perp(r) > 0 with a uniform field: aligned sources have a positive "
      "cross term 2 beta (h1.h2) R(x1 - x2) at every separation, not only for mirror pairs. (a) at all orders: the "
      "two-level law with sources is the source-free law tilted by exp(beta h1.sigma(x1) + beta h2.sigma(x2)), so every "
      "cross term of log Z is a mixed cumulant of the source-free records at the two sites, and the unnormalised "
      "stationary weight factorises exactly (no pair term in the formation law).")
print("HIT: for two held sources under light-cone formation the second-order cross term 2 beta (h1.h2) R(x1 - x2) has "
      "R > 0 at every separation (beta > 0; zero uniform field, or the transverse components with one), by Griffiths' first "
      "inequality on the doubled graph with the sphere menu; every cross term of log Z is a mixed cumulant of the "
      "source-free records at the two sites, whose unnormalised stationary weight has no pair term")
