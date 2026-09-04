"""T22 - REFLECTION POSITIVITY done properly: canonical fibre reflection.
The OS reflection of a FORM field under x^0 -> -x^0 is the pullback r*, which
sends e^0 -> -e^0 and e^i -> e^i, i.e. Theta_fib e_S = (-1)^[0 in S] e_S.
T20 used the identity on the fibre; here the canonical Theta is used, and all
four diagonal sign patterns are scanned as a robustness check.  A branch is
OS-positive iff the Hermitian form <theta f, G f> on strictly-positive-time
fields is positive semidefinite."""
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
CANON = [(-1)**(1 if 0 in b else 0) for b in BAS]     # +1,-1,+1,-1
PATTERNS = {"CANONICAL r* (e0->-e0)": CANON, "identity": [1,1,1,1],
            "degree parity": [1,-1,-1,1], "e1 flip": [1,1,-1,-1]}
def run(g, label, L=4, m=R(1,2)):
    gi = sp.simplify(g.inv())
    Gam = [sp.Matrix(sp.simplify(epsm(a)+iota(a,gi))) for a in range(2)]
    sites = [(t,x) for t in range(L) for x in range(L)]
    sid = {s:i for i,s in enumerate(sites)}; N = L*L
    K = sp.zeros(4*N,4*N)
    for s in sites:
        for a in range(2):
            for sgn, r in ((+1, ((s[0]+(a==0))%L,(s[1]+(a==1))%L)),
                           (-1, ((s[0]-(a==0))%L,(s[1]-(a==1))%L))):
                i,j = sid[s]*4, sid[r]*4
                for p in range(4):
                    for q in range(4): K[i+p,j+q] += sgn*R(1,2)*Gam[a][p,q]
    G = (m*sp.eye(4*N) + K).inv()
    pos = [s for s in sites if 1 <= s[0] <= L//2 - 1]
    n = len(pos)*4
    print(f"{label}   L={L}  {len(pos)} positive-time sites  ({n}x{n})", flush=True)
    for pname, th in PATTERNS.items():
        M_ = sp.zeros(n,n)
        for A, sa in enumerate(pos):
            ta = ((-sa[0]) % L, sa[1])
            for B, sb in enumerate(pos):
                for p in range(4):
                    for q in range(4):
                        M_[A*4+p, B*4+q] = th[p]*G[sid[ta]*4+p, sid[sb]*4+q]
        herm = sp.simplify(M_ - M_.conjugate().T).is_zero_matrix
        H = sp.Matrix(n,n, lambda i,j: sp.nsimplify(R(1,2)*(M_[i,j]+sp.conjugate(M_[j,i]))))
        sg = {"pos":0,"neg":0,"zero":0}
        for e,mlt in H.eigenvals().items():
            r_ = sp.simplify(sp.re(e))
            sg["zero" if r_==0 else ("pos" if r_>0 else "neg")] += mlt
        print(f"   theta_fib = {pname:24s} hermitian={str(herm):5s} "
              f"signature +{sg['pos']}/-{sg['neg']}/0{sg['zero']}   "
              f"OS-POSITIVE={sg['neg']==0}", flush=True)
for L in (4,6):
    run(sp.Matrix([[1,0],[0,1]]),  "EUCLIDEAN  g=diag( 1,1)", L=L)
    run(sp.Matrix([[-1,0],[0,1]]), "LORENTZIAN g=diag(-1,1)", L=L)
    print()
