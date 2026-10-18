"""Exact native fourth-order aligned-column splitting, no selected parity."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import json
EDGES=[(0,1,'X'),(2,3,'X'),(0,2,'Y'),(1,3,'Y')]
def hop(s,j,e):
 a,b,t=EDGES[e];a+=4*j;b+=4*j
 amp=-1 if t=='X' else (1-2*((s>>a)&1))*(1-2*((s>>b)&1))
 return s^(1<<a)^(1<<b),amp
loops=[]
for end in [False,True]:
 for c in range(16):
  total=F(0)
  for order in permutations(range(4)):
   s=c;amp=F(1)
   for k,e in enumerate(order):
    s,v=hop(s,0,e);amp*=v
    if k<3:amp/=-(2 if end else 4)*(s^c).bit_count()
   assert s==c;total+=amp
  expected=F(-(-1)**c.bit_count(),16 if end else 128);assert total==expected
  loops.append(dict(end=end,color=c,coefficient=str(total)))
rows=[]
for L in [5,6,7,8]:
 def energy(s):return 2*sum((((s>>(4*j))^(s>>(4*(j+1))))&15).bit_count() for j in range(L-1))
 for c in range(16):
  vac=sum(c<<(4*j) for j in range(L));one={}
  for j in range(L):
   for e in range(4):
    s,v=hop(vac,j,e);one[s]=one.get(s,F(0))+v
  E2=sum(F(v*v,-energy(s)) for s,v in one.items());metric=sum(F(v*v,energy(s)**2) for s,v in one.items())
  middle={}
  for s,v in one.items():
   for j in range(L):
    for e in range(4):
     d,w=hop(s,j,e)
     if energy(d):middle[d]=middle.get(d,F(0))+F(w*v,-energy(s))
  direct=sum(v*v/F(-energy(s)) for s,v in middle.items());E4=direct-E2*metric
  rows.append(dict(L=L,color=c,parity=(-1)**c.bit_count(),E2=str(E2),E4=str(E4)))
 for c in range(16):
  ref=rows[-16]['E4'];r=rows[-16+c]
  assert F(r['E4'])-F(ref)==(0 if r['parity']==1 else F(L+14,64))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(loops=loops,full_fourth_order=rows,scope='Exact fixed-order coefficients; fixed finite-size small-anisotropy sector selection, not uniform 3D ground theorem'),indent=2)+'\n')
print('all16 colors, bulk/end loops and full canonical fourth-order L5..8 passed')
