AUDIT_TIMEOUT_SEC=300
from fractions import Fraction as F
from collections import defaultdict
import json

def syn(c):
 s=set()
 for x,y in c:s^={(x,y),(x-1,y),(x,y-1),(x-1,y-1)}
 return frozenset(s)
def per(s):return sum((x+dx,y+dy) not in s for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
def minimum(c):
 if len(c)!=2:return False
 a,b=sorted(c);return (abs(a[0]-b[0]),abs(a[1]-b[1])) in [(2,0),(0,2)]
initial=frozenset([(-1,0),(1,0)])
weights={initial:F(1)};outs={}
for k in range(1,5):
 nxt=defaultdict(F)
 for c,w in weights.items():
  # Every Q-preserving edge must overlap the current syndrome; disjoint adds Q4.
  candidates=set()
  for x,y in syn(c):
   for dx in range(-1,3):
    for dy in range(-1,3):
     for ex,ey in [(1,0),(0,1)]:candidates.add(frozenset([(x+dx,y+dy),(x+dx+ex,y+dy+ey)]))
  for e in candidates:
   f=c^e;s=syn(f)
   if len(s)!=8:continue
   if k<4:
    if minimum(f):continue
    gap=per(s)-12
    assert gap>0
    nxt[f]+=w/F(gap)
   elif minimum(f):
    a,b=sorted(f)
    if a[0]==b[0]:nxt[f]+=w
 weights=nxt

for c,w in sorted(weights.items(),key=lambda x:sorted(x[0])):
 a,b=sorted(c);outs[str((a[0],(a[1]+b[1])//2))]=str(w)
print(json.dumps(dict(kernel=outs,total=str(sum(weights.values()))),indent=2))
