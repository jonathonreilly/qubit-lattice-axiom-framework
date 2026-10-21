#!/usr/bin/env python3
"""Exact (sympy) evaluation of the continuum sharp-cutoff TT bubble coefficient: for H = alpha.p,
minimal-coupling vertex O = -(1/2) eps_ij alpha_i k_j at the midpoint momentum, the angular integral
int dOmega F2(n) is computed in closed form (-52 pi/105), giving c_G^sharp = 13 Lambda^2/(840 pi^2)."""
import sys
import sympy as sp
t, x, y, z = sp.symbols('t x y z', real=True)
n = sp.Matrix([x, y, z])                       # unit vector, |n| = 1 imposed after expansion
qh = sp.Matrix([0, 0, 1])
eps = sp.diag(1, -1, 0)/sp.sqrt(2)
a = n + t*qh; b = n - t*qh
na = sp.sqrt(1 + 2*t*z + t**2); nb = sp.sqrt(1 - 2*t*z + t**2)   # |a|, |b| with |n| = 1
o = eps*n/2
o2 = (o.T*o)[0]
num = o2*(1 + (a.T*b)[0]/(na*nb)) - 2*((a.T*o)[0]/na)*((b.T*o)[0]/nb)
F = 2*num/(na + nb)
F2 = sp.expand(sp.series(F, t, 0, 3).removeO().coeff(t, 2))
F0 = sp.expand(sp.series(F, t, 0, 1).removeO())
th, ph = sp.symbols('theta phi', real=True)
sub = {x: sp.sin(th)*sp.cos(ph), y: sp.sin(th)*sp.sin(ph), z: sp.cos(th)}
def sphere(expr):
    e = sp.expand(expr.subs(sub))
    return sp.simplify(sp.integrate(sp.integrate(e*sp.sin(th), (ph, 0, 2*sp.pi)), (th, 0, sp.pi)))
J = sphere(F2)
J0 = sphere(F0)
print('int dOmega F2(n) =', J, '=', sp.N(J, 15))
kG = sp.simplify(-J/(4*(2*sp.pi)**3))
print('c_G^sharp / Lambda^2 =', kG, '=', sp.N(kG, 15))
print('ratio to heat kernel 1/(96 pi^2):', sp.simplify(kG*96*sp.pi**2))
ok = sp.simplify(kG - sp.Rational(13, 840)/sp.pi**2) == 0
print(('PASS' if ok else 'FAIL') + ' [exact] continuum sharp-cutoff TT bubble: c_G = 13 Lambda^2/(840 pi^2) = (52/35) x heat kernel')
print(f"TOTAL: PASS={int(ok)} FAIL={int(not ok)}")
sys.exit(0 if ok else 1)
