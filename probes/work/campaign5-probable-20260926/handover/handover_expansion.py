"""Exact local form of the comparator's merged touching at the handover (J = 1, kappa = 1/2, f = (1/4, 3/4, 1/2)): D = det H, its
gradient and Hessian, and the weighted-degree-4 part with u = d1 - d2 (weight 2), v = d1 + d2, t = d3 (weight 1)."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import sympy as sp
from kc_aniso import Dsym, z1, z2, w, kk, JJ
D, _ = Dsym()
u, v, t, eps = sp.symbols("u v t eps", real=True)
Dx = sp.expand(D.subs({JJ: 1, kk: sp.Rational(1, 2)}))
d1 = eps * v / 2 + eps ** 2 * u / 2; d2 = eps * v / 2 - eps ** 2 * u / 2; d3 = eps * t
E = lambda base, d: base * sp.exp(2 * sp.pi * sp.I * d)
ser = sp.series(sp.expand(Dx.subs({z1: E(sp.I, d1), z2: E(-sp.I, d2), w: E(-1, d3)})), eps, 0, 5).removeO()
print("orders eps^0..3:", [sp.simplify(ser.coeff(eps, k)) for k in range(4)])
q4 = sp.factor(sp.nsimplify(sp.simplify(sp.expand(ser.coeff(eps, 4)))))
print("weighted-degree-4 part:", q4)
s = sp.symbols("s", real=True)
f = 64 * (s ** 2 - s + 1) ** 2 - sp.Rational(128, 3) * (s - 1) ** 2      # after completing the square in u, per t^4, v = s t
print("residual quartic in s:", sp.expand(f), "real roots:", sp.real_roots(sp.Poly(sp.expand(3 * f), s)))
