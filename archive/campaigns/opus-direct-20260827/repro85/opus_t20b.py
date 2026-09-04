"""T20 — REFLECTION POSITIVITY: the rigorous branch selector.
Osterwalder-Schrader positivity is the property that turns a Euclidean theory
into a quantum one with a positive Hamiltonian and a Hilbert space.  Test it
directly on both branches: with theta the reflection about a time slice, the
form  <theta f, G f>  on fields supported at positive times must be PSD.
This is the rigorous version of 'records need the Euclidean branch', and it
connects to the lane's landed OS machinery (Blocks 195-199)."""
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
            T = tuple(x for x in Sx if x != i); M[IDX[T], IDX[Sx]] += (-1)**pos*gi[a,i]
    return M
def os_test(g, label, L=4, m=R(1,2)):
    gi = sp.simplify(g.inv())
    Gam = [sp.Matrix(sp.simplify(epsm(a)+iota(a,gi))) for a in range(2)]
    sites = [(t,x) for t in range(L) for x in range(L)]
    sid = {s:i for i,s in enumerate(sites)}; N = L*L
    K = sp.zeros(4*N,4*N)
    for s in sites:
        for a in range(2):
            for sgn, r in ((+1, ((s[0]+(a==0))%L,(s[1]+(a==1))%L)), (-1, ((s[0]-(a==0))%L,(s[1]-(a==1))%L))):
                i,j = sid[s]*4, sid[r]*4
                for p in range(4):
                    for q in range(4): K[i+p,j+q] += sgn*R(1,2)*Gam[a][p,q]
    Q = sp.Matrix(4*N,4*N, lambda i,j: (m if i==j else 0)+K[i,j])
    G = Q.inv()
    # reflection about the slice t = 0 : theta(t, x) = (-t mod L, x)
    pos = [s for s in sites if 1 <= s[0] <= L//2 - 1]     # strictly positive times
    n = len(pos)*4
    M_ = sp.zeros(n, n)
    for A, sa in enumerate(pos):
        ta = ((-sa[0]) % L, sa[1])
        for B, sb in enumerate(pos):
            for p in range(4):
                for q in range(4):
                    M_[A*4+p, B*4+q] = G[sid[ta]*4+p, sid[sb]*4+q]
    Msym = sp.Matrix(n, n, lambda i,j: sp.simplify(R(1,2)*(M_[i,j]+sp.conjugate(M_[j,i]))))
    iszero = Msym.is_zero_matrix
    rk = Msym.rank()
    mins = [sp.simplify(Msym[:k,:k].det()) for k in range(1, min(n,6)+1)]
    ev = Msym.eigenvals() if n <= 24 else None
    print(f"{label}: OS form on {len(pos)} positive-time sites ({n}x{n})", flush=True)
    print(f"   form identically zero: {iszero}      rank: {rk} of {n}", flush=True)
    print(f"   first leading minors: {[str(sp.nsimplify(x)) for x in mins]}", flush=True)
    if ev is not None:
        sgn = {"pos":0,"neg":0,"zero":0}
        for e, mlt in ev.items():
            r = sp.simplify(sp.re(e))
            sgn["zero" if r == 0 else ("pos" if r > 0 else "neg")] += mlt
        print(f"   eigenvalue signs: {sgn}", flush=True)
        strict = sgn["neg"] == 0 and sgn["zero"] == 0
        semi = sgn["neg"] == 0
        print(f"   REFLECTION POSITIVE strictly: {strict}   positive SEMI-definite: {semi}", flush=True)
os_test(sp.Matrix([[1,0],[0,1]]),  "EUCLIDEAN  g = diag(1,1)")
os_test(sp.Matrix([[-1,0],[0,1]]), "LORENTZIAN g = diag(-1,1)")
