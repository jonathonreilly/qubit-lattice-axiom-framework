"""R10-4: Lemma PT-q check in FRW minisuperspace with q-dependent gravity couplings.

L = N a^3 [ Omega(q) R + beta(q) R^2 - eps(q) ],  q = A_dot/(N a^3),  flat FRW with lapse N.
Shift symmetry A -> A + const  =>  p_A = dL/dA_dot is conserved (Noether): p_A = -mu.
Check: at a static flat configuration (a = a0, N = 1, q = q0 constant) the N- and a-equations
reduce to eps(q0) - q0 eps'(q0) = 0 and mu = eps'(q0), independent of Omega and beta.
"""
import sympy as sp
from sympy.calculus.euler import euler_equations

t = sp.symbols('t')
N = sp.Function('N')(t); a = sp.Function('a')(t); A = sp.Function('A')(t)
Om = sp.Function('Omega'); be = sp.Function('beta'); eps = sp.Function('eps')
q = sp.diff(A, t) / (N * a**3)
R = 6 / N**2 * (sp.diff(a, t, 2) / a + sp.diff(a, t)**2 / a**2 - sp.diff(a, t) * sp.diff(N, t) / (a * N))
L = N * a**3 * (Om(q) * R + be(q) * R**2 - eps(q))
eqs = euler_equations(L, [N, a, A], t)
a0, q0 = sp.symbols('a0 q0', positive=True)
def static(expr):
    e = expr.lhs if hasattr(expr, 'lhs') else expr
    e = e.doit()
    # substitute derivatives first (highest order first)
    for k in range(4, 0, -1):
        e = e.subs(sp.diff(a, t, k), 0).subs(sp.diff(N, t, k), 0)
    for k in range(4, 1, -1):
        e = e.subs(sp.diff(A, t, k), 0)
    e = e.subs(sp.diff(A, t), q0 * a0**3).subs(N, 1).subs(a, a0)
    return sp.simplify(e)
names = ['N-equation (energy constraint)', 'a-equation (pressure)', 'A-equation']
for nm, e in zip(names, eqs):
    print(nm, ':', static(e), '= 0')
pA = sp.diff(L, sp.diff(A, t))
print('p_A = dL/dA_dot at static flat point :', static(pA), ' (conserved; define mu = -p_A)')
print('=> static flat solution requires eps(q0) - q0*eps\'(q0) = 0 and mu = eps\'(q0); Omega, beta drop out.')
