"""T193 - THE PHYSICAL INTERNAL SYMMETRY: commuting with BOTH the Dirac operator
AND the lattice symmetry.

T192 turned up a constraint R119 and R124 both missed.  They computed the commutant
of the Gamma_mu -- the taste algebra -- and asked whether su(3)+su(2)+u(1) fits
inside it.  But a GAUGE symmetry must also commute with the LATTICE SYMMETRY,
because gauge transformations are internal while rotations are spacetime.

Here that is a real restriction rather than a formality, because the taste index IS
the hypercube corner label r in {0,1}^3, and the octahedral group PERMUTES those
corners.  The taste index is not purely internal -- the lattice acts on it.  This
is the well-known entanglement of staggered taste symmetry with lattice rotations,
and T192 measured its cost: the commutant of the corner action inside u(8) is only
FOUR dimensional, against 64 for u(8) itself.

So compute the physical object: the commutant of {Gamma_mu} TOGETHER WITH the
lattice action, in the full space, for both site algebras.

CONTROLS: dropping the lattice generators must reproduce R117/R119's numbers
(32 for M_2, 128 for M_4); the lattice action must be a genuine representation."""
import numpy as np, itertools
s=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex); Z2=np.zeros((2,2),dtype=complex)
blk=lambda a,b,c,d: np.block([[a,b],[c,d]])
g0=blk(I2,Z2,Z2,-I2); gi=[blk(Z2,x,-x,Z2) for x in s]
R8=[tuple(r) for r in itertools.product([0,1],repeat=3)]; I8={r:i for i,r in enumerate(R8)}
def cubic():
    R=[]
    for p in itertools.permutations(range(3)):
        for sg in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,q in enumerate(p): M[i,q]=sg[i]
            if abs(np.linalg.det(M)-1)<1e-9: R.append(M)
    return R
ROT=cubic()
def corner_perm(R):
    P=np.zeros((8,8))
    for r in R8:
        v=np.array(r)*2-1; w=R@v
        P[I8[tuple(((w+1)/2).astype(int))],I8[r]]=1.0
    return P
def spin_rep(R,which):
    """how a cubic rotation acts on the spin index"""
    if which=='pauli':
        ang=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
        if abs(ang)<1e-9: return np.eye(2,dtype=complex)
        if abs(ang-np.pi)<1e-9:
            w,v=np.linalg.eigh((R+np.eye(3))/2); ax=v[:,np.argmax(w)]
        else:
            ax=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])/(2*np.sin(ang))
        ax=ax/np.linalg.norm(ax)
        return np.cos(ang/2)*np.eye(2)-1j*np.sin(ang/2)*sum(ax[i]*s[i] for i in range(3))
    U=spin_rep(R,'pauli')
    return np.block([[U,Z2],[Z2,U]])          # Dirac: block-diagonal spin rotation
def parts(a,sg):
    Mi=np.zeros((8,8),dtype=complex); Mc=np.zeros((8,8),dtype=complex)
    for r in R8:
        t=list(r)
        if sg>0:
            if r[a]==0: t[a]=1; Mi[I8[tuple(t)],I8[r]]+=1
            else:       t[a]=0; Mc[I8[tuple(t)],I8[r]]+=1
        else:
            if r[a]==1: t[a]=0; Mi[I8[tuple(t)],I8[r]]+=1
            else:       t[a]=1; Mc[I8[tuple(t)],I8[r]]+=1
    return Mi,Mc
def build(gam,which):
    n=gam[0].shape[0]; N=8*n
    G=[]
    for mu in range(3):
        tot=np.zeros((N,N),dtype=complex)
        Pi,Pc=parts(mu,1); Mi,Mc=parts(mu,-1)
        tot+=np.kron(1j*Pc+1j*Mc,gam[mu])
        G.append(tot/2.0)
    L=[np.kron(corner_perm(R),spin_rep(R,which)) for R in ROT]
    return G,L,N
def cdim(mats,N):
    M=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    sv=np.linalg.svd(M,compute_uv=False)
    return int(np.sum(sv<=max(M.shape)*np.finfo(float).eps*sv.max()))
print("T193  internal symmetry commuting with the Dirac operator AND the lattice")
print(f"   {'site algebra':>14} {'Gamma only':>12} {'Gamma + lattice':>17} {'SM needs 12':>13}")
for nm,gam,which in (("M_2(C)",s,'pauli'),("M_4(C)",gi,'dirac')):
    G,L,N=build(gam,which)
    a=cdim(G,N); b=cdim(G+L,N)
    print(f"   {nm:>14} {a:12d} {b:17d} {('fits' if b>=12 else 'TOO SMALL'):>13}")
print()
print("   CONTROL: the 'Gamma only' column must reproduce R117 (32) and R119 (128).")
