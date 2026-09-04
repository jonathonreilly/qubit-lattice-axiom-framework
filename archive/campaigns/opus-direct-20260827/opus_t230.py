"""
T230 - does anything still single out the Born weight among R147's SIX
parameters at M4(C)?

At M2(C) the Born weight was characterised uniquely: the member of the
(one-parameter) family vanishing exactly on ORTHOGONAL states, which was also
the positivity boundary.  At M4(C) the family is six-dimensional (R147).

Test: evaluate each invariant form on many ORTHOGONAL pure-state pairs.
  - the isotropic form c.c' must be CONSTANT (= -1) there, since
    Tr(rho rho') = 1/4 + (1/4) c.c' and orthogonality means Tr = 0;
  - if the other five are NOT constant on that set, then demanding phi = 0 on
    ALL orthogonal pairs forces their coefficients to zero, and the Born weight
    is again the unique member -- distinguished by exactly the same property.
"""
import numpy as np, itertools

n = 4
def gens(n):
    B = []
    for i in range(n):
        for j in range(i+1, n):
            E = np.zeros((n,n),dtype=complex); E[i,j]=1; E[j,i]=1; B.append(E/np.sqrt(2))
            F = np.zeros((n,n),dtype=complex); F[i,j]=-1j; F[j,i]=1j; B.append(F/np.sqrt(2))
    for k in range(1, n):
        d = np.zeros(n); d[:k]=1; d[k]=-k
        B.append(np.diag(d).astype(complex)/np.sqrt(k*k+k))
    return B
T = gens(n); m = len(T)
print(f"traceless Hermitian generators: {m} (expect 15); "
      f"orthonormal to {max(abs(np.trace(T[i].conj().T@T[j]) - (i==j)) for i in range(m) for j in range(m)):.1e}")

# rebuild the 6 invariant forms from T229's construction
def hyperoct(d):
    out=[]
    for perm in itertools.permutations(range(d)):
        for sg in itertools.product([1,-1],repeat=d):
            R=np.zeros((d,d))
            for i,p in enumerate(perm): R[i,p]=sg[i]
            if abs(np.linalg.det(R)-1)<1e-12: out.append(R)
    return out
I2=np.eye(2,dtype=complex)
SX=np.array([[0,1],[1,0]],dtype=complex); SY=np.array([[0,-1j],[1j,0]],dtype=complex)
SZ=np.array([[1,0],[0,-1]],dtype=complex)
GAM=[np.kron(SX,I2),np.kron(SY,I2),np.kron(SZ,SX),np.kron(SZ,SY)]
def spin_U(R):
    rows=[]
    for mu in range(4):
        tgt=sum(R[nu,mu]*GAM[nu] for nu in range(4))
        rows.append(np.kron(np.eye(4),GAM[mu].T)-np.kron(tgt,np.eye(4)))
    A=np.vstack(rows); U_,sv,Vt=np.linalg.svd(A,full_matrices=False)
    return Vt[-1].conj().reshape(4,4)
Os=[]
for R in hyperoct(4):
    U=spin_U(R); Ui=np.linalg.inv(U)
    O=np.zeros((m,m))
    for j,Bj in enumerate(T):
        X=U@Bj@Ui
        for i,Bi in enumerate(T): O[i,j]=np.real(np.trace(Bi.conj().T@X))
    Os.append(O)
idx=[(i,j) for i in range(m) for j in range(i,m)]
rows=[]
for O in Os:
    for a,(i,j) in enumerate(idx):
        r=np.zeros(len(idx))
        for b,(k,l) in enumerate(idx):
            r[b]+=O[k,i]*O[l,j]+(O[l,i]*O[k,j] if k!=l else 0.0)
        r[a]-=1.0; rows.append(r)
A=np.array(rows); U_,sv,Vt=np.linalg.svd(A,full_matrices=False)
tol=max(A.shape)*np.finfo(float).eps*sv.max(); K=int(np.sum(sv<=tol))
forms=[]
for t in range(K):
    v=Vt[len(Vt)-K+t]; S=np.zeros((m,m))
    for b,(k,l) in enumerate(idx):
        S[k,l]+=v[b]; 
        if k!=l: S[l,k]+=v[b]
    forms.append(S)
print(f"invariant symmetric forms recovered: {len(forms)} (expect 6)")

rng=np.random.default_rng(11)
def pure():
    z=rng.normal(size=n)+1j*rng.normal(size=n); z/=np.linalg.norm(z)
    return np.outer(z,z.conj()), z
def coords(rho): return np.array([np.real(np.trace(t.conj().T@rho)) for t in T])

# orthogonal pairs
print("\n=== value of each invariant form on ORTHOGONAL pure-state pairs ===")
vals=[[] for _ in forms]; born=[]
for _ in range(400):
    r1,z1=pure()
    w=rng.normal(size=n)+1j*rng.normal(size=n)
    w=w-(z1.conj()@w)*z1; w/=np.linalg.norm(w)          # orthogonal to z1
    r2=np.outer(w,w.conj())
    c1,c2=coords(r1),coords(r2)
    born.append(np.real(np.trace(r1@r2)))
    for i,S in enumerate(forms): vals[i].append(c1@S@c2)
print(f"  check: Tr(rho rho') on these pairs = {max(abs(b) for b in born):.1e}  (must be 0)")
print("  form   min          max          spread     constant on orthogonal pairs?")
for i,v in enumerate(vals):
    v=np.array(v); sp=v.max()-v.min()
    print(f"   {i}   {v.min():+.6f}   {v.max():+.6f}   {sp:.2e}   "
          f"{'YES' if sp < 1e-9 else 'no'}")


# ---------------------------------------------------------------------------
# CORRECTION: the SVD returns an ARBITRARY orthonormal basis of the invariant
# subspace, so no single basis element need be the isotropic one.  Constancy is
# a property of a DIRECTION in the 6-dim family, not of a basis vector.
# (Testing basis elements where the object is a subspace is this packet's most
#  repeated error -- R139, T184, T185.)
# ---------------------------------------------------------------------------
print("\n=== done properly: which DIRECTIONS in the 6-dim family are constant? ===")
V = np.array(vals).T                      # (pairs, 6)
ones = np.ones((V.shape[0], 1))
Aug = np.hstack([V, -ones])               # V lam = mu * 1
U_, sv2, Vt2 = np.linalg.svd(Aug, full_matrices=False)
tol2 = max(Aug.shape)*np.finfo(float).eps*sv2.max()
kk = int(np.sum(sv2 <= tol2))
print(f"  dim of {{lam : V lam is constant across orthogonal pairs}} = {kk}")
sol = Vt2[len(Vt2)-kk:].conj()
# is the isotropic form (identity on the 15-dim space) in the invariant span?
Id = np.eye(m)
G = np.array([f.ravel() for f in forms])
coef, res, *_ = np.linalg.lstsq(G.T, Id.ravel(), rcond=None)
print(f"  identity form lies in the invariant span: residual "
      f"{np.max(np.abs(G.T@coef - Id.ravel())):.2e}")
for t in range(kk):
    lam = sol[t][:6]; mu = sol[t][6]
    S = sum(lam[i]*forms[i] for i in range(6))
    S = S/np.linalg.norm(S)*np.linalg.norm(Id)/np.sqrt(1)
    ov = abs(np.sum(S*Id))/(np.linalg.norm(S)*np.linalg.norm(Id))
    print(f"  solution {t}: |<S, identity>|/(|S||I|) = {ov:.10f}   "
          f"{'IS the isotropic form' if ov > 1-1e-8 else 'not isotropic'}")
print("""
=== reading ===
  Exactly one direction in the six-parameter family is constant on the
  orthogonal set, and it is the isotropic (Born) form.  So 'phi vanishes on
  every orthogonal pair' still picks out ONE member, exactly as at M2(C).""")
