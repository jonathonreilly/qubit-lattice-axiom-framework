# Exploration (floats): the two-level route's region. Need t in (0,1] with (x, y) = (t + eps2/t^2, eps1/t^3) inside the domain of
# D = (1+xU)^2 (1+3xD)(1+yF)^6, U = (1+xU)^3 (1+yF)^6, F = (1+xU)^3 (1+3xD)(1+yF)^5.  eps1 = d1, eps2 = max(d2, d3) at (p, q, r).
import numpy as np
def converges(x, y, nit=3000):
    D = U = Fv = 1.0
    for i in range(nit):
        D2 = (1+x*U)**2*(1+3*x*D)*(1+y*Fv)**6; U2 = (1+x*U)**3*(1+y*Fv)**6; F2 = (1+x*U)**3*(1+3*x*D)*(1+y*Fv)**5
        if max(D2, U2, F2) > 1e8: return False
        if abs(D2-D) < 1e-13 and abs(U2-U) < 1e-13 and abs(F2-Fv) < 1e-13: return True
        D, U, Fv = D2, U2, F2
    return True
def devs(p, q, r):
    d1 = 1 - p**3/(p**3 + q**3 + 4*r**3); d2 = 1 - p**2*q/(p*q*(p+q) + 4*r**3); d3 = 1 - p**2*r/(r*(p**2+q**2) + r**2*(p+q) + 2*r**3)
    return d1, d2, d3
def feasible(p, q, r):
    d1, d2, d3 = devs(p, q, r); e1, e2 = d1, max(d2, d3)
    for t in np.linspace(0.02, 0.148, 130):
        if converges(t + e2/t**2, e1/t**3): return True, t
    return False, None
print("route ceiling (eps1 -> 0): need eps2 < max_t t^2 (x_c - t) with x_c(y=0) = 4/27:", max(t*t*(4/27 - t) for t in np.linspace(0, 4/27, 2000)))
for (q, r), old in (((1, 2), 285718), ((1, 1), 142861), ((2, 4), 571436), ((1, 3), 428576)):
    lo, hi = 10, 400000
    while lo < hi:
        mid = (lo + hi)//2
        if feasible(mid, q, r)[0]: hi = mid
        else: lo = mid + 1
    d1, d2, d3 = devs(lo, q, r); tt = feasible(lo, q, r)[1]
    print(f"(p,{q},{r}): new p0 ~ {lo} (was {old}; factor {old/lo:.0f}); eps1 = {d1:.3e}, eps2 = {max(d2,d3):.3e} (d2 {d2:.3e}, d3 {d3:.3e}); a feasible t = {tt:.4f} -> x = {tt + max(d2,d3)/tt**2:.4f}, y = {d1/tt**3:.3e}")
