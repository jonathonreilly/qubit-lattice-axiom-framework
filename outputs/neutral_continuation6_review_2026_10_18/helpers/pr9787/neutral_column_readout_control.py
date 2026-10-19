from fractions import Fraction as Q
from math import comb
from itertools import permutations
import json,numpy as np
from scipy.linalg import eigh
rows=[]
for L in range(4,17,2):
 full=(1<<L)-1;F=[Q(0)]*(1<<L);T=F.copy();F[0]=Q(1)
 for s in range(1,full):
  c=sum(((s>>i)&1) and not((s>>((i-1)%L))&1) for i in range(L))
  d=sum(((s>>i)^(s>>((i+2)%L)))&1 for i in range(L))
  singles=sum(((s>>i)&1) and not((s>>((i-1)%L))&1) and not((s>>((i+1)%L))&1) for i in range(L))
  empty=full^s
  singles+=sum(((empty>>i)&1) and not((empty>>((i-1)%L))&1) and not((empty>>((i+1)%L))&1) for i in range(L))
  assert d==4*c-2*singles
  prev=[s^(1<<i) for i in range(L) if(s>>i)&1]
  F[s]=sum((F[x] for x in prev),Q(0))/c
  T[s]=sum((T[x] for x in prev),Q(0))/c+Q(d,c)*F[s]
 ans=sum(T[full^(1<<i)] for i in range(L))/comb(2*L-2,L-1)
 assert ans==Q(6*(L-1)*(L-2),2*L-3)
 rows.append(dict(L=L,A=str(ans)))
# Four-edge square physical Pauli phases, fixed ordered surrounding spins.
edges=[(0,1,'X'),(2,3,'X'),(0,2,'Y'),(1,3,'Y')]
squares=[]
for ref in range(16):
 val=Q(0);deriv=Q(0)
 for perm in permutations(range(4)):
  flipped=0;num=1;den=1
  for k,e in enumerate(perm):
   i,j,axis=edges[e]
   # V=-XX or -YY. YY action introduces minus times the two input signs.
   if axis=='X':num*=-1
   else:num*=(-1)**((((ref^flipped)>>i)&1)+(((ref^flipped)>>j)&1))
   flipped^=(1<<i)|(1<<j)
   if k<3:den*=-4*flipped.bit_count()
  assert flipped==0
  val+=Q(num,den)
  deriv+=3*Q(num,den) # Delta=4k(1-h), sqrtV=J=1.
 parity=(-1)**ref.bit_count()
 assert val==Q(-parity,128) and deriv==Q(-3*parity,128)
 squares.append(dict(reference=ref,energy=str(val),source=str(deriv)))
ed=[]
for L in [4,6]:
 dim=1<<L;ix=np.arange(dim);full=dim-1
 H0=np.diag([-2*sum((1-2*((s>>i)&1))*(1-2*((s>>((i+1)%L))&1)) for i in range(L)) for s in range(dim)]).astype(float)
 C=np.array([2*sum((1-2*((s>>i)&1))*(1-2*((s>>((i+2)%L))&1)) for i in range(L)) for s in range(dim)],float)
 V=np.zeros_like(H0)
 for s in range(dim):
  for i in range(L):V[s^(1<<i),s]=-1
 # exact global-X parity bases avoid ambiguous near-degenerate eigenvectors
 reps=list(range(dim//2));bases=[]
 for sign in [1,-1]:
  U=np.zeros((dim,len(reps)))
  for j,s in enumerate(reps):U[s,j]=1/np.sqrt(2);U[s^full,j]=sign/np.sqrt(2)
  bases.append(U)
 for lam in [.3,.2,.15]:
  cs=[]
  for U in bases:
   e,v=eigh(U.T@(H0+lam*V)@U);g=U@v[:,0];cs.append(float((g*C)@g))
  obs=(cs[0]-cs[1])/2
  gamma=lam**L*comb(2*L-2,L-1)/8**(L-1)
  pred=-gamma*3*(L-1)*(L-2)/(2*L-3)
  ed.append(dict(L=L,lam=lam,source_offdiag=obs,predicted=pred,ratio=obs/pred))
 assert abs(ed[-1]['ratio']-1)<abs(ed[-3]['ratio']-1)
print(json.dumps(dict(winding=rows,square=squares,virtual_dressing=ed,scope='Fixed coefficient controls with J=sqrtV=1; restricted winding subproblem is not full lattice dynamics'),indent=2))
