"""Lemma L (scalar relabelling algebra has no local linear representation with a derivative-like action).
Claim: no Laurent polynomial b(x,z) with b(x,1)=0 and (z d_z b)(1,1) != 0 satisfies
   b(x,yz) b(y,z) - b(y,xz) b(x,z) = beta(x,y) b(xy,z)   for some Laurent polynomial beta.
Proof sketch: top/bottom z-degree (see report). Here: brute-force confirmation over a small coefficient box."""
import itertools, sympy as sp, numpy as np
x, y, z = sp.symbols('x y z')
XS = [0, 1]; ZS = [-1, 0, 1, 2]
cells = list(itertools.product(XS, ZS))
found = 0; tested = 0
def solve_beta(b):
    lhs = sp.expand(b.subs(z, y*z) .subs(x, x) * b.subs({x: y}) - b.subs({x: y, z: x*z}) * b)   # b(x,yz)b(y,z) - b(y,xz)b(x,z)
    # careful: b(x,yz) = b with z->y z ; b(y,z)= b with x->y ; b(y,xz) = b with x->y, z->x z
    lhs = sp.expand(b.subs(z, y*z) * b.subs(x, y) - b.subs({x: y, z: x*z}) * b)
    bxy = sp.expand(b.subs(x, x*y))
    # unknown beta = sum c_{pq} x^p y^q, p,q in [-2,3]
    P = list(itertools.product(range(-2, 4), range(-2, 4)))
    cs = sp.symbols('c0:%d' % len(P))
    beta = sum(c * x**p * y**q for c, (p, q) in zip(cs, P))
    eq = sp.expand(lhs - beta * bxy)
    # collect coefficients over x,y,z monomials (multiply by big power to clear negatives)
    eq = sp.expand(eq * x**8 * y**8 * z**8)
    poly = sp.Poly(eq, x, y, z)
    eqs = poly.coeffs()
    sol = sp.linsolve(eqs, cs)
    return sol != sp.EmptySet
import random
random.seed(1)
coefs = [-1, 0, 1]
allb = []
for vals in itertools.product(coefs, repeat=len(cells)):
    b = sum(v * x**a * z**c for v, (a, c) in zip(vals, cells))
    if b == 0: continue
    if sp.expand(b.subs(z, 1)) != 0: continue            # derivative-like: kills constants
    d = sp.expand(sp.diff(b, z).subs({x: 1, z: 1}))
    if d == 0: continue                                    # nonzero first moment (continuum limit ~ derivative)
    allb.append(b)
print("candidate b's (derivative-like, coefficients in {-1,0,1}, x in {0,1}, z in {-1..2}):", len(allb))
# test a random sample plus all with small support (sample 400) because sympy is slow
sample = random.sample(allb, min(400, len(allb)))
ok = [b for b in sample if solve_beta(b)]
print("of", len(sample), "tested, solutions with a local bracket beta:", len(ok))
print("examples that closed:", ok[:3])
