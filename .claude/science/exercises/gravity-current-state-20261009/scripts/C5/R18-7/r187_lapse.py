#!/usr/bin/env python3
"""R18-7 [1b]: gauge-invariant (static-slicing) check of the noise's ACTIVE density at O(G^2).
Static metric g = -N^2 dt^2 + (1+2eU) dx^2, N = 1 - eU + e^2 N2.  Exact static identity R_00 = N D^2 N (checked here at O(e^2)),
Einstein with a pressureless static source of static-observer energy density rho_H: R_00 = 4 pi N^2 rho_H.
=> lap N2 = 4 pi U rho + |grad U|^2 + 4 pi rho_H^(1)   (rho = -lap U/4pi).  Units G = c = 1.  Subtraction: none.
"""
import sympy as sp
x, y, z, e = sp.symbols('x y z e', real=True)
X = [sp.Symbol('t'), x, y, z]
U = sp.Function('U')(x, y, z); N2 = sp.Function('N2')(x, y, z)
N = 1 - e*U + e**2*N2
g = sp.diag(-N**2, 1 + 2*e*U, 1 + 2*e*U, 1 + 2*e*U)
gi = sp.diag(*[1/g[i, i] for i in range(4)])
def tr2(expr):
    expr = sp.expand(expr)
    return sum(sp.diff(expr, e, k).subs(e, 0)*e**k/sp.factorial(k) for k in range(3))
D = lambda f, m: 0 if m == 0 else sp.diff(f, X[m])
Gam = [[[tr2(sum(gi[a, d]*(D(g[d, b], c) + D(g[d, c], b) - D(g[b, c], d)) for d in range(4))/2)
         for c in range(4)] for b in range(4)] for a in range(4)]
R00 = 0
for a in range(4):
    R00 += D(Gam[a][0][0], a) - D(Gam[a][0][a], 0)
    for d in range(4):
        R00 += Gam[a][a][d]*Gam[d][0][0] - Gam[a][0][d]*Gam[d][0][a]
R00 = tr2(R00)
gam = 1 + 2*e*U
D2N = tr2(gam**sp.Rational(-3, 2)*sum(sp.diff(gam**sp.Rational(1, 2)*sp.diff(N, v), v) for v in (x, y, z)))
print("[1b] R_00 - N D^2 N at O(e^2) = %s  (static identity)" % sp.simplify(tr2(R00 - N*D2N)))
lapU = sum(sp.diff(U, v, 2) for v in (x, y, z)); g2 = sum(sp.diff(U, v)**2 for v in (x, y, z))
lapN2 = sum(sp.diff(N2, v, 2) for v in (x, y, z))
print("     D^2 N, O(e^2) part = %s" % sp.simplify(D2N.coeff(e, 2)))
print("     check: equals lap N2 - 2U lap U + ... ? residual vs (lapN2 + 2 U lapU - |gradU|^2): %s" % sp.simplify(D2N.coeff(e, 2) - (lapN2 + 2*U*lapU - g2)))
