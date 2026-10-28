#!/usr/bin/env python3
# checks/ad1_exp.py  --  T55-K adjudication, check ad1.
# Criteria pre-registered in checks/ad1_criteria.md BEFORE this file existed.
# Exact integer / Fraction arithmetic. No numpy, no sympy, no BLAS. No numeric lock.
#
# Decides ONLY: does a stated leg-counting rule, forced first to reproduce the two
# exponents NORMS.md already carries, return strictly negative exponents for the four
# NEW background vertex families at the delivered weight pair?

from fractions import Fraction as F

# ---------------------------------------------------------------- the rule
# E = d - (coefficient weight) - (sum of leg weights).
# Coefficient weights: O(|X_p|) -> th_wc ; O(|rho|) -> th_wr ; 1+O(.) -> 0.
# Leg weights: background-coboundary / residual leg -> th_wc (Wilson) or th_wr (soft);
#              undifferentiated level-k response leg -> th_A.
# Soft families are per-level: the returned number is the SLOPE in the level index n.

def exponent(d, coeff_w, legs):
    return d - coeff_w - sum(legs)

def families(d, th_wc, th_wr, th_A):
    """Returns dict name -> exponent (Wilson: the exponent; soft: the slope in n)."""
    return {
        # --- the two NORMS already carries (reproduction control) ---
        "1deriv_wilson": exponent(d, 0,      [th_wc, th_A, th_A]),   # d - th_wc - 2 th_A
        "1deriv_soft":   exponent(d, 0,      [th_wr, th_A, th_A]),   # d - th_wr - 2 th_A
        # --- the four new ones at a nontrivial background ---
        "3deriv_wilson": exponent(d, th_wc,  [th_wc, th_wc, th_wc]), # d - 4 th_wc
        "0deriv_wilson": exponent(d, th_wc,  [th_A, th_A, th_A]),    # d - th_wc - 3 th_A
        "3deriv_soft":   exponent(d, th_wr,  [th_wr, th_wr, th_wr]), # d - 4 th_wr
        "0deriv_soft":   exponent(d, th_wr,  [th_A, th_A, th_A]),    # d - th_wr - 3 th_A
    }

NEW = ("3deriv_wilson", "0deriv_wilson", "3deriv_soft", "0deriv_soft")

def theta_A_of(th_wc):
    "NORMS.md l.656-657."
    return min(F(1), th_wc - 1)

# ---------------------------------------------------------------- ad1-A
print("=== ad1-A  REPRODUCTION CONTROL (must PASS or the gate is void) ===")
d, th_wc, th_wr = F(4), F(2), F(3)
th_A = theta_A_of(th_wc)
print(f"  (d, th_wc, th_wr, th_A) = ({d}, {th_wc}, {th_wr}, {th_A})   [th_A from NORMS l.656-657]")
f4 = families(d, th_wc, th_wr, th_A)
w1_at_d4 = f4["1deriv_wilson"]
s1_at_d4 = f4["1deriv_soft"]
s1_at_d5 = families(F(5), th_wc, th_wr, th_A)["1deriv_soft"]
print(f"  1-derivative Wilson exponent at d=4 : {w1_at_d4}   (NORMS: 'exactly marginal' => 0)")
print(f"  1-derivative soft slope     at d=4 : {s1_at_d4}   (NORMS: subcritical for d<5 => <0)")
print(f"  1-derivative soft slope     at d=5 : {s1_at_d5}   (NORMS: critical at d=5 => 0)")
A_ok = (w1_at_d4 == 0) and (s1_at_d4 < 0) and (s1_at_d5 == 0)
print(f"  ad1-A: {'PASS' if A_ok else 'FAIL'}")

# ---------------------------------------------------------------- ad1-B
print()
print("=== ad1-B  THE GATE: are the four NEW families strictly subcritical at (4,2,3,1)? ===")
for nm in NEW:
    print(f"  {nm:15s} exponent = {f4[nm]}")
B_ok = all(f4[nm] < 0 for nm in NEW)
print(f"  ad1-B: {'PASS' if B_ok else 'FAIL'}   (criterion: all four < 0)")
# critical dimensions, reported (not pre-registered as targets)
print("  critical dimensions (d at which each new family's exponent vanishes), reported only:")
for nm in NEW:
    # exponent is linear in d with slope 1, so d_crit = d - exponent
    print(f"    {nm:15s} d_crit = {d - f4[nm]}")

# ---------------------------------------------------------------- ad1-C
print()
print("=== ad1-C  DESIGNED-FAIL CONTROL (must FIRE: ad1-B's criterion must FAIL here) ===")
th_wc0 = F(0)
th_A0 = theta_A_of(th_wc0)
print(f"  (d, th_wc, th_wr, th_A) = ({d}, {th_wc0}, {th_wr}, {th_A0})")
f0 = families(d, th_wc0, th_wr, th_A0)
for nm in NEW:
    print(f"  {nm:15s} exponent = {f0[nm]}")
B_at_control = all(f0[nm] < 0 for nm in NEW)
C_fired = not B_at_control
print(f"  ad1-B's criterion at this input: {'PASS' if B_at_control else 'FAIL'}")
print(f"  ad1-C: {'CONTROL FIRED (gate is falsifiable)' if C_fired else 'CONTROL DID NOT FIRE -> ad1-B IS NO EVIDENCE'}")

# ---------------------------------------------------------------- ad1-D
print()
print("=== ad1-D  SECOND DESIGNED-FAIL CONTROL (formula sensitivity) ===")
legcount_3soft = f4["3deriv_soft"]                      # d - 4 th_wr
alt_3soft = d - th_wr - 2*th_wc - th_A                  # the alternative algebraic form
print(f"  leg-counting 3-derivative soft slope : {legcount_3soft}   (= d - 4*th_wr)")
print(f"  alternative form                     : {alt_3soft}   (= d - th_wr - 2*th_wc - th_A)")
D_fired = (legcount_3soft != alt_3soft)
print(f"  ad1-D: {'CONTROL FIRED (the gate is formula-sensitive, not a tautology)' if D_fired else 'CONTROL DID NOT FIRE'}")
print(f"  robustness line (separate, not a pass): both negative? "
      f"{(legcount_3soft < 0) and (alt_3soft < 0)}  -> ad1-B's verdict "
      f"{'does not' if ((legcount_3soft < 0) and (alt_3soft < 0)) else 'does'} depend on which form is used")

# ---------------------------------------------------------------- summary
print()
print("=== SUMMARY ===")
print(f"  ad1-A reproduction control : {'PASS' if A_ok else 'FAIL'}")
print(f"  ad1-B gate                 : {'PASS' if B_ok else 'FAIL'}" + ("" if A_ok else "  [VOID: ad1-A failed]"))
print(f"  ad1-C designed-FAIL control: {'FIRED' if C_fired else 'DID NOT FIRE'}")
print(f"  ad1-D designed-FAIL control: {'FIRED' if D_fired else 'DID NOT FIRE'}")
