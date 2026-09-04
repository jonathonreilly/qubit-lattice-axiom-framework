"""T36 - BUILD THE MISSING CONNECTION, THEN RUN IT THROUGH THE GATE.
Result 19 showed the metric-only construction is not diffeomorphism invariant,
and identified why: the metric enters only through iota_a(g^-1) with the hop
directions welded to the lattice axes.  There is no frame rotation, so a
diffeomorphism (which rotates frames) cannot be absorbed.  The repair, which is
also the cross-lane review's proposed route, is a SELECTED ORTHOGONAL EDGE
FACTOR from the polar part of the relative coframe map:

    e_s = sqrt(g_s)  (symmetric positive coframe)
    M_(s<-r) = e_s e_r^-1 ,   polar  M = R P  ->  R_(s<-r) = M (M^T M)^(-1/2)
    R_hat = the exterior-algebra lift of R  (k-th compound matrix on Lambda^k)
    Gamma^mu(s) = sum_a (e_s^-1)^mu_a gamma^a      [flat gammas in the frame]
    Lambda_(s<-r) = 1/2 [ Gamma^mu(s) R_hat + R_hat Gamma^mu(r) ]

Then the SAME first-order diffeomorphism gate as opus_t35.py:
    delta g_11 = 2 d_1 xi_1 ,  delta m = xi_1 d_1 m ,  and the two pieces must
    cancel.  Old construction: they did not (residual ~69% of the largest piece).
Both constructions are measured side by side in this one run."""
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
def sqrtm_sym(g):
    w,V=np.linalg.eigh(g); return V@np.diag(np.sqrt(w))@V.T
def polar_R(M):
    U,_,Vt=np.linalg.svd(M); return U@Vt
def lift(R,B,IDX,NF):
    """exterior-algebra lift: on Lambda^k it is the k-th compound matrix of R."""
    Lm=np.zeros((NF,NF))
    for T in B:
        for Sx in B:
            if len(T)!=len(Sx): continue
            if len(T)==0: Lm[IDX[T],IDX[Sx]]=1.0; continue
            sub=np.array([[R[t,s] for s in Sx] for t in T])
            Lm[IDX[T],IDX[Sx]]=np.linalg.det(sub)
    return Lm
def Wfun(D,L,mfield,gfield,frame,WAVE=1):
    B,IDX,NF,epsm,iotam=make_ops(D)
    EPSf=[epsm(a) for a in range(D)]
    GAMflat=[EPSf[a]+iotam(a,np.eye(D)) for a in range(D)]      # flat gammas
    gi=[np.linalg.inv(gfield[x]) for x in range(L)]
    if frame:
        e=[sqrtm_sym(gfield[x]) for x in range(L)]
        einv=[np.linalg.inv(e[x]) for x in range(L)]
        GAM=[[sum(einv[x][mu,a]*GAMflat[a] for a in range(D)) for mu in range(D)] for x in range(L)]
        Rh=[lift(polar_R(e[x]@einv[(x+1)%L]),B,IDX,NF) for x in range(L)]   # s=x <- r=x+1
        Rhm=[lift(polar_R(e[x]@einv[(x-1)%L]),B,IDX,NF) for x in range(L)]  # s=x <- r=x-1
    else:
        GAM=[[EPSf[mu]+iotam(mu,gi[x]) for mu in range(D)] for x in range(L)]
    trans=[a for a in range(D) if a!=WAVE]
    tot=0.0
    for pidx in itertools.product(range(L),repeat=D-1):
        p={a:2*np.pi*pidx[i]/L for i,a in enumerate(trans)}
        Q=np.zeros((L*NF,L*NF),dtype=complex)
        for x in range(L):
            i=x*NF
            Q[i:i+NF,i:i+NF]+=mfield[x]*np.eye(NF)
            for a in trans: Q[i:i+NF,i:i+NF]+=1j*np.sin(p[a])*GAM[x][a]
            for sgn in (+1,-1):
                y=(x+sgn)%L; j=y*NF
                if frame:
                    U=Rh[x] if sgn==+1 else Rhm[x]
                    blk=0.5*(GAM[x][WAVE]@U + U@GAM[y][WAVE])
                else:
                    blk=0.5*(GAM[x][WAVE]+GAM[y][WAVE])
                Q[i:i+NF,j:j+NF]+=0.5*sgn*blk
        tot+=float(np.real(np.linalg.slogdet(Q)[1]))
    return tot
def gate(D,L,m0,mu,pw,nw,frame,e=1e-4):
    xs=np.arange(L)
    xi=np.sin(2*np.pi*nw*xs/L); dxi=(2*np.pi*nw/L)*np.cos(2*np.pi*nw*xs/L)
    m=m0+mu*np.cos(2*np.pi*pw*xs/L); dm=-mu*(2*np.pi*pw/L)*np.sin(2*np.pi*pw*xs/L)
    def build(h,which):
        g=[np.eye(D) for _ in range(L)]; mm=list(m)
        for x in range(L):
            if which in ("both","metric"):
                g[x]=np.eye(D); g[x][1,1]=1.0+2*h*dxi[x]
            if which in ("both","matter"): mm[x]=m[x]+h*xi[x]*dm[x]
        return mm,g
    out={}
    for which in ("metric","matter","both"):
        mp,gp=build(+e,which); mm_,gm=build(-e,which)
        out[which]=(Wfun(D,L,mp,gp,frame)-Wfun(D,L,mm_,gm,frame))/(2*e)
    return out
print("T36  first-order diffeomorphism gate:  metric piece + matter piece must be 0")
print("     OLD = metric-only (Result 19)   NEW = polar-frame connection")
print()
for D,Ls in ((2,(8,12,16)),(4,(6,8))):
    print(f"  d={D}")
    for L in Ls:
        o=gate(D,L,0.9,0.35,1,1,frame=False)
        n=gate(D,L,0.9,0.35,1,1,frame=True)
        ro=abs(o["both"])/max(abs(o["metric"]),abs(o["matter"]),1e-30)
        rn=abs(n["both"])/max(abs(n["metric"]),abs(n["matter"]),1e-30)
        print(f"   L={L:2d} OLD metric={o['metric']:+12.5f} matter={o['matter']:+12.5f} "
              f"SUM={o['both']:+12.5f} rel={ro:.6f}", flush=True)
        print(f"   L={L:2d} NEW metric={n['metric']:+12.5f} matter={n['matter']:+12.5f} "
              f"SUM={n['both']:+12.5f} rel={rn:.6f}", flush=True)
    print(flush=True)
print("  rel -> 0 for NEW would mean the polar-frame connection restores diff invariance.")
