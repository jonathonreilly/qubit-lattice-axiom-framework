"""T28b - WHY is the off-diagonal channel exactly silent?  Symmetry or structure?
Kill every reflection symmetry with a deliberately lopsided matter configuration
and a lopsided bump profile.  If the off-diagonal response is STILL exactly zero,
the silence is structural: the first-order effective action does not see the
off-diagonal metric at all in this construction, and a vielbein/frame treatment
is required before any rotational-covariance claim can be made."""
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
L=5; m0=0.8
sites=[(t,x) for t in range(L) for x in range(L)]; sid={s:i for i,s in enumerate(sites)}; NS=len(sites)
def nb(s,a,sgn): return ((s[0]+sgn*(a==0))%L,(s[1]+sgn*(a==1))%L)
def Qmat(m_site,prof,h,E):
    Q=np.zeros((NF*NS,NF*NS))
    for s in sites: Q[sid[s]*NF:(sid[s]+1)*NF,sid[s]*NF:(sid[s]+1)*NF]+=m_site[s]*np.eye(NF)
    gi={s:np.linalg.inv(np.eye(D)+h*prof[s]*E) for s in sites}
    for s in sites:
        for a in range(D):
            for sgn in (+1,-1):
                r=nb(s,a,sgn)
                Q[sid[s]*NF:(sid[s]+1)*NF,sid[r]*NF:(sid[r]+1)*NF]+=0.25*sgn*(2*EPS[a]+iota(a,gi[s])+iota(a,gi[r]))
    return Q
def dQmat(prof,E):
    dQ=np.zeros((NF*NS,NF*NS)); IE=[iota(a,-E) for a in range(D)]
    for s in sites:
        for a in range(D):
            for sgn in (+1,-1):
                r=nb(s,a,sgn)
                dQ[sid[s]*NF:(sid[s]+1)*NF,sid[r]*NF:(sid[r]+1)*NF]+=0.25*sgn*(prof[s]+prof[r])*IE[a]
    return dQ
Ed=np.array([[1.,0.],[0.,-1.]]); Eo=np.array([[0.,1.],[1.,0.]]); Ec=np.eye(2)
rng=np.random.default_rng(7)
prof_rand={s:float(rng.random()) for s in sites}
m_rand={s: m0+0.4*float(rng.random()) for s in sites}
prof_pt={s:(1.0 if s==(2,2) else 0.0) for s in sites}
m_lop={s:m0 for s in sites}; m_lop[(1,2)]+=0.3; m_lop[(3,3)]+=0.17; m_lop[(0,4)]+=0.41
print("T28b  L=5 (odd, no antipodal pairing) -- every reflection symmetry deliberately broken")
for label, m_, p_ in (("random matter + random bump profile", m_rand, prof_rand),
                      ("lopsided 3-defect matter + point bump", m_lop, prof_pt),
                      ("random matter + point bump", m_rand, prof_pt)):
    Q0=Qmat(m_,p_,0.0,Ed)
    Qi=np.linalg.inv(Q0)
    out=[]
    for nm,E in (("diag(1,-1)",Ed),("offdiag",Eo),("conformal",Ec)):
        dQ=dQmat(p_,E)
        out.append(f"{nm}={float(np.trace(Qi@dQ)):+.6e}")
        if nm=="offdiag":
            nz=int(np.count_nonzero(np.abs(dQ)>1e-14)); fro=float(np.linalg.norm(dQ))
            extra=f"   [dQ_offdiag is nonzero: {nz} entries, ||dQ||_F={fro:.4f}]"
    print(f"   {label:38s} " + "  ".join(out) + extra, flush=True)
print()
print("   Interpretation: if the offdiag column is exactly 0 while ||dQ_offdiag|| != 0,")
print("   the silence is STRUCTURAL, not a symmetry accident.")
print()
# is it exactly zero at SECOND order too?
p_=prof_pt; m_=m_lop
for e in (1e-3, 1e-2, 5e-2):
    w=[np.linalg.slogdet(Qmat(m_,p_,hh,Eo))[1] for hh in (-e,0.0,e)]
    print(f"   offdiag, h=+-{e}:  W(-h)={w[0]:.10f}  W(0)={w[1]:.10f}  W(+h)={w[2]:.10f}   "
          f"1st={ (w[2]-w[0])/(2*e):+.3e}  2nd={(w[2]-2*w[1]+w[0])/e**2:+.6e}", flush=True)
