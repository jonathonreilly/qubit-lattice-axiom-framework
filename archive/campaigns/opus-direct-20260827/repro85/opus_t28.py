"""T28 - IS THE RESPONSE A TENSOR?  The sharpest form of T27.
T27 showed: uniform and isotropic matter give zero shear response, axis-aligned
anisotropic matter gives an equal-and-opposite response under t<->x, and the
OFF-DIAGONAL shear response to axis-aligned matter is exactly zero.  If the
response is a genuine rank-2 tensor  R_ab ~ (anisotropic stress)_ab, then
rotating the matter by 45 degrees must ROTATE the response: matter stretched
along the (t+x) diagonal must source the OFF-DIAGONAL shear and give ZERO
diag(1,-1) response -- the exact mirror of the axis-aligned case.
Two independent derivative routes: analytic tr(Q^-1 dQ/dh) and finite difference."""
import numpy as np
D=2; BAS=[(),(0,),(1,),(0,1)]; IDX={b:i for i,b in enumerate(BAS)}; NF=4
def epsm(a):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        if a in Sx: continue
        T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
    return M
def iota(a,gi):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
    return M
EPS=[epsm(a) for a in range(D)]
L=6; m0=0.8; zc=(3,3)
sites=[(t,x) for t in range(L) for x in range(L)]; sid={s:i for i,s in enumerate(sites)}
NS=len(sites)
def nb(s,a,sgn): return ((s[0]+sgn*(a==0))%L,(s[1]+sgn*(a==1))%L)
def Qmat(m_site,prof,h,E):
    Q=np.zeros((NF*NS,NF*NS))
    for s in sites: Q[sid[s]*NF:(sid[s]+1)*NF,sid[s]*NF:(sid[s]+1)*NF]+=m_site[s]*np.eye(NF)
    gi={s:np.linalg.inv(np.eye(D)+h*prof[s]*E) for s in sites}
    for s in sites:
        for a in range(D):
            for sgn in (+1,-1):
                r=nb(s,a,sgn)
                Q[sid[s]*NF:(sid[s]+1)*NF,sid[r]*NF:(sid[r]+1)*NF]+=0.25*sgn*(
                    EPS[a]+iota(a,gi[s])+EPS[a]+iota(a,gi[r]))
    return Q
def dQmat(prof,E):
    dQ=np.zeros((NF*NS,NF*NS))
    IE=[iota(a,-E) for a in range(D)]
    for s in sites:
        for a in range(D):
            for sgn in (+1,-1):
                r=nb(s,a,sgn)
                dQ[sid[s]*NF:(sid[s]+1)*NF,sid[r]*NF:(sid[r]+1)*NF]+=0.25*sgn*(prof[s]+prof[r])*IE[a]
    return dQ
def resp(m_site,prof,E,fd=False):
    Q0=Qmat(m_site,prof,0.0,E)
    an=float(np.trace(np.linalg.solve(Q0,dQmat(prof,E))))
    if not fd: return an,None
    e=1e-5
    f=(np.linalg.slogdet(Qmat(m_site,prof,e,E))[1]-np.linalg.slogdet(Qmat(m_site,prof,-e,E))[1])/(2*e)
    return an,f
prof={s:(1.0 if s==zc else 0.0) for s in sites}
Ed=np.array([[1.,0.],[0.,-1.]]); Eo=np.array([[0.,1.],[1.,0.]])
def matter(pairs,delta=0.3):
    m={s:m0 for s in sites}
    for p in pairs: m[p]+=delta
    return m
CFG={"uniform":[], "point":[(3,3)],
     "t-pair  (along t)":[(2,3),(4,3)], "x-pair  (along x)":[(3,2),(3,4)],
     "diag-pair  (t+x)":[(2,2),(4,4)],  "anti-diag (t-x)":[(2,4),(4,2)]}
print("T28  L=6  m0=0.8 delta=0.3   shear response of the rule's effective action")
print("     [analytic tr(Q^-1 dQ/dh); finite difference in brackets]")
print(f"     {'matter':22s} {'E=diag(1,-1)':>26s} {'E=offdiag':>26s}")
for nm,pairs in CFG.items():
    m=matter(pairs)
    ad,fdd=resp(m,prof,Ed,fd=True); ao,fdo=resp(m,prof,Eo,fd=True)
    print(f"     {nm:22s} {ad:+.6e} [{fdd:+.3e}] {ao:+.6e} [{fdo:+.3e}]", flush=True)
print()
print("     PREDICTION if the response is a rank-2 tensor:")
print("       axis-aligned matter -> nonzero diag,  ZERO offdiag")
print("       45-degree matter    -> ZERO diag,     nonzero offdiag  (the mirror)")
print()
print("     rotation covariance check: |R| should be the same for the axis-aligned")
print("     pair and the 45-degree pair if the response rotates rigidly:")
m1=matter(CFG["t-pair  (along t)"]); m2=matter(CFG["diag-pair  (t+x)"])
r1=abs(resp(m1,prof,Ed)[0]); r2=abs(resp(m2,prof,Eo)[0])
print(f"       |R(t-pair, diag shear)| = {r1:.6e}")
print(f"       |R(diag-pair, offdiag shear)| = {r2:.6e}    ratio = {r2/r1 if r1 else float('nan'):.6f}")
