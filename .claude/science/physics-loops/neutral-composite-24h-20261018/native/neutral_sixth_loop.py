from fractions import Fraction as F
from itertools import permutations
import json

def loop(w,h):
 coords=[(x,0) for x in range(w+1)]+[(w,y) for y in range(1,h+1)]+[(x,h) for x in range(w-1,-1,-1)]+[(0,y) for y in range(h-1,0,-1)]
 edges=[]
 for k,a in enumerate(coords):
  b=coords[(k+1)%len(coords)];edges.append(('x' if a[1]==b[1] else 'y',k,(k+1)%len(coords)))
 return edges

def val(w,h):
 es=loop(w,h);n=len(es);total=F(0);weighted=F(0)
 for word in permutations(range(n)):
  state=0;v=F(1);rs=[]
  for k,b in enumerate(word):
   axis,i,j=es[b];v*= -1 if axis=='x' else (1 if ((state>>i)^(state>>j))&1==0 else -1)
   state^=(1<<i)|(1<<j)
   if k<n-1:
    den=-4*state.bit_count();assert den
    v/=den;rs.append(F(1,den))
  assert state==0;total+=v;weighted+=v*sum(rs)
 return dict(w=w,h=h,per_layer=str(total),squared_resolvent_sum=str(weighted))
print(json.dumps([val(1,1),val(2,1),val(1,2)],indent=2))
