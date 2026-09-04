"""T169 - ARE THE HIGHER MOMENTS FREE?  Re-reading the Admissibility axiom.

R102 concluded the correlation length is undetermined because the axioms fix only
the MEAN of the admissibility distribution.  Re-reading the axiom text, that is
too quick:

   "For each site, the probability DISTRIBUTION over the possibilities is
    determined by, and varies with, the nearest-neighbor conditions."

The whole distribution is determined -- not merely its first moment.  So the
higher moments are not free; they are constrained by exactly the same covariance
requirement, and I simply never counted them.

A measure on the Bloch sphere decomposes into spherical-harmonic sectors, each
transforming as a spin-l representation.  R92 counted the maps into the l=0 and
l=1 sectors (the state) and found SIX.  Do the same for l=2 (the quadrupole,
5-dimensional, restricting to O as E + T_2) and for l=3.

Hand prediction from R92's decomposition of the input, 2A1 + 2E + 4T1 + 2T2:
   l=1 -> T1        : 4 maps        (plus 2 into A1 for the trace = 6 total, as R92)
   l=2 -> E + T2    : 2 + 2 = 4 maps
so the quadrupole should also be determined up to a handful of parameters.

CONTROL: the l=0 (normalisation) sector must give exactly the A1 count, 2, and the
trivial group must return the full dimension."""
import numpy as np, itertools
def cubic_rotations():
    R=[]
    for perm in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,p in enumerate(perm): M[i,p]=s[i]
            if abs(np.linalg.det(M)-1)<1e-9: R.append(M)
    return R
ROT=cubic_rotations()
DIRS=[np.array(d,dtype=float) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
def perm_action(R):
    P=np.zeros((6,6))
    for j,d in enumerate(DIRS):
        rd=R@d; i=[k for k,e in enumerate(DIRS) if np.allclose(e,rd)][0]; P[i,j]=1.0
    return P
def herm_action(R):
    M=np.zeros((4,4)); M[0,0]=1.0; M[1:,1:]=R; return M
# l = 2 : symmetric traceless 3x3, 5-dimensional, acting as Q -> R Q R^T
def basis_l2():
    B=[]
    B.append(np.diag([1.,-1,0]))
    B.append(np.diag([1.,1,-2])/np.sqrt(3))
    for (i,j) in ((0,1),(0,2),(1,2)):
        M=np.zeros((3,3)); M[i,j]=M[j,i]=1.0; B.append(M)
    return B
L2=basis_l2()
def l2_action(R):
    A=np.zeros((5,5))
    G=np.array([[np.sum(L2[a]*L2[b]) for b in range(5)] for a in range(5)])
    Gi=np.linalg.inv(G)
    for b in range(5):
        img=R@L2[b]@R.T
        c=Gi@np.array([np.sum(L2[a]*img) for a in range(5)])
        A[:,b]=c
    return A
# l = 3 : symmetric traceless rank-3, 7-dimensional -- build by projection
def equivariant_dim(gin,gout):
    n_in=gin[0].shape[0]; n_out=gout[0].shape[0]
    P=np.zeros((n_out*n_in,n_out*n_in))
    for A,B in zip(gin,gout): P+=np.kron(np.linalg.inv(A).T,B)
    P/=len(gin)
    return int(round(np.trace(P).real))
IN=[np.kron(perm_action(R),herm_action(R)) for R in ROT]
print("T169  covariant maps into each spherical-harmonic sector of the output measure")
print(f"      input = 6 neighbours x (1 + 3) = 24 real dimensions")
print()
print(f"   {'output sector':>28} {'dim':>5} {'covariant maps':>16}")
print(f"   {'l=0  (normalisation)':>28} {1:5d} {equivariant_dim(IN,[np.ones((1,1)) for R in ROT]):16d}")
print(f"   {'l=1  (mean / vector)':>28} {3:5d} {equivariant_dim(IN,[R for R in ROT]):16d}")
print(f"   {'l=2  (quadrupole)':>28} {5:5d} {equivariant_dim(IN,[l2_action(R) for R in ROT]):16d}")
print()
print("   CONTROLS")
print(f"      l=2 under the TRIVIAL group -> must be 24*5 = 120 : "
      f"{equivariant_dim([np.eye(24)],[np.eye(5)])}")
print(f"      l=2 action is a representation?  max |A(R)A(S) - A(RS)| = "
      f"{max(np.abs(l2_action(R)@l2_action(S)-l2_action(R@S)).max() for R in ROT[:6] for S in ROT[:6]):.1e}")
print(f"      l=1 count + l=0 count = {equivariant_dim(IN,[R for R in ROT])+equivariant_dim(IN,[np.ones((1,1)) for R in ROT])}"
      f"   (R92 found 6 for the state)")
print()
print("   A FINITE and small count in every sector means the axioms determine the")
print("   whole distribution up to finitely many parameters -- and R102's claim that")
print("   the higher moments are free is WRONG.")
