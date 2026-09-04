"""T183 - THE CONTINUUM TASTE ALGEBRA.  Does R116's u(2) survive the continuum limit?

T182 turned up a nuance that may overturn R116.  The Z^4+scalar (staggered)
construction gave taste algebra u(1) -- NOT the u(4) that T138 measured for the
continuum Kahler-Dirac operator.  That discrepancy is not an error: it is the
well-known fact that STAGGERED FERMIONS HAVE ONLY U(1) EXACT TASTE SYMMETRY AT
FINITE LATTICE SPACING, with the full SU(4) emerging only as a -> 0.

So R116 measured the EXACT FINITE-a algebra of the Z^3+qubit construction, and got
u(2).  But the Standard Model's gauge symmetry would be an EMERGENT continuum
symmetry, so the relevant object is the CONTINUUM taste algebra -- which can be
strictly larger.  R116's negative may therefore be about the wrong limit.

Compute the continuum algebra: expand D(p) about p = 0, keep the leading linear
term D(p) ~ sum_mu p_mu Gamma_mu, and take the commutant of {Gamma_mu}.  That is
the symmetry of the continuum operator the lattice flows to.

CONTROLS: (a) the Z^4+scalar case must return u(4) (dim 16), reproducing T138 and
confirming the method detects emergent symmetry that the finite-a computation
misses; (b) the Gamma_mu must satisfy a Clifford-like algebra."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
def commutant_dim(mats,N):
    A=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    s=np.linalg.svd(A,compute_uv=False)
    return int(np.sum(s<=max(A.shape)*np.finfo(float).eps*s.max()))
def grads(Dfun,d,N,h=1e-5):
    G=[]
    for mu in range(d):
        e=np.zeros(d); e[mu]=h
        G.append((Dfun(e)-Dfun(-e))/(2*h))
    return G
R8=[tuple(r) for r in itertools.product([0,1],repeat=3)]; I8={r:i for i,r in enumerate(R8)}
def shift3(a,sg,p):
    M=np.zeros((8,8),dtype=complex)
    for r in R8:
        s=list(r)
        if sg>0:
            if r[a]==0: s[a]=1; ph=1.0
            else: s[a]=0; ph=np.exp(1j*p[a])
        else:
            if r[a]==1: s[a]=0; ph=1.0
            else: s[a]=1; ph=np.exp(-1j*p[a])
        M[I8[tuple(s)],I8[r]]+=ph
    return M
D3=lambda p: sum(np.kron(shift3(a,1,p)-shift3(a,-1,p),S[a]) for a in range(3))/2.0
R16=[tuple(r) for r in itertools.product([0,1],repeat=4)]; I16={r:i for i,r in enumerate(R16)}
def shift4(a,sg,p):
    M=np.zeros((16,16),dtype=complex)
    for r in R16:
        s=list(r)
        if sg>0:
            if r[a]==0: s[a]=1; ph=1.0
            else: s[a]=0; ph=np.exp(1j*p[a])
        else:
            if r[a]==1: s[a]=0; ph=1.0
            else: s[a]=1; ph=np.exp(-1j*p[a])
        M[I16[tuple(s)],I16[r]]+=((-1)**sum(r[:a]))*ph
    return M
D4=lambda p: sum(shift4(a,1,p)-shift4(a,-1,p) for a in range(4))/2.0
print("T183  continuum vs finite-a taste algebra")
print()
for nm,Dfun,d in (("Z^3 + qubit  (the axioms' own)",D3,3),
                  ("Z^4 + scalar (staggered)",D4,4)):
    G=grads(Dfun,d,16)
    cl=max(np.abs(G[a]@G[b]+G[b]@G[a]-(2 if a==b else 0)*np.eye(16)*
                  (np.trace(G[a]@G[a]).real/16)).max() for a in range(d) for b in range(d))
    dc=commutant_dim(G,16)
    rng=np.random.default_rng(3)
    ps=[rng.uniform(-np.pi,np.pi,size=d) for _ in range(40)]
    df=commutant_dim([Dfun(p) for p in ps],16)
    print(f"   {nm}")
    print(f"      finite-a taste algebra   : dim {df:3d}  -> u({int(round(np.sqrt(df)))})")
    print(f"      CONTINUUM taste algebra  : dim {dc:3d}  -> u({int(round(np.sqrt(dc)))})")
    print(f"      Clifford residual of the Gamma_mu: {cl:.1e}")
    print()
print("   CONTROL: the Z^4 staggered continuum algebra must be u(4) = 16 (T138).")
print("   If it is, the method detects emergent symmetry the finite-a count misses,")
print("   and the Z^3 continuum number is the one that matters for the SM.")
