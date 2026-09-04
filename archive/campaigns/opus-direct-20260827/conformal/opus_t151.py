"""T151 - WHAT IS THE FRAMEWORK'S FIBRE, AS A REPRESENTATION?

T150's accounting raises the TOE-level question directly.  The fibre is 16
components; the commutant (taste algebra) is 16-dimensional; and the campaign
separately found su(2) sitting in the Clifford bivectors B_i = (1/2) gamma_j gamma_k.
So the fibre should decompose under

        (taste algebra)  x  (Clifford / spin algebra)

and the SHAPE of that decomposition is a statement about what particle content the
framework can carry.  Count it exactly rather than by hand-waving:

  (i)   is the taste algebra u(4) (i.e. does the commutant contain a u(4), with
        the fibre a 4 of it)?  Check by decomposing the commutant into its
        hermitian generators and finding the rank of a maximal abelian subalgebra.
  (ii)  do the Clifford bivectors close into su(2) + su(2) = so(4)?  In 4D
        Spin(4) = SU(2)_L x SU(2)_R and the Dirac spinor is (2,1) + (1,2).
  (iii) does CL (the Clifford chirality, verified real with CL^2 = +I in T148)
        split the fibre into two halves of dimension 8, and does the taste
        algebra act within each half?  That is the statement
             16 = (4_taste, 2_L) + (4_taste, 2_R)
        whose Weyl count is 8 + 8.
  (iv)  the honest Weyl accounting, done twice: once treating the field as
        complex, once as real.

I am NOT claiming a Standard Model identification here.  I am counting, exactly,
what representation the framework's own fibre is -- which is the prerequisite for
any such claim and is checkable without one."""
import numpy as np, itertools, sys
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
print(f"T151  the framework's fibre as a representation.  d=4, fibre {NF}")
print()
print("(i) the taste algebra")
herm=[]
for X in B:
    for Y in (0.5*(X+X.T), 0.5j*(X-X.T)):
        if np.abs(Y).max()>1e-9: herm.append(Y)
Mh=np.array([Y.ravel() for Y in herm])
print(f"    commutant dim {len(B)};  hermitian generators span {np.linalg.matrix_rank(Mh,tol=1e-9)} real dims"
      f"   (u(4) has 16)")
# maximal abelian: greedily collect mutually commuting hermitian elements
rng=np.random.default_rng(0)
cart=[]
for _ in range(400):
    Y=sum(rng.normal()*h for h in herm); Y=0.5*(Y+Y.conj().T)
    if all(np.abs(Y@Z-Z@Y).max()<1e-9 for Z in cart):
        V=np.array([Z.ravel() for Z in cart]+[Y.ravel()])
        if np.linalg.matrix_rank(V,tol=1e-9)>len(cart): cart.append(Y)
print(f"    maximal abelian subalgebra (Cartan) rank = {len(cart)}   (u(4) has rank 4)")

print()
print("(ii) Clifford bivectors")
biv=[0.5*(G[a]@G[b]) for a in range(d) for b in range(d) if a<b]
print(f"    {len(biv)} bivectors B_ab = (1/2) Gamma_a Gamma_b   (so(4) has dim 6)")
Mb=np.array([X.ravel() for X in biv]); print(f"    they span {np.linalg.matrix_rank(Mb,tol=1e-9)} dims")
clo=[]
for X in biv:
    for Y in biv: clo.append((X@Y-Y@X).ravel())
allb=np.vstack([Mb,np.array(clo)])
print(f"    closed under commutators?  span of {{B}} u {{[B,B]}} = {np.linalg.matrix_rank(allb,tol=1e-9)}"
      f"   {'CLOSES -> so(4)' if np.linalg.matrix_rank(allb,tol=1e-9)==6 else ''}")
# self-dual / anti-self-dual split = su(2)_L + su(2)_R
SD=[];ASD=[]
idx=[(a,b) for a in range(d) for b in range(d) if a<b]
for (a,b) in idx:
    c,e=[x for x in range(d) if x not in (a,b)]
    Bab=0.5*G[a]@G[b]; Bce=0.5*G[c]@G[e]
    SD.append(Bab+Bce); ASD.append(Bab-Bce)
print(f"    self-dual span {np.linalg.matrix_rank(np.array([X.ravel() for X in SD]),tol=1e-9)},"
      f" anti-self-dual span {np.linalg.matrix_rank(np.array([X.ravel() for X in ASD]),tol=1e-9)}"
      f"   (su(2)+su(2) = 3+3)")

print()
print("(iii) does CL split the fibre, with taste acting inside each half?")
Pp=0.5*(np.eye(NF)+CL); Pm=0.5*(np.eye(NF)-CL)
print(f"    rank P+ = {int(round(np.trace(Pp).real))}, rank P- = {int(round(np.trace(Pm).real))}")
inside=max(max(np.abs(Pp@X@Pm).max(),np.abs(Pm@X@Pp).max()) for X in B)
print(f"    taste algebra maps each CL-half to itself?  max off-block = {inside:.1e}"
      f"   {'YES -- taste acts within each half' if inside<1e-9 else 'NO'}")
bl=max(max(np.abs(Pp@X@Pm).max(),np.abs(Pm@X@Pp).max()) for X in SD)
bl2=max(max(np.abs(Pp@X@Pm).max(),np.abs(Pm@X@Pp).max()) for X in ASD)
print(f"    self-dual bivectors off-block {bl:.1e};  anti-self-dual off-block {bl2:.1e}")
print()
print("(iv) Weyl accounting")
print(f"    16 complex components = 4 taste x 4 Dirac = 4 x 2 Weyl = 8 Weyl")
print(f"    one CL-half           = 8 complex = 4 taste x 2 = 4 Weyl")
print(f"    a Standard Model generation = 16 Weyl")
