"""T188 - WHAT SPLITS THE TWO BLOCKS?  Identifying the central element.

R120's obstruction is that the framework's two taste blocks are completely
decoupled -- no Dirac operator and no mass term connects them -- so they cannot be
the two chiralities of a Standard Model generation.  R119 showed the split survives
the enlargement M_2 -> M_2 (x) M_k (centre stays 2 at k=1 and k=2), which is
expected: an extra tensor factor commutes with everything and just enlarges each
block rather than merging them.

So the question is what the central element IS.  If it is a recognisable operator,
that says what the two sectors are and whether any modification could couple them.

Candidates to test it against, all built from objects the construction supplies:
   * Gamma_1 Gamma_2 Gamma_3    -- the 3D 'chirality' (product of all three Gammas)
   * a doubler-space operator   -- something acting only on the 8 block-index slots
   * the spin operator sigma_a  -- acting only on the 2 spin slots

CONTROL: whatever Z is, it must commute with every Gamma_mu (it is central in the
commutant) and square to a multiple of the identity if it is to define a clean
two-block split."""
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
D3=lambda p: sum(np.kron(shift3(a,1,p)-shift3(a,-1,p),S[a]) for a in range(3))/2.0
G=[]
for mu in range(3):
    e=np.zeros(3); e[mu]=1e-5; G.append((D3(e)-D3(-e))/2e-5)
N=16
A=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in G])
U,s,Vt=np.linalg.svd(A,full_matrices=False)
k=int(np.sum(s<=max(A.shape)*np.finfo(float).eps*s.max()))
B=[Vt[len(Vt)-k+i].conj().reshape(N,N) for i in range(k)]
C=np.vstack([np.array([(Bi@Bj-Bj@Bi).ravel() for Bi in B]).T for Bj in B])
U2,s2,V2=np.linalg.svd(C,full_matrices=False)
kc=int(np.sum(s2<=max(C.shape)*np.finfo(float).eps*s2.max()))
cen=[sum(V2[len(V2)-kc+i].conj()[j]*B[j] for j in range(len(B))) for i in range(kc)]
# pick the traceless central element (the identity is the other one)
Z=None
for Zc in cen:
    Zt=Zc-np.trace(Zc)/N*np.eye(N)
    if np.abs(Zt).max()>1e-8: Z=Zt/np.abs(np.linalg.eigvals(Zt)).max(); break
Z=0.5*(Z+Z.conj().T)
print("T188  identifying the central element that splits the blocks")
print(f"   CONTROL [Z, Gamma_mu] = {max(np.abs(Z@g-g@Z).max() for g in G):.2e}")
print(f"   Z^2 = I ?  max |Z^2 - I| = {np.abs(Z@Z-np.eye(N)).max():.2e}")
w=np.linalg.eigvalsh(Z); u,c=np.unique(np.round(w,8),return_counts=True)
print(f"   eigenvalues {np.round(u,6)} with multiplicities {list(c)}")
print()
print("   testing Z against candidate operators")
G123=G[0]@G[1]@G[2]
cands={"Gamma_1 Gamma_2 Gamma_3": G123/max(np.abs(np.linalg.eigvals(G123)).max(),1e-30)}
for a in range(3):
    cands[f"I_8 (x) sigma_{a+1}"]=np.kron(np.eye(8),S[a])
# doubler-space operators: parity r -> 1-r, and the 'staggered sign'
P=np.zeros((8,8))
for r in R8: P[I8[tuple(1-np.array(r))],I8[r]]=1.0
cands["block parity (r -> 1-r)"]=np.kron(P,np.eye(2))
E=np.diag([(-1)**sum(r) for r in R8]).astype(complex)
cands["block (-1)^{r_1+r_2+r_3}"]=np.kron(E,np.eye(2))
for nm,X in cands.items():
    X=0.5*(X+X.conj().T)
    if np.abs(X).max()<1e-12: 
        print(f"   {nm:>26}: zero operator"); continue
    Xn=X/max(np.abs(np.linalg.eigvals(X)).max(),1e-30)
    d=min(np.abs(Z-Xn).max(),np.abs(Z+Xn).max())
    print(f"   {nm:>26}: |Z -+ X| = {d:.3e}   {'<-- MATCH' if d<1e-6 else ''}")
