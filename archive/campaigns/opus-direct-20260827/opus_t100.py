"""T100 - IS THERE A GAMMA-5?  The anticommutant of the framework's operator.
T99: the framework's index is the Euler characteristic, not the gauge index, so
the operator does NOT carry the chiral anomaly.  Result 41 says why it might be
structural: the internal symmetry is the vector phase alone, with no axial
partner.  A chiral symmetry needs an operator that ANTICOMMUTES with D, so
compute the anticommutant

        { M : M D(q) + D(q) M = 0  for every q }

exactly, the same way Result 41/T94 computed the commutant -- and with the
tolerance lesson from T94 applied, sweeping the number of momenta so a near-null
direction cannot be mistaken for a symmetry.

  dim 0  -> no chiral operator at all
  dim 1  -> exactly one: the degree parity G, which gives chi and not the anomaly
  dim >1 -> something else exists and the chiral question is open"""
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
allq=[tuple(2*np.pi*np.array(n)/6) for n in itertools.product(range(6),repeat=d)]
rng=np.random.default_rng(2); order=rng.permutation(len(allq))
print("T100  anticommutant dimension vs momenta imposed (tolerance lesson from T94)")
print(f"   {'#momenta':>9} {'smallest 3 singular values':>38} {'dim':>6}")
for nq in (5,20,100,400,1296):
    sel=[allq[i] for i in order[:nq]]
    A=np.vstack([np.kron(np.eye(NF),Dq(q))+np.kron(Dq(q).T,np.eye(NF)) for q in sel])
    s=np.linalg.svd(A,compute_uv=False)
    s=np.concatenate([s,np.zeros(max(0,NF*NF-len(s)))])
    dim=int(np.sum(s<1e-8*max(1.0,s.max())))
    print(f"   {nq:9d} {str([f'{v:.3e}' for v in np.sort(s)[:3]]):>38} {dim:6d}", flush=True)
sel=[allq[i] for i in order[:1296]]
A=np.vstack([np.kron(np.eye(NF),Dq(q))+np.kron(Dq(q).T,np.eye(NF)) for q in sel])
u,s,vh=np.linalg.svd(A)
dim=int(np.sum(s<1e-8*s.max()))+(A.shape[1]-len(s))
print(f"\n   anticommutant dimension (all momenta): {dim}")
if dim>0:
    B=vh[len(s)-dim:].conj().reshape(dim,NF,NF)
    par=np.diag([(-1)**len(b) for b in BAS]).astype(complex)
    v=par.reshape(-1)/np.linalg.norm(par)
    P=B.reshape(dim,-1); Q,_=np.linalg.qr(P.conj().T)
    res=float(np.linalg.norm(v-Q@(Q.conj().T@v)))
    print(f"   is it the degree parity G = (-1)^deg?  residual {res:.2e}  -> {res<1e-7}")
    for i,M in enumerate(B[:3]):
        print(f"   element {i}: hermitian {bool(np.allclose(M,M.conj().T,atol=1e-8))}, "
              f"M^2 proportional to I: "
              f"{bool(np.allclose(M@M-np.trace(M@M)/NF*np.eye(NF),0,atol=1e-8))}")
print()
print("   dim 1 and it is G  =>  the ONLY chiral-type operator is the degree parity,")
print("   which by Result 39 gives the Euler characteristic and not the gauge index.")
print("   The framework has no gamma-5, hence no axial symmetry and no chiral anomaly.")
