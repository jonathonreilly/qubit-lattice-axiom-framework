"""Control C, block 11: the off-line candidates decided by exact interval exclusion.
E1(p,q) = V1 V5^2 - V3^3 and G(p,q) = E2 / (-(p-q)^2) are symmetric in (p, q) (r = 1).  A common positive zero (p0, q0)
with p0 != q0 has p0 and q0 among the positive real roots of R(p) = Res_q(E1, E2).  Those roots are isolated exactly
(Sturm intervals, refined to rational width 10^-12); for every ordered candidate pair the rigorous rational enclosure of
E1 and of G over the box is computed monomial by monomial; a box whose enclosure of E1 or of G excludes 0 is not a common
zero.  Exact rational arithmetic only (sympy Rational); no floats as evidence."""
import sympy as sp
from itertools import product
p, q, r = sp.symbols('p q r', positive=True)
V1 = p**3 + q**3 + 4*r**3; V2 = p*q*(p+q) + 4*r**3; V3 = r*(p**2+q**2) + r**2*(p+q) + 2*r**3; V4 = 2*p*q*r + r**2*(p+q) + 2*r**3; V5 = 3*r**2*(p+q)
E1 = sp.expand((V1*V5**2 - V3**3).subs(r, 1)); E2 = sp.expand((V1*V4**2 - V2*V3**2).subs(r, 1))
G = sp.expand(sp.cancel(sp.factor(E2) / (-(p-q)**2)))
assert sp.expand(E1.subs({p: q, q: p}, simultaneous=True) - E1) == 0 and sp.expand(G.subs({p: q, q: p}, simultaneous=True) - G) == 0
R = sp.resultant(E1, E2, q)
factors = [(f, m) for f, m in sp.factor_list(R)[1] if sp.Poly(f, p).degree() >= 1]
eps = sp.Rational(1, 10**12)
cands = []
for f, m in factors:
    P = sp.Poly(f, p)
    for (a, b), mult in P.intervals():
        if b <= 0: continue
        a2, b2 = P.refine_root(a, b, eps=eps)
        if b2 <= 0: continue
        cands.append((str(f), sp.Rational(a2), sp.Rational(b2)))
print("candidate positive roots of R(p):", [(f, str(a), str(b)) for f, a, b in cands])
def enclosure(poly, box):
    (pa, pb), (qa, qb) = box
    lo = sp.Rational(0); hi = sp.Rational(0)
    for (i, j), c in sp.Poly(poly, p, q).terms():
        mlo = pa**i * qa**j; mhi = pb**i * qb**j  # positive box: monomials increasing
        if c > 0: lo += c*mlo; hi += c*mhi
        else: lo += c*mhi; hi += c*mlo
    return lo, hi
excluded, undecided = [], []
for (f1, a1, b1), (f2, a2, b2) in product(cands, repeat=2):
    box = ((a1, b1), (a2, b2))
    e1 = enclosure(E1, box); g = enclosure(G, box)
    if e1[0] > 0 or e1[1] < 0 or g[0] > 0 or g[1] < 0:
        excluded.append((f1, f2))
    else:
        undecided.append((f1, f2, (str(a1), str(b1)), (str(a2), str(b2)), [str(x) for x in e1], [str(x) for x in g]))
print("ordered candidate pairs:", len(cands)**2, "; excluded by enclosure:", len(excluded))
print("undecided pairs (possible common zeros):")
for u in undecided:
    print("  ", u[0], "x", u[1], "p-box", u[2], "q-box", u[3], "E1 enclosure", u[4], "G enclosure", u[5])
