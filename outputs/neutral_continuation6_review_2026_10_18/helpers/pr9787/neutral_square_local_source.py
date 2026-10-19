from fractions import Fraction as Q
from itertools import permutations
edges=[(0,1,'X'),(2,3,'X'),(0,2,'Y'),(1,3,'Y')]
for ref in range(16):
 d=[Q(0) for _ in range(4)]
 for perm in permutations(range(4)):
  flip=0;num=1;den=1;marked=[Q(0) for _ in range(4)]
  for k,e in enumerate(perm):
   i,j,a=edges[e]
   num*= -1 if a=='X' else (-1)**((((ref^flip)>>i)&1)+(((ref^flip)>>j)&1))
   flip^=(1<<i)|(1<<j)
   if k<3:
    den*=-4*flip.bit_count()
    for v in range(4):marked[v]+=Q((flip>>v)&1,flip.bit_count())
  for v in range(4):d[v]+=Q(num,den)*marked[v]
 assert d==[Q(-3*(-1)**ref.bit_count(),512)]*4
print('16 reference patterns, four independently marked vertices each PASS: -3P/512')
