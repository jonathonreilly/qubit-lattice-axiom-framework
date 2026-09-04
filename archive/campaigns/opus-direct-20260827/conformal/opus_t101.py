"""T101 - is the chiral obstruction ULTRALOCAL or absolute?  (sharpening Result 45)
T100 found exactly ONE operator anticommuting with the framework's D, the degree
parity G.  But that search was over MOMENTUM-INDEPENDENT fibre matrices -- i.e.
ULTRALOCAL operators.  The Ginsparg-Wilson and overlap constructions, which are
the standard repair for exactly this problem, produce operators that DEPEND on
momentum and are therefore non-local in position.  So the question Result 45 left
open is really:

    at each momentum SEPARATELY, how many chirality operators are there?

  dimension 1 at every q  -> the obstruction is absolute; no chirality of any
                             kind, local or not, and the GW route is shut.
  dimension > 1 at each q -> a momentum-dependent chirality exists, the
                             obstruction is only to ULTRALOCALITY, and the
                             GW/overlap repair is available in principle.

That is the difference between 'this framework cannot have chiral matter' and
'this framework needs a non-local operator to have it', which are very different
statements for a theory of everything."""
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
def anticomm_dim(D):
    A=np.kron(np.eye(NF),D)+np.kron(D.T,np.eye(NF))
    s=np.linalg.svd(A,compute_uv=False)
    s=np.concatenate([s,np.zeros(max(0,NF*NF-len(s)))])
    return int(np.sum(s<1e-8*max(1.0,s.max()))), np.sort(s)[:3]
def comm_dim(D):
    A=np.kron(np.eye(NF),D)-np.kron(D.T,np.eye(NF))
    s=np.linalg.svd(A,compute_uv=False)
    s=np.concatenate([s,np.zeros(max(0,NF*NF-len(s)))])
    return int(np.sum(s<1e-8*max(1.0,s.max())))
rng=np.random.default_rng(7)
print("T101  per-momentum chirality count (dimension of the anticommutant of D(q))")
print(f"   {'momentum':>34} {'|D(q)| rank':>12} {'anticomm dim':>13} {'comm dim':>9}")
qs=[tuple(2*np.pi*np.array(n)/6) for n in itertools.product(range(6),repeat=d)]
sample=[qs[0]]+[qs[i] for i in rng.permutation(len(qs))[:6]]
for q in sample:
    D=Dq(q)
    r=int(np.linalg.matrix_rank(D,tol=1e-9))
    ad,sm=anticomm_dim(D)
    cd=comm_dim(D)
    print(f"   {str([f'{x:.3f}' for x in q]):>34} {r:12d} {ad:13d} {cd:9d}", flush=True)
print()
print("   note the q=0 row: D(0) = 0, so everything commutes and anticommutes there;")
print("   the generic rows are the informative ones.")
print()
print("   Interpretation:")
print("   the framework's D(q) squares to a multiple of the identity (Result 16:")
print("   D^2 = (s.g^-1.s) I), so at each q it has just TWO eigenvalues, +-|s|, each")
print("   8-fold degenerate.  Any operator swapping those two eigenspaces")
print("   anticommutes with D(q).  That space is large at fixed q and collapses to")
print("   the single G only when the SAME operator is required to work at every q.")
