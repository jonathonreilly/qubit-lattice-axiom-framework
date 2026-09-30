"""R2 says 'for ordinary positive local odds a Born form comes free'. That needs a static joint law mu whose full conditionals ARE the odds.
Check compatibility (Brook/loop condition) of the 09-06 note's SUM rule r(s|eta) ~ 1 + lam*sum_y <s,eta_y> on path3 (menu = 6 axis unit vectors, lam=1/4)."""
import itertools, numpy as np
E = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], float)
lam = 0.25
def r(s, nbv):
    w = np.array([1 + lam*sum(E[t]@E[v] for v in nbv) for t in range(6)])
    return w[s]/w.sum()
# path 0-1-2. Full conditionals: site0 | (v1); site1 | (v0,v2); site2 | (v1)
worst = 0.0
for a, a2, b, b2, c in itertools.product(range(6), repeat=5):
    # loop (a,b,c) -> (a2,b,c) -> (a2,b2,c) -> (a,b2,c) -> (a,b,c)
    f  = r(a2, [b])/r(a, [b])              # mu(a2,b,c)/mu(a,b,c)
    g  = r(b2, [a2, c])/r(b, [a2, c])      # mu(a2,b2,c)/mu(a2,b,c)
    h  = r(a, [b2])/r(a2, [b2])            # mu(a,b2,c)/mu(a2,b2,c)
    k  = r(b, [a, c])/r(b2, [a, c])        # mu(a,b,c)/mu(a,b2,c)
    worst = max(worst, abs(f*g*h*k - 1))
print("sum rule on path3: max |loop product - 1| =", worst, "(0 iff a joint law with these conditionals exists)")
# product rule control
PHI = np.array([[3 if s==t else (1 if s//2==t//2 else 2) for t in range(6)] for s in range(6)], float)
def rp(s, nbv):
    w = np.ones(6)
    for v in nbv: w = w*PHI[:, v]
    return w[s]/w.sum()
worstp = 0.0
for a, a2, b, b2, c in itertools.product(range(6), repeat=5):
    f  = rp(a2, [b])/rp(a, [b]); g = rp(b2, [a2, c])/rp(b, [a2, c]); h = rp(a, [b2])/rp(a2, [b2]); k = rp(b, [a, c])/rp(b2, [a, c])
    worstp = max(worstp, abs(f*g*h*k - 1))
print("product rule on path3 (control): max |loop product - 1| =", worstp)
