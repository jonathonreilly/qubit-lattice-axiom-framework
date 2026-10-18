#!/usr/bin/env python3
"""M6b: with the general couplings of chk_continuum_matter, is the shear coupling forced to (lam_s/lam1) x metric stress?
scalar: coefficient of h01 d0phi d1phi must be -(lam_m/lam1) c ; Maxwell: coefficient of h01 E0 E1 must be +(lam_A/lam1) g2."""
import sympy as sp, random
import chk_continuum_matter as cm
rng = random.Random(3)
ok = True
for trial in range(2):
    r = lambda: sp.Rational(rng.randint(1, 9), rng.randint(1, 9))
    lam1, lamm, lamA = r(), r(), r(); pars = (r(), r(), r(), r(), r())
    S1, S2, Np = cm.lapse()
    es, us = cm.matter_eqs(lam1, lamm, lamA, Np, pars, True, False)
    ea, ua = cm.matter_eqs(lam1, lamm, lamA, Np, pars, False, True)
    ts, ta = sp.Symbol("c1_01_01"), sp.Symbol("d_01_2")
    o1, s1, _ = cm.solveQ(es, us + list(S1) + list(S2), [ts])
    o2, s2, _ = cm.solveQ(ea, ua + list(S1) + list(S2), [ta])
    exp_s, exp_a = -(lamm / lam1) * pars[1], (lamA / lam1) * pars[3]
    print(f"   trial {trial}: scalar h01 d0phi d1phi coeff = {s1.get(ts)} (expect {exp_s}); Maxwell h01 E0E1 coeff = {s2.get(ta)} (expect {exp_a})")
    ok = ok and s1.get(ts) == exp_s and s2.get(ta) == exp_a
print(("PASS" if ok else "FAIL") + ": M6b shear coupling uniquely forced to (lam_s/lam1) x metric stress for scalar and Maxwell (general ansatz)")
print(f"TOTAL: PASS={int(ok)} FAIL={int(not ok)}")
