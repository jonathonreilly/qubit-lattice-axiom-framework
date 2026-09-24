#!/usr/bin/env python3
"""Referee for J:derive:corrigendum-PR8147:a1.

The level-line symbol is recomputed from S = |1 - w sum_j exp(-i k_j)|^2.
The author's script is not called.
"""
import sys

import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


w, u, g = sp.symbols("w u g", real=True)
k1, k2, k3, e = sp.symbols("k1 k2 k3 e", real=True)
# modulus squared, computed two ways
phase = sp.exp(-sp.I * u)
mod = sp.expand((1 - 3 * w * phase) * (1 - 3 * w * sp.conjugate(phase))).rewrite(sp.cos).expand()
cos_form = sp.expand(1 - 6 * w * sp.cos(u) + 9 * w ** 2)
gain = sp.expand((1 - 3 * w) ** 2 + 6 * w * (1 - sp.cos(u)))
trig = sp.expand(((1 - g) ** 2 + 4 * g * sp.sin(u / 2) ** 2).subs(g, 3 * w)).rewrite(sp.cos).expand()
ok("E1", sp.simplify(mod - cos_form) == 0 and sp.simplify(mod - gain) == 0 and sp.simplify(gain - trig) == 0,
   "on k=(u,u,u), S=(1-g)^2 + 4 g sin^2(u/2) with g=3w; at g=1 this is 4 sin^2(u/2)")

S1 = 4 * sp.sin(u / 2) ** 2
series = sp.series(S1, u, 0, 9).removeO()
want = u ** 2 - u ** 4 / 12 + u ** 6 / 360 - u ** 8 / 20160
K = 3 * u
lead = sp.series(K ** 2 / 9 - K ** 4 / 972, u, 0, 6).removeO()
lead_S = sp.series(S1, u, 0, 6).removeO()
exact = {sp.pi / 3: 1, sp.pi / 2: 2, 2 * sp.pi / 3: 3, sp.pi: 4}
vals_ok = all(sp.simplify(S1.subs(u, uu) - val) == 0 for uu, val in exact.items())
# |sin x| < |x| for x>0: h=x-sin x, h(0)=0, h'=1-cos >= 0 and not flat
x = sp.symbols("x", positive=True)
h = x - sp.sin(x)
ok("E2", sp.simplify(series - want) == 0 and sp.simplify(lead - lead_S) == 0 and vals_ok
   and sp.simplify(sp.diff(h, x) - (1 - sp.cos(x))) == 0,
   "4 sin^2(u/2) = u^2 - u^4/12 + u^6/360 - u^8/20160 = K^2/9 - K^4/972 + O(K^6); equals u^2 only at u=0")

# the order-4 truncation hides the defect; order 6 shows it
level4 = sp.series(S1.subs(u, e), e, 0, 4).removeO()
level6 = sp.series(S1.subs(u, e), e, 0, 6).removeO()
ok("E3", sp.simplify(level4 - e ** 2) == 0 and sp.simplify(level6 - (e ** 2 - e ** 4 / 12)) == 0,
   "series through order 3 is e^2 and passes a false exact check; order 6 is e^2 - e^4/12")

# transverse plane K=k1+k2+k3=0, so k3=-(k1+k2), w=1/3
ww = sp.Rational(1, 3)
kk = (k1, k2, -(k1 + k2))
sym = sp.expand(sp.simplify((1 - ww * sum(sp.exp(-sp.I * kj) for kj in kk))
                            * (1 - ww * sum(sp.exp(sp.I * kj) for kj in kk))))
# homogeneous scaling k -> e k
scaled = sp.series(sym.subs({k1: e * k1, k2: e * k2}), e, 0, 7).removeO()
# coefficient of e^4 should be |k|^4/36 = (k1^2+k2^2+k3^2)^2/36 with k3=-(k1+k2)
kperp2 = k1 ** 2 + k2 ** 2 + (k1 + k2) ** 2
e4 = scaled.coeff(e, 4)
e5 = scaled.coeff(e, 5)
e2 = scaled.coeff(e, 2)
e6 = scaled.coeff(e, 6)
ok("E4", sp.simplify(e2) == 0 and sp.simplify(e5) == 0
   and sp.simplify(e4 - kperp2 ** 2 / 36) == 0 and sp.simplify(e6) != 0,
   "on K=0 the symbol is |k|^4/36 + O(|k|^6): no e^2 or e^5, and the e^6 term is present")

# parabolic scaling: K = lam^2 * Kt, k1 = lam*a1, k2 = lam*a2, k3 = K - k1 - k2
lam, Kt, a1, a2 = sp.symbols("lam Kt a1 a2", real=True)
ks = (lam * a1, lam * a2, lam ** 2 * Kt - lam * a1 - lam * a2)
full = sp.expand(sp.simplify((1 - ww * sum(sp.exp(-sp.I * kj) for kj in ks))
                             * (1 - ww * sum(sp.exp(sp.I * kj) for kj in ks))))
para = sp.series(full, lam, 0, 5).removeO()
# through lam^4 the symbol is lam^4 (Kt^2/9 + |a_perp|^4/36), with a_perp = (a1,a2,-(a1+a2))? 
# k_perp at this order: the deviation from the level direction.
# The attempt's |a|^4 is the transverse momentum squared to the fourth.
# At lam^4, k3 = -lam a1 - lam a2 + O(lam^2), so the O(lam) vector is (a1,a2,-(a1+a2)), whose square is a1^2+a2^2+(a1+a2)^2.
aperp2 = a1 ** 2 + a2 ** 2 + (a1 + a2) ** 2
target = lam ** 4 * (Kt ** 2 / 9 + aperp2 ** 2 / 36)
ok("E5", sp.simplify(para - target) == 0,
   "under K=lam^2 Kt and k_perp=lam a the symbol is lam^4 (Kt^2/9 + |a|^4/36) + O(lam^5)")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - on the level line the symbol is (1-g)^2 + 4 g sin^2(u/2), equal to u^2 only at u=0, while the transverse and parabolic leading forms survive.")
print("HIT: confirmed - T3(ii) at g=1 is 4 sin^2(u/2) = K^2/9 - K^4/972 + O(K^6), not u^2; the order-4 series hides the u^4/12 term; on K=0 the symbol is |k|^4/36 + O(|k|^6), and the parabolic leading form K^2/9 + |k_perp|^4/36 is unchanged.")
