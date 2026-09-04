"""T36b - the gauge mode that actually engages the frame.
T36 found OLD and NEW identical to every digit, for a structural reason worth
recording: the polar orthogonal factor of e_s e_r^-1 is the IDENTITY whenever
the metrics on the two ends of a link COMMUTE -- in particular for every
all-diagonal metric field.  A diffeomorphism along the same axis it depends on
generates exactly such a diagonal perturbation, so the polar selector is
literally inert there.

The gauge mode that does engage it: xi points along axis 2 while depending on
x_1, so  delta g_12 = delta g_21 = d_1 xi_2  is OFF-DIAGONAL.  Take the matter
field to depend on x_1 only, so  delta m = xi_2 d_2 m = 0  identically and the
matter piece drops out.  Diffeomorphism invariance then demands the metric piece
ALONE vanish -- the cleanest possible gate.  Measured for both constructions,
with ||R - I|| reported so it is visible that the frame factor is engaged."""
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
    Lm=np.zeros((NF,NF))
    for T in B:
        for Sx in B:
            if len(T)!=len(Sx): continue
            if len(T)==0: Lm[IDX[T],IDX[Sx]]=1.0; continue
            Lm[IDX[T],IDX[Sx]]=np.linalg.det(np.array([[R[t,s] for s in Sx] for t in T]))
    return Lm
def Wfun(D,L,mfield,gfield,frame,WAVE=1,report=False):
    B,IDX,NF,epsm,iotam=make_ops(D)
    EPSf=[epsm(a) for a in range(D)]
    GAMflat=[EPSf[a]+iotam(a,np.eye(D)) for a in range(D)]
    gi=[np.linalg.inv(gfield[x]) for x in range(L)]
    rdev=0.0
    if frame:
        e=[sqrtm_sym(gfield[x]) for x in range(L)]; einv=[np.linalg.inv(z) for z in e]
        GAM=[[sum(einv[x][mu,a]*GAMflat[a] for a in range(D)) for mu in range(D)] for x in range(L)]
        Rp=[polar_R(e[x]@einv[(x+1)%L]) for x in range(L)]
        Rm_=[polar_R(e[x]@einv[(x-1)%L]) for x in range(L)]
        rdev=max(np.linalg.norm(R-np.eye(D)) for R in Rp+Rm_)
        Rh=[lift(R,B,IDX,NF) for R in Rp]; Rhm=[lift(R,B,IDX,NF) for R in Rm_]
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
    return (tot,rdev) if report else tot
def offdiag_gate(D,L,m0,mu,nw,frame,e=1e-4):
    """xi = (0,0,xi_2(x_1),0...) -> delta g_12 = d_1 xi_2 (OFF-DIAGONAL); delta m = 0."""
    xs=np.arange(L)
    dxi=(2*np.pi*nw/L)*np.cos(2*np.pi*nw*xs/L)
    m=list(m0+mu*np.cos(2*np.pi*xs/L))
    def g_of(h):
        g=[]
        for x in range(L):
            G=np.eye(D); G[1,2]=G[2,1]=h*dxi[x]; g.append(G)
        return g
    wp,rd=Wfun(D,L,m,g_of(+e),frame,report=True)
    wm=Wfun(D,L,m,g_of(-e),frame)
    w0=Wfun(D,L,m,g_of(0.0),frame)
    return (wp-wm)/(2*e), (wp-2*w0+wm)/e**2, rd
print("T36b  OFF-DIAGONAL pure-gauge mode.  delta m = 0 identically, so")
print("      diffeomorphism invariance demands the metric piece ALONE vanish.")
print("      (D>=3 needed for an off-diagonal gauge mode transverse to the wave.)")
print()
print(f"   {'':22s} {'dW/dh':>16} {'d2W/dh2':>16} {'||R-I||':>12}")
for D in (3,4):
    for L in (6,8):
        o1,o2,_ = offdiag_gate(D,L,0.9,0.35,1,frame=False)
        n1,n2,rd = offdiag_gate(D,L,0.9,0.35,1,frame=True)
        print(f"   d={D} L={L} OLD (metric only) {o1:+16.8f} {o2:+16.6f} {'--':>12}", flush=True)
        print(f"   d={D} L={L} NEW (polar frame) {n1:+16.8f} {n2:+16.6f} {rd:12.6f}", flush=True)
    print(flush=True)
print("   ||R-I|| > 0 confirms the frame factor is actually engaged this time.")
print("   dW/dh -> 0 for NEW (and not for OLD) would mean the polar connection")
print("   restores first-order diffeomorphism invariance in the sector that fails.")
