"""Control D, block 11: decide the two undecided candidate families exactly.
(i) p = r = 1: gcd over Q of E1(1, q) and G(1, q) — a common cubic factor would be an exact exceptional point (1, rho, 1).
(ii) the structure on the line p = r: phi depends only on 'opposite or not' (two classes), K_3 depends on the antipodal pattern;
     pair-additivity there is one equation — derive it and compare with the gcd.
(iii) the sextic pair: a lex Groebner basis of (E1, G) exposes the solution structure; then decide whether the pair
     (sigma_1, sigma_2) is a common zero by exact evaluation of the basis element p - phi(q) (or by the gcd of E1, G
     modulo the sextic)."""
import sympy as sp, time
p, q, r, t = sp.symbols('p q r t', positive=True)
V1 = p**3 + q**3 + 4*r**3; V2 = p*q*(p+q) + 4*r**3; V3 = r*(p**2+q**2) + r**2*(p+q) + 2*r**3; V4 = 2*p*q*r + r**2*(p+q) + 2*r**3; V5 = 3*r**2*(p+q)
E1 = sp.expand((V1*V5**2 - V3**3).subs(r, 1)); E2 = sp.expand((V1*V4**2 - V2*V3**2).subs(r, 1))
G = sp.expand(sp.cancel(sp.factor(E2) / (-(p-q)**2)))
print("(i) p = 1: gcd(E1(1,q), G(1,q)) =", sp.factor(sp.gcd(sp.Poly(E1.subs(p, 1), q), sp.Poly(G.subs(p, 1), q)).as_expr()))
print("    E1(1,q) factored:", sp.factor(E1.subs(p, 1)))
print("    G(1,q) factored:", sp.factor(G.subs(p, 1)))
# (ii) structure on p = r: pattern values with p = r =: 1, q free: K_3 depends on how many antipodal pairs the triple has? enumerate exactly
def orbit(s, u): return 'p' if s == u else ('q' if s//2 == u//2 else 'r')
w = {'p': sp.Integer(1), 'q': q, 'r': sp.Integer(1)}
def Z3(a, b, c): return sp.expand(sum(w[orbit(s, a)]*w[orbit(s, b)]*w[orbit(s, c)] for s in range(6)))
vals = {}
for a in range(6):
    for b in range(6):
        for c in range(6):
            vals.setdefault(Z3(a, b, c), []).append((a, b, c))
print("(ii) distinct Z_3 values on the line p = r (as polynomials in q):", len(vals))
for v, trip in vals.items():
    print("     ", v, "  e.g.", trip[0], " count", len(trip))
# pair-additivity on this line: all cross-ratios c-independent — test the full set of third differences symbolically as ratios,
# collect the distinct nontrivial numerator polynomials
def K3(a, b, c): return Z3(a, b, c)
ratios = set()
import itertools
axes = range(6)
for a, a2, b, b2, c, c2 in itertools.product(axes, repeat=6):
    if a == a2 or b == b2 or c == c2: continue
    num = K3(a,b,c)*K3(a2,b2,c)*K3(a2,b,c2)*K3(a,b2,c2)
    den = K3(a2,b,c)*K3(a,b2,c)*K3(a,b,c2)*K3(a2,b2,c2)
    d = sp.factor(sp.expand(num - den))
    if d != 0: ratios.add(d)
print("     distinct nonzero third-difference numerators on p = r:", len(ratios))
for d in list(ratios)[:6]: print("      ", d)
# (iii) Groebner basis of (E1, G), lex p > q
t0 = time.time()
Gb = sp.groebner([E1, G], p, q, order='lex')
print("(iii) Groebner basis (lex p>q), %d elements, %.1fs:" % (len(Gb.exprs), time.time()-t0))
for g in Gb.exprs:
    print("      ", sp.factor(g) if sp.Poly(g, p, q).total_degree() <= 12 else str(g)[:200])
