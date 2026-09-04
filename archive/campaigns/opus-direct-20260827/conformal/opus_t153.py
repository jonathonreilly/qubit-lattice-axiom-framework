"""T153 - HOW MUCH DOES THE ADMISSIBILITY AXIOM'S COVARIANCE ACTUALLY CONSTRAIN THE RULE?

Working the ACTUAL axioms this time (R91), not the assumed Kahler-Dirac realization.

  Lattice:       sites are Z^3, nearest-neighbour adjacency, translations and
                 PROPER CUBIC ROTATIONS.
  Qubit:         each site's possibility domain has presentation M_2(C) ~ Cl(3,0).
  Admissibility: ONE FIXED nearest-neighbour rule, COVARIANT under translations
                 and proper cubic rotations, determining the site's probability
                 distribution over possibilities from the neighbour conditions.

The axioms explicitly leave the rule's form open ("the distribution's extensional
form and values are not specified by this memo").  But covariance is named axiom
content, and covariance is a hard constraint that can be COUNTED.  So: how big is
the space of rules the axioms permit?

Setup, all forced by the axiom text:
  * a site has 6 nearest neighbours in Z^3 (the face directions +-x, +-y, +-z);
  * proper cubic rotations form the octahedral group O, order 24, permuting those
    6 directions;
  * O acts on M_2(C) by spinor conjugation rho -> U rho U^dag; on the real
    4-dimensional space of hermitian 2x2 matrices this is 1 (+) 3 (identity is
    invariant, the Pauli vector rotates);
  * so the input is 6 x 4 = 24 real dimensions and the output is 4.

Count the equivariant linear maps by group averaging -- exact, finite, no fitting.
A SMALL answer means the axioms nearly determine their own dynamics; a large one
means covariance is weak and the rule needs far more input.

Controls: (a) the group must actually close (24 elements, each orthogonal, det=+1);
(b) averaging over the TRIVIAL group must return the full 96, or the projector is
broken; (c) a deliberately non-equivariant map must be killed by the projector."""
import numpy as np, itertools

# --- the 24 proper cubic rotations
def cubic_rotations():
    R=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,p in enumerate(perm): M[i,p]=signs[i]
            if abs(np.linalg.det(M)-1)<1e-9: R.append(M)
    return R
ROT=cubic_rotations()
print(f"T153  proper cubic rotations found: {len(ROT)}  (octahedral group O has 24)")
assert len(ROT)==24
clo=all(any(np.allclose(A@B,C) for C in ROT) for A in ROT for B in ROT)
print(f"   closed under multiplication: {clo}")

# --- spinor rep: for R in SO(3) find U in SU(2) with U sigma_i U^dag = sum_j R_ji sigma_j
S=[np.array([[0,1],[1,0]],dtype=complex),
   np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
def spinor(R):
    # build from axis-angle
    ang=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    if abs(ang)<1e-9: return np.eye(2,dtype=complex)
    if abs(ang-np.pi)<1e-9:
        w,v=np.linalg.eigh((R+np.eye(3))/2); ax=v[:,np.argmax(w)]
    else:
        ax=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])/(2*np.sin(ang))
    ax=ax/np.linalg.norm(ax)
    return np.cos(ang/2)*np.eye(2)-1j*np.sin(ang/2)*sum(ax[i]*S[i] for i in range(3))
# verify the spinor rep reproduces each rotation
err=0.0
for R in ROT:
    U=spinor(R)
    for i in range(3):
        lhs=U@S[i]@U.conj().T; rhs=sum(R[j,i]*S[j] for j in range(3))
        err=max(err,np.abs(lhs-rhs).max())
print(f"   spinor rep verified: max |U sigma_i U^dag - sum_j R_ji sigma_j| = {err:.2e}")

# --- action on the hermitian 2x2 space, basis (I, sx, sy, sz), real 4-dim
def herm_action(R):
    M=np.zeros((4,4)); M[0,0]=1.0
    M[1:,1:]=R
    return M
# --- action on the 6 face directions
DIRS=[np.array(d) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
def perm_action(R):
    P=np.zeros((6,6))
    for j,d in enumerate(DIRS):
        rd=R@d
        i=[k for k,e in enumerate(DIRS) if np.allclose(e,rd)][0]
        P[i,j]=1.0
    return P

IN=[np.kron(perm_action(R),herm_action(R)) for R in ROT]   # 24x24
OUT=[herm_action(R) for R in ROT]                          # 4x4
def equivariant_dim(group_in,group_out):
    n_in=group_in[0].shape[0]; n_out=group_out[0].shape[0]
    D=n_out*n_in
    Pj=np.zeros((D,D))
    for A,B in zip(group_in,group_out):
        Pj+=np.kron(np.linalg.inv(A).T,B)          # L -> B L A^{-1}
    Pj/=len(group_in)
    return int(round(np.trace(Pj).real)), Pj
d,Pj=equivariant_dim(IN,OUT)
print()
print(f"   space of ALL linear maps (6 neighbours x 4) -> 4 :  {24*4} real dimensions")
print(f"   COVARIANT (O-equivariant) subspace              :  {d} real dimensions")
print(f"   projector check  P^2 = P : {np.abs(Pj@Pj-Pj).max():.2e}")
dt,_=equivariant_dim([np.eye(24)],[np.eye(4)])
print(f"   CONTROL, trivial group -> must give {24*4}: {dt}")
rng=np.random.default_rng(1)
L=rng.normal(size=(4,24))
Lp=(Pj@L.T.ravel()).reshape(24,4).T if False else None
v=L.ravel(order='F') if False else None
# apply the projector properly and check equivariance of the result
Lv=L.reshape(-1)
Pv=(Pj@L.T.reshape(-1)).reshape(24,4).T
resid=max(np.abs(B@Pv@np.linalg.inv(A)-Pv).max() for A,B in zip(IN,OUT))
print(f"   CONTROL, projected random map is equivariant: max residual {resid:.2e}")
print(f"   CONTROL, raw random map is NOT: max residual {max(np.abs(B@L@np.linalg.inv(A)-L).max() for A,B in zip(IN,OUT)):.2e}")
