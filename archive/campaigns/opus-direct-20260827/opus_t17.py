"""T17 — DOES RECORD POSITIVITY SELECT THE EUCLIDEAN BRANCH?
The two-faces conjecture: propagation closes on both branches of V^2 = det g,
but RECORDS need positive weights, and on the Lorentzian (imaginary-volume)
branch the carrier is complex.  Test positivity of the on-site record gram on
BOTH branches, same lattice, same mass."""
import sympy as sp
R = sp.Rational; I = sp.I
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
def run(g, label, L=4, m=R(1,2)):
    gi = sp.simplify(g.inv()); detg = sp.simplify(g.det()); V = sp.sqrt(detg)
    D = sp.zeros(4,4)
    D[0,0] = V; D[3,3] = sp.simplify(V*gi.det())
    D[1,1] = sp.simplify(V*gi[0,0]); D[2,2] = sp.simplify(V*gi[1,1])
    D[1,2] = sp.simplify(V*gi[0,1]); D[2,1] = sp.simplify(V*gi[1,0])
    Gam = [sp.Matrix(sp.simplify(epsm(a)+iota(a,gi))) for a in range(2)]
    sites = [(x,y) for x in range(L) for y in range(L)]; sid = {s:i for i,s in enumerate(sites)}; N=L*L
    K = sp.zeros(4*N,4*N)
    for s in sites:
        for a in range(2):
            for sgn, r in ((+1, ((s[0]+(a==0))%L, (s[1]+(a==1))%L)), (-1, ((s[0]-(a==0))%L, (s[1]-(a==1))%L))):
                i,j = sid[s]*4, sid[r]*4
                for p in range(4):
                    for q in range(4): K[i+p,j+q] += sgn*R(1,2)*Gam[a][p,q]
    Q = sp.Matrix(4*N,4*N, lambda i,j: (m if i==j else 0)+K[i,j])
    Qi = Q.inv()
    G = sp.Matrix(4,4, lambda p,q: sp.simplify(R(1,2)*(Qi[p,q]+sp.conjugate(Qi[q,p]))))
    tr = sp.simplify(sum(G[k,k] for k in range(4)))
    mins = [sp.simplify(G[:k,:k].det()) for k in range(1,5)]
    diag = [sp.simplify(G[k,k]/tr) for k in range(4)]
    realdiag = all(sp.simplify(sp.im(d)) == 0 for d in diag)
    posdiag = all(sp.simplify(sp.re(d)) > 0 for d in diag) if realdiag else False
    print(f"{label}:  det g = {detg}, V = {sp.simplify(V)}", flush=True)
    print(f"   record weights = {[str(d) for d in diag]}", flush=True)
    print(f"   weights REAL: {realdiag}    all POSITIVE: {posdiag}", flush=True)
    print(f"   gram leading minors: {[str(x) for x in mins]}", flush=True)
run(sp.Matrix([[1,0],[0,1]]),  "EUCLIDEAN  g = diag(1,1)")
run(sp.Matrix([[-1,0],[0,1]]), "LORENTZIAN g = diag(-1,1)")
