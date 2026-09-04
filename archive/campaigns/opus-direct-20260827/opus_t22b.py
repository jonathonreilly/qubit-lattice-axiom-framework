"""T22b - OS reflection with the CORRECT fibre operator.
A time reflection must flip Gamma_0 and fix Gamma_1.  Conjugation by a sign
pattern cannot do that; conjugation by the SPATIAL gamma can:
   Gamma_1 Gamma_0 Gamma_1^-1 = -Gamma_0 ,  Gamma_1 Gamma_1 Gamma_1^-1 = +Gamma_1
(using {Gamma_a,Gamma_b} = 2 g^-1_ab, diagonal g).  So the reflection is
theta = R_sites o (product of spatial gammas), the Kahler-Dirac analogue of
the Dirac  psi -> psi^dagger Gamma_0.  HERMITICITY OF THE FORM IS THE FILTER:
only a theta that makes <theta f, G f> Hermitian is a legitimate reflection.
Among those, positivity decides the branch."""
import sympy as sp
R = sp.Rational
BAS = [(), (0,), (1,), (0,1)]; IDX = {b:i for i,b in enumerate(BAS)}
def epsm(a):
    M = sp.zeros(4,4)
    for Sx in BAS:
        if a in Sx: continue
        T = tuple(sorted(Sx+(a,))); M[IDX[T], IDX[Sx]] = (-1)**sum(1 for i in Sx if i<a)
    return M
def iota(a, gi):
    M = sp.zeros(4,4)
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i); M[IDX[T], IDX[Sx]] += (-1)**pos*gi[a,i]
    return M
def run(g, label, L=4, m=R(1,2)):
    gi = sp.simplify(g.inv())
    Gam = [sp.Matrix(sp.simplify(epsm(a)+iota(a,gi))) for a in range(2)]
    G0, G1 = Gam
    CAN = sp.diag(1,-1,1,-1)
    cands = {"Gamma_1 (spatial gamma)": G1, "-Gamma_1": -G1, "Gamma_0": G0,
             "Gamma_0 Gamma_1": G0*G1, "Gamma_1 * r*": G1*CAN, "r* * Gamma_1": CAN*G1,
             "identity": sp.eye(4), "r* (e0->-e0)": CAN}
    sites = [(t,x) for t in range(L) for x in range(L)]
    sid = {s:i for i,s in enumerate(sites)}; N=L*L
    K = sp.zeros(4*N,4*N)
    for s in sites:
        for a in range(2):
            for sgn, r in ((+1,((s[0]+(a==0))%L,(s[1]+(a==1))%L)),
                           (-1,((s[0]-(a==0))%L,(s[1]-(a==1))%L))):
                i,j = sid[s]*4, sid[r]*4
                for p in range(4):
                    for q in range(4): K[i+p,j+q] += sgn*R(1,2)*Gam[a][p,q]
    Gm = (m*sp.eye(4*N)+K).inv()
    pos = [s for s in sites if 1 <= s[0] <= L//2-1]
    n = len(pos)*4
    print(f"{label}  L={L}  ({n}x{n} form on {len(pos)} positive-time sites)", flush=True)
    for nm, TH in cands.items():
        M_ = sp.zeros(n,n)
        for A,sa in enumerate(pos):
            ta = ((-sa[0])%L, sa[1])
            for B,sb in enumerate(pos):
                sub = sp.Matrix(4,4, lambda p,q: Gm[sid[ta]*4+p, sid[sb]*4+q])
                blk = TH*sub
                for p in range(4):
                    for q in range(4): M_[A*4+p,B*4+q] = blk[p,q]
        herm = sp.simplify(M_ - M_.conjugate().T).is_zero_matrix
        H = sp.Matrix(n,n, lambda i,j: R(1,2)*(M_[i,j]+sp.conjugate(M_[j,i])))
        sg = {"p":0,"n":0,"z":0}
        for e,mlt in H.eigenvals().items():
            r_ = sp.simplify(sp.re(e)); sg["z" if r_==0 else ("p" if r_>0 else "n")] += mlt
        tag = "  <== LEGITIMATE" if herm else ""
        print(f"   theta_fib={nm:24s} hermitian={str(herm):5s} sig +{sg['p']}/-{sg['n']}/0{sg['z']}"
              f"  POSITIVE={sg['n']==0}{tag}", flush=True)
for L in (4,6):
    run(sp.Matrix([[1,0],[0,1]]),  "EUCLIDEAN  g=diag( 1,1)", L=L)
    run(sp.Matrix([[-1,0],[0,1]]), "LORENTZIAN g=diag(-1,1)", L=L)
    print()
