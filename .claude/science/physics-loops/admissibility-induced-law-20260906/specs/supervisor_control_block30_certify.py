# Exact certificates for the two-level route: at (p, q, r) with eps1 = d1, eps2 = max(d2, d3) (exact rationals), choose rational t;
# x = t + eps2/t^2, y = eps1/t^3; find a rational super-solution (D, U, F) of the recursion along the Perron direction; report the least
# integer p at which a certificate is found, with R-bar and the bound eps1 * R-bar.  Also: the empirical budget (E - 3(|S|-1))/|A|.
import numpy as np, sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
def devs(p, q, r):
    p, q, r = F(p), F(q), F(r)
    return (1 - p**3/(p**3 + q**3 + 4*r**3), 1 - p**2*q/(p*q*(p+q) + 4*r**3), 1 - p**2*r/(r*(p**2+q**2) + r**2*(p+q) + 2*r**3))
def rhs(x, y, D, U, Fv):
    return ((1+x*U)**2*(1+3*x*D)*(1+y*Fv)**6, (1+x*U)**3*(1+y*Fv)**6, (1+x*U)**3*(1+3*x*D)*(1+y*Fv)**5)
def certificate(x, y):
    xf, yf = float(x), float(y); D = U = Fv = 1.0
    for i in range(20000):
        D2, U2, F2 = (1+xf*U)**2*(1+3*xf*D)*(1+yf*Fv)**6, (1+xf*U)**3*(1+yf*Fv)**6, (1+xf*U)**3*(1+3*xf*D)*(1+yf*Fv)**5
        if max(D2, U2, F2) > 1e9: return None
        if abs(D2-D) + abs(U2-U) + abs(F2-Fv) < 1e-14: D, U, Fv = D2, U2, F2; break
        D, U, Fv = D2, U2, F2
    v = np.array([D, U, Fv]); h = 1e-7; J = np.zeros((3, 3))
    def rf(w): return np.array([(1+xf*w[1])**2*(1+3*xf*w[0])*(1+yf*w[2])**6, (1+xf*w[1])**3*(1+yf*w[2])**6, (1+xf*w[1])**3*(1+3*xf*w[0])*(1+yf*w[2])**5])
    for j in range(3):
        e = np.zeros(3); e[j] = h; J[:, j] = (rf(v+e) - rf(v-e))/(2*h)
    w, V = np.linalg.eig(J); k = np.argmax(w.real); vec = np.abs(V[:, k].real); vec /= vec.max()
    for dl in (1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2):
        cand = v + dl*vec; Db, Ub, Fb = (F(round(c*10**12), 10**12) for c in cand)
        r = rhs(x, y, Db, Ub, Fb)
        if Db >= r[0] and Ub >= r[1] and Fb >= r[2]:
            Rbar = (1+x*Ub)**3*(1+3*x*Db)*(1+y*Fb)**6; return (Db, Ub, Fb, Rbar, w.real[k])
    return None
def best_cert(p, q, r):
    d1, d2, d3 = devs(p, q, r); e1, e2 = d1, max(d2, d3)
    for tn in range(60, 140):
        t = F(tn, 1000); x = t + e2/t**2; y = e1/t**3
        if x >= F(4, 27): continue
        c = certificate(x, y)
        if c: return t, x, y, c
    return None
for (q, r) in ((1, 2), (1, 1), (2, 4), (1, 3)):
    lo, hi = 1000, 20000
    while lo < hi:
        mid = (lo+hi)//2
        if best_cert(mid, q, r): hi = mid
        else: lo = mid + 1
    t, x, y, (Db, Ub, Fb, Rbar, rho) = best_cert(lo, q, r); d1, d2, d3 = devs(lo, q, r)
    print(f"(p,{q},{r}): least certified p = {lo}: t = {t}, x = {float(x):.5f}, y = {float(y):.3e}, spectral radius {rho:.3f}, R-bar = {float(Rbar):.4f}, bound eps1 R-bar = {float(d1*Rbar):.3e}; eps1 = {d1} , eps2 = {max(d2,d3)}")
    print(f"    certificate D,U,F = {Db}, {Ub}, {Fb}")
import sympy as sp
v = sp.symbols("v", positive=True); print("ceiling: max over v >= 1 of (v-1)/v^3 =", sp.maximum((v-1)/v**3, v, sp.Interval(1, sp.oo)), "= 4/27; max_t t^2(4/27 - t) =", sp.maximum(sp.Symbol('t')**2*(sp.Rational(4,27)-sp.Symbol('t')), sp.Symbol('t'), sp.Interval(0, sp.Rational(4,27))), "=", float(F(256, 531441)))
