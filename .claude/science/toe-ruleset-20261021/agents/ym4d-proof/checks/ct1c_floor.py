#!/usr/bin/env python3
"""ct1c_floor.py -- POST-HOC (written after ct1b_out.txt). C_T as a function of the single
product C_1*C_V, including the forced floor C_1*C_V = 1, and the q needed at each value.
Pure python, single thread."""
import math
N1, N3 = 3**4*6, 7**4*6
F = 175.802817          # optimised schedule, max over R>=32 (ct1b)
F_w = 4080.0            # written schedule, max over R>=128 (ct1b)

def B(m, n=200):
    return math.exp(sum((m/(2.0*2**i))*math.log(2.0*2**i-1.0) for i in range(n)))

def CT(q, prod, Fuse=F, cc=50.0, eps=1e-4, C1=None, R0=32.0):
    a = q/(q-4.0)
    c1 = C1 if C1 is not None else math.sqrt(prod)   # split evenly when only the product is fixed
    cv = prod/c1
    Ags = 36.0*prod*N1
    Agc = 36.0*c1*(N3**0.75)*cc*eps
    Vinf = cv*R0**(-2.0+8.0/q)
    Q = 1.0+18.0*Vinf*N1
    return math.sqrt(6.0)*Fuse*B(4.0*a)*(0.5*Ags**a + 0.5*Agc**2 + 288.0*c1*Q)

print("F(optimised)=%.3f  F(written)=%.1f  B(8)=%.2f  B(4)=%.3f" % (F, F_w, B(8), B(4)))
print()
print("A_s gamma_s = 36*C_1*C_V*|N_1| = %g * (C_1 C_V)" % (36*N1))
print()
print("%-12s %-14s %-14s %-8s %-8s" % ("C_1*C_V", "C_T(q=8,opt)", "C_T(q=8,writ)", "q_min", "C_T(q_min)"))
for prod in (1.0, 3.0, 10.0, 100.0, 1000.0, 2000.0, 10000.0, 50000.0):
    q8 = CT(8.0, prod); q8w = CT(8.0, prod, Fuse=F_w)
    qm = None
    for q in range(5, 20001):
        if CT(float(q), prod) < 1e13:
            qm = q; break
    print("%-12g %-14.4g %-14.4g %-8s %-8.4g" %
          (prod, q8, q8w, qm, CT(float(qm), prod) if qm else float('nan')))
print()
print("the largest C_1*C_V for which q=8 still clears 1e13 (optimised schedule):")
lo, hi = 1e-6, 1.0
for _ in range(200):
    mid = (lo+hi)/2
    if CT(8.0, mid) < 1e13: lo = mid
    else: hi = mid
print("   C_1*C_V <= %.4f   (both constants are >= 1 in any expansion, so q=8 cannot clear it)" % lo)
print()
print("C_T at the forced floor C_1*C_V = 1, by q:")
for q in (8, 10, 12, 16, 20, 24, 32, 50, 100):
    print("   q=%-5d C_T=%.4g" % (q, CT(float(q), 1.0)))
