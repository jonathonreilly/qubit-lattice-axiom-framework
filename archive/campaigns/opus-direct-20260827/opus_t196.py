"""T196 - WHICH PARTITION IS IT?  R126's conclusion depends on the answer.

T194 found the lattice-constrained internal symmetry at M_4(C) has dimension 24
and centre 6, and listed the partitions of 24 into six squares:
       [4,2,1,1,1,1]   largest u(4)
       [2,2,2,2,2,2]   largest u(2)
It never determined WHICH.  R126 then scaled by k and concluded M_8(C) suffices --
but that used the FIRST partition.  Under the second, scaling by k=2 gives
[4,4,4,4,4,4], every block u(4), and the Standard Model STILL DOES NOT FIT, since
a block needs m >= 5.

So R126's headline depends on a fact I never measured.  Measure it: find the six
central projections and compute dim P_i A P_i for each -- that is the block size
m_i^2 directly, no guessing between partitions.

CONTROLS: the projections must sum to the identity, be idempotent and mutually
orthogonal; and the block dimensions must sum to 24."""
import numpy as np, itertools
s=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex); Z2=np.zeros((2,2),dtype=complex)
blk=lambda a,b,c,d: np.block([[a,b],[c,d]])
gi=[blk(Z2,x,-x,Z2) for x in s]
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
def pauli_rep(R):
    ang=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    if abs(ang)<1e-9: return np.eye(2,dtype=complex)
    if abs(ang-np.pi)<1e-9:
        w,v=np.linalg.eigh((R+np.eye(3))/2); ax=v[:,np.argmax(w)]
    else:
        ax=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])/(2*np.sin(ang))
    ax=ax/np.linalg.norm(ax)
    return np.cos(ang/2)*np.eye(2)-1j*np.sin(ang/2)*sum(ax[i]*s[i] for i in range(3))
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
N=32
G=[]
for mu in range(3):
    Pi,Pc=parts(mu,1); Mi,Mc=parts(mu,-1)
    G.append(np.kron(1j*Pc+1j*Mc,gi[mu])/2.0)
L=[np.kron(corner_perm(R),np.block([[pauli_rep(R),Z2],[Z2,pauli_rep(R)]])) for R in ROT]
M=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in G+L])
U,sv,Vt=np.linalg.svd(M,full_matrices=False)
d=int(np.sum(sv<=max(M.shape)*np.finfo(float).eps*sv.max()))
B=[Vt[len(Vt)-d+i].conj().reshape(N,N) for i in range(d)]
C=np.vstack([np.array([(Bi@Bj-Bj@Bi).ravel() for Bi in B]).T for Bj in B])
U2,s2,V2=np.linalg.svd(C,full_matrices=False)
kc=int(np.sum(s2<=max(C.shape)*np.finfo(float).eps*s2.max()))
cen=[sum(V2[len(V2)-kc+i].conj()[j]*B[j] for j in range(len(B))) for i in range(kc)]
print(f"T196  block sizes of the lattice-constrained algebra at M_4(C)")
print(f"   dim = {d}, centre = {kc}")
rng=np.random.default_rng(8)
Z=sum(rng.normal()*(0.5*(Zc+Zc.conj().T)) for Zc in cen)
w,V=np.linalg.eigh(Z)
groups={}
for i,x in enumerate(np.round(w,7)): groups.setdefault(x,[]).append(i)
print(f"   generic central element: {len(groups)} distinct eigenvalues,"
      f" multiplicities {sorted(len(v) for v in groups.values())}")
Ps=[V[:,idx]@V[:,idx].conj().T for idx in groups.values()]
print(f"   CONTROL sum P = I: {np.abs(sum(Ps)-np.eye(N)).max():.1e};"
      f"  idempotent: {max(np.abs(P@P-P).max() for P in Ps):.1e}")
def subdim(mats):
    A=np.array([m.ravel() for m in mats])
    return np.linalg.matrix_rank(np.vstack([A.real,A.imag]),tol=1e-8)
sizes=[subdim([P@X@P for X in B]) for P in Ps]
print()
print(f"   BLOCK DIMENSIONS m_i^2 : {sorted(sizes,reverse=True)}   (sum {sum(sizes)}, must be {d})")
print(f"   so m_i = {sorted([int(round(np.sqrt(x))) for x in sizes],reverse=True)}")
mx=max(int(round(np.sqrt(x))) for x in sizes)
print()
print(f"   largest block u({mx});  at M_8(C) it becomes u({2*mx})")
print(f"   the SM needs a block with m >= 5:  {'FITS at M_8' if 2*mx>=5 else 'STILL FAILS at M_8'}")
