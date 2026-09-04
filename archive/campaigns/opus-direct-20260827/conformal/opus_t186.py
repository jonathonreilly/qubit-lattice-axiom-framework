"""T186 - HOW MUCH LARGER MUST THE SITE ALGEBRA BE?  A constructive answer.

R114/R116/R118 established that the Standard Model needs a larger site algebra than
M_2(C), and R118 located the obstruction precisely: a single fermion must carry
BOTH colour and weak isospin, but in the framework's block structure each fermion
sees one u(4), and su(3)+su(2) do not both fit in u(4) (centralizer of su(3) is 2,
su(2) needs 3).

That is a negative with a constructive complement, and the machinery to answer it
already exists.  The natural enlargement keeps the Clifford structure the axioms
supply and adds an internal factor:

        site algebra  =  Cl(3,0) (x) M_k(C)  =  M_2(C) (x) M_k(C)

so Gamma_a = sigma_a (x) I_k acts only on the Clifford part, and the extra M_k
commutes with every Gamma -- it is a genuine INTERNAL symmetry, u(k) per site,
before doubling.  k = 1 is the axioms as they stand.

Compute the continuum taste algebra for k = 1, 2, 3, and for each ask the question
that actually matters: DOES ONE BLOCK HOLD su(3) AND su(2) TOGETHER?  A block u(m)
does iff the centralizer of su(3) inside it has dimension >= 3, which (from T152)
means m >= 5.

CONTROL: k = 1 must reproduce R117's u(4) (+) u(4) with 8-dimensional blocks."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
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
def make_D(k):
    Ik=np.eye(k,dtype=complex)
    def D(p):
        return sum(np.kron(shift3(a,1,p)-shift3(a,-1,p),np.kron(S[a],Ik))
                   for a in range(3))/2.0
    return D,16*k//2*0+8*2*k     # dim = 8 blocks * 2 spin * k
def subdim(mats):
    M=np.array([m.ravel() for m in mats])
    return np.linalg.matrix_rank(np.vstack([M.real,M.imag]),tol=1e-8)
print("T186  taste algebra vs site-algebra size")
print(f"   {'k':>3} {'site alg':>12} {'fibre':>7} {'continuum taste dim':>21} {'centre':>7} {'blocks':>18} {'SM in one block?':>18}")
for k in (1,2,3):
    D,_=make_D(k); N=16*k
    G=[]
    for mu in range(3):
        e=np.zeros(3); e[mu]=1e-5; G.append((D(e)-D(-e))/2e-5)
    A=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in G])
    U,s,Vt=np.linalg.svd(A,full_matrices=False); kk=int(np.sum(s<=max(A.shape)*np.finfo(float).eps*s.max()))
    B=[Vt[len(Vt)-kk+i].conj().reshape(N,N) for i in range(kk)]
    C=np.vstack([np.array([(Bi@Bj-Bj@Bi).ravel() for Bi in B]).T for Bj in B])
    U2,s2,V2=np.linalg.svd(C,full_matrices=False); kc=int(np.sum(s2<=max(C.shape)*np.finfo(float).eps*s2.max()))
    cen=[sum(V2[len(V2)-kc+i].conj()[j]*B[j] for j in range(len(B))) for i in range(kc)]
    rng=np.random.default_rng(4)
    Z=sum(rng.normal()*Zc for Zc in cen); Z=0.5*(Z+Z.conj().T)
    w,V=np.linalg.eigh(Z); u=np.unique(np.round(w,6))
    blks=[]
    for uu in u:
        idx=np.where(np.abs(w-uu)<1e-5)[0]
        P=V[:,idx]@V[:,idx].conj().T
        blks.append(subdim([P@X@P for X in B]))
    ms=[int(round(np.sqrt(b))) for b in blks]
    fits = any(m>=5 for m in ms)
    print(f"   {k:3d} {'M_2 (x) M_%d'%k:>12} {N:7d} {kk:21d} {kc:7d}"
          f" {str(['u(%d)'%m for m in ms]):>18} {('YES' if fits else 'no'):>18}")
print()
print("   a block u(m) holds su(3) and su(2) together iff m >= 5 (T152).")
print("   CONTROL: k=1 must give two u(4) blocks, reproducing R117.")
