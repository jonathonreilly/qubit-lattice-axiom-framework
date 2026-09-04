"""T93b - debugging T93: the control failed, so something disagrees.
T93 measured a relative leakage of 0.2795 out of the 8-dimensional sector even
for the FLAT FREE operator, where T92 measured 1.5e-12 in momentum space.  One of
the two is wrong.  Isolate it: build the SAME projector and measure the leakage
(i) momentum by momentum, and (ii) in position space, on the same operator."""
import numpy as np, itertools
d=4
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
print(f"T93b  commutant dim {nul}")
I=np.eye(NF,dtype=complex)
for bi,M in enumerate(B):
    print(f"   basis {bi}: ||[M,D(q0)]|| = {np.linalg.norm(M@Dq(qs[0])-Dq(qs[0])@M):.3e}"
          f"   hermitian: {bool(np.allclose(M,M.conj().T,atol=1e-8))}"
          f"   ||M - tr(M)/16 I|| = {np.linalg.norm(M-np.trace(M)/NF*I):.3e}")
X=None
for M in B:
    Mp=M-np.trace(M)/NF*I
    if np.linalg.norm(Mp)>1e-8: X=Mp; break
print(f"   picked X: ||[X,D(q0)]|| = {np.linalg.norm(X@Dq(qs[0])-Dq(qs[0])@X):.3e}")
Xh=0.5*(X+X.conj().T); Xa=0.5j*(X-X.conj().T)
for nm,M in (("hermitian part",Xh),("antihermitian part",Xa)):
    print(f"   {nm}: norm {np.linalg.norm(M):.3e}   "
          f"||[M,D(q0)]|| = {np.linalg.norm(M@Dq(qs[0])-Dq(qs[0])@M):.3e}")
Xu = Xh if np.linalg.norm(Xh)>1e-8 else Xa
w,V=np.linalg.eigh(Xu)
print(f"   eigenvalues of the chosen generator: {sorted(set(np.round(w,6)))}")
sec=[i for i in range(NF) if w[i]<np.mean(w)]
P=V[:,sec]; Pp=V[:,[i for i in range(NF) if i not in sec]]
print(f"   sector sizes: {len(sec)} + {NF-len(sec)}")
print()
print("   (i) leakage momentum by momentum (should be ~0 if T92 is right)")
worst=0.0
for q in qs[:8]:
    lk=float(np.linalg.norm(Pp.conj().T@Dq(q)@P))/max(float(np.linalg.norm(Dq(q))),1e-12)
    worst=max(worst,lk)
print(f"       worst over 8 momenta: {worst:.3e}")
print()
print("   (ii) leakage in POSITION space on the same free operator")
L=3
sites=list(itertools.product(range(L),repeat=d)); sid={s:i for i,s in enumerate(sites)}
def shift(s,a):
    t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
N=len(sites)*NF; D=np.zeros((N,N),dtype=complex)
for s in sites:
    for S in BAS:
        for a in range(d):
            if a in S: continue
            T=tuple(sorted(S+(a,))); sg=(-1)**sum(1 for i in S if i<a)
            r=shift(s,a)
            D[sid[s]*NF+IDX[T], sid[s]*NF+IDX[S]] += -sg
            D[sid[s]*NF+IDX[T], sid[r]*NF+IDX[S]] +=  sg
D=D+D.conj().T
Pb=np.kron(np.eye(len(sites)),P); Ppb=np.kron(np.eye(len(sites)),Pp)
print(f"       relative leakage: {float(np.linalg.norm(Ppb.conj().T@D@Pb))/float(np.linalg.norm(D)):.3e}")
print()
print("   if (i) is ~0 and (ii) is not, the position-space operator is not the same")
print("   object as the momentum-space one and T93's control failure is a bug in it.")
