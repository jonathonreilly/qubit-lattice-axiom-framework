"""Supervisor control, block 11: the exceptional locus of the three-body term (exact algebra, sympy over Q).
Values of Z_3 by pattern on the six-menu: V1 (x,x,x), V2 (x,x,-x), V3 (x,x,y), V4 (x,-x,y), V5 (x,y,z).
Pair-additivity of log K_3 <=> every cross-ratio CR_c(a,a',b,b') is c-independent.
Witness W1: (a,a',b,b') = (x,y,x,y), c in {x,z}: E1 := V1*V5^2 - V3^3 = 0.
Witness W2: (a,a',b,b') = (x,-x,x,-x), c in {x,y}: E2 := V1*V4^2 - V2*V3^2 = 0.
(1) k = 2: Delta_2 log K_2 vanishes iff K^2 has rank one iff p = q = r (eigenvalues of K).
(2) on the line p = q = t r: E1 reduces to (t-1)^3 (t^3 - 3t^2 - 6t - 1); the positive root t* of the cubic is an exceptional point.
(3) for p != q: the common zeros of E1 and E2 (dehomogenized r = 1) by resultant and exact root isolation.
(4) at p = q: all third differences vanish iff W2^3 = W1 W3^2 (the 3-axis collapse) -- a structural check on the patterns.
"""
import sympy as sp
p, q, r, t = sp.symbols('p q r t', positive=True)
V1 = p**3 + q**3 + 4*r**3
V2 = p*q*(p+q) + 4*r**3
V3 = r*(p**2+q**2) + r**2*(p+q) + 2*r**3
V4 = 2*p*q*r + r**2*(p+q) + 2*r**3
V5 = 3*r**2*(p+q)
# sanity: recompute the pattern values from the definition on the six-menu
def orbit(s, u):
    return 'p' if s == u else ('q' if s//2 == u//2 else 'r')
w = {'p': p, 'q': q, 'r': r}
def Z3(a, b, c):
    return sum(w[orbit(s, a)]*w[orbit(s, b)]*w[orbit(s, c)] for s in range(6))
x, mx, y, my, z, mz = 0, 1, 2, 3, 4, 5
checks = [sp.simplify(Z3(x,x,x)-V1), sp.simplify(Z3(x,x,mx)-V2), sp.simplify(Z3(x,x,y)-V3), sp.simplify(Z3(x,mx,y)-V4), sp.simplify(Z3(x,y,z)-V5)]
print("pattern values verified:", all(c == 0 for c in checks))
E1 = sp.expand(V1*V5**2 - V3**3)
E2 = sp.expand(V1*V4**2 - V2*V3**2)
print("=== (1) k=2: eigenvalues of K (Z_1 K): 1, (p-q)/Z1 x3, (p+q-2r)/Z1 x2 -> K^2 rank one iff p=q=r; the ratio K2(a,b)K2(0,0)/(K2(a,0)K2(0,b)) at (a,b)=(-x,-x):")
Z1 = p + q + 4*r
K2 = lambda a, b: sum(w[orbit(s, a)]*w[orbit(s, b)] for s in range(6))
ratio22 = sp.factor(K2(mx, mx)*K2(x, x)/(K2(mx, x)*K2(x, mx)))
print("   ratio =", ratio22, " (= 1 iff p = q; the (x,y|x,y) witness for p=q:", sp.factor(K2(y, y)*K2(x, x)/(K2(y, x)*K2(x, y))), ")")
print("=== (2) the line p = q = t r")
E1t = sp.factor(E1.subs({p: t, q: t, r: 1}))
E2t = sp.factor(E2.subs({p: t, q: t, r: 1}))
print("   E1 on the line:", E1t)
print("   E2 on the line:", E2t)
cubic = sp.Poly(t**3 - 3*t**2 - 6*t - 1, t)
roots = sp.Poly(cubic).intervals()
print("   real roots of t^3-3t^2-6t-1 (isolating intervals):", roots)
tstar_iv = [iv for iv, m in roots if iv[0] > 0][0]
print("   positive root t* in", tstar_iv, "~", sp.N(sp.Poly(cubic).nroots()[-1], 12), "(numeric label only)")
print("=== (3) common zeros of E1, E2 off the line p = q (r = 1)")
E1r = sp.Poly(E1.subs(r, 1), p, q); E2r = sp.Poly(E2.subs(r, 1), p, q)
# remove the trivial factor structure: factor both
print("   factor E1:", sp.factor(E1.subs(r,1)))
print("   factor E2:", sp.factor(E2.subs(r,1)))
res = sp.resultant(E1.subs(r,1), E2.subs(r,1), q)
resf = sp.factor(res)
print("   resultant in p (factored):", resf)
# positive real roots of the resultant
for fac, mult in sp.factor_list(res)[1]:
    P = sp.Poly(fac, p)
    if P.degree() >= 1:
        ivs = [iv for iv, m in P.intervals() if iv[1] > 0]
        print("      factor", fac, "degree", P.degree(), "positive real root intervals:", ivs)
print("=== (4) at p = q: all third differences vanish iff W2^3 = W1 W3^2 (structural): W1 =", sp.factor(V1.subs({p:t,q:t,r:1})), "W2 =", sp.factor(V3.subs({p:t,q:t,r:1})), "W3 =", sp.factor(V5.subs({p:t,q:t,r:1})))
print("   W2^3 - W1 W3^2 =", sp.factor((V3**3 - V1*V5**2).subs({p:t,q:t,r:1})))
