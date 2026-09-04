"""T37b - (i) does the gate residual survive the CONTINUUM limit?  (ii) the polar
edge factor is second order in the perturbation -- measured, not just argued.

(i) T35's residual did not shrink from L=8 to L=12, but that is a short lever.
Push the wavelength out in d=2 (cheap) to k = 2pi/32 and watch the RATIO
|sum| / max|piece|.  A discretisation artefact must die like k^2; a structural
failure must not.

(ii) CLAIM: for any linearised metric perturbation the polar orthogonal factor
of e_s e_r^-1 is I + O(h^2), so it CANNOT reproduce the linearised Levi-Civita
spin connection, which is O(h).  Proof: g = I + hA, e = sqrt(g) = I + (h/2)A;
M = e_s e_r^-1 = I + (h/2)(A_s - A_r) + O(h^2), and (A_s - A_r) is SYMMETRIC, so
M = I + h*(symmetric) + O(h^2); for M = I + hS with S symmetric the polar factor
is M(M^T M)^(-1/2) = (I+hS)(I-hS) + O(h^2) = I + O(h^2).  Measured below by
scaling h over four decades with two NON-COMMUTING metric directions."""
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
def Wfun(D,L,mfield,gfield,WAVE=1):
    B,IDX,NF,epsm,iotam=make_ops(D)
    EPS=[epsm(a) for a in range(D)]
    gi=[np.linalg.inv(gfield[x]) for x in range(L)]
    IOT=[[iotam(a,gi[x]) for a in range(D)] for x in range(L)]
    GAM=[[EPS[a]+IOT[x][a] for a in range(D)] for x in range(L)]
    trans=[a for a in range(D) if a!=WAVE]; tot=0.0
    for pidx in itertools.product(range(L),repeat=D-1):
        p={a:2*np.pi*pidx[i]/L for i,a in enumerate(trans)}
        Q=np.zeros((L*NF,L*NF),dtype=complex)
        for x in range(L):
            i=x*NF
            Q[i:i+NF,i:i+NF]+=mfield[x]*np.eye(NF)
            for a in trans: Q[i:i+NF,i:i+NF]+=1j*np.sin(p[a])*GAM[x][a]
            for sgn in (+1,-1):
                y=(x+sgn)%L; j=y*NF
                Q[i:i+NF,j:j+NF]+=0.25*sgn*(2*EPS[WAVE]+IOT[x][WAVE]+IOT[y][WAVE])
        tot+=float(np.real(np.linalg.slogdet(Q)[1]))
    return tot
def gate(D,L,m0,mu,nw,e=1e-4):
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
        o[which]=(Wfun(D,L,mp,gp)-Wfun(D,L,mm_,gm))/(2*e)
    return o
print("T37b (i)  continuum limit of the gate residual, d=2, nw=1")
print(f"   {'L':>3} {'k=2pi/L':>9} {'metric':>14} {'matter':>14} {'SUM':>14} {'rel':>9} {'rel/k^2':>10}")
for L in (8,12,16,24,32):
    o=gate(2,L,0.9,0.35,1); k=2*np.pi/L
    rel=abs(o["both"])/max(abs(o["metric"]),abs(o["matter"]))
    print(f"   {L:3d} {k:9.5f} {o['metric']:+14.6f} {o['matter']:+14.6f} {o['both']:+14.6f}"
          f" {rel:9.6f} {rel/k**2:10.4f}", flush=True)
print()
print("   A discretisation artefact would show rel falling like k^2 (rel/k^2 constant).")
print()
print("T37b (ii)  polar edge factor scaling: two NON-COMMUTING metric directions")
A=np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,0.]])          # off-diagonal (1,2)
Bm=np.array([[0.,0.,1.],[0.,0.,0.],[1.,0.,0.]])         # off-diagonal (1,3); [A,B] != 0
print(f"   [A,B] nonzero: {not np.allclose(A@Bm, Bm@A)}")
def sq(g):
    w,V=np.linalg.eigh(g); return V@np.diag(np.sqrt(w))@V.T
print(f"   {'h':>10} {'||R - I||':>16} {'||R-I||/h':>14} {'||R-I||/h^2':>14}")
for h in (1e-1,1e-2,1e-3,1e-4):
    gs=np.eye(3)+h*A; gr=np.eye(3)+h*Bm
    M=sq(gs)@np.linalg.inv(sq(gr))
    U,_,Vt=np.linalg.svd(M); R=U@Vt
    n=np.linalg.norm(R-np.eye(3))
    print(f"   {h:10.1e} {n:16.10e} {n/h:14.6e} {n/h**2:14.6e}", flush=True)
print("   constant in the LAST column = second order = cannot be the spin connection.")
