#!/usr/bin/env python3
"""r55n_a1 -- exact arithmetic behind NORMS Thm N1-15, §N4, §N7 and NQ-1's constant.
REVIEW55_NORMS reviewer (claude-opus-5-5). Criteria: checks/r55n_a1_criteria.md (written before this file).
Exact Fractions; quoted decimals parsed exactly; rounding only for comparing with printed values."""
from fractions import Fraction as Fr
out = []
def say(s):
    out.append(s); print(s, flush=True)
def rnd(x, nd):            # round-half-up of a positive Fraction to nd decimals, returned as Fraction
    q = Fr(10) ** nd
    return Fr(int(x * q + Fr(1, 2)), 1) / q

res = {}
# a1-1
S = Fr(0); ok = True; prev = Fr(-1)
for K in range(1, 41):
    S += Fr(3) ** (3 - K)
    ok &= (S < Fr(27, 2)) and (S > prev) and (Fr(27, 2) - S == Fr(27, 2) * Fr(1, 3 ** K))
    prev = S
L, d = 3, 4
ok &= (Fr(L ** (d - 1), L - 1) == Fr(27, 2))
say("a1-1 sum_{n=1}^{40} 3^(3-n) = %s ; 27/2 - S_40 = (27/2)3^-40 : %s ; L^(d-1)/(L-1) = %s"
    % (float(S), ok, Fr(L ** (d - 1), L - 1)))
for LL in (3, 5, 7, 9, 11):
    say("a1-1 L=%d : L^3/(L-1) = %s = %.4f" % (LL, Fr(LL ** 3, LL - 1), float(Fr(LL ** 3, LL - 1))))
res['a1-1'] = ok
# a1-2
ok = True
for dd in range(2, 8):
    for n in range(1, 7):
        for tr in (Fr(dd - 1), Fr(5, 2), Fr(2), Fr(3)):
            for tA in (Fr(1), Fr(1, 2), Fr(0)):
                lhs = dd * n - tr * (n - 1) - 2 * tA * n
                ok &= (lhs == (dd - tr - 2 * tA) * n + tr)
        ok &= (dd * n - (dd - 1) * (n - 1) - 2 * n == (dd - 1) - n)
        ok &= ((dd - 2 - 2) * n == (dd - 4) * n)
    # n-coefficient at canonical triple
    ok &= (dd - (dd - 1) - 2 == -1)
say("a1-2 exponent identities for d=2..7, n=1..6: %s ; A_soft exponent coefficient = -1 for every d" % ok)
res['a1-2'] = ok
# a1-3
ok = True; viol = []
grid = [Fr(i, 1000) for i in range(1, 2001)]
for t in grid:
    tA = min(Fr(1), t - 1)
    if t + 2 * tA > 4: viol.append(t)
    if t + 2 * Fr(1) > 4: viol.append(('cap', t))
ok = (len(viol) == 0)
say("a1-3 single common theta_w in (0,2] (step 1/1000): solutions of theta_w + 2 min(1, theta_w - 1) > 4: %d ; "
    "with the cap theta_A <= 1 only: %d" % (len([v for v in viol if not isinstance(v, tuple)]),
                                              len([v for v in viol if isinstance(v, tuple)])))
res['a1-3'] = ok
# a1-4
q0 = lambda LL, dd: 1 + Fr(dd * (LL + 1), 2 * LL)
ok = (q0(3, 4) == Fr(11, 3))
vals = [q0(LL, 4) for LL in range(3, 102, 2)]
ok &= all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
for LL in (3, 5, 7):
    for dd in (2, 3, 4):
        for j in range(1, 9):
            a = LL ** j + Fr(dd * (LL * LL - 1), 2 * LL) * Fr(LL ** j - 1, LL - 1)
            b = LL ** j + Fr(dd * (LL + 1), 2 * LL) * (LL ** j - 1)
            ok &= (a == b) and (a <= q0(LL, dd) * LL ** j)
say("a1-4 q0(3,4) = %s ; q0 at L=3,5,7,9,11,101 (d=4): %s ; identities: %s"
    % (q0(3, 4), [str(q0(LL, 4)) for LL in (3, 5, 7, 9, 11, 101)], ok))
say("a1-4 p_L/L at L=3,5 (p_L = 5L-4): %s, %s ; L*q0 = L + d(L+1)/2 at L=3,5: %s, %s"
    % (Fr(11, 3), Fr(21, 5), 3 + Fr(4 * 4, 2), 5 + Fr(4 * 6, 2)))
res['a1-4'] = ok
# a1-5
Zc, Zr = Fr("156.08"), Fr("2.849")
v1 = Zc * Zr ** 2; v2 = (1 + Zc) * (1 + Zr) ** 2
v3 = 81 * Fr("0.1202"); v4 = Fr(2, 3) * Fr("2.219"); v5 = Zc / v3
g1 = v1 / (9 * Fr("0.1202")); g3 = v1 / (9 * Fr("0.1236")) ** 3
ok = (rnd(v1, 2) == Fr("1266.87") and rnd(v2, 2) == Fr("2327.11") and rnd(v3, 2) == Fr("9.74")
      and rnd(v4, 2) == Fr("1.48") and rnd(v5, 2) == Fr("16.03") and rnd(g1, 1) == Fr("1171.1")
      and rnd(g3, 1) == Fr("920.3"))
say("a1-5 Zcol*Zrow^2 = %.4f ; (1+Zcol)(1+Zrow)^2 = %.4f ; 81*0.1202 = %.4f ; (2/3)2.219 = %.4f ; "
    "156.08/9.7362 = %.4f ; gains %.2f (a=1,K=.1202), %.2f (a=3,K=.1236)"
    % (float(v1), float(v2), float(v3), float(v4), float(v5), float(g1), float(g3)))
say("a1-5 extra: 156.08/(9.7362+1.4793) = %.3f ; (11/3)^2 = %s = %.4f ; 1266.87/(121/9) = %.2f ; "
    "205/81 = %.6f ; 2021/729 = %.6f ; 6115/2187 = %.6f"
    % (float(Zc / (v3 + v4)), Fr(121, 9), float(Fr(121, 9)), float(v1 / Fr(121, 9)),
       float(Fr(205, 81)), float(Fr(2021, 729)), float(Fr(6115, 2187))))
res['a1-5'] = ok
# a1-6 (informational)
pig = 6 * (v3 + v4)
say("a1-6 pigeonhole bound on max column mass: (d(d-1)/2)(L^d K + (2/3)K_rho) = 6 * %.4f = %.4f"
    % (float(v3 + v4), float(pig)))
say("SUMMARY " + " ".join("%s=%s" % (k, "PASS" if v else "FAIL") for k, v in sorted(res.items())))
