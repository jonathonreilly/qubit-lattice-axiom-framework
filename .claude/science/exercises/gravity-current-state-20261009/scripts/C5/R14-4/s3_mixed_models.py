# R14-4 s3: random local, proper-cubic (O, 24) covariant, PSD Gaussian Hamiltonians of the six symmetric-tensor
# canonical pairs WITH h-E mixing at every order (on-site mixing angles at k=0, parity-odd O(k) h-E cross terms,
# generic O(k^2) cross terms).  Checks:
#  (a) covariance, PSD, the k=0 structure (Eg and T2g blocks rank 1 along a MIXED direction);
#  (b) the leading-order soft theory (rescaled Schur reduction, incl. gyroscopic O(k) h-E terms) reproduces the exact
#      small-k frequencies omega/k;
#  (c) V2(k) (soft Schur complement) lies in the span of the six invariants I1..I6 of s1 (fit residual);
#  (d) the counting r >= rank V2 (number of linear branches >= rank of the soft potential), direction by direction.
import numpy as np, itertools, sys
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 7)
# --- tensor basis (orthonormal, 6) and traceless basis (5) ---
idx=[(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
Bs=[]
for (i,j) in idx:
    M=np.zeros((3,3))
    if i==j: M[i,i]=1
    else: M[i,j]=M[j,i]=1/np.sqrt(2)
    Bs.append(M)
vec=lambda M: np.array([np.sum(M*b) for b in Bs])
G24=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        R=np.zeros((3,3))
        for i in range(3): R[i,p[i]]=s[i]
        if np.linalg.det(R)>0: G24.append(R)
D6=lambda R: np.column_stack([vec(R@b@R.T) for b in Bs])
D12=lambda R: np.kron(np.eye(2),D6(R))
r2,r6=np.sqrt(2),np.sqrt(6)
T1=vec(np.diag([1,-1,0])/r2); S=vec(np.diag([-1,-1,2])/r6); X=vec(np.array([[0,1,0],[1,0,0],[0,0,0]])/r2)
Y=vec(np.array([[0,0,0],[0,0,1],[0,1,0]])/r2); Z=vec(np.array([[0,0,1],[0,0,0],[1,0,0]])/r2); TR=vec(np.eye(3)/np.sqrt(3))
PEg=np.outer(T1,T1)+np.outer(S,S); PT2=np.outer(X,X)+np.outer(Y,Y)+np.outer(Z,Z); PA1=np.outer(TR,TR)
L5=np.array([T1,S,X,Y,Z]).T   # 6x5 traceless basis (columns), same order as s1: a=T1,b=S,c=X,d=Y,e=Z
J12=np.block([[np.zeros((6,6)),np.eye(6)],[-np.eye(6),np.zeros((6,6))]])
# --- on-site mixing rotation: in each irrep rotate the (h,E) plane by its own angle ---
def onsite_rot(thE,thT,thA=0.0):
    def blk(P,th): c,s=np.cos(th),np.sin(th); return np.block([[c*P,-s*P],[s*P,c*P]])
    return blk(PEg,thE)+blk(PT2,thT)+blk(PA1,thA)
nbrs=[np.zeros(3)]+[s*e for e in np.eye(3) for s in (1,-1)]+[np.array(v) for v in itertools.product([1,-1,0],repeat=3) if sum(abs(np.array(v)))==2]
def make_model(thE,thT,m=14,scale1=1.0):
    W=onsite_rot(thE,thT)              # canonical, on-site, O-covariant
    soft=W@np.vstack([np.hstack([PEg+PT2,np.zeros((6,6))]),np.zeros((6,12))])@W.T   # projector onto soft dirs (mixed)
    Pi=np.eye(12)-soft
    Fx=[rng.normal(size=(m,12)) for _ in nbrs]; Fpx=[scale1*rng.normal(size=(m,12)) for _ in nbrs]
    def F(k): return sum(np.exp(1j*k@x)*A@Pi + (np.exp(1j*k@x)-1)*B for x,A,B in zip(nbrs,Fx,Fpx))
    def H(k):
        out=np.zeros((12,12),complex)
        for R in G24:
            D=D12(R); Fk=F(R.T@k); out+=D@(Fk.conj().T@Fk)@D.T
        return out/len(G24)
    return H,W
def freqs(Hk):
    ev=np.linalg.eigvals(1j*J12@Hk); return np.sort(np.abs(ev.real))
def taylor(H,n,eps=1e-4):
    Hp,Hm,H0=H(eps*n),H(-eps*n),H(0*n)
    return H0,(Hp-Hm)/(2*eps),(Hp+Hm-2*H0)/(2*eps**2)
def soft_theory(H,W,n):
    # rotate to the frame where soft = traceless h, hard = traceless E (+ A1g pair); W^T H W
    H0,H1,H2=[W.T@M@W for M in taylor(H,n)]
    hs=[*range(6)]; Es=[*range(6,12)]
    Ph=np.zeros((12,5)); Ph[:6,:]=L5            # soft positions (traceless h)
    Pe=np.zeros((12,5)); Pe[6:,:]=L5            # their conjugates (traceless E)
    Pt=np.zeros((12,2)); Pt[:6,0]=TR; Pt[6:,1]=TR   # A1g pair (hard here)
    K0=Pe.T@H0@Pe; Ht=Pt.T@H0@Pt
    A1=Pe.T@H1@Ph                                # O(k) E-h cross term (rescaled e = E/k)
    V2=Ph.T@H2@Ph - (Ph.T@H1@Pt)@np.linalg.solve(Ht,Pt.T@H1@Ph)
    Hs=np.block([[V2,A1.conj().T],[A1,K0]])      # leading-order soft Hamiltonian in (h, e)
    J10=np.block([[np.zeros((5,5)),np.eye(5)],[-np.eye(5),np.zeros((5,5))]])
    ev=np.linalg.eigvals(1j*J10@Hs); w=np.sort(np.abs(ev.real))
    Vschur=V2-A1.conj().T@np.linalg.solve(K0,A1)
    return w, Vschur, K0, H0
# invariants I1..I6 as 5x5 matrices on traceless coordinates
def inv_mats(k):
    out=[]
    def Q(f):
        M=np.zeros((5,5))
        for i in range(5):
            for j in range(5):
                hi=L5[:,i]; hj=L5[:,j]
                def ten(v): return sum(c*b for c,b in zip(v,Bs))
                # polarisation of the quadratic form
                M[i,j]=0.25*(f(ten(hi+hj))-f(ten(hi-hj)))
        return M
    kk=k@k
    out.append(Q(lambda h: kk*np.sum(h*h)))
    out.append(Q(lambda h: (h@k)@(h@k)))
    out.append(Q(lambda h: sum(k[i]**2*h[i,i]**2 for i in range(3))))
    out.append(Q(lambda h: sum(k[i]**2*(h@h)[i,i] for i in range(3))))
    out.append(Q(lambda h: sum(k[i]*k[j]*h[i,j]*h[i,i] for i in range(3) for j in range(3))))
    out.append(Q(lambda h: kk*sum(h[i,i]**2 for i in range(3))))
    return out
if __name__=="__main__":
    thE,thT=rng.uniform(0.2,1.3),rng.uniform(0.2,1.3)
    H,W=make_model(thE,thT)
    print("mixing angles thE=%.3f thT=%.3f (radians; 0 = pure E kinetic at k=0)"%(thE,thT))
    k=rng.normal(size=3)
    print("(a) covariance max err:",max(np.abs(H(R@k)-D12(R)@H(k)@D12(R).T).max() for R in G24))
    print("    PSD: min eig over 200 random k:",min(np.linalg.eigvalsh(H(rng.uniform(-np.pi,np.pi,3))).min() for _ in range(200)))
    H0=H(np.zeros(3)); Wt=W.T@H0@W
    print("    k=0 frame check: |traceless-h rows of W^T H(0) W| =",np.abs(L5.T@Wt[:6,:]).max(), " (original frame, same rows:",np.abs(L5.T@H0[:6,:]).max(),")")
    Kt=L5.T@Wt[6:,6:]@L5; print("    K0 (traceless E block) eigenvalues:",np.round(np.linalg.eigvalsh(Kt),3))
    print("    parity-odd content |H(k)-H(-k)| at k=0.1 n:",np.abs(H(0.1*k/np.linalg.norm(k))-H(-0.1*k/np.linalg.norm(k))).max())
    dirs=[(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1),(1,2,0),(2,1,3),(1,-1,2),(3,1,2),(1,2,5)]
    print("(b,d) exact omega/k at |k|=1e-3 vs leading soft theory; rank V2; # linear branches")
    for d in dirs:
        n=np.array(d,float); n/=np.linalg.norm(n)
        t=1e-3; we=freqs(H(t*n))/t
        lin_exact=np.sort(we)[:10]   # the 10 smallest |eigenvalues| = soft part (hard modes are O(1)/t)
        ws,Vs,K0,_=soft_theory(H,W,n)
        r=np.sum(np.linalg.eigvalsh(Vs)>1e-6*np.abs(np.linalg.eigvalsh(Vs)).max())
        print("  n=%-9s exact soft w/k: %s   (hard min w/k = %.0f)"%(str(d),np.round(lin_exact,4),np.sort(we)[10]))
        print("  %-11s theory  w/k: %s   rank V2=%d"%("",np.round(ws[ws>1e-6],4),r))
    print("(c) V2 in span{I1..I6}: fit residuals")
    for d in dirs[:5]:
        n=np.array(d,float); n/=np.linalg.norm(n)
        _,Vs,_,_=soft_theory(H,W,n)
        if d==dirs[0]: pass
    # fit c from several directions jointly
    A=[];bvec=[]
    for d in dirs:
        n=np.array(d,float); n/=np.linalg.norm(n)
        _,Vs,_,_=soft_theory(H,W,n); Ms=inv_mats(n)
        A.append(np.array([M.ravel() for M in Ms]).T); bvec.append(Vs.real.ravel())
    A=np.vstack(A); bvec=np.concatenate(bvec); cfit,res,_,_=np.linalg.lstsq(A,bvec,rcond=None)
    print("   c =",np.round(cfit,5)," relative residual =",np.linalg.norm(A@cfit-bvec)/np.linalg.norm(bvec))
    print("   axis values: TT1=%.4f TT2=%.4f S=%.4f VEC=%.4f"%(cfit[0]+cfit[5],cfit[0],cfit[0]+2/3*sum(cfit[1:5])+cfit[5],cfit[0]+(cfit[1]+cfit[3])/2))
