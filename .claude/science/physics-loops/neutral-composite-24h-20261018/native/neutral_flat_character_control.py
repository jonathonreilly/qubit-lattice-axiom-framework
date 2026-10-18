from itertools import combinations,product
from fractions import Fraction
import json,random

def setup(R):
 # R row flips and R-1 column flips form an independent generator set.
 gs=[sum(1<<(x*R+y) for y in range(R)) for x in range(R)]+[sum(1<<(x*R+y) for x in range(R)) for y in range(R-1)]
 group={0:0}
 for j,g in enumerate(gs):
  group.update({a^g:m|(1<<j) for a,m in list(group.items())})
 return gs,group
rows=[]
for R in (4,6,8):
 gs,G=setup(R);minimum=min(g.bit_count() for g in G if g)
 assert minimum==R
 # Closed form weight for a rows and b columns.
 assert all((a*(R-b)+(R-a)*b>=R or (a,b) in ((0,0),(R,R))) for a in range(R+1) for b in range(R+1))
 rng=random.Random(R);checks=0
 for _ in range(120):
  T=sum(1<<i for i in rng.sample(range(R*R),2));Tp=sum(1<<i for i in rng.sample(range(R*R),2))
  # Local native-type X edge and arbitrary plaquette-invariant Z word.
  x,y=rng.randrange(R),rng.randrange(R)
  A=(1<<(x*R+y))^(1<<(x*R+(y+1)%R))
  B=sum(1<<(((x+dx)%R)*R+(y+dy)%R) for dx,dy in product((0,1),repeat=2))
  assert all((B&g).bit_count()%2==0 for g in gs)
  g=T^Tp^A
  if R>6:assert g not in G or g==0
  vals=[]
  for chi in (0,1,3,(1<<len(gs))-1,rng.randrange(1<<len(gs))):
   v=0 if g not in G else (-1)**((G[g]&chi).bit_count()+(B&T).bit_count())
   vals.append(v)
  if g.bit_count()<R:assert len(set(vals))==1
  checks+=1
 rows.append(dict(R=R,dimension=len(G),minimum_flat_flip=minimum,checks=checks))
# Show why an arbitrary noninvariant observable/preparation is not covered.
R=4;gs,G=setup(R);B=1
assert any((B&g).bit_count()%2 for g in gs)
# The classical flat state has Z_0=+1; every character Fourier state has zero.
mean=sum((-1)**((B&g).bit_count()) for g in G)/len(G)
assert mean==0
direct_checks=0
R=4;gs,G=setup(R);rng=random.Random(918)
words=[(0,0),(gs[0],0),(0,1),(0,(1<<0)|(1<<1)|(1<<4)|(1<<5))]
words += [(rng.randrange(1<<16),rng.randrange(1<<16)) for _ in range(20)]
for A,B in words:
 for chi in range(1<<len(gs)):
  direct=0
  for g,m in G.items():
   if g^A in G:
    direct+=(-1)**((chi&m).bit_count()+(chi&G[g^A]).bit_count()+(B&g).bit_count())
  direct=Fraction(direct,len(G))
  predicted=0 if A not in G or any((B&g).bit_count()%2 for g in gs) else (-1)**((chi&G[A]).bit_count())
  assert direct==predicted
  direct_checks+=1
# A whole row is exactly the support threshold and can distinguish characters.
assert (-1)**(G[gs[0]]&0).bit_count()!=(-1)**(G[gs[0]]&1).bit_count()
print(json.dumps(dict(rows=rows,direct_orbit_checks=direct_checks,noninvariant_Z_character_mean=mean,noninvariant_Z_classical_flat=1,scope='Exact code algebra; arbitrary local noninvariant readouts are not state independent')))
