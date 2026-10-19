import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
import json,itertools
from fractions import Fraction as F
import numpy as np
from scipy.linalg import eigh
from neutral_four_layer_geometry import geometry,diagonal
rows=[]
for periodic_z in [False,True]:
 total=F(0);marked=F(0)
 for order in itertools.permutations(range(4)):
  s=set();w=F(1);mark=F(0)
  for k in order[:-1]:
   s.add(k)
   if periodic_z:
    c=sum((i in s)!=((i+1)%4 in s) for i in range(4))//2
    d=sum((i in s)!=((i+2)%4 in s) for i in range(4))
   else:
    c=sum((i in s)!=((i+1) in s) for i in range(3))
    d=sum((i in s)!=((i+2) in s) for i in range(2))
   w/=c;mark+=F(d,c)
  total+=w;marked+=w*mark
 assert total==(20 if periodic_z else 8)
 assert marked/total==(F(36,5) if periodic_z else 3)
 rows.append(dict(periodic_z=periodic_z,path_sum=str(total),mark=str(marked/total)))
checks=[]
for R in [3,4]:
 for periodic_xy in [False,True]:
  _,_,edges,flips=geometry(R,periodic_xy);n=1<<((R-1)**2);states=np.arange(n,dtype=np.int64)
  E=-diagonal(states,edges)/5
  for open_z in [False,True]:
   a,b,c=(18,16,8/3) if open_z else (4,5,3)
   H=np.diag(-b*E)
   for f in flips:H[states,states^f]-=a
   ev,u=eigh(H);g=u[:,0];q=-c*(E-g@(E*g))*g
   assert np.min(abs(g))>0
   assert np.linalg.norm(H@g-ev[0]*g)<1e-9
   weights=abs(u.T@q)**2
   assert weights[0]<1e-20 and weights.sum()>1
   visible=np.flatnonzero(weights>1e-8)[0]
   checks.append(dict(R=R,periodic_xy=periodic_xy,open_z=open_z,ground=float(ev[0]),source_norm2=float(q@q),first_visible_gap=float(ev[visible]-ev[0]),first_visible_weight=float(weights[visible]),closure_error=float(abs(weights.sum()-q@q))))
print(json.dumps(dict(winding=rows,finite_coefficient_controls=checks,scope='Finite coefficient matrices and exact native path controls; no full-H diagonalization or observed-data test')))
