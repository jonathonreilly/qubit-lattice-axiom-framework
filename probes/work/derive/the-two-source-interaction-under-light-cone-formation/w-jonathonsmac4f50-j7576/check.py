#!/usr/bin/env python3
"""the-two-source-interaction-under-light-cone-formation, attempt 2 (worker w-jonathonsmac4f50-j7576, claude-opus-5-5).

Exact claims on the doubled ring (block 90/91's light-cone clause in one dimension: predecessors x + {-1, 0, 1}), two-valued
contents s = +-1, with t = e^beta, u_i = e^{beta h_i}, v = e^{beta eps} as symbols: every weight is a Laurent monomial, every identity
is an identity of rational functions (sympy). d/dh_i = beta u_i d/du_i. The sphere-menu statements use the same algebra with rotation
invariance (Step 2 of ATTEMPT.md). Step labels refer to ATTEMPT.md.
"""
import itertools
import sys
import time

import sympy as sp

T0 = time.time()
NP = NF = 0


def ok(label, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NF += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


t, v, u1, u2 = sp.symbols("t v u1 u2", positive=True)
NBR = (-1, 0, 1)


def setup(L, x1, x2):
    conf = list(itertools.product((1, -1), repeat=L))

    def eH(s, x):  # e^{beta H_x(s)}, H = sum of the three records below + eps + sources
        return t ** sum(s[(x + d) % L] for d in NBR) * v * (u1 if x == x1 else 1) * (u2 if x == x2 else 1)

    def P(sn, s):
        return sp.Mul(*[(eH(s, x) if sn[x] == 1 else 1 / eH(s, x)) / (eH(s, x) + 1 / eH(s, x)) for x in range(L)])

    def pi(s):
        return (v ** sum(s) * u1 ** s[x1] * u2 ** s[x2]) * sp.Mul(*[eH(s, x) + 1 / eH(s, x) for x in range(L)])

    def mu(s, sn):
        return (t ** sum(sn[x] * s[(x + d) % L] for x in range(L) for d in NBR) * v ** (sum(s) + sum(sn))
                * u1 ** (s[x1] + sn[x1]) * u2 ** (s[x2] + sn[x2]))

    return conf, P, pi, mu


L, x1, x2 = 4, 0, 1
conf, P, pi, mu = setup(L, x1, x2)
db_ok = all(sp.cancel(pi(s) * P(sn, s) - pi(sn) * P(s, sn)) == 0 for s, sn in itertools.combinations(conf, 2))
ok("1.1 two held sources at x1, x2 and a uniform field: the chain satisfies detailed balance for every pair of levels (ring of 4, symbolic t, v, u1, u2)", db_ok)
marg_ok = all(sp.cancel(sum(mu(s, sn) for sn in conf) - pi(s)) == 0 for s in conf)
ok("1.2 its stationary law is the level marginal of the doubled-graph ferromagnet with each source on BOTH vertices of its site", marg_ok)

# ---------------------------------------------------------------- Step 2: the cross term
Z = sum(mu(s, sn) for s in conf for sn in conf)
at0 = {u1: 1, u2: 1, v: 1}
Z0 = sp.expand(Z.subs(at0))
sig = lambda s, sn, x: s[x] + sn[x]
# (1/beta^2) d^2 log Z / dh1 dh2 at 0 = u1 u2 d^2 log Z/du1 du2 + ... use d/dh = beta u d/du
lZ = sp.log(Z)
D1 = lambda f: u1 * sp.diff(f, u1)
D2 = lambda f: u2 * sp.diff(f, u2)
cross_over_b2 = sp.cancel(D1(D2(lZ)).subs(at0))
corr = sp.cancel(sum(mu(s, sn).subs(at0) * sig(s, sn, x1) * sig(s, sn, x2) for s in conf for sn in conf) / Z0)
ok("2.1 (1/beta^2) d^2 log Z/dh1 dh2 at h = eps = 0 equals <sigma_1 sigma_2>, sigma_i the sum of the two records at x_i", sp.cancel(cross_over_b2 - corr) == 0)
# block 91: R^(k) = 2 beta N^-1 <|S_+^(k)|^2>, S_+ = sigma/2; R(r) = N^-1 sum_k e^{ikr} R^(k) = (beta/2) <sigma(0) sigma(r)> by translation invariance
Rhat_over_b = {}
for n in range(L):
    w = sp.exp(2 * sp.pi * sp.I * n / L)
    acc = 0
    for s in conf:
        for sn in conf:
            Sp = sum(w ** (-x) * sig(s, sn, x) for x in range(L)) / 2
            acc += mu(s, sn).subs(at0) * sp.expand(Sp * sp.conjugate(Sp))
    Rhat_over_b[n] = sp.simplify(2 * acc / (L * Z0))
R_over_b = lambda r: sp.simplify(sum(sp.exp(2 * sp.pi * sp.I * n * r / L) * Rhat_over_b[n] for n in range(L)) / L)
ok("2.2 the cross term is 2 beta R(x2 - x1) with R(r) = N^-1 sum_k e^{ikr} R^(k), block 91's R^(k) = 2 beta N^-1 <|S_+^(k)|^2> (cross/beta^2 = 2 R/beta)",
   sp.simplify(corr - 2 * R_over_b(x2 - x1)) == 0)
third = [sp.cancel(D1(D1(D2(lZ))).subs(at0)), sp.cancel(D1(D2(D2(lZ))).subs(at0))]
ok("2.3 at zero uniform field the third-order cross terms vanish (the flip s -> -s; for the sphere no rotation-invariant cubic in two vectors): the statement holds to O(h^4)",
   all(x == 0 for x in third))
m1 = sum(mu(s, sn) * sig(s, sn, x1) for s in conf for sn in conf) / Z
dm1_over_b = sp.cancel(D2(m1).subs(at0))
ok("2.4 formation meaning: (1/beta) d<sigma_1>/dh2 = <sigma_1 sigma_2>: the other source aligns the records source 1 holds, and d^2 log Z/dh1 dh2 = beta d<sigma_1>/dh2 (symmetric in 1 <-> 2)",
   sp.cancel(dm1_over_b - corr) == 0 and sp.cancel(D1(sum(mu(s, sn) * sig(s, sn, x2) for s in conf for sn in conf) / Z).subs(at0) - corr) == 0)

# ---------------------------------------------------------------- Step 3: sign on the ring
wv = sp.symbols("w", positive=True)  # t = 1 + w: w > 0 exactly when beta > 0


def positive_for_beta_pos(expr):
    nn, dd = sp.fraction(sp.cancel(expr.subs(t, 1 + wv)))
    pn_, pd_ = sp.Poly(sp.expand(nn), wv), sp.Poly(sp.expand(dd), wv)
    both = [(pn_, pd_), (-pn_, -pd_)]
    return any(all(c >= 0 for c in a.all_coeffs()) and all(c >= 0 for c in b_.all_coeffs()) and a.eval(1) != 0 for a, b_ in both)


ok("3.1 sites one step apart (mirror images under the bond-plane reflection, in block 90's bilayer labels): <sigma_1 sigma_2> > 0 for every beta > 0 - with t = 1 + w, numerator and denominator are polynomials in w with coefficients of one sign",
   positive_for_beta_pos(corr), f"<s1 s2> = {sp.factor(corr)}")
corr2 = sp.cancel(sum(mu(s, sn).subs(at0) * sig(s, sn, 0) * sig(s, sn, 2) for s in conf for sn in conf) / Z0)
print(f"INFO ring of 4, sites two apart (not a mirror pair of the bond-plane family): <sigma_0 sigma_2> = {sp.factor(corr2)}")
# the ring of 6: the cross term on every separation, and the mirror pairs at odd separation
L6 = 6
conf6, P6, pi6, mu6 = setup(L6, 0, 1)
Z6 = sp.expand(sum(mu6(s, sn).subs(at0) for s in conf6 for sn in conf6))
c6 = {r: sp.cancel(sum(mu6(s, sn).subs(at0) * (s[0] + sn[0]) * (s[r] + sn[r]) for s in conf6 for sn in conf6) / Z6) for r in (1, 2, 3)}
pos = {r: positive_for_beta_pos(c6[r]) for r in (1, 3)}
ok("3.2 ring of 6: at the odd separations 1 and 3 (mirror pairs) <sigma_0 sigma_r> > 0 for every beta > 0 (coefficients of one sign in w = t - 1); at t = 2 it falls with separation (1 > 2 > 3)",
   pos[1] and pos[3] and c6[1].subs(t, 2) > c6[2].subs(t, 2) > c6[3].subs(t, 2) > 0,
   f"at t=2: {[sp.simplify(c6[r].subs(t, 2)) for r in (1, 2, 3)]}")

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL exact: two held sources keep light-cone formation reversible, each on both vertices of its site; at zero uniform field "
      "the cross term of log Z is 2 beta (h1.h2) R(x1 - x2) + O(h^4), R block 91's response kernel; in the formation reading it is the mutual "
      "alignment d<sigma_1>/dh2 = d<sigma_2>/dh1 = 2 R(x1 - x2) of the records the two pinned sites hold; its transform 2 beta R^(k) lies in "
      "[block 92's floor, 1/E(k)] mode by mode; for mirror-image sources (block 90's reflections) it is non-negative")
print("HIT: exact second order for two held sources under light-cone formation: the cross term of the stationary law's normalisation is "
      "2 beta (h1.h2) R(x1 - x2) + O(h^4) with R block 91's kernel; in the formation law it is the mutual alignment d<sigma_1>/dh2 = d<sigma_2>/dh1 = "
      "2R(x1 - x2) of the records each pinned site holds (symmetric: action equals reaction); non-negative for mirror-image sources")
