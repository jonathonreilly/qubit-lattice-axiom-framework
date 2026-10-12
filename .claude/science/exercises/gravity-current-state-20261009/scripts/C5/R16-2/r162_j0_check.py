"""Check the closed-form q0 integrals used by the scalar on-shell runner, at p0 = iE with E < E_k (no pole crossing):
J1 = int dq0/2pi 1/((q0^2+W^2)((p0-q0)^2+Ek^2)),  J0 = int dq0/2pi (2 p0 - q0)^2/((q0^2+W^2)((p0-q0)^2+Ek^2))."""
import numpy as np, sympy as sp
from scipy.integrate import quad
a, b, e = sp.symbols('a b e', positive=True)
J0 = -(2*e-a)**2/(2*a*(b**2-(a-e)**2)) - (e-b)**2/(2*b*(a**2-(e+b)**2))
J0s = sp.factor(sp.simplify(J0))
J1 = (a+b)/(2*a*b*((a+b)**2-e**2))
print('J0 simplified:', J0s)
f0 = sp.lambdify((a, b, e), J0s); f1 = sp.lambdify((a, b, e), J1)
for (W, Ek, E) in [(0.3, 0.5, 0.2), (1.0, 0.7, 0.4), (0.05, 0.12, 0.1), (2.0, 1.5, 1.2)]:
    p0 = 1j*E
    g1 = lambda q: (1/((q*q+W*W)*((p0-q)**2+Ek*Ek))).real
    g0 = lambda q: ((2*p0-q)**2/((q*q+W*W)*((p0-q)**2+Ek*Ek))).real
    n1 = quad(g1, -np.inf, np.inf, limit=400)[0]/(2*np.pi); n0 = quad(g0, -np.inf, np.inf, limit=400)[0]/(2*np.pi)
    i1 = quad(lambda q: (1/((q*q+W*W)*((p0-q)**2+Ek*Ek))).imag, -np.inf, np.inf, limit=400)[0]
    print('W=%.2f Ek=%.2f E=%.2f  J1 closed %.12f numeric %.12f | J0 closed %.12f numeric %.12f | Im part %.1e'
          % (W, Ek, E, f1(W, Ek, E), n1, f0(W, Ek, E), n0, i1))
