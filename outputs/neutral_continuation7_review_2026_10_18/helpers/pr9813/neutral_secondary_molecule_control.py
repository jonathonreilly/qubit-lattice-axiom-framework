AUDIT_TIMEOUT_SEC=300
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json
@lru_cache(None)
def syn(c):
 s=set()
 for x,y in c:s^={(x,y),(x-1,y),(x,y-1),(x-1,y-1)}
 return frozenset(s)
def per(s):return sum((x+dx,y+dy) not in s for x,y in s for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)))
def count(s,p):
 a=set()
 for dx,dy in p:a^={(x-dx,y-dy) for x,y in s}
 return len(a)
box={(0,0),(1,0),(0,1),(1,1)}
@lru_cache(None)
def energy(c):
 s=syn(c);a=sum(count(s,p) for p in [[(0,0),(1,0),(2,0)],[(0,0),(0,1),(0,2)],box]);b=sum(count(s,box-{p}) for p in box);d=sum(count(s,p) for p in [[(0,0),(1,1)],[(0,1),(1,0)]])
 return 2*(F(9,262144)*a-F(5,262144)*b-F(29,1327104)*d)+F(545,442368)
v=F(9,32768)
def band(c):
 if len(c)!=2:return False
 a,b=sorted(c);return abs(a[0]-b[0])+abs(a[1]-b[1])==3 and (a[0]==b[0] or a[1]==b[1])
@lru_cache(None)
def neighbors(c):
 s=syn(c);edges=set()
 for x,y in s:
  for a in (x-1,x+1):
   for b in (y,y+1):edges.add(frozenset({(a,b),(a+1,b)}))
  for a in (x,x+1):
   for b in (y-1,y+1):edges.add(frozenset({(a,b),(a,b+1)}))
 out=[]
 for e in edges:
  z=c^e;t=syn(z)
  if len(t)==8 and per(t)==16:out.append(z)
 return out
start=frozenset({(0,0),(3,0)});states={start:F(1)};results={}
for step in range(1,7):
 new=defaultdict(F);ends=defaultdict(F)
 for c,w in states.items():
  for z in neighbors(c):
   if band(z):ends[z]+=w
   else:new[z]+=w/(energy(z)+v)
 results[step]=ends;states=new

from math import comb
C=F(1046023065421557893414518784,118275147)
vertical={z:w for z,w in results[6].items() if len({x for x,y in z})==1}
assert len(vertical)==16
for z,w in vertical.items():
 x=next(iter(z))[0];y=min(y for x,y in z)
 assert w==C*comb(3,x)*comb(3,y+3)
assert sum(vertical.values())==64*C
assert results[2][frozenset(((-1,0),(2,0)))]==1/v
assert results[2][frozenset(((0,1),(3,1)))]==4/v
for step in range(1,6):assert not any(len({x for x,y in z})==1 for z in results[step])
for a in range(2,12):
 for b in range(a+1):
  cs=frozenset(((0,0),(a,b)))
  if len(syn(cs))!=8 or per(syn(cs))!=16:continue
  expected=-v if (a,b)==(3,0) else -v/2 if (a,b)==(3,1) else F(545,5308416) if (a,b)==(2,2) else F(0)
  assert energy(cs)==expected
for d in range(3,102,2):
 cs=frozenset({(x,0) for x in range(d)}|{(d+1,0)})
 assert len(syn(cs))==8 and per(syn(cs))==16 and energy(cs)==v
assert energy(frozenset(((0,0),(1,0),(2,0),(1,1))))==F(683,663552)
# Root one-step shape tails, grouped by unoriented relative displacement.
relative={}
for z in neighbors(start):
 assert len(z)==2
 a,b=sorted(z);r=(b[0]-a[0],b[1]-a[1])
 relative[r]=relative.get(r,F(0))+1/(energy(z)+v)
assert relative=={(4,0):2/v,(3,-1):4/v,(3,1):4/v}
for R in (12,14,18):
 for dx,dy in ((3,0),(0,3),(4,0),(3,1),(3,-1)):
  columns={(0,0),(dx%R,dy%R)}
  flipped=sum(((x,y) in columns)!=((x,(y+1)%R) in columns) for x in range(R) for y in range(R))
  assert flipped==4
print(json.dumps(dict(two_hop=[dict(columns=sorted(c),weight=str(w)) for c,w in results[2].items()],orientation=[dict(columns=sorted(c),weight=str(w)) for c,w in vertical.items()],orientation_sum=str(64*C),rod_lengths_checked=list(range(3,102,2)))))
