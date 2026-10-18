from fractions import Fraction as F
from itertools import permutations
import json

def square(x,y,z):
 p=[(x,y,z),(x+1,y,z),(x+1,y+1,z),(x,y+1,z)]
 return [(p[k],p[(k+1)%4], 'Y' if p[k][0]==p[(k+1)%4][0] else 'X') for k in range(4)]
def run(dz):
 edges=square(0,0,0)+square(1,1,dz);vertices=sorted(set(v for e in edges for v in e[:2]));ix={v:i for i,v in enumerate(vertices)}
 edges=[(ix[a],ix[b],ax) for a,b,ax in edges]
 links=[(i,j) for i,v in enumerate(vertices) for j,w in enumerate(vertices) if v[:2]==w[:2] and w[2]==v[2]+1]
 def cost(s):return 4*s.bit_count()-4*sum(((s>>i)&1)*((s>>j)&1) for i,j in links)
 def word(order):
  s=0;w=F(1);deriv=F(0)
  for k,e in enumerate(order):
   i,j,ax=edges[e];w*= -1 if ax=='X' else (-1 if ((s>>i)^(s>>j))&1 else 1);s^=(1<<i)|(1<<j)
   if k<len(order)-1:
    if s==0:return F(0),F(0)
    c=cost(s);w/= -c;deriv+=F(1,c)
  assert s==0
  return w,w*deriv
 raw=sum((word(p)[0] for p in permutations(range(8))),F(0))
 ea=da=eb=db=F(0)
 for p in permutations(range(4)):
  a,d=word(p);ea+=a;da+=d
 for p in permutations(range(4,8)):
  a,d=word(p);eb+=a;db+=d
 fold=ea*db+eb*da
 return dict(dz=dz,raw=str(raw),fold=str(fold),connected=str(raw+fold),E4=str(ea),derivative4=str(da))
rows=[run(z) for z in [0,1,2]]
print(json.dumps(rows,indent=2))
