"""R10-1: symbolic reduction of the one-loop photon speed shift (Dirac sea, Ward-forced Peierls vertex)
to anomaly moments along a k_x line.

Setting (R8-5 BQ class, q along x, transverse current y): x = d h/dk_y is constant along the k_x line.
R8-5 formulas (r85_box_qed.py:6-16, 81-118):
   P_E integrand = (|x|^2 - (x.n)^2)/(2E^3)
   chi_yy(q)     = phi(q) + phi(-q),   phi(q) = [x^2 (1 + n.n(q)) - 2 (x.n)(x.n(q))]/(E + E(q))
   P_M integrand = -phi''(0)      (q -> 0, d(q) = q in the photon box)
   dc_gamma      = (P_M - P_E)/2.
Here h(t), t = k_x, is a generic 4-vector function (Clifford components); hp = h', hpp = h''.
Continuum: hp = e1 (unit, orthogonal to x), hpp = 0.
Anomaly variables (all vanish in the continuum):
   a  = |hp|^2 - 1      (Clifford velocity-norm anomaly)
   b  = h.hpp           (curvature along h)      A_xx = Hess_xx(E^2/2) - 1 = a + b
   c1 = x.hp            (Wilson mixing of vertex and velocity)
   c2 = x.hpp
We find G(h,hp) with L - dG/dt = residual linear in (a,b,c2) and polynomial in c1.
"""
import sympy as sp

t = sp.symbols('t', real=True)
q = sp.symbols('q', real=True)
h = sp.Matrix(sp.symbols('h1:5', real=True))
hp = sp.Matrix(sp.symbols('p1:5', real=True))
hpp = sp.Matrix(sp.symbols('r1:5', real=True))
x = sp.Matrix(sp.symbols('x1:5', real=True))
dot = lambda u, v: (u.T * v)[0]

hq = h + q * hp + q**2 / 2 * hpp
E = sp.sqrt(dot(h, h))
Eq = sp.sqrt(dot(hq, hq))
phi = (dot(x, x) * (E * Eq + dot(h, hq)) - 2 * dot(x, h) * dot(x, hq)) / (E * Eq * (E + Eq))
phi2 = sp.diff(phi, q, 2).subs(q, 0)
PE = (dot(x, x) - dot(x, h)**2 / E**2) / (2 * E**3)
L = sp.Rational(1, 2) * (-phi2 - PE)

# scalar invariants
E2, U, X, X2, a, b, c1, c2 = sp.symbols('E2 U X X2 a b c1 c2', real=True)  # U = h.hp, X = x.h, X2 = x.x
# Express L through invariants: need dot products h.hp, hp.hp, x.hp, h.hpp, x.hpp, hp.hpp(not present?)
subs_map = {}
# brute-force: replace by choosing a basis where symbolic dot products can be read off is hard; instead
# verify numerically at random points that L equals an expression in invariants found below.
Lf = sp.lambdify((h, hp, hpp, x), L, 'math')

# Ansatz: compute L symbolically in terms of invariants by writing every dot product generically.
# Do it by treating dot products as independent symbols via a polynomial substitution trick:
hh, hhp, hphp, xhp, hhpp, xhpp, xx, xh, hphpp, hpphpp = sp.symbols('hh hhp hphp xhp hhpp xhpp xx xh hphpp hpphpp', real=True)
Es = sp.sqrt(hh)
# |hq|^2 to order q^2: hh + 2q hhp + q^2 (hphp + hhpp) + O(q^3)
Eqs = sp.sqrt(hh + 2*q*hhp + q**2*(hphp + hhpp))
hhq = hh + q*hhp + q**2/2*hhpp
xhq = xh + q*xhp + q**2/2*xhpp
phis = (xx*(Es*Eqs + hhq) - 2*xh*xhq)/(Es*Eqs*(Es + Eqs))
phi2s = sp.diff(phis, q, 2).subs(q, 0)
PEs = (xx - xh**2/hh)/(2*Es**3)
Ls = sp.simplify(sp.Rational(1, 2)*(-phi2s - PEs))

# numeric consistency check of the invariant form
import random, math
random.seed(1)
maxerr = 0
for _ in range(20):
    hv = [random.uniform(-1, 1) for _ in range(4)]; hv[3] += 1.5
    pv = [random.uniform(-1, 1) for _ in range(4)]
    rv = [random.uniform(-1, 1) for _ in range(4)]
    xv = [random.uniform(-1, 1) for _ in range(4)]
    d = lambda u, v: sum(i*j for i, j in zip(u, v))
    val = Lf(hv, pv, rv, xv)
    vs = float(Ls.subs({hh: d(hv, hv), hhp: d(hv, pv), hphp: d(pv, pv), xhp: d(xv, pv), hhpp: d(hv, rv),
                        xhpp: d(xv, rv), xx: d(xv, xv), xh: d(xv, hv)}))
    maxerr = max(maxerr, abs(val - vs))
print('invariant form check, max |L - L_inv| =', maxerr)

# Continuum restriction: hphp = 1, hhpp = 0, xhp = 0, xhpp = 0, hhp = t (h1 = t), hh = t^2 + R, xh = X const
R = sp.symbols('R', positive=True)
Lc = sp.simplify(Ls.subs({hphp: 1, hhpp: 0, xhp: 0, xhpp: 0}).subs({hhp: t, hh: t**2 + R}))
print('continuum L(t) =', sp.factor(Lc))
Gc = sp.simplify(sp.integrate(Lc, t))
print('continuum primitive G(t) =', sp.factor(Gc))
# covariantize: t -> hhp (= E E'), t^2 + R -> hh
Gcov = Gc.subs(R, hh - t**2).subs(t, hhp)
Gcov = sp.simplify(Gcov)
print('G_cov(h,hp) =', Gcov)
# dG/dt on the lattice: d(hh)/dt = 2 hhp ; d(hhp)/dt = hphp + hhpp ; d(xh)/dt = xhp
dG = sp.diff(Gcov, hh)*2*hhp + sp.diff(Gcov, hhp)*(hphp + hhpp) + sp.diff(Gcov, xh)*xhp
res = sp.simplify(Ls - dG)
# rewrite residual in anomaly variables
resA = sp.simplify(res.subs({hphp: 1 + a, hhpp: b, xhp: c1, xhpp: c2}))
resA = sp.expand(sp.simplify(resA))
print()
print('residual L - dG/dt in anomaly variables (a=|h\'|^2-1, b=h.h\'\', c1=x.h\', c2=x.h\'\'):')
poly = sp.Poly(resA, a, b, c1, c2)
for mon, coef in zip(poly.monoms(), poly.coeffs()):
    print('  a^%d b^%d c1^%d c2^%d :' % mon, sp.factor(sp.simplify(coef)))
# A-combination test: is the coefficient of a equal to that of b?
ca = sp.simplify(sp.diff(resA, a).subs({a: 0, b: 0, c1: 0, c2: 0}))
cb = sp.simplify(sp.diff(resA, b).subs({a: 0, b: 0, c1: 0, c2: 0}))
print()
print('coef(a) - coef(b) =', sp.simplify(ca - cb))
print('coef(b) =', sp.factor(cb))
