from itertools import permutations,product
from fractions import Fraction as F
import json

def walls(q):return (q^((q<<1|q>>3)&15)).bit_count()
rows=[]
for axis,si,sj,z in product(['x','y'],[-1,1],[-1,1],range(4)):
 a=(15 if si<0 else 0)^(1<<z);b=15 if sj<0 else 0
 initial=(a,b);terms=[]
 for order in permutations([k for k in range(4) if k!=z]):
  a,b=initial;amp=F(1);ns=[]
  for step,k in enumerate(order):
   amp*= -1 if axis=='x' else (1-2*((a>>k)&1))*(1-2*((b>>k)&1))
   a^=1<<k;b^=1<<k
   n=walls(a)+walls(b);ns.append(n)
   if step<2:assert n!=2;amp/=4-2*n
  assert a==(15 if si>0 else 0)
  assert b==((15 if sj>0 else 0)^(1<<z))
  terms.append(amp)
 total=sum(terms);expected=F(-1,4) if axis=='x' else F(si*sj,4)
 assert total==expected
 rows.append(dict(axis=axis,si=si,sj=sj,z=z,amplitude=str(total),path_terms=list(map(str,terms))))
print(json.dumps(dict(status='pass',cases=rows,scope='exact complementary-layer native three-hop path; not complete D3')))
