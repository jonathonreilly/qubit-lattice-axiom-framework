from itertools import permutations
from fractions import Fraction as F
import json
# perimeter of 3x2 rectangle: X01,12,34,45; Y03,25
edges=[(0,1,'X'),(1,2,'X'),(3,4,'X'),(4,5,'X'),(0,3,'Y'),(2,5,'Y')]
rows=[]
for d in [2,4]:
 for c in range(64):
  total=F(0)
  for order in permutations(range(6)):
   s=c;amp=F(1)
   for k,e in enumerate(order):
    a,b,t=edges[e]
    amp*= -1 if t=='X' else (1-2*((s>>a)&1))*(1-2*((s>>b)&1))
    s^=(1<<a)|(1<<b)
    if k<5:amp/= -d*(s^c).bit_count()
   assert s==c;total+=amp
  parity=(-1)**sum((c>>i)&1 for i in [0,2,3,5])
  expected=-F(3,256 if d==2 else 8192)*parity
  assert total==expected
  rows.append(dict(cost=d,color=c,corner_parity=parity,coefficient=str(total)))
 print(d,rows[-64:][:4],flush=True)
open(__file__.replace('.py','.json'),'w').write(json.dumps(rows,indent=2)+'\n')
