"""T18 — THE STRUCTURAL DISCRIMINATOR BETWEEN THE BRANCHES.
Euclidean: Q = m + K with K skew-adjoint in a POSITIVE carrier -> Q^dag Q =
m^2 - K^2 >= m^2 > 0, so Q is invertible for every real m != 0 and the
propagator is unique.
Lorentzian: the mass shell m^2 = q.g^-1.q has REAL solutions, so on a lattice
whose momenta hit the shell, Q becomes SINGULAR - no unique propagator without
a boundary condition.  Test: real zeros of det Q(m) on each branch."""
import sympy as sp
R = sp.Rational
BAS = [(), (0,), (1,), (0,1)]; IDX = {b:i for i,b in enumerate(BAS)}
def epsm(a):
    M = sp.zeros(4,4)
    for Sx in BAS:
        if a in Sx: continue
        T = tuple(sorted(Sx+(a,))); M[IDX[T], IDX[Sx]] = (-1)**sum(1 for i in Sx if i < a)
    return M
def iota(a, gi):
    M = sp.zeros(4,4)
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i); M[IDX[T], IDX[Sx]] += (-1)**pos * gi[a,i]
    return M
m = sp.Symbol("m", real=True)
def branch(g, label, L=4):
    gi = sp.simplify(g.inv())
    Gam = [sp.Matrix(sp.simplify(epsm(a)+iota(a,gi))) for a in range(2)]
    sites = [(x,y) for x in range(L) for y in range(L)]; sid={s:i for i,s in enumerate(sites)}; N=L*L
    K = sp.zeros(4*N,4*N)
    for s in sites:
        for a in range(2):
            for sgn, r in ((+1, ((s[0]+(a==0))%L,(s[1]+(a==1))%L)), (-1, ((s[0]-(a==0))%L,(s[1]-(a==1))%L))):
                i,j = sid[s]*4, sid[r]*4
                for p in range(4):
                    for q in range(4): K[i+p,j+q] += sgn*R(1,2)*Gam[a][p,q]
    # symbol route: eigenvalues of K per momentum, then det Q = prod (m + lambda)
    lams = set()
    for nx in range(L):
        for ny in range(L):
            s0 = sp.sin(2*sp.pi*nx/L); s1 = sp.sin(2*sp.pi*ny/L)
            Msym = sp.I*(s0*Gam[0] + s1*Gam[1])
            for ev in Msym.eigenvals(): lams.add(sp.simplify(ev))
    reals = sorted({sp.simplify(-l) for l in lams if sp.simplify(sp.im(l)) == 0}, key=lambda z: sp.N(z))
    print(f"{label}", flush=True)
    print(f"   distinct symbol eigenvalues: {sorted({str(sp.simplify(l)) for l in lams})}", flush=True)
    print(f"   REAL masses m at which Q is SINGULAR: {[str(r_) for r_ in reals]}", flush=True)
    print(f"   -> unique propagator for all real m != 0 : {len([r_ for r_ in reals if sp.simplify(r_) != 0]) == 0}", flush=True)
branch(sp.Matrix([[1,0],[0,1]]),  "EUCLIDEAN  g = diag(1,1)")
branch(sp.Matrix([[-1,0],[0,1]]), "LORENTZIAN g = diag(-1,1)")
