"""T91 - WHAT IS THE FRAMEWORK'S INTERNAL SYMMETRY?  The commutant of the rule.
Result 40 found a U(1) gauge field in the phase freedom of the comparison.  A
theory of everything needs more than U(1), and there is a framework-native place
for it: Result 33's FOUR FLAVOURS.  If the operator has an internal symmetry
acting on those, that symmetry is a gauge-group-shaped object arising from the
framework rather than imposed on it.

That is computable exactly.  In momentum space the operator is a 16x16 matrix
D(q) at each momentum, and the internal symmetry is the COMMUTANT: the set of
fibre matrices M with [M, D(q)] = 0 for EVERY q.  Its dimension is the answer:

   dim 1   -> no internal symmetry beyond a phase
   dim 16  -> u(4), the flavour symmetry of four Dirac species
   dim 256 -> everything commutes, i.e. D carries no fibre structure at all

The commutant is a linear condition on M, so this is a null-space computation
and the dimension is exact."""
import numpy as np, itertools
d=4; L=6
BAS=[]
for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
print(f"T91  cubical complex, d={d}: fibre dimension {NF} (degrees {[len([b for b in BAS if len(b)==k]) for k in range(d+1)]})")
def Dq(q):
    """momentum-space coboundary + adjoint on the 2^d fibre"""
    D=np.zeros((NF,NF),dtype=complex)
    for S in BAS:
        for a in range(d):
            if a in S: continue
            T=tuple(sorted(S+(a,))); sg=(-1)**sum(1 for i in S if i<a)
            ph=np.exp(1j*q[a])-1.0
            D[IDX[T],IDX[S]]+=sg*ph
    return D+D.conj().T
qs=[tuple(2*np.pi*np.array(n)/L) for n in itertools.product(range(L),repeat=d)]
sel=qs[::7][:60]
print(f"     sampling {len(sel)} momenta out of {len(qs)}")
rows=[]
for q in sel:
    D=Dq(q)
    # [M,D] = 0  ->  (I kron D^T - D kron I) vec(M) = 0   (row-major vec)
    rows.append(np.kron(np.eye(NF),D) - np.kron(D.T,np.eye(NF)))
A=np.vstack(rows)
u,s,vh=np.linalg.svd(A)
tol=1e-9*max(A.shape)*s[0]
nul=int(np.sum(s<tol)) + (A.shape[1]-len(s))
print(f"     commutant dimension over the sampled momenta: {nul}")
print(f"     (fibre matrix space is {NF*NF} dimensional)")
basis=vh[len(s)-nul:].conj() if nul>0 else np.zeros((0,NF*NF))
print()
print("   what the commutant contains:")
ident=np.eye(NF).reshape(-1)
ident=ident/np.linalg.norm(ident)
if nul>0:
    B=basis.reshape(nul,NF,NF)
    proj=abs(basis@ident)
    print(f"     identity is in it: {bool(np.max(proj)>1e-8)}")
    herm=sum(1 for M in B if np.allclose(M,M.conj().T,atol=1e-8))
    print(f"     {herm} of {nul} basis elements are hermitian")
    # does the commutant preserve form DEGREE?
    degop=np.diag([len(b) for b in BAS]).astype(complex)
    comm_deg=sum(1 for M in B if np.allclose(M@degop-degop@M,0,atol=1e-8))
    print(f"     {comm_deg} of {nul} commute with the degree operator")
print()
print("   dim 1 => only the phase of Result 40.  dim 16 => u(4), the flavour")
print("   symmetry of four Dirac species, arising from the framework itself.")
