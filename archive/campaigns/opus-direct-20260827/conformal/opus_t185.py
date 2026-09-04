"""T185 - HOW DOES THE 16 DECOMPOSE, AND IS THE u(4)+u(4) CHIRAL?

R117 identified the continuum taste algebra of the axioms' own construction as
u(4) (+) u(4) -- two blocks, centre 2 -- and showed su(3)+su(2)+u(1) fits inside.
The next question is the REPRESENTATION content, and the block structure already
constrains it hard.

An algebra M_4 (+) M_4 acting on a 16-dimensional space splits it by the two
central projections, V = V_1 (+) V_2, with M_4 acting on each as C^4 (x) C^m.
Since dim V_1 + dim V_2 = 16 and each is 4m, the multiplicities satisfy
m_1 + m_2 = 4.  The symmetric case m_1 = m_2 = 2 would give

        16  =  (4 taste, 2 spin)  (+)  (4 taste, 2 spin)

i.e. FOUR TASTES OF DIRAC FERMION, split into two Weyl halves with an INDEPENDENT
u(4) acting on each.  An independent gauge algebra per chirality is a CHIRAL gauge
structure -- which is exactly what the Standard Model needs and what this
campaign's earlier chirality results said was obstructed.

So measure: (1) the ranks of the two central projections; (2) whether the Gamma_mu
map one block to the other (they must, being odd operators); (3) whether each u(4)
factor annihilates the opposite block, which is what 'chiral' means here.

CONTROL: the two central projections must be orthogonal, sum to the identity, and
each be idempotent."""
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
U,s,Vt=np.linalg.svd(A)
k=int(np.sum(s<=max(A.shape)*np.finfo(float).eps*s.max()))
B=[Vt[len(Vt)-k+i].conj().reshape(N,N) for i in range(k)]
# centre as a subspace
rows=[np.array([(Bi@Bj-Bj@Bi).ravel() for Bi in B]).T for Bj in B]
C=np.vstack(rows); U2,s2,V2=np.linalg.svd(C)
kc=int(np.sum(s2<=max(C.shape)*np.finfo(float).eps*s2.max()))
cen=[sum(V2[len(V2)-kc+i][j]*B[j] for j in range(len(B))) for i in range(kc)]
print("T185  block structure of the continuum taste algebra")
print(f"   commutant dim {len(B)}, centre dim {kc}")
# diagonalise a generic central element to get the projections
Z=cen[0]+0.7*cen[1] if kc>1 else cen[0]
Z=0.5*(Z+Z.conj().T)
w,V=np.linalg.eigh(Z)
groups={}
for i,x in enumerate(np.round(w,8)): groups.setdefault(x,[]).append(i)
print(f"   generic central element has {len(groups)} distinct eigenvalues,"
      f" multiplicities {sorted(len(v) for v in groups.values())}")
Ps=[V[:,idx]@V[:,idx].conj().T for idx in groups.values()]
print()
print("   CONTROL projections")
print(f"      sum P_i = I ?          max dev {np.abs(sum(Ps)-np.eye(N)).max():.1e}")
print(f"      each idempotent ?      max dev {max(np.abs(P@P-P).max() for P in Ps):.1e}")
print(f"      mutually orthogonal ?  max dev {max(np.abs(Ps[i]@Ps[j]).max() for i in range(len(Ps)) for j in range(len(Ps)) if i!=j):.1e}")
print(f"      ranks: {[int(round(np.trace(P).real)) for P in Ps]}")
print()
print("   do the Gamma_mu connect the blocks (odd operators must)?")
for i,P in enumerate(Ps):
    same=max(np.abs(P@g@P).max() for g in G)
    print(f"      block {i}: max |P Gamma P| = {same:.2e}"
          f"   {'-> Gamma maps block to the OTHER block' if same<1e-9 else ''}")
print()
print("   does each taste factor annihilate the opposite block (chirality)?")
alg=[X for X in B]
nblk=len(Ps)
if nblk==2:
    cnt=0
    for X in alg:
        a=np.abs(Ps[0]@X@Ps[0]).max(); b=np.abs(Ps[1]@X@Ps[1]).max()
        if a>1e-9 and b<1e-9: cnt+=1
    print(f"      basis elements living ONLY in block 0: {cnt} of {len(alg)}")
    print(f"      (a chiral structure has the algebra split, ~half in each block)")
