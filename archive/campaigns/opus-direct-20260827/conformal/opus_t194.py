"""T194 - IDENTIFYING THE 24-DIMENSIONAL ALGEBRA, AND HOW BIG THE SITE ALGEBRA MUST BE.

R125 measured the physical internal symmetry -- commuting with BOTH the Dirac
operator and the lattice -- as 24-dimensional at M_4(C).  Whether the Standard
Model fits needs the BLOCK structure, not the total, because R118 showed a single
fermion must carry colour and weak isospin together, which requires ONE BLOCK
u(m) whose centralizer of su(3) holds su(2) -- and T152 established that needs
m >= 5.

THERE IS A COUNTING ARGUMENT BEFORE ANY COMPUTATION.  A block u(m) has dimension
m^2, so m >= 5 needs a block of dimension >= 25.  The entire algebra is 24.
    24 < 25
so NO block can be u(5) or larger, and the Standard Model cannot fit at M_4(C)
once the lattice constraint is imposed -- regardless of how the 24 decomposes.

Confirm that by computing the centre and blocks anyway, then answer the
constructive question: how large must the site algebra be for ONE BLOCK to reach
u(5)?  Test the tensor tower M_4 (x) M_k."""
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
def analyse(k):
    Ik=np.eye(k,dtype=complex); n=4*k; N=8*n
    G=[]
    for mu in range(3):
        Pi,Pc=parts(mu,1); Mi,Mc=parts(mu,-1)
        G.append(np.kron(1j*Pc+1j*Mc,np.kron(gi[mu],Ik))/2.0)
    L=[np.kron(corner_perm(R),np.kron(np.block([[pauli_rep(R),Z2],[Z2,pauli_rep(R)]]),Ik))
       for R in ROT]
    mats=G+L
    M=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    U,sv,Vt=np.linalg.svd(M,full_matrices=False)
    d=int(np.sum(sv<=max(M.shape)*np.finfo(float).eps*sv.max()))
    B=[Vt[len(Vt)-d+i].conj().reshape(N,N) for i in range(d)]
    C=np.vstack([np.array([(Bi@Bj-Bj@Bi).ravel() for Bi in B]).T for Bj in B])
    U2,s2,V2=np.linalg.svd(C,full_matrices=False)
    kc=int(np.sum(s2<=max(C.shape)*np.finfo(float).eps*s2.max()))
    return d,kc
print("T194  block structure of the lattice-constrained internal symmetry")
print()
print("   COUNTING ARGUMENT: one block u(m) with m>=5 needs dim >= 25.")
print()
print(f"   {'site algebra':>16} {'fibre':>7} {'internal dim':>13} {'centre':>7} {'largest block <= ':>18} {'SM?':>6}")
for k,nm in ((1,"M_4(C)"),(2,"M_4 (x) M_2")):
    d,kc=analyse(k)
    # largest possible block: dim - (kc-1) other blocks of at least 1 each
    maxblk=d-(kc-1)
    m=int(np.floor(np.sqrt(maxblk)))
    print(f"   {nm:>16} {8*4*k:7d} {d:13d} {kc:7d} {'u(%d)'%m:>18} {('yes' if m>=5 else 'NO'):>6}")
print()
print("   CONTROL: k=1 must reproduce R125's 24.")
