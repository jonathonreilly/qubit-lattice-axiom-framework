from collections import defaultdict
import random,json
R=6;L=4;N=R*R
rng=random.Random(1810)
def wall(s):
 return sum((((s>>(4*c))&15)^((((s>>(4*c))&15)<<1|((s>>(4*c))&15)>>3)&15)).bit_count() for c in range(N))
bonds=[]
for x in range(R):
 for y in range(R):
  for z in range(4):
   i=x*R+y
   for axis,j in [('x',((x+1)%R)*R+y),('y',x*R+(y+1)%R)]:bonds.append((axis,i,j,4*i+z,4*j+z,z))
checks=0;preserved=0
for _ in range(32):
 bg=[rng.choice([-1,1]) for i in range(N)];aligned=sum(15<<(4*i) for i,s in enumerate(bg) if s<0)
 for i in [0,5,35]:
  for z in range(4):
   state=aligned^(1<<(4*i+z));assert wall(state)==2
   for axis,a,b,ia,ib,zz in bonds:
    out=state^(1<<ia)^(1<<ib);n=wall(out);checks+=1
    expected=(i in [a,b] and z==zz)
    assert (n==2)==expected
    if expected:
     j=b if i==a else a;assert out==aligned^(1<<(4*j+z))
     za=1-2*((state>>ia)&1);zb=1-2*((state>>ib)&1)
     amp=-1 if axis=='x' else za*zb
     assert amp==(-1 if axis=='x' else -bg[i]*bg[j]);preserved+=1
# Four-hop rooted return words in the background variables.
paths=[((0,0),0)]
for _ in range(4):
 new=[]
 for (x,y),mask in paths:
  for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
   xx=(x+dx)%R;yy=(y+dy)%R;m=mask
   if dy:m^=(1<<(x*R+y))^(1<<(xx*R+yy))
   new.append(((xx,yy),m))
 paths=new
words=defaultdict(int)
for pos,m in paths:
 if pos==(0,0):words[m]+=1
assert words[0]==28 and sorted(words.values())==[2,2,2,2,28]
for x,y in [(0,0),(R-1,0),(0,R-1),(R-1,R-1)]:
 mask=sum(1<<(((x+a)%R)*R+(y+b)%R) for a,b in [(0,0),(1,0),(0,1),(1,1)])
 assert words[mask]==2
print(json.dumps(dict(physical_bond_checks=checks,preserved_hops=preserved,return_words={str(k):v for k,v in words.items()},scope='Exact native physical bit actions and path-word enumeration; no fitted or added interaction')))
