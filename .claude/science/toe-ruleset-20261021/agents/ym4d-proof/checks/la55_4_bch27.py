# la55_4: rigorous check of 6 s^2 + f(4s) <= 9 s^2 at s = 1/27. Criteria: la55_4_criteria.md.
from fractions import Fraction as F
from math import factorial
import sys
def exp_encl(x, M=20):
    lo = sum(F(x)**m / factorial(m) for m in range(M + 1)); return lo, lo + 2*F(x)**(M+1)/factorial(M+1)
def f_of(sig, E):
    u = E - 1; assert u < 1
    return (E-1-sig-sig**2/2) + sig*(E-1-sig) + (E-1-sig)**2/2 + u**3/(3*(1-u)), u
res = []
def rep(n, ok, d, c=False):
    res.append((n, ok, c)); print(f"{n}: {'PASS' if ok else 'FAIL'}  {d}")
s = F(1, 27); sig = 4*s
lo, up = exp_encl(sig); Fu, uu = f_of(sig, up)
rep("E1", 6*s**2 + Fu <= 9*s**2, f"(6s^2+F_up)/s^2 = {float((6*s**2+Fu)/s**2):.5f} (exact comparison with 9 done in Fractions)")
rep("E2", uu < 1, f"u_up = {float(uu):.6f}")
s2 = F(1, 24); sig2 = 4*s2
lo2, up2 = exp_encl(sig2); Fl2, _ = f_of(sig2, lo2)
rep("CONTROL", 6*s2**2 + Fl2 <= 9*s2**2, f"(6s^2+F_lo)/s^2 at s=1/24 = {float((6*s2**2+Fl2)/s2**2):.5f} (designed to FAIL)", True)
bad = [n for n, ok, c in res if not c and not ok]; fired = any(c and not ok for n, ok, c in res)
print("SUMMARY: non-control FAILs =", bad, "| control fired =", fired); sys.exit(0 if not bad and fired else 1)
