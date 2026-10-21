from fractions import Fraction as F
from itertools import permutations
import json
R=8;L=6

def bond(x,y,z,a):
 i=((x%R)*R+y%R)*L+z%L;j=(((x+(a=='x'))%R)*R+(y+(a=='y'))%R)*L+z%L
 return (a,min(i,j),max(i,j))
es=[bond(0,0,0,'x'),bond(1,0,0,'y'),bond(0,1,0,'x'),bond(0,0,0,'y')]
def wall(s):
 out=0
 while s:
  bit=(s&-s).bit_length()-1;c=bit//L;q=(s>>(c*L))&63;out+=(q^((q<<1|q>>5)&63)).bit_count();s &= ~(63<<(c*L))
 return out

def raw(b):
 edges=es+[b,b];total=F(0)
 for word in set(permutations(edges)):
  state=0;v=F(1)
  for k,(a,i,j) in enumerate(word):
   v*= -1 if a=='x' else 1-2*(((state>>i)^(state>>j))&1)
   state^=(1<<i)|(1<<j)
   if k<5:
    den=-2*wall(state)
    if not den:v=F(0);break
    v/=den
  total+=v
 return total
rows=[]
for z in [0,1,L-1,2]:
 seen=set()
 for x,y in [(0,0),(1,0),(0,1),(1,1)]:
  for a in ['x','y']:
   for d in [0,-1]:seen.add(bond(x+(d if a=='x' else 0),y+(d if a=='y' else 0),z,a))
 subtotal=F(0)
 for b in sorted(seen):
  rr=raw(b);val=rr+F(7,16384);subtotal+=val;rows.append(dict(z=z,b=b,raw=str(rr),connected=str(val)))
 print(json.dumps(dict(z=z,total=str(subtotal))),flush=True)
