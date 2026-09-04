"""T38 - WHAT IS ACTUALLY MISSING?  Localise the diffeomorphism failure.
Result 21 corollary 2 sharpened the question: the failing gauge mode
g = diag(A(x_1),1,1,1) is FLAT in disguise (coframe e^1 = sqrt(A) dx^1, de^1 = 0,
omega = 0, R = 0), yet log det Q changes by 54%.  No connection can fix that.
So find out WHERE the invariance breaks by testing the one thing a coordinate
change really does to a lattice: it makes the PROPER STEP LENGTH vary.

Under x -> y = int sqrt(A) dx the operator becomes exactly flat.  On the lattice
the hop is one COORDINATE step, i.e. proper length sqrt(A(x)), which varies.
Three candidate repairs, each a different way of restoring a uniform proper
step, are measured against the same first-order gate:

  (0) NONE            - the Result 19 construction
  (1) LINK-LENGTH     - weight the direction-1 hop by 1/sqrt(A) at the link
                        (geometric mean of the endpoints)
  (2) LINK-LENGTH ARI - the same with the arithmetic mean
  (3) MASS-DENSITY    - weight the on-site mass by sqrt(det g_s) and the hop by
                        the geometric mean, i.e. an honest volume density
A repair that makes metric + matter cancel identifies the missing object."""
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
def Wfun(D,L,mfield,gfield,mode,WAVE=1):
    B,IDX,NF,epsm,iotam=make_ops(D)
    EPS=[epsm(a) for a in range(D)]
    gi=[np.linalg.inv(gfield[x]) for x in range(L)]
    IOT=[[iotam(a,gi[x]) for a in range(D)] for x in range(L)]
    GAM=[[EPS[a]+IOT[x][a] for a in range(D)] for x in range(L)]
    rootg=[float(np.sqrt(np.linalg.det(gfield[x]))) for x in range(L)]
    ell=[float(np.sqrt(gfield[x][WAVE,WAVE])) for x in range(L)]     # proper step along the wave axis
    trans=[a for a in range(D) if a!=WAVE]; tot=0.0
    for pidx in itertools.product(range(L),repeat=D-1):
        p={a:2*np.pi*pidx[i]/L for i,a in enumerate(trans)}
        Q=np.zeros((L*NF,L*NF),dtype=complex)
        for x in range(L):
            i=x*NF
            mw = rootg[x] if mode==3 else 1.0
            Q[i:i+NF,i:i+NF]+=mw*mfield[x]*np.eye(NF)
            for a in trans: Q[i:i+NF,i:i+NF]+=1j*np.sin(p[a])*GAM[x][a]*(mw if mode==3 else 1.0)
            for sgn in (+1,-1):
                y=(x+sgn)%L; j=y*NF
                if   mode==0: w=1.0
                elif mode==1: w=1.0/np.sqrt(ell[x]*ell[y])
                elif mode==2: w=2.0/(ell[x]+ell[y])
                else:         w=float(np.sqrt(rootg[x]*rootg[y]))
                Q[i:i+NF,j:j+NF]+=w*0.25*sgn*(2*EPS[WAVE]+IOT[x][WAVE]+IOT[y][WAVE])
        tot+=float(np.real(np.linalg.slogdet(Q)[1]))
    return tot
def gate(D,L,m0,mu,nw,mode,e=1e-4):
    xs=np.arange(L)
    xi=np.sin(2*np.pi*nw*xs/L); dxi=(2*np.pi*nw/L)*np.cos(2*np.pi*nw*xs/L)
    m=m0+mu*np.cos(2*np.pi*nw*xs/L); dm=-mu*(2*np.pi*nw/L)*np.sin(2*np.pi*nw*xs/L)
    def build(h,which):
        g=[np.eye(D) for _ in range(L)]; mm=list(m)
        for x in range(L):
            if which in ("both","metric"): g[x]=np.eye(D); g[x][1,1]=1.0+2*h*dxi[x]
            if which in ("both","matter"): mm[x]=m[x]+h*xi[x]*dm[x]
        return mm,g
    o={}
    for which in ("metric","matter","both"):
        mp,gp=build(+e,which); mm_,gm=build(-e,which)
        o[which]=(Wfun(D,L,mp,gp,mode)-Wfun(D,L,mm_,gm,mode))/(2*e)
    return o
NAMES={0:"(0) NONE  [Result 19]",1:"(1) LINK-LENGTH geo",2:"(2) LINK-LENGTH ari",3:"(3) MASS-DENSITY"}
print("T38  first-order diffeomorphism gate under four candidate repairs")
print("     metric + matter must cancel;  rel = |SUM| / max|piece|")
print()
for D,Ls in ((2,(12,16,24)),(4,(8,))):
    print(f"  d={D}")
    for L in Ls:
        for mode in (0,1,2,3):
            o=gate(D,L,0.9,0.35,1,mode)
            rel=abs(o["both"])/max(abs(o["metric"]),abs(o["matter"]),1e-30)
            flag="   <== CANCELS" if rel<1e-3 else ""
            print(f"   L={L:2d} {NAMES[mode]:22s} metric={o['metric']:+11.5f} "
                  f"matter={o['matter']:+11.5f} SUM={o['both']:+11.5f} rel={rel:.6f}{flag}", flush=True)
        print(flush=True)
