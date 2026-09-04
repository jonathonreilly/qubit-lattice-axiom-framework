"""T93 - does the 8+8 split SURVIVE curvature and gauge field?
Result 41 found the framework's 16-component fibre splits into two invariant
8-dimensional sectors (two flavours each), exact to 1.5e-12 for the free operator
on a flat torus.  Robust structure, or a flat-space accident?  Result 34 showed
curvature splits the flavour degeneracy, so it is a fair bet curvature also
breaks this -- and that is worth knowing either way.

Test in position space (where curvature and gauge fields live) rather than
momentum space: build the projector onto one sector, and measure how much the
operator LEAKS out of it, for
   (a) the flat free operator      -- must be ~0, the control;
   (b) a curved metric             -- Result 34's mechanism;
   (c) a U(1) gauge flux           -- Result 40's mechanism."""
import numpy as np, itertools
d=4; L=3
BAS=[]
for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
def Dq(q):
    D=np.zeros((NF,NF),dtype=complex)
    for S in BAS:
        for a in range(d):
            if a in S: continue
            T=tuple(sorted(S+(a,))); sg=(-1)**sum(1 for i in S if i<a)
            D[IDX[T],IDX[S]]+=sg*(np.exp(1j*q[a])-1.0)
    return D+D.conj().T
qs=[tuple(2*np.pi*np.array(n)/6) for n in itertools.product(range(6),repeat=d)][::7][:60]
A=np.vstack([np.kron(np.eye(NF),Dq(q))-np.kron(Dq(q).T,np.eye(NF)) for q in qs])
u,s,vh=np.linalg.svd(A); tol=1e-9*max(A.shape)*s[0]
nul=int(np.sum(s<tol))+(A.shape[1]-len(s))
B=vh[len(s)-nul:].conj().reshape(nul,NF,NF)
I=np.eye(NF,dtype=complex); X=None
for M in B:
    Mp=M-np.trace(M.conj().T@I)/NF*I
    if np.linalg.norm(Mp)>1e-8: X=Mp; break
Xh=0.5*(X+X.conj().T)
if np.linalg.norm(Xh)<1e-8: Xh=0.5j*(X-X.conj().T)
w,V=np.linalg.eigh(Xh)
sec=[i for i in range(NF) if w[i]<0]; oth=[i for i in range(NF) if w[i]>=0]
P=V[:,sec]; Pp=V[:,oth]
print(f"T93  sector projector built: {len(sec)} + {len(oth)}")
sites=list(itertools.product(range(L),repeat=d)); sid={s:i for i,s in enumerate(sites)}
def shift(s,a):
    t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
def bigD(metric=None,flux=0.0):
    N=len(sites)*NF; D=np.zeros((N,N),dtype=complex)
    for s in sites:
        g=np.ones(d) if metric is None else metric(s)
        for S in BAS:
            for a in range(d):
                if a in S: continue
                T=tuple(sorted(S+(a,))); sg=(-1)**sum(1 for i in S if i<a)
                ph=np.exp(1j*flux*s[0]) if a==1 else 1.0
                wgt=np.sqrt(g[a])
                r=shift(s,a)
                D[sid[s]*NF+IDX[T], sid[s]*NF+IDX[S]] += -sg*wgt
                D[sid[s]*NF+IDX[T], sid[r]*NF+IDX[S]] +=  sg*wgt*ph
    return D+D.conj().T
def leakage(D):
    N=len(sites)
    Pb=np.kron(np.eye(N),P); Ppb=np.kron(np.eye(N),Pp)
    return float(np.linalg.norm(Ppb.conj().T@D@Pb))/max(float(np.linalg.norm(D)),1e-12)
curved=lambda s: np.array([1.0+0.3*np.cos(2*np.pi*s[1]/L),
                           1.0+0.3*np.cos(2*np.pi*s[2]/L),
                           1.0+0.3*np.cos(2*np.pi*s[3]/L),1.0])
print(f"   {'configuration':>28} {'relative leakage out of the sector':>36}")
print(f"   {'flat, free (control)':>28} {leakage(bigD()):36.3e}")
print(f"   {'curved metric':>28} {leakage(bigD(metric=curved)):36.3e}")
for fl in (0.3,1.0):
    print(f"   {'U(1) flux '+str(fl):>28} {leakage(bigD(flux=fl)):36.3e}", flush=True)
print()
print("   control ~0 and the others nonzero => curvature and gauge fields BREAK the")
print("   8+8 split, so it is a property of the free flat rule, not a conserved")
print("   quantum number of the theory.  All ~0 => the split is robust structure.")
