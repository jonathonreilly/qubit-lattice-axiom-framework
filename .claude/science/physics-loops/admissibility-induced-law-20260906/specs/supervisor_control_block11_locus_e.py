"""Control E, block 11: the sextic candidate pair decided exactly via the lex Groebner basis of (E1, G).
The basis has a univariate h(q) and an element linear in p: A(q) p - B(q).  On a factor m(q) of h, p = B/A mod m.
Test: is p0 = (B/A mod m)(sigma) a root of the sextic, and does it equal sigma_1 (the (1,2) root) when q = sigma_2?"""
import sympy as sp
p, q, r = sp.symbols('p q r', positive=True)
V1 = p**3 + q**3 + 4*r**3; V2 = p*q*(p+q) + 4*r**3; V3 = r*(p**2+q**2) + r**2*(p+q) + 2*r**3; V4 = 2*p*q*r + r**2*(p+q) + 2*r**3; V5 = 3*r**2*(p+q)
E1 = sp.expand((V1*V5**2 - V3**3).subs(r, 1)); E2 = sp.expand((V1*V4**2 - V2*V3**2).subs(r, 1))
G = sp.expand(sp.cancel(sp.factor(E2) / (-(p-q)**2)))
Gb = sp.groebner([E1, G], p, q, order='lex')
h = [g for g in Gb.exprs if not g.has(p)][0]
print("h(q) factored:", sp.factor(h))
lin = [g for g in Gb.exprs if sp.Poly(g, p).degree() == 1][0]
A = sp.Poly(lin, p).coeff_monomial(p); B = -sp.Poly(lin, p).coeff_monomial(1)
A = sp.expand(A); B = sp.expand(B)
print("linear element: A(q) =", sp.factor(A))
sext = q**6 - 6*q**5 - 3*q**4 + 4*q**3 - 3*q**2 - 6*q + 31
m = sp.Poly(sext, q)
# p mod m
Ainv = sp.invert(sp.Poly(A, q), m)  # A^{-1} mod m
psi = (sp.Poly(B, q) * Ainv).rem(m)
print("psi(q) = p mod sextic:", psi.as_expr())
# is psi a root of the sextic modulo m?  m(psi) mod m
comp = sp.Poly(sext.subs(q, psi.as_expr()), q).rem(m)
print("sextic(psi) mod sextic = 0 ?", comp.is_zero)
# which root: enclose psi(q) over the isolating interval of each positive root of the sextic (exact rational enclosure of a univariate polynomial on an interval via monotone-term bounds is not valid for mixed signs; use the sextic's refined interval and Horner with interval arithmetic)
def horner_interval(poly, a, b):
    # interval Horner for q in [a, b] with a, b positive rationals
    lo, hi = sp.Rational(0), sp.Rational(0)
    for c in sp.Poly(poly, q).all_coeffs():
        # multiply [lo, hi] by [a, b] (a, b > 0): products of endpoints
        cands = [lo*a, lo*b, hi*a, hi*b]
        lo, hi = min(cands) + c, max(cands) + c
    return lo, hi
eps = sp.Rational(1, 10**30)
for (a, b), mult in m.intervals():
    if b <= 0: continue
    a2, b2 = m.refine_root(a, b, eps=eps)
    lo, hi = horner_interval(psi.as_expr(), sp.Rational(a2), sp.Rational(b2))
    print(f"root of the sextic in ({float(a2):.12f}, {float(b2):.12f}): p = psi(q) in ({float(lo):.12f}, {float(hi):.12f})  [floats are labels only]")
# cross-check: also evaluate E1 and G at (psi(q), q) modulo m exactly
E1m = sp.Poly(E1.subs(p, psi.as_expr()), q).rem(m); Gm = sp.Poly(G.subs(p, psi.as_expr()), q).rem(m)
print("E1(psi(q), q) mod sextic = 0 ?", E1m.is_zero, "; G(psi(q), q) mod sextic = 0 ?", Gm.is_zero)
# and the other factors of h: p mod each factor
for fac, mult in sp.factor_list(h)[1]:
    P = sp.Poly(fac, q)
    if P.degree() < 1: continue
    try:
        Ai = sp.invert(sp.Poly(A, q), P); ps = (sp.Poly(B, q) * Ai).rem(P)
        pos = [(float(P.refine_root(a, b, eps=sp.Rational(1,10**8))[0])) for (a, b), mm in P.intervals() if b > 0]
        print("factor", fac, "positive roots (labels):", pos, "; p = ", ps.as_expr() if P.degree() <= 3 else "(degree %d expression)" % P.degree())
    except Exception as e:
        print("factor", fac, ": A not invertible mod factor ->", e)
