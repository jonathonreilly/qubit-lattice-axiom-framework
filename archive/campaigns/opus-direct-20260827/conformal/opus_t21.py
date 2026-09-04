"""T21 — THE TWO-BRANCH RESULT IN 3+1 DIMENSIONS (the physical case).
16-component exterior carrier.  Check the selector, the closure, and the symbol
on Minkowski g = diag(-1,1,1,1): if it closes with V = sqrt(det g) = i and the
symbol is  -q0^2 + q1^2 + q2^2 + q3^2, the light cone is the framework's own in
the dimension that matters.  Also the even-dimension subtlety flagged in
Result 1: in d=4 the middle degree (2-forms) is self-dual, so check whether the
two-half assignment is still consistent."""
import sympy as sp
from itertools import combinations
def basis(d):
    out = []
    for k in range(d+1): out += [tuple(c) for c in combinations(range(d), k)]
    return out
def lam(gi, I, J):
    if len(I) == 0: return sp.Integer(1)
    return sp.Matrix(len(I), len(I), lambda a,b: gi[I[a], J[b]]).det()
def check(g, label):
    d = g.shape[0]; B = basis(d); n = len(B); idx = {b:i for i,b in enumerate(B)}
    gi = sp.simplify(g.inv()); detg = sp.simplify(g.det()); V = sp.sqrt(detg)
    D = sp.zeros(n,n)
    for I in B:
        for J in B:
            if len(I)==len(J): D[idx[I], idx[J]] = sp.simplify(V*lam(gi,I,J))
    def eps(a):
        M = sp.zeros(n,n)
        for Sx in B:
            if a in Sx: continue
            T = tuple(sorted(Sx+(a,))); M[idx[T], idx[Sx]] = (-1)**sum(1 for i in Sx if i<a)
        return M
    Dinv = sp.simplify(D.inv())
    G = [sp.Matrix(n,n, lambda p,q: sp.simplify((eps(a)+Dinv*eps(a).T*D)[p,q])) for a in range(d)]
    qs = sp.symbols(f"q0:{d}")
    Gam = sp.zeros(n,n)
    for a in range(d): Gam += qs[a]*G[a]
    Gsq = sp.Matrix(n,n, lambda p,q: sp.simplify(sp.expand((Gam*Gam)[p,q])))
    tgt = sp.simplify(sp.expand((sp.Matrix([qs])*gi*sp.Matrix([qs]).T)[0,0]))
    ok = sp.Matrix(n,n, lambda p,q: sp.simplify(Gsq[p,q]-(tgt if p==q else 0))).is_zero_matrix
    print(f"{label}  (fibre dim {n})", flush=True)
    print(f"   det g = {detg}   V = {sp.simplify(V)}", flush=True)
    print(f"   Clifford closes: {ok}", flush=True)
    print(f"   symbol = {sp.expand(tgt)}", flush=True)
check(sp.diag(1,1,1,1),   "4D EUCLIDEAN   g = diag(1,1,1,1)")
check(sp.diag(-1,1,1,1),  "4D MINKOWSKI   g = diag(-1,1,1,1)   <-- the physical case")
c = sp.Symbol("c")
gm = sp.diag(-1,1,1,1); gm[1,2] = c; gm[2,1] = c
check(gm, "4D MINKOWSKI with a spatial shear")
