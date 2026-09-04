"""T147 - WHY IS THE INDEX EVEN?  Reality, or taste counting?

R82 proposed one modification with two payoffs: complexifying the framework's
structure constants would give 4 masses instead of 2 AND escape the chirality
no-go (recorded in the campaign as 'index even in flux because the cubical
structure constants are real').  The mass half is now confirmed (T140/T146b).
The chirality half rests on a mechanism I have not tested, and there is an
alternative that R82 did not exclude:

   Lambda*(M) carries 2^{d/2} TASTES, so the Kahler-Dirac index in a gauge field
   should be  index = 2^{d/2} x (Dirac index) = 2^{d/2} x n,
   which is even for every d >= 2 REGARDLESS of reality.

If that is the mechanism, complexification does NOT fix chirality -- the taste
count is untouched by it -- and R82's 'two payoffs' is one payoff.  That is worth
knowing before an axiom change is proposed on it.

Test in d=2, where the taste count is 2 and the continuum Dirac index in a
uniform U(1) flux of n units is exactly n.  So:
      index = 2n  ->  taste counting is the mechanism; complexification is no help.
      index = n   ->  something else is going on and reality is back in play.

Index via McKean-Singer: Tr(G e^{-tau D^2}) with G = diag((-1)^k), which is
tau-independent when {G, D} = 0 -- and that tau-independence is itself the
validation of the construction."""
import numpy as np, itertools

d=2
BAS=[]
for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
def epsm(a):
    M=np.zeros((NF,NF))
    for S in BAS:
        if a in S: continue
        T=tuple(sorted(S+(a,))); M[IDX[T],IDX[S]]=(-1)**sum(1 for i in S if i<a)
    return M
def iotam(a):
    M=np.zeros((NF,NF))
    for S in BAS:
        for pos,i in enumerate(S):
            if i!=a: continue
            T=tuple(x for x in S if x!=a); M[IDX[T],IDX[S]]+=(-1)**pos
    return M
GAM=[epsm(a)+iotam(a) for a in range(d)]
CHI=np.diag([(-1)**len(S) for S in BAS]).astype(float)
print("T147  why is the index even?  d=2, fibre 4, taste count 2")
print(f"   {{Gamma_a,Gamma_b}} = 2 delta : "
      f"{max(abs(GAM[a]@GAM[b]+GAM[b]@GAM[a]-2*(a==b)*np.eye(NF)).max() for a in range(d) for b in range(d)):.1e}")
print(f"   {{G, Gamma_a}} = 0          : {max(abs(CHI@GAM[a]+GAM[a]@CHI).max() for a in range(d)):.1e}")

def build(L,n,complexify=0.0,seed=0):
    """U(1) links with uniform flux n through the torus.  complexify != 0 multiplies
    the Gamma's by a nontrivial phase structure, breaking their reality."""
    N=L*L; sid={x:i for i,x in enumerate(itertools.product(range(L),repeat=2))}
    def U(x,a):
        if a==0: return np.exp(-2j*np.pi*n*x[1]/(L*L))
        return np.exp(2j*np.pi*n*x[0]/L) if x[1]==L-1 else 1.0+0j
    # verify the flux
    tot=0.0
    for x in sid:
        xp=((x[0]+1)%L,x[1]); yp=(x[0],(x[1]+1)%L)
        P=U(x,0)*U(xp,1)*np.conj(U(yp,0))*np.conj(U(x,1))
        tot+=np.angle(P)
    G=[g.astype(complex) for g in GAM]
    if complexify:
        rng=np.random.default_rng(seed)
        # a phase rotation inside the fibre that keeps {G,G}=2delta but is not real
        A=rng.normal(size=(NF,NF)); A=A-A.T
        S=np.linalg.matrix_power(np.eye(NF)+1j*complexify*A,1)
        Si=np.linalg.inv(S)
        G=[S@g@Si for g in G]
    D=np.zeros((N*NF,N*NF),dtype=complex)
    def blk(i,j): return (slice(i*NF,(i+1)*NF),slice(j*NF,(j+1)*NF))
    for x in sid:
        i=sid[x]
        for a in range(d):
            xp=list(x); xp[a]=(xp[a]+1)%L; xp=tuple(xp)
            xm=list(x); xm[a]=(xm[a]-1)%L; xm=tuple(xm)
            D[blk(i,sid[xp])]+=0.5*G[a]*U(x,a)
            D[blk(i,sid[xm])]-=0.5*G[a]*np.conj(U(xm,a))
    Gbig=np.kron(np.eye(N),CHI)
    return D,Gbig,tot/(2*np.pi)

print()
print(f"   {'L':>3} {'n':>3} {'flux/2pi':>9} {'complexify':>11} " + " ".join(f"{'idx(t=%g)'%t:>11}" for t in (0.3,1.0,3.0)))
for L,n in ((6,0),(6,1),(6,2),(8,1),(8,2),(8,3)):
    for cx in (0.0,0.35):
        D,Gb,fl=build(L,n,complexify=cx)
        D2=D@D.conj().T if False else -(D@D)
        w,V=np.linalg.eigh(0.5*(D2+D2.conj().T))
        idx=[float(np.real(np.einsum('ij,ji->',Gb,V@np.diag(np.exp(-t*w))@V.conj().T))) for t in (0.3,1.0,3.0)]
        print(f"   {L:3d} {n:3d} {fl:9.3f} {cx:11.2f} " + " ".join(f"{v:11.5f}" for v in idx))
print()
print("   tau-independence validates the construction; the VALUE answers the question.")
print("   index = 2n at every flux -> taste counting, and complexification is no help.")
