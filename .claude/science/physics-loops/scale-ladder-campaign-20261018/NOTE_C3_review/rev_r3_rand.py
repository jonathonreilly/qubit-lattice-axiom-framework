# Reviewer: R3 for the runner's rand_r3 family (same seed/recipe re-typed, not imported)
from fractions import Fraction as Fr
import numpy as np, sympy as sp
rng = np.random.default_rng(20261018)
A = {}
for r in (-1, 0, 1, 2):
    for c_ in (-1, 0, 1, 2):
        if r != c_:
            A[(r, c_)] = Fr(int(rng.integers(-5, 6)), 7)
for r in (-1, 0, 1, 2):
    s = sum(v for (rr, cc), v in A.items() if rr == r and cc != 0)
    A[(r, 0)] = -s
z, y = sp.symbols("z y")
d = lambda zz: sum(sp.Rational(v.numerator, v.denominator) * zz ** (c_ - r) for (r, c_), v in A.items())
g = sp.expand((d(z * y) - d(z)) * z ** 8)
P = sp.Poly(g, z)
co = [c for m, c in zip(P.monoms(), P.coeffs()) if m[0] != 8]
gg = sp.gcd_list([sp.numer(sp.together(c)) for c in co])
print("d(z) =", sp.factor(d(z)))
print("gcd of non-constant z-coefficients:", sp.factor(gg), "roots:", sp.Poly(gg, y).all_roots())
