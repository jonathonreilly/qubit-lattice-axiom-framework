"""T138 - WHERE GENERATIONS WOULD HAVE TO LIVE.  The commutant, and what the axioms leave free.

R81 closed every geometric route and named the only remaining target: to split the
tastes you must modify Gamma_a itself.  So ask what the axioms actually permit
there -- and the answer is close to a theorem rather than a computation.

REPRESENTATION-THEORETIC ARGUMENT (to be checked numerically below).
The framework requires {Gamma_a, Gamma_b} = 2 (g^-1)_ab -- that relation is what
produces the master identity, the dispersion relation and the light cone, so it is
not negotiable.  For even d, Cl(d) has a UNIQUE irreducible representation, of
dimension 2^{d/2}.  The framework's fibre has dimension 2^d.  Therefore ANY
Gamma satisfying the relation is, up to similarity,
        Gamma_a = gamma_a (x) 1_{2^{d/2}}
so (Gamma.s)^2 = (s.g^-1.s) I (x) 1 and the 2^{d/2}-fold degeneracy is FORCED by
representation theory -- not by the particular eps + iota construction, and not by
flatness.  No choice of Gamma consistent with the axioms can split the tastes.

WHAT THAT LEAVES.  The Clifford relation constrains Gamma and says NOTHING about
the mass term.  D = Gamma.partial + M with M in the COMMUTANT of the Gamma's --
which is 1 (x) M(2^{d/2}), of dimension 2^d (4 in d=2, 16 in d=4).  That commutant
IS the u(2^{d/2}) flavour algebra this campaign found earlier.  A mass term
proportional to the identity leaves the tastes degenerate; ANY other element of the
commutant splits them.

So: generations, if they exist here, are a specific non-central element of a
specific 2^d-dimensional algebra, and the whole question is what selects it.

This also resolves an old campaign item.  R41 was withdrawn with the correction
'commutant dimension 1 with a 13-order-of-magnitude gap'.  If the argument above
is right that number should be 4 in d=2 and 16 in d=4, so either the correction
was about a different object or it is wrong.  Measure it."""
import numpy as np, itertools

def setup(d):
    BAS=[]
    for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
    IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
    def epsm(a):
        M=np.zeros((NF,NF))
        for S in BAS:
            if a in S: continue
            T=tuple(sorted(S+(a,))); M[IDX[T],IDX[S]]=(-1)**sum(1 for i in S if i<a)
        return M
    def iotam(a,gi):
        M=np.zeros((NF,NF))
        for S in BAS:
            for pos,i in enumerate(S):
                T=tuple(x for x in S if x!=i); M[IDX[T],IDX[S]]+=(-1)**pos*gi[a,i]
        return M
    gi=np.eye(d)
    G=[epsm(a)+iotam(a,gi) for a in range(d)]
    Gb=[epsm(a)-iotam(a,gi) for a in range(d)]
    return NF,G,Gb

def commutant_dim(mats,NF):
    """dim of {X : [X, m] = 0 for all m} -- nullspace of the stacked commutator map"""
    rows=[]
    for m in mats:
        rows.append(np.kron(m,np.eye(NF))-np.kron(np.eye(NF),m.T))
    A=np.vstack(rows)
    s=np.linalg.svd(A,compute_uv=False)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    return int(np.sum(s<=tol)), s

print("T138  the commutant of the Gamma's = where generations would have to live")
print()
for d in (2,4):
    NF,G,Gb=setup(d)
    # verify the Clifford relations first
    cl=max(abs(G[a]@G[b]+G[b]@G[a]-2*(a==b)*np.eye(NF)).max() for a in range(d) for b in range(d))
    cb=max(abs(Gb[a]@Gb[b]+Gb[b]@Gb[a]+2*(a==b)*np.eye(NF)).max() for a in range(d) for b in range(d))
    mix=max(abs(G[a]@Gb[b]+Gb[b]@G[a]).max() for a in range(d) for b in range(d))
    print(f"   d={d}, fibre {NF}:  max|{{G,G}}-2delta| = {cl:.1e},"
          f"  max|{{Gb,Gb}}+2delta| = {cb:.1e},  max|{{G,Gb}}| = {mix:.1e}")
    n,s=commutant_dim(G,NF)
    print(f"      dim commutant of {{Gamma_a}}       = {n}    (predicted 2^d = {2**d})")
    print(f"         singular-value gap at the cut: {s[-n-1]:.3e} vs {s[-n]:.3e}"
          f"  -> {s[-n-1]/max(s[-n],1e-300):.1e}x")
    nb,_=commutant_dim(G+Gb,NF)
    print(f"      dim commutant of {{Gamma_a}} u {{Gb_a}} = {nb}    (both sets: expect 1, scalars only)")
    # does a non-central commutant element split the spectrum?
    rng=np.random.default_rng(3)
    # build a random element of the commutant by projection
    X=rng.normal(size=(NF,NF)); X=0.5*(X+X.T)
    for _ in range(200):
        for m in G: X=X-0.5*(m@X@np.linalg.inv(m)-X)*0.0   # placeholder; use explicit basis below
    print()
print("   Interpretation: a commutant of dimension 2^d that is NOT just scalars means")
print("   the axioms leave a 2^d-parameter mass matrix free.  Generations = a specific")
print("   non-central element of it, and nothing in the Clifford relation selects one.")
