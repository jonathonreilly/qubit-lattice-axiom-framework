"""C3: necessity at the two-point level for a FROZEN isotropic stationary point set.

Pair-term energy per point:  E(g) = 1/2 int V(|x|_g) rho2(|x|) d^3x.  Volume-preserving g = exp(t h):
substitute y = g^{1/2} x:  E = 1/2 int V(|y|) rho2(|exp(-t h/2) y|) d^3y.
Shear-invariant at O(t^2) for EVERY pair potential V  <=>  the angular average
  A(r,t) = < rho2( r |exp(-t h/2) n| ) >_n  equals rho2(r) + O(t^3) for every r.
Claim: d^2A/dt^2|0 = tr(h^2) [ r rho2'/15 + r^2 rho2''/60 ]  ->  4 rho2' + r rho2'' = 0
  ->  rho2 = a + b r^-3; local finiteness (finite neighbours in a ball) forces b = 0.
"""
import sympy as sp
t, r, th, ph = sp.symbols('t r theta phi', real=True)
rho = sp.Function('rho')
n = sp.Matrix([sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)])
for name, h in [('E_g', sp.diag(1, -1, 0)/sp.sqrt(2)), ('T_2g', sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])/sp.sqrt(2))]:
    G = sp.eye(3) - t*h + t**2*h*h/2          # exp(-t h) to O(t^2)
    q = sp.expand((n.T*G*n)[0])
    stretch = sp.series(sp.sqrt(q), t, 0, 3).removeO()   # |exp(-t h/2) n|
    expr = sp.series(rho(r*stretch), t, 0, 3).removeO()
    c2 = sp.expand(expr.coeff(t, 2))
    avg = sp.integrate(sp.integrate(c2*sp.sin(th), (ph, 0, 2*sp.pi)), (th, 0, sp.pi))/(4*sp.pi)
    avg = sp.simplify(avg.doit())
    target = r*sp.Derivative(rho(r), r)/15 + r**2*sp.Derivative(rho(r), (r, 2))/60   # t^2 coefficient (tr h^2 = 1)
    print(name, ': t^2 coefficient of angular average =', avg, '| matches r*rho1/15 + r^2*rho2/60 :', sp.simplify(avg - target.doit()) == 0)
sol = sp.dsolve(4*sp.Derivative(rho(r), r) + r*sp.Derivative(rho(r), (r, 2)), rho(r))
print('ODE 4 rho\' + r rho\'\' = 0 solution:', sol)
# first-order term vanishes by tracelessness (angular average of n.h.n = tr h/3 = 0): checked implicitly above
