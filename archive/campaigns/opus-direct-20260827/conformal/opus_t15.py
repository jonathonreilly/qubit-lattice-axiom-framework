"""T15 — THE LORENTZIAN BRANCH OF THE FRAMEWORK'S OWN SELECTOR.
Result 1: the rule propagates iff the exterior weights are degree-uniform,
which for the two-half carrier is  V^2 = det g.  That condition is ALGEBRAIC —
it never asked for V > 0.  For a LORENTZIAN metric det g < 0, so the same
condition forces  V = i |V| : an IMAGINARY volume element.  Wick rotation is
not performed by hand here; it is the second branch of the framework's own
closure condition.
TEST: put g = diag(-1, 1) (and the 3D/4D analogues), set V^2 = det g, and ask
whether the Clifford relation still closes and what the symbol becomes.
If it closes, the symbol is  q^T g^-1 q = -q_t^2 + q_x^2 : A LIGHT CONE."""
import sympy as sp
from itertools import combinations
I = sp.I
def basis(d):
    out = []
    for k in range(d+1): out += [tuple(c) for c in combinations(range(d), k)]
    return out
def lam(gi, Ii, Jj):
    if len(Ii) == 0: return sp.Integer(1)
    return sp.Matrix(len(Ii), len(Ii), lambda a,b: gi[Ii[a], Jj[b]]).det()
def check(d, g, label):
    B = basis(d); n = len(B); idx = {b:i for i,b in enumerate(B)}
    gi = sp.together(g.inv()); detg = sp.expand(g.det())
    V = sp.sqrt(detg)                      # the selector, both branches
    rho = [V]*(d+1)                        # degree-uniform (Result 1)
    D = sp.zeros(n, n)
    for Ii in B:
        for Jj in B:
            if len(Ii) == len(Jj): D[idx[Ii], idx[Jj]] = sp.simplify(rho[len(Ii)]*lam(gi, Ii, Jj))
    def eps(a):
        M = sp.zeros(n, n)
        for Sx in B:
            if a in Sx: continue
            T = tuple(sorted(Sx+(a,))); M[idx[T], idx[Sx]] = (-1)**sum(1 for i in Sx if i < a)
        return M
    Dinv = sp.simplify(D.inv())
    G = [sp.Matrix(n, n, lambda p,q: sp.simplify((eps(a) + Dinv*eps(a).T*D)[p,q])) for a in range(d)]
    qs = sp.symbols(f"q0:{d}")
    Gam = sp.zeros(n, n)
    for a in range(d): Gam += qs[a]*G[a]
    Gsq = sp.Matrix(n, n, lambda p,q: sp.simplify(sp.expand((Gam*Gam)[p,q])))
    tgt = sp.simplify(sp.expand((sp.Matrix([qs])*gi*sp.Matrix([qs]).T)[0,0]))
    resid = sp.Matrix(n, n, lambda p,q: sp.simplify(Gsq[p,q] - (tgt if p==q else 0)))
    print(f"{label}", flush=True)
    print(f"   det g = {detg}   selector volume V = sqrt(det g) = {sp.simplify(V)}"
          f"   {'IMAGINARY -> Lorentzian branch' if sp.im(sp.N(V)) != 0 else 'real -> Riemannian branch'}", flush=True)
    print(f"   Clifford closes: {resid.is_zero_matrix}", flush=True)
    print(f"   symbol  Gamma(q)^2 = {sp.expand(tgt)}", flush=True)
    return resid.is_zero_matrix, sp.expand(tgt)
check(2, sp.Matrix([[1,0],[0,1]]), "2D EUCLIDEAN  g = diag(1,1)")
check(2, sp.Matrix([[-1,0],[0,1]]), "2D LORENTZIAN g = diag(-1,1)")
check(3, sp.diag(-1,1,1), "3D LORENTZIAN g = diag(-1,1,1)")
c = sp.Symbol("c")
check(2, sp.Matrix([[-1, c],[c, 1]]), "2D LORENTZIAN with shear g = [[-1,c],[c,1]]")
print("\nREADING: on the Lorentzian branch the symbol is  -q_t^2 + q_x^2 (+...)", flush=True)
print("i.e. a LIGHT CONE, and the on-shell condition m^2 + q.g^-1.q = 0 becomes", flush=True)
print("the relativistic mass shell rather than a positive-definite spectrum.", flush=True)
