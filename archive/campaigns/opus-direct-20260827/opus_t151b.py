"""T151b - fixing T151's broken Cartan search, and getting the L/R structure.

T151 reported the taste algebra's Cartan rank as 1, which cannot be right for a
16-dimensional algebra -- my greedy search picked one random element and then
found nothing commuting with it, because random elements of a 16-dim algebra
almost never commute.  The right measure is the CENTRALIZER of a generic element:
for u(4) a generic hermitian element has centralizer = the Cartan = 4.

And the decomposition question T151 left open: CL splits the fibre 8+8 with taste
acting inside each half, but BOTH self-dual and anti-self-dual bivectors came out
block-diagonal.  For the reading 16 = (4_taste, 2_L) + (4_taste, 2_R) one needs
su(2)_L to act nontrivially on ONE half and trivially on the other.  Measure the
rank of each su(2) restricted to each half -- that is what decides it."""
import numpy as np, sys
sys.path.insert(0,".")
from opus_t138 import setup

def cbasis(mats,NF):
    A=np.vstack([np.kron(m,np.eye(NF))-np.kron(np.eye(NF),m.T) for m in mats])
    U,s,Vt=np.linalg.svd(A)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    return [v.reshape(NF,NF) for v in Vt[np.sum(s>tol):]]

d=4; NF,G,Gb=setup(d)
CL=np.eye(NF)
for a in range(d): CL=CL@G[a]
B=cbasis(G,NF)
herm=[]
for X in B:
    for Y in (0.5*(X+X.T),0.5j*(X-X.T)):
        if np.abs(Y).max()>1e-9: herm.append(Y)
Hb=[]
M=[]
for Y in herm:
    M.append(Y.ravel())
    if np.linalg.matrix_rank(np.array(M),tol=1e-9)>len(Hb): Hb.append(Y)
    else: M.pop()
print(f"T151b  taste algebra: {len(Hb)} independent hermitian generators")
rng=np.random.default_rng(11)
X=sum(rng.normal()*Y for Y in Hb); X=0.5*(X+X.conj().T)
# centralizer of X inside the taste algebra
rows=[]
for Y in Hb: rows.append((X@Y-Y@X).ravel())
A=np.array(rows)
null=len(Hb)-np.linalg.matrix_rank(A,tol=1e-9)
ev=np.linalg.eigvalsh(X)
u,c=np.unique(np.round(ev,8),return_counts=True)
print(f"   centralizer of a generic hermitian element = {null}   (u(4) Cartan rank = 4)")
print(f"   its eigenvalues: {len(u)} distinct, multiplicities {list(c)}")
print()
Pp=0.5*(np.eye(NF)+CL); Pm=0.5*(np.eye(NF)-CL)
idx=[(a,b) for a in range(4) for b in range(4) if a<b]
SD=[];ASD=[]
for (a,b) in idx:
    c2,e=[x for x in range(4) if x not in (a,b)]
    Bab=0.5*G[a]@G[b]; Bce=0.5*G[c2]@G[e]
    SD.append(Bab+Bce); ASD.append(Bab-Bce)
def rk(L,P):
    R=[(P@X@P).ravel() for X in L]
    return np.linalg.matrix_rank(np.array(R),tol=1e-9)
print("   how each su(2) acts on the two CL-halves (rank of the restricted generators):")
print(f"      {'':>14} {'on P+ (dim 8)':>15} {'on P- (dim 8)':>15}")
print(f"      {'self-dual':>14} {rk(SD,Pp):15d} {rk(SD,Pm):15d}")
print(f"      {'anti-self-dual':>14} {rk(ASD,Pp):15d} {rk(ASD,Pm):15d}")
print()
print("   3 and 0 on opposite halves = 16 = (4_taste, 2_L) + (4_taste, 2_R).")
print("   3 and 3 on both = CL is not the L/R chirality and the reading fails.")
# and the taste rank inside one half
Rt=[(Pp@X@Pp).ravel() for X in B]
print(f"   taste algebra restricted to P+ spans {np.linalg.matrix_rank(np.array(Rt),tol=1e-9)} dims"
      f"   (u(4) on a 4 would give 16)")
