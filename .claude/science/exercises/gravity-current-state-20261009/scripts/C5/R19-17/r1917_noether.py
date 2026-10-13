"""(v2: sign fixed after v1 run, see r1917_noether_signcheck_v1.out: v1 residual was exactly 2 div T.)
C5 R19-17 (b): Noether identity for a local covariant adiabatic functional of (metric g, lattice labels X).
1+1 dimensions, general metric (g_tt, g_tx, g_xx) and lattice label X(t,x). Site density n = sqrt(g^{mn} dX dX),
lattice frame u^m = eps^{mn} d_n X / (sqrt(-g) n), expansion theta = div u.
Gamma_ad = int sqrt(-g) [ -eps(n) + c(n) theta^2 + d(n) (u.grad n)^2 ]  (order 0 + frame-dependent order-2 terms).
Claim (diffeomorphism invariance): div T_ad^nu = +(1/sqrt(-g)) E_X g^{nu m} d_m X, with T^{mn} = (2/sqrt(-g)) dGamma/dg_mn
and E_X the Euler-Lagrange expression of X.  Checked exactly at random rational points with random polynomial fields."""
import sympy as sp, random
from sympy.calculus.euler import euler_equations
t, x = sp.symbols('t x')
p, q, r, X = [sp.Function(nm)(t, x) for nm in ('p', 'q', 'r', 'X')]
gm = sp.Matrix([[p, q], [q, r]]); detg = p*r - q*q; sg = sp.sqrt(-detg); gi = gm.inv()
co = (t, x)
dX = [sp.diff(X, c) for c in co]
n = sp.sqrt(sum(gi[i, j]*dX[i]*dX[j] for i in range(2) for j in range(2)))
epsmn = [[0, 1], [-1, 0]]
u = [sum(epsmn[m][k]*dX[k] for k in range(2))/(sg*n) for m in range(2)]
theta = sum(sp.diff(sg*u[m], co[m]) for m in range(2))/sg
udn = sum(u[m]*sp.diff(n, co[m]) for m in range(2))
eps = lambda y: y**2 + y**4/5
cfun = lambda y: 1/(1 + y**2)
dfun = lambda y: y/3
Lag = sg*(-eps(n) + cfun(n)*theta**2 + dfun(n)*udn**2)
print('building Euler-Lagrange expressions ...', flush=True)
EL = euler_equations(Lag, [p, q, r, X], [t, x])
ELp, ELq, ELr, ELX = [e.lhs for e in EL]
# T^{mn} = (2/sg) dS/dg_mn ; q appears for both tx and xt
Tup = sp.Matrix([[2*ELp/sg, ELq/sg], [ELq/sg, 2*ELr/sg]])
random.seed(7)
def rpoly(c0):
    return c0 + sum(sp.Rational(random.randint(-3, 3), random.randint(4, 9))*t**i*x**j for i in range(3) for j in range(3) if 0 < i + j <= 2)
subsd = {p: -1 + rpoly(0)/5, q: rpoly(0)/7, r: 1 + rpoly(0)/5, X: x + rpoly(0)/4}
print('substituting explicit fields ...', flush=True)
Ts = Tup.subs(subsd).doit(); ELXs = ELX.subs(subsd).doit()
gms = gm.subs(subsd); gis = gms.inv(); sgs = sp.sqrt(-gms.det())
Gam = [[[sum(gis[a, d]*(sp.diff(gms[d, b], co[c]) + sp.diff(gms[d, c], co[b]) - sp.diff(gms[b, c], co[d])) for d in range(2))/2
         for c in range(2)] for b in range(2)] for a in range(2)]
dXs = [sp.diff(subsd[X], c) for c in co]
for pt in [(sp.Rational(1, 3), sp.Rational(-2, 7)), (sp.Rational(-1, 5), sp.Rational(1, 2))]:
    sub = {t: pt[0], x: pt[1]}
    res = []
    for nu in range(2):
        div = sum(sp.diff(Ts[m, nu], co[m]) for m in range(2)) \
            + sum(Gam[m][m][l]*Ts[l, nu] for m in range(2) for l in range(2)) \
            + sum(Gam[nu][m][l]*Ts[m, l] for m in range(2) for l in range(2))
        rhs = +ELXs*sum(gis[nu, m]*dXs[m] for m in range(2))/sgs
        val = sp.N((div - rhs).subs(sub), 30); scale = sp.N(div.subs(sub), 30)
        res.append((val, scale))
    print(f'point {pt}: [div T^nu - E_X d^nu X/sqrt(-g)] = {res[0][0]:.3e}, {res[1][0]:.3e}   (div T^nu itself: {res[0][1]:.3e}, {res[1][1]:.3e})', flush=True)
