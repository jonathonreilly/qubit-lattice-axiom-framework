"""T94 - the commutant done properly: is it 2-dimensional or just the identity?
T93b traced the failed control to my own sampling: the commutant in T91/T92 was
computed from 60 of 1296 momenta, so the 'second element' X commutes with the
SAMPLED momenta and not with all of them.  The evidence was in the numbers and I
missed it -- X's traceless part has norm 0.0157 against a basis vector of norm 1,
and its eigenvalues are +-0.0039.  That is a near-null direction picked up by the
tolerance, not a symmetry.

Redo it honestly: sweep the number of momenta and watch the singular-value gap.
A genuine commutant element stays in the null space as momenta are added; an
artefact is squeezed out."""
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
rng=np.random.default_rng(1)
order=rng.permutation(len(allq))
print("T94  commutant dimension vs how many momenta are imposed")
print(f"   {'#momenta':>9} {'smallest 4 singular values':>44} {'dim (tol 1e-8)':>16}")
for nq in (5,20,60,200,600,1296):
    sel=[allq[i] for i in order[:nq]]
    A=np.vstack([np.kron(np.eye(NF),Dq(q))-np.kron(Dq(q).T,np.eye(NF)) for q in sel])
    s=np.linalg.svd(A,compute_uv=False)
    s=np.concatenate([s,np.zeros(max(0,NF*NF-len(s)))])
    small=np.sort(s)[:4]
    dim=int(np.sum(s<1e-8*max(1.0,s.max())))
    print(f"   {nq:9d} {str([f'{v:.3e}' for v in small]):>44} {dim:16d}", flush=True)
print()
print("   the gap tells the story: if only ONE singular value is at machine zero")
print("   once enough momenta are imposed, the commutant is the identity alone and")
print("   the 8+8 split of Result 41 was an artefact of undersampling.")
