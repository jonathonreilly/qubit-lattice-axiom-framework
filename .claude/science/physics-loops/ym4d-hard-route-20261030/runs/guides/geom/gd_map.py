# GUIDE only. The doubling map of Lemmas T1, T2 with all Casimir factors bounded by d.
import math
def psi_d(r, d):
    rho = (1-r)/(1+r); x = min(1.0, rho*rho*math.exp(2*d))
    return (1-x)/(1+x)
def G(r, d): return psi_d(psi_d(r, d), d)**4*math.exp(-6*d)
def scan(d, n=20000):
    pts = [(i+0.5)/n for i in range(n)]
    good = [r for r in pts if G(r, d) >= r]
    return (min(good), max(good)) if good else None
for d in (0.0, 0.001, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10):
    s = scan(d)
    print("d=%.3f  region where G_d(r) >= r: %s" % (d, "none" if s is None else "r in [%.4f, %.4f]" % s))
lo, hi = 0.0, 0.2
for _ in range(60):
    mid = (lo+hi)/2
    if scan(mid, 4000): lo = mid
    else: hi = mid
print("largest d with a non-empty region: about %.4f" % lo)
