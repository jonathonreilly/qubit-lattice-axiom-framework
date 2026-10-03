"""A34 c6: which law-level tick phases phi(x) (mod tau) treat every site and turn alike UP TO A GLOBAL TIME SHIFT?

Covariance up to a global shift under every translation e forces phi(x+e) - phi(x) = const_e, so
phi(x) = u.x + phi0 (mod tau). Covariance (up to a shift) under the 24 proper turns about any site then
needs R^T u = u (mod tau Z^3) for every turn R. Enumerate u in (tau/q) Z^3, q = 1..24.
Expected (EXACT by hand): u = 0 (one global tick) or u = (tau/2)(1,1,1) (a two-sub-grid checkerboard).
"""
import itertools
import numpy as np
from fractions import Fraction

rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for r in range(3):
            R[r, perm[r]] = sg[r]
        if round(np.linalg.det(R)) == 1:
            rots.append(R)
sols = set()
for q in range(1, 25):
    for a, b, c in itertools.product(range(q), repeat=3):
        u = [Fraction(a, q), Fraction(b, q), Fraction(c, q)]
        ok = True
        for R in rots:
            v = [sum(int(R[j, i]) * u[j] for j in range(3)) for i in range(3)]   # R^T u
            if any((v[i] - u[i]) % 1 != 0 for i in range(3)):
                ok = False
                break
        if ok:
            sols.add(tuple(x % 1 for x in u))
print("u/tau (mod 1) allowed:", sorted(sols))
