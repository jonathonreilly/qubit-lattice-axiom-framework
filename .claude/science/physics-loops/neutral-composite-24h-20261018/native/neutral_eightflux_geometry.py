from itertools import combinations
from collections import Counter
import json

def syndrome(cols):
 s=set()
 for x,y in cols:
  s^={(x,y),(x-1,y),(x,y-1),(x-1,y-1)}
 return s

def perimeter(s):return sum((x+dx,y+dy) not in s for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
# Exhaust bounding boxes with w+h<=6 required by perimeter<=12.
mins=[]
for w in range(1,6):
 for h in range(1,7-w):
  if w*h<8:continue
  cells=[(x,y) for x in range(w) for y in range(h)]
  for tup in combinations(cells,8):
   s=set(tup)
   if min(x for x,y in s)!=0 or max(x for x,y in s)!=w-1 or min(y for x,y in s)!=0 or max(y for x,y in s)!=h-1:continue
   if perimeter(s)>12:continue
   if any(sum(x==a for x,y in s)%2 for a in range(w)) or any(sum(y==b for x,y in s)%2 for b in range(h)):continue
   mins.append(dict(w=w,h=h,points=sorted(s),perimeter=perimeter(s)))
initial={(0,0),(2,0)}
edges=[frozenset([(x,y),(x+dx,y+dy)]) for x in range(-3,6) for y in range(-3,4) for dx,dy in [(1,0),(0,1)]]
paths={}
for e1 in edges:
 mid=initial^e1;s=syndrome(mid)
 for e2 in edges:
  final=mid^e2
  if len(final)!=2 or final==initial:continue
  p,q=sorted(final)
  if abs(p[0]-q[0])+abs(p[1]-q[1])!=2 or (p[0]!=q[0] and p[1]!=q[1]):continue
  key=str(sorted(final));paths.setdefault(key,[]).append(dict(Q=len(s),perimeter=perimeter(s),mid=sorted(mid)))
print(json.dumps(dict(minima=mins,paths=paths),indent=2))
