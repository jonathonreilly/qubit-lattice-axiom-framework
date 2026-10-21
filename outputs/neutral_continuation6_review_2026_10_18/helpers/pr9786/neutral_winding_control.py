from fractions import Fraction
from math import comb
import json
import numpy as np
from scipy.linalg import eigvalsh
rows=[]
for L in range(4,17,2):
 full=(1<<L)-1
 F=[Fraction(0)]*(1<<L);F[0]=Fraction(1)
 for s in range(1,full):
  clusters=sum(((s>>i)&1) and not ((s>>((i-1)%L))&1) for i in range(L))
  F[s]=sum((F[s^(1<<i)] for i in range(L) if (s>>i)&1),Fraction(0))/clusters
  lengths=[]
  for i in range(L):
   if ((s>>i)&1) and not ((s>>((i-1)%L))&1):
    ell=1
    while (s>>((i+ell)%L))&1:ell+=1
    lengths.append(ell)
  prod=1
  for ell in lengths:prod*=comb(2*ell,ell)//(ell+1)
  assert F[s]==prod
 total=sum(F[full^(1<<i)] for i in range(L))
 assert total==comb(2*L-2,L-1)
 rows.append({'L':L,'subsets_checked':full-1,'sum':str(total),'coefficient':str(total/Fraction(8**(L-1)))})
# Restricted two-column rung Hamiltonian checks the squarefree native monomial,
# not a replacement of the full physical Hamiltonian by a ladder.
ed=[]
for L in [4,6]:
 dim=1<<L
 H0=np.diag([-2*sum((1-2*((s>>i)&1))*(1-2*((s>>((i+1)%L))&1)) for i in range(L)) for s in range(dim)]).astype(float)
 V=np.zeros_like(H0)
 for s in range(dim):
  for i in range(L):V[s^(1<<i),s]=-1
 for lam in ([.2,.1,.05] if L==4 else [.3,.2,.15]):
  ev=eigvalsh(H0+lam*V)
  gamma=lam**L*comb(2*L-2,L-1)/8**(L-1)
  ratio=(ev[1]-ev[0])/(2*gamma)
  ed.append({'L':L,'lambda':lam,'splitting_over_2gamma':ratio})
 assert abs(ed[-1]['splitting_over_2gamma']-1)<abs(ed[-3]['splitting_over_2gamma']-1)
print(json.dumps({'exact_subset_controls':rows,'fixed_L_monomial_ED':ed},indent=2))
