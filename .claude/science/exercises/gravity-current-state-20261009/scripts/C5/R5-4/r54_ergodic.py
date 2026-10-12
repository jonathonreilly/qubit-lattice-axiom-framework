"""C5 R5-4 (3): an element of Gamma = SO+(Q7,Z) acting ergodically on T^4 (needed for the dichotomy theorem).
A toral automorphism is Haar-ergodic iff no eigenvalue is a root of unity (Halmos). Its dual action on
quasi-momenta is gamma^{-T}, with the inverse eigenvalues. Check: characteristic polynomial irreducible
over Q and not cyclotomic (an irreducible polynomial with a root-of-unity root is cyclotomic)."""
import sympy as sp
def emb(a, b, c, d, i, j):
    M = sp.eye(4); M[i, i], M[i, j], M[j, i], M[j, j] = a, b, c, d; return M
G7 = sp.diag(-7, 1, 1, 1)
B1, B2, B3 = emb(8, 3, 21, 8, 0, 1), emb(8, 3, 21, 8, 0, 2), emb(8, 3, 21, 8, 0, 3)
x = sp.symbols('x')
for name, g in (("B1", B1), ("B1*B2", B1*B2), ("B1*B2*B3", B1*B2*B3)):
    assert g.T*G7*g == G7 and g.det() == 1 and g[0, 0] > 0
    for nm, h in ((name, g), (name + " dual (g^-T)", g.inv().T)):
        cp = sp.factor_list(h.charpoly(x).as_expr())
        ev = [complex(e) for e in sp.Poly(h.charpoly(x).as_expr(), x).nroots(n=15, maxsteps=500)]
        print(f"{nm:22s} charpoly factors over Q: {cp[1]};  |eigenvalues| = {[round(abs(e), 6) for e in ev]}")
    print("   cyclotomic test (irreducible deg-4 factor, non-cyclotomic):",
          all(sp.Poly(f, x).degree() == 4 and not sp.Poly(f, x).is_cyclotomic for f, _ in sp.factor_list(g.charpoly(x).as_expr())[1]))
