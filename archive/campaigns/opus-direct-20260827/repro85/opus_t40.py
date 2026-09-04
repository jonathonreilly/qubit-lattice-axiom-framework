"""T40 - DOES THE LINK-LENGTH WEIGHT RESTORE DIFFEOMORPHISM INVARIANCE IN THE
CONTINUUM LIMIT?
T38 found the only candidate that moved the gate: weighting the hop by the
inverse proper step length along the link.  It cut the residual from rel=0.545
to rel=0.090 at L=16 AND, unlike the unweighted case, rel keeps FALLING with L
(0.1042, 0.0900, 0.0797 at L = 12,16,24).  The unweighted case converged to
0.537 instead.  So the question is whether rel -> 0.

Pushed out to L = 96 in d=2 (cheap), with the required multiplier printed
alongside: the metric piece must reach |matter|/|metric| for exact cancellation,
and the link weight supplies exactly 2.  Watch whether the requirement falls to 2.

Also excluded en route (recorded so nobody re-walks them):
  * per-site volume weight  -- factors out of the determinant exactly (T38 mode 3
    reproduced mode 0 to every digit)
  * overall  c * sum_s log det g_s  -- its first-order variation vanishes for a
    wave xi, for every c
  * the beta family  Gamma^1 = A^-b eps + A^(b-1) iota  -- Clifford closure holds
    for all beta and the DETERMINANT IS BLIND TO IT (T39: identical to 6 digits
    across beta = -0.5 .. 1.5, in d=2 and d=4)"""
import numpy as np, itertools
def carrier(D):
    B=[]
    for k in range(D+1): B+=[tuple(c) for c in itertools.combinations(range(D),k)]
    return B,{b:i for i,b in enumerate(B)}
def make_ops(D):
    B,IDX=carrier(D); NF=len(B)
    def epsm(a):
        M=np.zeros((NF,NF))
        for Sx in B:
            if a in Sx: continue
            T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
        return M
    def iotam(a,gi):
        M=np.zeros((NF,NF))
        for Sx in B:
            for pos,i in enumerate(Sx):
                T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
        return M
    return B,IDX,NF,epsm,iotam
def Wfun(D,L,mfield,A,weighted,WAVE=1):
    B,IDX,NF,epsm,iotam=make_ops(D)
    EPS=[epsm(a) for a in range(D)]; IOTf=[iotam(a,np.eye(D)) for a in range(D)]
    G1=[EPS[WAVE]+ (1.0/A[x])*IOTf[WAVE] for x in range(L)]
    GT=[EPS[a]+IOTf[a] for a in range(D)]
    ell=[float(np.sqrt(A[x])) for x in range(L)]
    trans=[a for a in range(D) if a!=WAVE]; tot=0.0
    for pidx in itertools.product(range(L),repeat=D-1):
        p={a:2*np.pi*pidx[i]/L for i,a in enumerate(trans)}
        Q=np.zeros((L*NF,L*NF),dtype=complex)
        for x in range(L):
            i=x*NF
            Q[i:i+NF,i:i+NF]+=mfield[x]*np.eye(NF)
            for a in trans: Q[i:i+NF,i:i+NF]+=1j*np.sin(p[a])*GT[a]
            for sgn in (+1,-1):
                y=(x+sgn)%L; j=y*NF
                w=1.0/np.sqrt(ell[x]*ell[y]) if weighted else 1.0
                Q[i:i+NF,j:j+NF]+=w*0.5*sgn*0.5*(G1[x]+G1[y])
        tot+=float(np.real(np.linalg.slogdet(Q)[1]))
    return tot
def gate(D,L,m0,mu,nw,weighted,e=1e-4):
    xs=np.arange(L)
    xi=np.sin(2*np.pi*nw*xs/L); dxi=(2*np.pi*nw/L)*np.cos(2*np.pi*nw*xs/L)
    m=m0+mu*np.cos(2*np.pi*nw*xs/L); dm=-mu*(2*np.pi*nw/L)*np.sin(2*np.pi*nw*xs/L)
    def build(h,which):
        A=np.ones(L); mm=np.array(m,dtype=float)
        if which in ("both","metric"): A=1.0+2*h*dxi
        if which in ("both","matter"): mm=m+h*xi*dm
        return list(mm),list(A)
    o={}
    for which in ("metric","matter","both"):
        mp,Ap=build(+e,which); mm_,Am=build(-e,which)
        o[which]=(Wfun(D,L,mp,Ap,weighted)-Wfun(D,L,mm_,Am,weighted))/(2*e)
    return o
print("T40  d=2, nw=1, m0=0.9 mu=0.35.  UNWEIGHTED vs LINK-LENGTH-WEIGHTED hop.")
print(f"   {'L':>4} {'rel (unwtd)':>13} {'rel (weighted)':>15} {'needed multiplier':>19} {'supplied':>9}")
for L in (12,16,24,32,48,64,96):
    u=gate(2,L,0.9,0.35,1,False); w=gate(2,L,0.9,0.35,1,True)
    ru=abs(u["both"])/max(abs(u["metric"]),abs(u["matter"]))
    rw=abs(w["both"])/max(abs(w["metric"]),abs(w["matter"]))
    need=abs(u["matter"])/abs(u["metric"]); sup=w["metric"]/u["metric"]
    print(f"   {L:4d} {ru:13.7f} {rw:15.7f} {need:19.7f} {sup:9.5f}", flush=True)
print()
print("   'needed multiplier' -> 2 would mean the link-length weight is exactly right")
print("   in the continuum limit; rel(weighted) -> 0 is the same statement.")
