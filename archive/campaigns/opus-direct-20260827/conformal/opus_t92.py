"""T92 - DOES THE FIBRE SPLIT?  Can the four flavours be reduced?
T91: the momentum-diagonal commutant of the framework's operator is
2-dimensional -- identity plus one element X, and X is NOT the Hodge star, the
degree operator or the parity.  By Schur's lemma a 2-dimensional commutant means
the 16-component fibre is NOT irreducible: it splits into invariant subspaces,
and X is what labels them.

That bears directly on Result 33's counting problem.  If the fibre splits 8+8,
the operator preserves two sectors of two flavours each, and 'four flavours' is
really 'two sectors of two'.  If it splits 15+1 or something lopsided, that is a
different story again.

Find X, diagonalise it, and read off the dimensions of the invariant subspaces --
then verify directly that D really does preserve them at every momentum."""
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
L=6
qs=[tuple(2*np.pi*np.array(n)/L) for n in itertools.product(range(L),repeat=d)]
sel=qs[::7][:60]
A=np.vstack([np.kron(np.eye(NF),Dq(q))-np.kron(Dq(q).T,np.eye(NF)) for q in sel])
u,s,vh=np.linalg.svd(A)
tol=1e-9*max(A.shape)*s[0]; nul=int(np.sum(s<tol))+(A.shape[1]-len(s))
B=vh[len(s)-nul:].conj().reshape(nul,NF,NF)
print(f"T92  commutant dimension {nul}")
# project out the identity to isolate X
I=np.eye(NF,dtype=complex)
X=None
for M in B:
    Mp=M-np.trace(M.conj().T@I)/NF*I
    if np.linalg.norm(Mp)>1e-8: X=Mp/np.linalg.norm(Mp); break
if X is None:
    print("   commutant is only the identity"); raise SystemExit
Xh=0.5*(X+X.conj().T)
if np.linalg.norm(Xh)<1e-8: Xh=0.5j*(X-X.conj().T)
Xh=Xh/np.linalg.norm(Xh)
w,V=np.linalg.eigh(Xh)
groups=[]
for z in np.round(w,8):
    if groups and abs(z-groups[-1][0])<1e-6: groups[-1][1]+=1
    else: groups.append([z,1])
print(f"   the non-identity element X: eigenvalues {[(round(float(a),6),b) for a,b in groups]}")
print(f"   => the fibre splits as {[b for _,b in groups]}")
print()
print("   verifying that D really preserves those subspaces, at every sampled momentum:")
worst=0.0
for a,(val,mult) in enumerate(groups):
    idx=[i for i in range(NF) if abs(w[i]-val)<1e-6]
    P=V[:,idx]                                   # basis of the subspace
    Pperp=V[:,[i for i in range(NF) if i not in idx]]
    for q in sel[:20]:
        leak=float(np.linalg.norm(Pperp.conj().T@Dq(q)@P))
        worst=max(worst,leak)
    print(f"     subspace of dimension {mult}: max leakage out of it = {worst:.3e}")
print()
print(f"   worst leakage over all subspaces and momenta: {worst:.3e}")
print("   near zero => the framework's operator preserves the split, so the 16")
print("   components are not one irreducible block and the flavour count has")
print("   internal structure.  Large => X is an artefact and the fibre is irreducible.")
