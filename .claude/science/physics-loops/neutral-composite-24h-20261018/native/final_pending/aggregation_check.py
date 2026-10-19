from itertools import combinations
from fractions import Fraction as F
from collections import Counter

def syndrome(A):
 out=set()
 for i,j in A:
  for x,y in [(4*i,3*j),(4*i+1,3*j)]:out^={(x,y),(x-1,y),(x,y-1),(x-1,y-1)}
 return out
patterns=[]
c=F(9,262144);h=F(5,262144);k=F(29,1327104)
patterns +=[(frozenset([(0,0),(1,0),(2,0)]),-c),(frozenset([(0,0),(0,1),(0,2)]),-c),(frozenset([(0,0),(1,0),(0,1),(1,1)]),-c)]
box={(0,0),(1,0),(0,1),(1,1)}
patterns += [(frozenset(box-{z}),h) for z in box]
patterns +=[(frozenset([(0,0),(1,1)]),k),(frozenset([(0,1),(1,0)]),k)]
def value(A):
 S=syndrome(A);val=F(0)
 for P,t in patterns:
  anchors={(x-u,y-v) for x,y in S for u,v in P}
  odd=sum(sum((a+u,b+v) in S for u,v in P)%2 for a,b in anchors)
  val-=2*t*odd
 return val
single=value([(0,0)])
for d in [(1,0),(0,1),(1,1),(2,0),(0,2)]:print('pair',d,value([(0,0),d])-2*single)
cells=[(i,j) for i in range(3) for j in range(3)]
for bits in range(1<<len(cells)):
 A={z for j,z in enumerate(cells) if bits>>j&1};edges=sum((i+di,j+dj) in A for i,j in A for di,dj in [(1,0),(0,1)])
 assert value(A)-len(A)*single==-F(9,32768)*edges
print('all 512 subsets pass')
# For every pattern count number of motifs reached and odd mark per reached motif.
for P,t in patterns:
 types=Counter()
 for a in range(-5,10):
  for b in range(-5,8):
   reached=[]
   for cell in cells:
    z=sum((a+u,b+v) in syndrome([cell]) for u,v in P)
    if z:reached.append((cell,z%2))
   if len(reached)>1:types[tuple(sorted(z for cell,z in reached))]+=1
 print(sorted(P),t,dict(types))
