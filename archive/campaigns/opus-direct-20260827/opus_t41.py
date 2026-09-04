"""T41 - CAN ANY GEOMETRIC WEIGHT WORK?  The decisive test (see RESULT 22 item 5).
A weight w = (l_s l_r)^-gamma supplies a multiplier 1 + 2 gamma on the metric
piece of the gate, so cancellation needs gamma = (needed - 1)/2.  A GEOMETRIC
weight cannot know about the matter.  If the needed exponent depends on m0 or mu,
no universal weight of this class can restore diffeomorphism invariance."""
import numpy as np
D=2; BAS=[(),(0,),(1,),(0,1)]; IDX={b:i for i,b in enumerate(BAS)}; NF=4
def epsm(a):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        if a in Sx: continue
        T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
    return M
def iotam(a,gi):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
    return M
EPS=[epsm(a) for a in range(D)]; IOTf=[iotam(a,np.eye(D)) for a in range(D)]
def Wfun(L,mfield,A,WAVE=1):
    G1=[EPS[WAVE]+(1.0/A[x])*IOTf[WAVE] for x in range(L)]
    tot=0.0
    for j in range(L):
        p=2*np.pi*j/L
        Q=np.zeros((L*NF,L*NF),dtype=complex)
        for x in range(L):
            i=x*NF
            Q[i:i+NF,i:i+NF]+=mfield[x]*np.eye(NF)+1j*np.sin(p)*(EPS[0]+IOTf[0])
            for sgn in (+1,-1):
                y=(x+sgn)%L; Q[i:i+NF,y*NF:y*NF+NF]+=0.5*sgn*0.5*(G1[x]+G1[y])
        tot+=float(np.real(np.linalg.slogdet(Q)[1]))
    return tot
def needed(L,m0,mu,nw=1,e=1e-4):
    xs=np.arange(L)
    xi=np.sin(2*np.pi*nw*xs/L); dxi=(2*np.pi*nw/L)*np.cos(2*np.pi*nw*xs/L)
    m=m0+mu*np.cos(2*np.pi*nw*xs/L); dm=-mu*(2*np.pi*nw/L)*np.sin(2*np.pi*nw*xs/L)
    def piece(which):
        out=[]
        for h in (+e,-e):
            A=np.ones(L); mm=np.array(m,dtype=float)
            if which=="metric": A=1.0+2*h*dxi
            if which=="matter": mm=m+h*xi*dm
            out.append(Wfun(L,list(mm),list(A)))
        return (out[0]-out[1])/(2*e)
    a=piece("metric"); b=piece("matter")
    return abs(b)/abs(a), a, b
print("T41  needed multiplier (and weight exponent gamma = (needed-1)/2)")
print(f"   {'L':>4} {'m0':>5} {'mu':>5} {'needed':>11} {'gamma':>9}")
for m0 in (0.4,0.9,1.6,2.5):
    n,_,_=needed(48,m0,0.35); print(f"   {48:4d} {m0:5.2f} {0.35:5.2f} {n:11.6f} {(n-1)/2:9.5f}", flush=True)
print()
for mu in (0.15,0.35,0.60):
    n,_,_=needed(48,0.9,mu); print(f"   {48:4d} {0.9:5.2f} {mu:5.2f} {n:11.6f} {(n-1)/2:9.5f}", flush=True)
