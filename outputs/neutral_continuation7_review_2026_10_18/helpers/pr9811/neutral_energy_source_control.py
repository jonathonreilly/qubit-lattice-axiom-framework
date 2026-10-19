"""Native bond marks and long-wave energy-source coefficient checks."""
AUDIT_TIMEOUT_SEC=300
from fractions import Fraction as F
from itertools import permutations
from math import comb
import json
edges=[(0,1,'X'),(2,3,'X'),(0,2,'Y'),(1,3,'Y')]
rows=[]
for ref in range(16):
 value=F(0);vertex=[F(0)]*4;edge=[F(0)]*4
 for order in permutations(range(4)):
  flip=0;num=1;den=1;mark=[F(0)]*4
  for n,e in enumerate(order):
   i,j,a=edges[e];num*= -1 if a=='X' else (-1)**((((ref^flip)>>i)&1)+(((ref^flip)>>j)&1))
   flip^=(1<<i)|(1<<j)
   if n<3:
    den*=-4*flip.bit_count()
    for v in range(4):mark[v]-=F((flip>>v)&1,flip.bit_count())
  weight=F(num,den);value+=weight
  for v in range(4):vertex[v]+=weight*mark[v];edge[v]+=weight
 assert [x/value for x in vertex]==[F(-3,4)]*4
 assert sum(edge)+sum(vertex)==value
 rows.append(dict(reference=ref,coefficient=str(value),edge_ratios=[str(x/value) for x in edge],vertex_ratios=[str(x/value) for x in vertex]))
# Each winding word uses L transverse bonds and L-1 denominators.
# Each denominator has equal broken-wall energy in its two columns.
winding=[]
for L in (4,6,8,10,12):
 gamma=F(comb(2*L-2,L-1),8**(L-1))
 numerator=F(L);per_column=-F(L-1,2)
 assert numerator+2*per_column==1
 # F4 expansion is 1+(qx²+qy²)/8. x syndrome contributes cos qx cos(qy/2).
 quadratic_x=F(1,8)-F(1,2)-F(L-1,8)
 quadratic_y=F(1,8)-F(1,8)
 assert quadratic_x==-F(L+2,8) and quadratic_y==0
 weight=gamma**2*F((L+2)**2,128*L)
 winding.append(dict(L=L,numerator=str(numerator),denominator_each_column=str(per_column),x_pair_qx2=str(quadratic_x),x_pair_qy2=str(quadratic_y),scalar_weight_coefficient=str(weight)))
print(json.dumps(dict(square=rows,winding=winding)))
