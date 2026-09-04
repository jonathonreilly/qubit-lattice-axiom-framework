"""T192 - DOES THE LATTICE FORCE A SUBGROUP OF u(8), OR IS THE EMBEDDING FREE?

R124 left representation content as the last matter-side item.  The counting works:
32 complex components = 16 Weyl = 8 left + 8 right, exactly one Standard Model
generation, now chirally coupled.  And the 8 per chirality would be the SM content
if u(8) is broken as (4,2) of su(4) x su(2) -- the Pati-Salam multiplet, since
4 = 3 + 1 gives (3,2) + (1,2) = Q_L + L_L.

But nothing so far SELECTS su(4) x su(2) inside u(8); u(8) has many subgroups.  So
the question is whether the framework itself distinguishes one.

It might.  The 8 doublers are labelled by the hypercube corners r in {0,1}^3, and
the LATTICE SYMMETRY acts on those labels -- the octahedral group permutes the
corners.  That is a distinguished structure inside u(8), supplied by the axioms'
own Lattice axiom rather than chosen.  So compute:

  (1) how the octahedral action on the 8 corners decomposes into irreps;
  (2) the COMMUTANT of that action inside u(8) -- the internal symmetry that
      survives the lattice symmetry, which is what a gauge group would have to
      live in;
  (3) whether that commutant is large enough to contain su(3) + su(2) + u(1).

If the commutant is small, the lattice constrains the gauge group sharply -- a
forcing.  If it is all of u(8), the embedding is free and the SM identification
remains a choice.

CONTROL: the corner action must be a genuine representation of the 24-element
group, and the trivial group must give the full u(8) = 64."""
import numpy as np, itertools
R8=[tuple(r) for r in itertools.product([0,1],repeat=3)]; I8={r:i for i,r in enumerate(R8)}
def cubic():
    R=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,q in enumerate(p): M[i,q]=s[i]
            if abs(np.linalg.det(M)-1)<1e-9: R.append(M)
    return R
ROT=cubic()
def corner_perm(R):
    """a rotation maps corner r (as a +-1 vector) to another corner"""
    P=np.zeros((8,8))
    for r in R8:
        v=np.array(r)*2-1
        w=R@v
        t=tuple(((w+1)/2).astype(int))
        P[I8[t],I8[r]]=1.0
    return P
A=[corner_perm(R) for R in ROT]
print("T192  does the lattice symmetry force a subgroup of u(8)?")
err=0.0
for i in range(8):
    for j in range(8):
        k=[t for t,X in enumerate(ROT) if np.allclose(X,ROT[i]@ROT[j])][0]
        err=max(err,np.abs(A[i]@A[j]-A[k]).max())
print(f"   CONTROL corner action is a representation: max |A(R)A(S)-A(RS)| = {err:.1e}")
print(f"   CONTROL all permutation matrices: {all(np.allclose(X.sum(0),1) and np.allclose(X.sum(1),1) for X in A)}")
# decompose: character of the corner rep
chars={}
for R,X in zip(ROT,A):
    tr=int(round(np.trace(X)))
    chars[tr]=chars.get(tr,0)+1
print(f"   trace multiset of the corner action: {dict(sorted(chars.items()))}")
def commutant_dim(mats,N):
    M=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    s=np.linalg.svd(M,compute_uv=False)
    return int(np.sum(s<=max(M.shape)*np.finfo(float).eps*s.max()))
d=commutant_dim(A,8)
print()
print(f"   commutant of the lattice action inside u(8): dim {d}   (u(8) itself = 64)")
print(f"   CONTROL trivial group -> must be 64: {commutant_dim([np.eye(8)],8)}")
print()
print(f"   does it hold su(3)+su(2)+u(1) (dim 12)?  {'possibly' if d>=12 else 'NO -- too small'}")
print()
print("   a commutant strictly between 12 and 64 would mean the lattice CONSTRAINS")
print("   the gauge group without fixing it; below 12 it excludes the SM outright.")
